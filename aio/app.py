"""
Standalone G30 → G60 converter GUI.

Default workflow: G30 .urs device export → G60 .urs (Enervista-ready).
Also supports G30 .xml → G60 .xml + HTML report.
"""

from __future__ import annotations

import io
import os
import sys
import threading
import tkinter as tk
import webbrowser
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

APP_DIR = Path(__file__).resolve().parent
REPO_ROOT = APP_DIR.parent

if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from convert_g30_to_g60 import convert  # noqa: E402
from convert_g30_to_g60_urs import convert_urs  # noqa: E402
from urs_io import resolve_urs_template  # noqa: E402

from base_templates import BaseTemplateInfo, app_base_dir, discover_base_templates  # noqa: E402


def default_output_dir() -> Path:
    return Path.home() / "Desktop" / "G60_Conversion"


class ConverterApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("G30 → G60 Converter")
        self.minsize(560, 480)
        self.geometry("680x500")

        self.g30_path = tk.StringVar()
        self.output_dir = tk.StringVar(value=str(default_output_dir()))
        self.base_choice = tk.StringVar()
        self.status = tk.StringVar(value="Select a G30 .urs file and target firmware.")
        self._templates: list[BaseTemplateInfo] = []
        self._last_xml: Path | None = None
        self._last_html: Path | None = None
        self._last_urs: Path | None = None
        self._busy = False

        self._build_ui()
        self._reload_bases()

    def _build_ui(self) -> None:
        pad = {"padx": 10, "pady": 4}
        outer = ttk.Frame(self, padding=10)
        outer.pack(fill=tk.BOTH, expand=True)

        ttk.Label(
            outer,
            text="Converts G30 relay settings to G60 format. "
            "URS device exports (.urs) are the default — ready for EnerVista.",
            wraplength=620,
        ).grid(row=0, column=0, columnspan=3, sticky=tk.W, padx=10, pady=(0, 6))

        ttk.Label(outer, text="Target firmware:").grid(row=1, column=0, sticky=tk.W, **pad)
        self.base_combo = ttk.Combobox(
            outer, textvariable=self.base_choice, state="readonly", width=56
        )
        self.base_combo.grid(row=1, column=1, columnspan=2, sticky=tk.EW, **pad)
        self.base_combo.bind("<<ComboboxSelected>>", self._on_firmware_changed)

        ttk.Label(outer, text="Output folder:").grid(row=2, column=0, sticky=tk.W, **pad)
        ttk.Entry(outer, textvariable=self.output_dir, width=58).grid(
            row=2, column=1, sticky=tk.EW, **pad
        )
        ttk.Button(outer, text="Browse…", command=self._browse_output).grid(row=2, column=2, **pad)

        ttk.Label(outer, text="G30 source file:").grid(row=3, column=0, sticky=tk.W, **pad)
        ttk.Entry(outer, textvariable=self.g30_path, width=58).grid(
            row=3, column=1, sticky=tk.EW, **pad
        )
        ttk.Button(outer, text="Browse…", command=self._browse_g30).grid(row=3, column=2, **pad)

        self.format_hint = ttk.Label(outer, text="", wraplength=620, foreground="#555")
        self.format_hint.grid(row=4, column=0, columnspan=3, sticky=tk.W, padx=10)

        btn_row = ttk.Frame(outer)
        btn_row.grid(row=5, column=0, columnspan=3, sticky=tk.W, padx=10, pady=(6, 0))
        self.convert_btn = ttk.Button(btn_row, text="Convert to G60", command=self._start_convert)
        self.convert_btn.pack(side=tk.LEFT, padx=(0, 8))
        ttk.Button(btn_row, text="Open output folder", command=self._open_output).pack(
            side=tk.LEFT, padx=(0, 8)
        )
        self.result_btn = ttk.Button(
            btn_row, text="Open converted file", command=self._open_result, state=tk.DISABLED
        )
        self.result_btn.pack(side=tk.LEFT, padx=(0, 8))
        self.report_btn = ttk.Button(
            btn_row, text="Open HTML report", command=self._open_report, state=tk.DISABLED
        )
        self.report_btn.pack(side=tk.LEFT)

        ttk.Label(outer, textvariable=self.status, wraplength=620).grid(
            row=6, column=0, columnspan=3, sticky=tk.W, **pad
        )

        self.log = tk.Text(outer, height=14, wrap=tk.WORD, state=tk.DISABLED)
        self.log.grid(row=7, column=0, columnspan=3, sticky=tk.NSEW, padx=10, pady=(0, 4))

        outer.columnconfigure(1, weight=1)
        outer.rowconfigure(7, weight=1)

        self.g30_path.trace_add("write", lambda *_: self._update_format_hint())

    def _reload_bases(self) -> None:
        base_dir = app_base_dir()
        self._templates = discover_base_templates(base_dir)
        labels = [t.label for t in self._templates]
        self.base_combo["values"] = labels

        if not labels:
            self.status.set(f"No base templates in {base_dir}. Add G60 Base*.xml files there.")
            self.convert_btn.config(state=tk.DISABLED)
            return

        default_idx = next(
            (i for i, t in enumerate(self._templates) if t.path.name == "G60 Base.xml"),
            0,
        )
        self.base_combo.current(default_idx)
        self._on_firmware_changed()

    def _on_firmware_changed(self, _event: object | None = None) -> None:
        self._update_format_hint()
        if not self._busy and self._templates:
            self.convert_btn.config(state=tk.NORMAL)

    def _update_format_hint(self) -> None:
        path = self.g30_path.get().strip()
        try:
            template = self._selected_template()
        except ValueError:
            template = None

        if path.lower().endswith(".urs"):
            if template and template.has_urs_pair:
                self.format_hint.config(
                    text=f"Output: G60 .urs  |  URS base: {template.urs_path.name}",
                    foreground="#333",
                )
            elif template:
                self.format_hint.config(
                    text=f"No paired .urs for {template.path.name}.",
                    foreground="#a33",
                )
            else:
                self.format_hint.config(text="Output: G60 .urs", foreground="#333")
        elif path.lower().endswith(".xml"):
            self.format_hint.config(
                text="Output: G60 .xml + HTML conversion report",
                foreground="#333",
            )
        else:
            self.format_hint.config(
                text="Select a G30 .urs file (recommended) or .xml settings export.",
                foreground="#555",
            )

    def _selected_template(self) -> BaseTemplateInfo:
        idx = self.base_combo.current()
        if idx < 0 or idx >= len(self._templates):
            raise ValueError("Select a target firmware base template.")
        return self._templates[idx]

    def _browse_g30(self) -> None:
        path = filedialog.askopenfilename(
            title="Select G30 source file",
            filetypes=[
                ("G30 device export (URS)", "*.urs"),
                ("UR Setup settings (XML)", "*.xml"),
                ("All files", "*.*"),
            ],
        )
        if path:
            self.g30_path.set(path)

    def _browse_output(self) -> None:
        path = filedialog.askdirectory(title="Select output folder")
        if path:
            self.output_dir.set(path)

    def _append_log(self, text: str) -> None:
        self.log.config(state=tk.NORMAL)
        self.log.insert(tk.END, text)
        self.log.see(tk.END)
        self.log.config(state=tk.DISABLED)

    def _set_busy(self, busy: bool) -> None:
        self._busy = busy
        self.convert_btn.config(state=tk.DISABLED if busy else tk.NORMAL)

    def _clear_log(self) -> None:
        self.log.config(state=tk.NORMAL)
        self.log.delete("1.0", tk.END)
        self.log.config(state=tk.DISABLED)

    def _output_path(self) -> Path:
        return Path(self.output_dir.get().strip() or str(default_output_dir()))

    def _start_convert(self) -> None:
        if self._busy:
            return

        g30 = Path(self.g30_path.get().strip())
        if not g30.is_file():
            messagebox.showerror("Missing file", "Select a valid G30 .urs or .xml file.")
            return

        suffix = g30.suffix.lower()
        if suffix == ".urs":
            self._start_urs_convert(g30)
        elif suffix == ".xml":
            self._start_xml_convert(g30)
        else:
            messagebox.showerror(
                "Unsupported file",
                "Select a G30 .urs device export or .xml settings file.",
            )

    def _start_xml_convert(self, g30: Path) -> None:
        try:
            template = self._selected_template()
        except ValueError as exc:
            messagebox.showerror("Missing base", str(exc))
            return

        out_dir = self._output_path()
        self._last_xml = None
        self._last_html = None
        self._last_urs = None
        self.result_btn.config(state=tk.DISABLED)
        self.report_btn.config(state=tk.DISABLED)
        self._clear_log()
        self.status.set("Converting XML…")
        self._set_busy(True)

        threading.Thread(
            target=self._run_xml_convert,
            args=(g30, template.path, out_dir),
            daemon=True,
        ).start()

    def _start_urs_convert(self, g30: Path) -> None:
        try:
            template = self._selected_template()
        except ValueError as exc:
            messagebox.showerror("Missing base", str(exc))
            return

        if not template.has_urs_pair:
            messagebox.showerror(
                "Missing URS base",
                f"No paired .urs template for {template.path.name}.\n\n"
                "Export a blank G60 .urs from UR Setup and save it as "
                f"{template.path.with_suffix('.urs').name} in bases/.",
            )
            return

        out_dir = self._output_path()
        self._last_xml = None
        self._last_html = None
        self._last_urs = None
        self.result_btn.config(state=tk.DISABLED)
        self.report_btn.config(state=tk.DISABLED)
        self._clear_log()
        self.status.set("Converting URS…")
        self._set_busy(True)

        threading.Thread(
            target=self._run_urs_convert,
            args=(g30, template, out_dir),
            daemon=True,
        ).start()

    def _run_xml_convert(self, g30: Path, template: Path, out_dir: Path) -> None:
        out_dir.mkdir(parents=True, exist_ok=True)
        buffer = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = buffer
        error: Exception | None = None
        try:
            convert(g30, template, out_dir)
        except Exception as exc:
            error = exc
        finally:
            sys.stdout = old_stdout

        self.after(0, lambda: self._xml_convert_done(out_dir, buffer.getvalue(), error))

    def _run_urs_convert(self, g30: Path, template: BaseTemplateInfo, out_dir: Path) -> None:
        out_dir.mkdir(parents=True, exist_ok=True)
        buffer = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = buffer
        error: Exception | None = None
        output_path: Path | None = None
        try:
            urs_template = resolve_urs_template(template.path, app_base_dir())
            output_path = convert_urs(g30, urs_template, template.path, out_dir)
        except Exception as exc:
            error = exc
        finally:
            sys.stdout = old_stdout

        self.after(
            0,
            lambda: self._urs_convert_done(out_dir, buffer.getvalue(), error, output_path),
        )

    def _xml_convert_done(
        self,
        out_dir: Path,
        log_text: str,
        error: Exception | None,
    ) -> None:
        self._set_busy(False)
        if log_text:
            self._append_log(log_text)

        if error:
            self.status.set(f"XML conversion failed: {error}")
            messagebox.showerror("Conversion failed", str(error))
            return

        xml_files = sorted(out_dir.glob("*.xml"), key=lambda p: p.stat().st_mtime, reverse=True)
        html_files = sorted(out_dir.glob("*_OR.html"), key=lambda p: p.stat().st_mtime, reverse=True)
        self._last_xml = xml_files[0] if xml_files else None
        self._last_html = html_files[0] if html_files else None

        if self._last_xml:
            self.result_btn.config(state=tk.NORMAL)
        if self._last_html:
            self.report_btn.config(state=tk.NORMAL)

        name = self._last_xml.name if self._last_xml else "output"
        self.status.set(f"Done — {name} written to {out_dir}")

    def _urs_convert_done(
        self,
        out_dir: Path,
        log_text: str,
        error: Exception | None,
        output_path: Path | None,
    ) -> None:
        self._set_busy(False)
        if log_text:
            self._append_log(log_text)

        if error:
            self.status.set(f"URS conversion failed: {error}")
            messagebox.showerror("Conversion failed", str(error))
            return

        self._last_urs = output_path
        if self._last_urs is None or not self._last_urs.is_file():
            urs_files = sorted(out_dir.glob("*.urs"), key=lambda p: p.stat().st_mtime, reverse=True)
            self._last_urs = urs_files[0] if urs_files else None

        if self._last_urs:
            self.result_btn.config(state=tk.NORMAL)

        name = self._last_urs.name if self._last_urs else "output"
        self.status.set(f"Done — {name} written to {out_dir}")

    def _open_output(self) -> None:
        path = self._output_path()
        path.mkdir(parents=True, exist_ok=True)
        os.startfile(path)

    def _open_result(self) -> None:
        if self._last_urs and self._last_urs.is_file():
            os.startfile(self._last_urs)
        elif self._last_xml and self._last_xml.is_file():
            os.startfile(self._last_xml)

    def _open_report(self) -> None:
        if self._last_html and self._last_html.is_file():
            webbrowser.open(self._last_html.as_uri())


def main() -> None:
    app = ConverterApp()
    app.mainloop()


if __name__ == "__main__":
    main()
