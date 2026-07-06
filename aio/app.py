"""
Standalone G30 → G60 converter GUI.

Imports convert() from the repo-root CLI script without modifying it.
Bundle base templates under aio/bases/ (G60 Base.xml, G60 Base 871.xml, …).
"""

from __future__ import annotations

import io
import sys
import threading
import tkinter as tk
import webbrowser
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

APP_DIR = Path(__file__).resolve().parent
REPO_ROOT = APP_DIR.parent


def default_output_dir() -> Path:
    return Path.home() / "Desktop" / "G60_Conversion"
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from convert_g30_to_g60 import convert  # noqa: E402

from base_templates import BaseTemplateInfo, app_base_dir, discover_base_templates


class ConverterApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("G30 → G60 Converter")
        self.minsize(520, 420)
        self.geometry("640x480")

        self.g30_path = tk.StringVar()
        self.output_dir = tk.StringVar(value=str(default_output_dir()))
        self.base_choice = tk.StringVar()
        self.status = tk.StringVar(value="Select a G30 settings file and target firmware.")
        self._templates: list[BaseTemplateInfo] = []
        self._last_xml: Path | None = None
        self._last_html: Path | None = None
        self._busy = False

        self._build_ui()
        self._reload_bases()

    def _build_ui(self) -> None:
        pad = {"padx": 10, "pady": 4}
        frame = ttk.Frame(self, padding=10)
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="G30 settings file:").grid(row=0, column=0, sticky=tk.W, **pad)
        ttk.Entry(frame, textvariable=self.g30_path, width=52).grid(
            row=0, column=1, sticky=tk.EW, **pad
        )
        ttk.Button(frame, text="Browse…", command=self._browse_g30).grid(row=0, column=2, **pad)

        ttk.Label(frame, text="Target firmware:").grid(row=1, column=0, sticky=tk.W, **pad)
        self.base_combo = ttk.Combobox(
            frame, textvariable=self.base_choice, state="readonly", width=49
        )
        self.base_combo.grid(row=1, column=1, columnspan=2, sticky=tk.EW, **pad)

        ttk.Label(frame, text="Output folder:").grid(row=2, column=0, sticky=tk.W, **pad)
        ttk.Entry(frame, textvariable=self.output_dir, width=52).grid(
            row=2, column=1, sticky=tk.EW, **pad
        )
        ttk.Button(frame, text="Browse…", command=self._browse_output).grid(row=2, column=2, **pad)

        btn_row = ttk.Frame(frame)
        btn_row.grid(row=3, column=0, columnspan=3, sticky=tk.EW, pady=(8, 4))
        self.convert_btn = ttk.Button(btn_row, text="Convert", command=self._start_convert)
        self.convert_btn.pack(side=tk.LEFT, padx=(0, 8))
        ttk.Button(btn_row, text="Open output folder", command=self._open_output).pack(
            side=tk.LEFT, padx=(0, 8)
        )
        self.report_btn = ttk.Button(
            btn_row, text="Open HTML report", command=self._open_report, state=tk.DISABLED
        )
        self.report_btn.pack(side=tk.LEFT)

        ttk.Label(frame, textvariable=self.status, wraplength=580).grid(
            row=4, column=0, columnspan=3, sticky=tk.W, **pad
        )

        self.log = tk.Text(frame, height=14, wrap=tk.WORD, state=tk.DISABLED)
        self.log.grid(row=5, column=0, columnspan=3, sticky=tk.NSEW, padx=10, pady=(0, 10))

        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(5, weight=1)

    def _reload_bases(self) -> None:
        base_dir = app_base_dir()
        self._templates = discover_base_templates(base_dir)
        labels = [t.label for t in self._templates]
        self.base_combo["values"] = labels

        if not labels:
            self.status.set(
                f"No base templates in {base_dir}. Add G60 Base*.xml files there."
            )
            self.convert_btn.config(state=tk.DISABLED)
            return

        self.convert_btn.config(state=tk.NORMAL)
        default_idx = next(
            (i for i, t in enumerate(self._templates) if t.path.name == "G60 Base.xml"),
            0,
        )
        self.base_combo.current(default_idx)

    def _selected_template(self) -> BaseTemplateInfo:
        idx = self.base_combo.current()
        if idx < 0 or idx >= len(self._templates):
            raise ValueError("Select a target firmware base template.")
        return self._templates[idx]

    def _browse_g30(self) -> None:
        path = filedialog.askopenfilename(
            title="Select G30 settings XML",
            filetypes=[("XML files", "*.xml"), ("All files", "*.*")],
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
        state = tk.DISABLED if busy else tk.NORMAL
        self.convert_btn.config(state=state if self._templates else tk.DISABLED)

    def _start_convert(self) -> None:
        if self._busy:
            return

        g30 = Path(self.g30_path.get().strip())
        if not g30.is_file():
            messagebox.showerror("Missing file", "Select a valid G30 settings XML file.")
            return

        out_dir = Path(self.output_dir.get().strip() or str(default_output_dir()))
        try:
            template = self._selected_template()
        except ValueError as exc:
            messagebox.showerror("Missing base", str(exc))
            return

        self._last_xml = None
        self._last_html = None
        self.report_btn.config(state=tk.DISABLED)
        self.log.config(state=tk.NORMAL)
        self.log.delete("1.0", tk.END)
        self.log.config(state=tk.DISABLED)
        self.status.set("Converting…")
        self._set_busy(True)

        thread = threading.Thread(
            target=self._run_convert,
            args=(g30, template.path, out_dir),
            daemon=True,
        )
        thread.start()

    def _run_convert(self, g30: Path, template: Path, out_dir: Path) -> None:
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

        log_text = buffer.getvalue()
        self.after(0, lambda: self._convert_done(g30, out_dir, log_text, error))

    def _convert_done(
        self,
        g30: Path,
        out_dir: Path,
        log_text: str,
        error: Exception | None,
    ) -> None:
        self._set_busy(False)
        if log_text:
            self._append_log(log_text)

        if error:
            self.status.set(f"Conversion failed: {error}")
            messagebox.showerror("Conversion failed", str(error))
            return

        xml_files = sorted(out_dir.glob("*.xml"), key=lambda p: p.stat().st_mtime, reverse=True)
        html_files = sorted(out_dir.glob("*_OR.html"), key=lambda p: p.stat().st_mtime, reverse=True)
        self._last_xml = xml_files[0] if xml_files else None
        self._last_html = html_files[0] if html_files else None

        if self._last_html:
            self.report_btn.config(state=tk.NORMAL)

        name = self._last_xml.name if self._last_xml else "output"
        self.status.set(f"Done — {name} written to {out_dir}")

    def _open_output(self) -> None:
        path = Path(self.output_dir.get().strip() or str(default_output_dir()))
        path.mkdir(parents=True, exist_ok=True)
        import os

        os.startfile(path)

    def _open_report(self) -> None:
        if self._last_html and self._last_html.is_file():
            webbrowser.open(self._last_html.as_uri())


def main() -> None:
    app = ConverterApp()
    app.mainloop()


if __name__ == "__main__":
    main()
