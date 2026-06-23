import cgi
import io
import logging
import tempfile
import zipfile
from pathlib import Path

import azure.functions as func

from convert_g30_to_g60 import convert, select_base_template

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


def _read_g30_input(req: func.HttpRequest) -> tuple[bytes, str]:
    """Return G30 file bytes and filename from multipart 'file' or raw POST body."""
    content_type = (req.headers.get("content-type") or "").lower()

    if "multipart/form-data" in content_type:
        if hasattr(req, "files") and req.files:
            uploaded = req.files.get("file")
            if uploaded:
                data = uploaded.read()
                name = getattr(uploaded, "filename", None) or "input.xml"
                if data:
                    return data, name

        environ = {
            "REQUEST_METHOD": "POST",
            "CONTENT_TYPE": req.headers.get("Content-Type", ""),
            "CONTENT_LENGTH": req.headers.get("Content-Length", "0"),
        }
        form = cgi.FieldStorage(
            fp=io.BytesIO(req.get_body()),
            environ=environ,
            keep_blank_values=True,
        )
        if "file" in form:
            file_item = form["file"]
            if getattr(file_item, "file", None):
                data = file_item.file.read()
                name = getattr(file_item, "filename", None) or "input.xml"
                if data:
                    return data, name

    body = req.get_body()
    if not body:
        raise ValueError(
            "Missing request body. Send multipart form field 'file' or raw POST body."
        )

    filename = req.params.get("filename", "input.xml")
    return body, filename


@app.route(route="convert", methods=["POST"], auth_level=func.AuthLevel.FUNCTION)
def convert_g30_to_g60_http(req: func.HttpRequest) -> func.HttpResponse:
    here = Path(__file__).parent

    try:
        g30_bytes, filename = _read_g30_input(req)
    except ValueError as exc:
        return func.HttpResponse(str(exc), status_code=400)

    if not g30_bytes:
        return func.HttpResponse("Empty file content.", status_code=400)

    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            g30_path = tmp_path / Path(filename).name
            output_dir = tmp_path / "output"
            output_dir.mkdir()

            g30_path.write_bytes(g30_bytes)

            try:
                g60_template_path = select_base_template(g30_path, here)
            except FileNotFoundError as exc:
                return func.HttpResponse(str(exc), status_code=400)

            try:
                convert(g30_path, g60_template_path, output_dir)
            except Exception as exc:
                logging.exception("Conversion failed")
                return func.HttpResponse(f"Conversion failed: {exc}", status_code=500)

            output_files = sorted(output_dir.glob("*.xml")) + sorted(
                output_dir.glob("*_OR.html")
            )
            if not output_files:
                return func.HttpResponse(
                    "Conversion produced no output files.", status_code=500
                )

            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as archive:
                for output_file in output_files:
                    archive.write(output_file, output_file.name)
            zip_buffer.seek(0)

            return func.HttpResponse(
                body=zip_buffer.getvalue(),
                status_code=200,
                mimetype="application/zip",
                headers={"Content-Disposition": "attachment; filename=converted.zip"},
            )
    except Exception as exc:
        logging.exception("Unexpected error during conversion")
        return func.HttpResponse(f"Internal server error: {exc}", status_code=500)
