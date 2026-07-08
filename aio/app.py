"""
Standalone G30 → G60 converter GUI (Flet).

Default workflow: G30 .urs device export → G60 .urs (Enervista-ready).
Also supports G30 .xml → G60 .xml + HTML report.
"""

from __future__ import annotations

import io
import os
import sys
import webbrowser
from pathlib import Path

import flet as ft

APP_DIR = Path(__file__).resolve().parent
REPO_ROOT = APP_DIR.parent

if getattr(sys, "frozen", False):
    _bundle_root = Path(getattr(sys, "_MEIPASS", APP_DIR))
    for _path in (_bundle_root, APP_DIR):
        if str(_path) not in sys.path:
            sys.path.insert(0, str(_path))
else:
    if str(REPO_ROOT) not in sys.path:
        sys.path.insert(0, str(REPO_ROOT))
    if str(APP_DIR) not in sys.path:
        sys.path.insert(0, str(APP_DIR))

from convert_g30_to_g60 import convert, validate_g30_settings_xml  # noqa: E402
from convert_g30_to_g60_urs import convert_urs  # noqa: E402
from urs_io import parse_urs_file, resolve_urs_template  # noqa: E402

from base_templates import BaseTemplateInfo, app_base_dir, discover_base_templates  # noqa: E402

# Design tokens — aligned with the HTML conversion report.
NAVY = "#1a2744"
BG = "#f4f6f9"
CARD = "#ffffff"
BORDER = "#dde1e8"
TEXT = "#1a1d23"
DIM = "#6b7280"
ACCENT = "#1d6fb8"
OK = "#1a7a44"
WARN = "#b45309"
ERROR = "#b91c1c"

STEP_LABELS = ("Start", "Source", "Firmware", "Output", "Convert")
WELCOME_STEP, SOURCE_STEP, FIRMWARE_STEP, OUTPUT_STEP, CONVERT_STEP = range(5)


def default_output_dir() -> Path:
    return Path.home() / "Desktop" / "G60_Conversion"


def _human_size(num_bytes: int) -> str:
    if num_bytes < 1024:
        return f"{num_bytes} B"
    if num_bytes < 1024 * 1024:
        return f"{num_bytes / 1024:.1f} KB"
    return f"{num_bytes / (1024 * 1024):.1f} MB"


class ConverterWizard:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.file_picker = ft.FilePicker()
        page.services.append(self.file_picker)

        self.step = WELCOME_STEP
        self.format_mode = "urs"
        self.g30_path = ""
        self.output_dir = str(default_output_dir())
        self.selected_template_idx = 0
        self.templates: list[BaseTemplateInfo] = []
        self.busy = False
        self.log_text = ""
        self.error_text = ""
        self._last_xml: Path | None = None
        self._last_html: Path | None = None
        self._last_urs: Path | None = None

        self.content_area = ft.Container(expand=True)
        self.header_area = ft.Container()
        self.next_btn = ft.FilledButton(content="Next", on_click=self._on_next)
        self.back_btn = ft.OutlinedButton(content="Back", on_click=self._on_back)
        self.step_row = ft.Row(alignment=ft.MainAxisAlignment.CENTER, spacing=8)

        self._configure_page()
        self._reload_bases()
        self._render()

    def _configure_page(self) -> None:
        self.page.title = "G30 → G60 Converter"
        self.page.bgcolor = BG
        self.page.padding = 0
        self.page.theme = ft.Theme(font_family="Segoe UI", color_scheme_seed=ACCENT)
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.window.width = 760
        self.page.window.height = 640
        self.page.window.min_width = 680
        self.page.window.min_height = 560

    def _reload_bases(self) -> None:
        self.templates = discover_base_templates(app_base_dir())
        if not self.templates:
            return
        default_idx = next(
            (i for i, t in enumerate(self.templates) if t.path.name == "G60 Base.xml"),
            0,
        )
        self.selected_template_idx = default_idx

    def _selected_template(self) -> BaseTemplateInfo:
        if not self.templates:
            raise ValueError("No target firmware base templates are bundled.")
        idx = self.selected_template_idx
        if idx < 0 or idx >= len(self.templates):
            raise ValueError("Select a target firmware base template.")
        return self.templates[idx]

    def _render(self) -> None:
        self._refresh_step_row()
        self.header_area.content = self._build_header()
        self.content_area.content = self._build_step_content()
        self._refresh_nav()
        if not self.page.controls:
            body = ft.Container(
                expand=True,
                padding=ft.Padding.symmetric(horizontal=28, vertical=20),
                content=ft.Column(
                    expand=True,
                    spacing=16,
                    controls=[
                        self.header_area,
                        ft.Divider(height=1, color=BORDER),
                        self.step_row,
                        self.content_area,
                        ft.Row(
                            alignment=ft.MainAxisAlignment.END,
                            controls=[self.back_btn, self.next_btn],
                        ),
                    ],
                ),
            )
            self.page.add(
                ft.Column(
                    expand=True,
                    spacing=0,
                    controls=[body],
                )
            )
        else:
            self.page.update()

    def _refresh_step_row(self) -> None:
        items: list[ft.Control] = []
        for idx, label in enumerate(STEP_LABELS):
            if idx > 0:
                items.append(
                    ft.Container(
                        width=28,
                        height=2,
                        bgcolor=ACCENT if idx <= self.step else BORDER,
                    )
                )
            done = idx < self.step
            active = idx == self.step
            circle_bg = ACCENT if done or active else BORDER
            circle_fg = "#ffffff" if done or active else DIM
            circle_content = (
                ft.Icon(ft.Icons.CHECK, size=14, color="#ffffff")
                if done
                else ft.Text(str(idx + 1), size=12, weight=ft.FontWeight.W_600, color=circle_fg)
            )
            items.append(
                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=4,
                    controls=[
                        ft.Container(
                            width=28,
                            height=28,
                            border_radius=14,
                            bgcolor=circle_bg,
                            alignment=ft.Alignment.CENTER,
                            content=circle_content,
                        ),
                        ft.Text(
                            label,
                            size=11,
                            weight=ft.FontWeight.W_600 if active else ft.FontWeight.NORMAL,
                            color=ACCENT if active else DIM,
                        ),
                    ],
                )
            )
        self.step_row.controls = items

    def _refresh_nav(self) -> None:
        self.back_btn.disabled = self.step == WELCOME_STEP or self.busy
        if self.step == CONVERT_STEP:
            if self.busy:
                self.next_btn.visible = False
            elif self._conversion_succeeded():
                self.next_btn.content = "Convert another"
                self.next_btn.visible = True
                self.next_btn.disabled = False
            else:
                self.next_btn.visible = False
        elif self.step == OUTPUT_STEP:
            self.next_btn.content = "Convert to G60"
            self.next_btn.visible = True
            self.next_btn.disabled = not self._step_valid(OUTPUT_STEP)
        else:
            self.next_btn.content = "Next"
            self.next_btn.visible = True
            self.next_btn.disabled = not self._step_valid(self.step)

    def _step_valid(self, step: int) -> bool:
        if step == WELCOME_STEP:
            return bool(self.templates)
        if step == SOURCE_STEP:
            return self._source_validation_error() is None
        if step == FIRMWARE_STEP:
            if not self.templates:
                return False
            try:
                template = self._selected_template()
            except ValueError:
                return False
            if self.format_mode == "urs":
                return template.has_urs_pair
            return True
        if step == OUTPUT_STEP:
            return bool(self.output_dir.strip())
        return True

    def _source_validation_error(self) -> str | None:
        if not self.g30_path.strip():
            return "Select a source file."
        path = Path(self.g30_path)
        if not path.is_file():
            return "File not found."

        expected_ext = ".urs" if self.format_mode == "urs" else ".xml"
        if path.suffix.lower() != expected_ext:
            label = "URS" if self.format_mode == "urs" else "XML"
            return f"Select a {label} file for this conversion type."

        try:
            if self.format_mode == "urs":
                parsed = parse_urs_file(path)
                order_code = (parsed.order_code or "").upper()
                if order_code.startswith("G60"):
                    return "This file appears to be a G60 device export. Select a G30 .urs file."
            else:
                validate_g30_settings_xml(path)
        except ValueError as exc:
            return str(exc)
        return None

    def _build_header(self) -> ft.Control:
        return ft.Container(
            padding=ft.Padding.only(bottom=4),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.START,
                controls=[
                    ft.Column(
                        spacing=2,
                        expand=True,
                        controls=[
                            ft.Text(
                                "G30 → G60 Converter",
                                size=18,
                                weight=ft.FontWeight.W_600,
                                color=NAVY,
                            ),
                            ft.Text(
                                "Convert GE Multilin UR G30 relay settings for G60 import",
                                size=12,
                                color=DIM,
                            ),
                        ],
                    ),
                    ft.Container(
                        bgcolor="#eef3fa",
                        border_radius=16,
                        padding=ft.Padding.symmetric(horizontal=12, vertical=4),
                        content=ft.Text(
                            f"Step {self.step + 1} of {len(STEP_LABELS)}",
                            size=12,
                            color=ACCENT,
                            weight=ft.FontWeight.W_600,
                        ),
                    ),
                ],
            ),
        )

    def _conversion_succeeded(self) -> bool:
        return bool(self._last_urs or self._last_xml) and not self.error_text

    async def _on_back(self, _event: ft.ControlEvent) -> None:
        if self.step > WELCOME_STEP and not self.busy:
            self.step -= 1
            self._render()

    async def _on_next(self, _event: ft.ControlEvent) -> None:
        if self.busy:
            return
        if self.step == CONVERT_STEP and self._conversion_succeeded():
            self._reset_for_new_run()
            return
        if self.step == OUTPUT_STEP:
            self.step = CONVERT_STEP
            self._render()
            self._start_convert()
            return
        if self._step_valid(self.step) and self.step < OUTPUT_STEP:
            self.step += 1
            self._render()

    def _reset_for_new_run(self) -> None:
        self.step = WELCOME_STEP
        self.g30_path = ""
        self.error_text = ""
        self.log_text = ""
        self._last_xml = None
        self._last_html = None
        self._last_urs = None
        self._render()

    def _card(self, content: ft.Control, *, padding: int = 20) -> ft.Container:
        return ft.Container(
            bgcolor=CARD,
            border=ft.Border.all(1, BORDER),
            border_radius=8,
            padding=padding,
            content=content,
        )

    def _section_title(self, title: str, subtitle: str) -> ft.Column:
        return ft.Column(
            spacing=4,
            controls=[
                ft.Text(title, size=20, weight=ft.FontWeight.W_600, color=TEXT),
                ft.Text(subtitle, size=13, color=DIM),
            ],
        )

    def _build_step_content(self) -> ft.Control:
        builders = (
            self._build_welcome_step,
            self._build_source_step,
            self._build_firmware_step,
            self._build_output_step,
            self._build_convert_step,
        )
        return builders[self.step]()

    def _build_welcome_step(self) -> ft.Control:
        if not self.templates:
            return self._card(
                ft.Column(
                    spacing=12,
                    controls=[
                        ft.Icon(ft.Icons.ERROR_OUTLINE, color=ERROR, size=32),
                        ft.Text(
                            "No G60 base templates found in the bundled bases/ folder.",
                            color=ERROR,
                            size=14,
                        ),
                        ft.Text(
                            f"Expected location: {app_base_dir()}",
                            size=12,
                            color=DIM,
                        ),
                    ],
                )
            )

        def format_card(
            mode: str,
            title: str,
            description: str,
            badge: str,
            recommended: bool = False,
        ) -> ft.Container:
            selected = self.format_mode == mode
            border_color = ACCENT if selected else BORDER
            bg = "#f0f7ff" if selected else CARD
            return ft.Container(
                border=ft.Border.all(2 if selected else 1, border_color),
                border_radius=8,
                bgcolor=bg,
                padding=16,
                on_click=lambda _e, m=mode: self._set_format_mode(m),
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Column(
                            spacing=4,
                            expand=True,
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            title,
                                            size=15,
                                            weight=ft.FontWeight.W_600,
                                            color=TEXT,
                                        ),
                                        ft.Container(
                                            bgcolor="#dbeafe" if recommended else "#f3f4f6",
                                            border_radius=4,
                                            padding=ft.Padding.symmetric(horizontal=8, vertical=2),
                                            content=ft.Text(
                                                badge,
                                                size=10,
                                                weight=ft.FontWeight.W_700,
                                                color=ACCENT if recommended else DIM,
                                            ),
                                        ),
                                    ],
                                    spacing=8,
                                ),
                                ft.Text(description, size=13, color=DIM),
                            ],
                        ),
                        ft.Icon(
                            ft.Icons.RADIO_BUTTON_CHECKED if selected else ft.Icons.RADIO_BUTTON_OFF,
                            color=ACCENT if selected else DIM,
                        ),
                    ],
                ),
            )

        return ft.Column(
            scroll=ft.ScrollMode.AUTO,
            spacing=16,
            controls=[
                self._section_title(
                    "Welcome",
                    "This wizard walks you through converting a G30 relay export into G60 format.",
                ),
                self._card(
                    ft.Column(
                        spacing=12,
                        controls=[
                            ft.Text("What are you converting?", size=14, weight=ft.FontWeight.W_600),
                            format_card(
                                "urs",
                                "URS device export",
                                "Recommended. Produces a .urs file ready to import in EnerVista on the G60.",
                                "Recommended",
                                recommended=True,
                            ),
                            format_card(
                                "xml",
                                "XML settings export",
                                "Legacy path. Produces G60 .xml plus an HTML conversion report for review.",
                                "Advanced",
                            ),
                        ],
                    )
                ),
                self._card(
                    ft.Column(
                        spacing=8,
                        controls=[
                            ft.Text("Before you begin", size=14, weight=ft.FontWeight.W_600),
                            ft.Text("1. Export your G30 settings from EnerVista as a .urs file.", size=13, color=DIM),
                            ft.Text(
                                "2. Know the target G60 firmware version you will load the file onto.",
                                size=13,
                                color=DIM,
                            ),
                            ft.Text(
                                "3. After conversion, import the output into UR Setup on the G60.",
                                size=13,
                                color=DIM,
                            ),
                        ],
                    ),
                    padding=16,
                ),
            ],
        )

    def _set_format_mode(self, mode: str) -> None:
        if mode == self.format_mode:
            return
        self.format_mode = mode
        if self.g30_path:
            expected = ".urs" if mode == "urs" else ".xml"
            if Path(self.g30_path).suffix.lower() != expected:
                self.g30_path = ""
        self._render()

    def _build_source_step(self) -> ft.Control:
        path = Path(self.g30_path) if self.g30_path else None
        validation_error = self._source_validation_error() if self.g30_path else None
        valid = validation_error is None and bool(path and path.is_file())
        expected = ".urs" if self.format_mode == "urs" else ".xml"
        picker_ext = "urs" if self.format_mode == "urs" else "xml"

        drop_border = ACCENT if valid else BORDER
        drop_bg = "#f0f7ff" if valid else "#fafbfc"

        summary: list[ft.Control] = []
        if valid and path is not None:
            summary.append(
                self._card(
                    ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.INSERT_DRIVE_FILE, color=ACCENT),
                            ft.Column(
                                expand=True,
                                spacing=2,
                                controls=[
                                    ft.Text(path.name, size=14, weight=ft.FontWeight.W_600),
                                    ft.Text(
                                        f"{_human_size(path.stat().st_size)} · {path.parent}",
                                        size=12,
                                        color=DIM,
                                    ),
                                ],
                            ),
                            ft.Icon(ft.Icons.CHECK_CIRCLE, color=OK),
                        ],
                    ),
                    padding=14,
                )
            )
        elif self.g30_path and validation_error:
            summary.append(
                ft.Text(
                    validation_error,
                    size=13,
                    color=ERROR,
                )
            )

        async def browse(_event: ft.ControlEvent) -> None:
            files = await self.file_picker.pick_files(
                dialog_title=f"Select G30 source file ({picker_ext.upper()})",
                file_type=ft.FilePickerFileType.CUSTOM,
                allowed_extensions=[picker_ext],
                allow_multiple=False,
            )
            if files and files[0].path:
                self.g30_path = files[0].path
                self._render()

        return ft.Column(
            scroll=ft.ScrollMode.AUTO,
            spacing=16,
            controls=[
                self._section_title(
                    "Select source file",
                    f"Choose the G30 {expected} export from EnerVista.",
                ),
                ft.Container(
                    border=ft.Border.all(2, drop_border),
                    border_radius=8,
                    bgcolor=drop_bg,
                    padding=28,
                    on_click=browse,
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10,
                        controls=[
                            ft.Icon(ft.Icons.UPLOAD_FILE, size=40, color=ACCENT),
                            ft.Text(
                                f"Click to browse for a G30 {expected} file",
                                size=15,
                                weight=ft.FontWeight.W_600,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Text(
                                "Export from EnerVista: Device → Export → URS format"
                                if self.format_mode == "urs"
                                else "UR Setup settings XML export",
                                size=12,
                                color=DIM,
                                text_align=ft.TextAlign.CENTER,
                            ),
                        ],
                    ),
                ),
                *summary,
            ],
        )

    def _build_firmware_step(self) -> ft.Control:
        cards: list[ft.Control] = []
        for idx, template in enumerate(self.templates):
            selected = idx == self.selected_template_idx
            urs_ok = template.has_urs_pair
            disabled = self.format_mode == "urs" and not urs_ok
            border_color = ACCENT if selected else BORDER
            bg = "#f0f7ff" if selected else CARD

            status_icon = ft.Icons.CHECK_CIRCLE if urs_ok else ft.Icons.WARNING_AMBER_ROUNDED
            status_color = OK if urs_ok else WARN
            status_text = (
                f"URS base available ({template.urs_path.name})"
                if urs_ok
                else "No paired .urs base — URS conversion unavailable"
            )

            cards.append(
                ft.Container(
                    border=ft.Border.all(2 if selected else 1, border_color),
                    border_radius=8,
                    bgcolor=bg if not disabled else "#fafafa",
                    opacity=0.55 if disabled else 1.0,
                    padding=14,
                    on_click=None if disabled else lambda _e, i=idx: self._select_template(i),
                    content=ft.Row(
                        controls=[
                            ft.Column(
                                expand=True,
                                spacing=4,
                                controls=[
                                    ft.Text(
                                        f"Firmware {template.version or 'unknown'}",
                                        size=15,
                                        weight=ft.FontWeight.W_600,
                                    ),
                                    ft.Text(
                                        template.order_code or template.path.name,
                                        size=12,
                                        color=DIM,
                                    ),
                                    ft.Row(
                                        spacing=6,
                                        controls=[
                                            ft.Icon(status_icon, size=16, color=status_color),
                                            ft.Text(status_text, size=12, color=status_color),
                                        ],
                                    ),
                                ],
                            ),
                            ft.Icon(
                                ft.Icons.RADIO_BUTTON_CHECKED if selected else ft.Icons.RADIO_BUTTON_OFF,
                                color=ACCENT if selected else DIM,
                            ),
                        ],
                    ),
                )
            )

        return ft.Column(
            scroll=ft.ScrollMode.AUTO,
            spacing=16,
            controls=[
                self._section_title(
                    "Choose target firmware",
                    "Pick the G60 firmware version you will load the converted settings onto.",
                ),
                ft.Column(spacing=10, controls=cards),
            ],
        )

    def _select_template(self, idx: int) -> None:
        self.selected_template_idx = idx
        self._render()

    def _build_output_step(self) -> ft.Control:
        g30 = Path(self.g30_path)
        try:
            template = self._selected_template()
            fw_label = f"Firmware {template.version}"
        except ValueError:
            fw_label = "—"

        output_hint = (
            "G60 .urs (EnerVista-ready)"
            if self.format_mode == "urs"
            else "G60 .xml + HTML conversion report"
        )

        async def browse_output(_event: ft.ControlEvent) -> None:
            directory = await self.file_picker.get_directory_path(
                dialog_title="Select output folder",
                initial_directory=self.output_dir or None,
            )
            if directory:
                self.output_dir = directory
                self._render()

        return ft.Column(
            scroll=ft.ScrollMode.AUTO,
            spacing=16,
            controls=[
                self._section_title(
                    "Output location",
                    "Choose where the converted file should be saved.",
                ),
                ft.Row(
                    controls=[
                        ft.TextField(
                            value=self.output_dir,
                            expand=True,
                            read_only=True,
                            border_color=BORDER,
                            on_change=lambda e: None,
                        ),
                        ft.OutlinedButton(content="Browse…", on_click=browse_output),
                    ],
                ),
                self._card(
                    ft.Column(
                        spacing=10,
                        controls=[
                            ft.Text("Review", size=14, weight=ft.FontWeight.W_600),
                            self._review_row("Source", g30.name),
                            self._review_row("Target firmware", fw_label),
                            self._review_row("Output", output_hint),
                            self._review_row("Folder", self.output_dir),
                        ],
                    ),
                ),
            ],
        )

    def _review_row(self, label: str, value: str) -> ft.Row:
        return ft.Row(
            controls=[
                ft.Text(label, width=130, size=13, color=DIM),
                ft.Text(value, expand=True, size=13, color=TEXT),
            ],
        )

    def _build_convert_step(self) -> ft.Control:
        if self.busy:
            return ft.Container(
                alignment=ft.Alignment.CENTER,
                expand=True,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=16,
                    controls=[
                        ft.ProgressRing(width=48, height=48, color=ACCENT),
                        ft.Text("Converting settings…", size=18, weight=ft.FontWeight.W_600),
                        ft.Text("This may take a moment for large device files.", size=13, color=DIM),
                    ],
                ),
            )

        if self.error_text:
            return ft.Column(
                scroll=ft.ScrollMode.AUTO,
                spacing=16,
                controls=[
                    ft.Container(
                        alignment=ft.Alignment.CENTER,
                        content=ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=8,
                            controls=[
                                ft.Icon(ft.Icons.ERROR_OUTLINE, size=48, color=ERROR),
                                ft.Text("Conversion failed", size=20, weight=ft.FontWeight.W_600, color=ERROR),
                                ft.Text(self.error_text, size=13, color=DIM, text_align=ft.TextAlign.CENTER),
                            ],
                        ),
                    ),
                    self._log_expansion(),
                    ft.Row(
                        controls=[
                            ft.OutlinedButton(
                                content="Back to output",
                                on_click=self._back_from_failure,
                            ),
                        ],
                    ),
                ],
            )

        result_name = (
            self._last_urs.name
            if self._last_urs
            else self._last_xml.name
            if self._last_xml
            else "output"
        )
        actions: list[ft.Control] = [
            ft.FilledButton(
                content="Open converted file",
                icon=ft.Icons.FOLDER_OPEN,
                on_click=lambda _e: self._open_result(),
            ),
            ft.OutlinedButton(
                content="Open output folder",
                on_click=lambda _e: self._open_output(),
            ),
        ]
        if self._last_html:
            actions.append(
                ft.OutlinedButton(
                    content="Open HTML report",
                    on_click=lambda _e: self._open_report(),
                )
            )

        return ft.Column(
            scroll=ft.ScrollMode.AUTO,
            spacing=16,
            controls=[
                ft.Container(
                    alignment=ft.Alignment.CENTER,
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=8,
                        controls=[
                            ft.Icon(ft.Icons.CHECK_CIRCLE, size=56, color=OK),
                            ft.Text("Conversion complete", size=22, weight=ft.FontWeight.W_600, color=OK),
                            ft.Text(result_name, size=15, weight=ft.FontWeight.W_600),
                            ft.Text(f"Saved to {self.output_dir}", size=13, color=DIM),
                        ],
                    ),
                ),
                self._card(
                    ft.Column(
                        spacing=8,
                        controls=[
                            ft.Text("Next steps", size=14, weight=ft.FontWeight.W_600),
                            ft.Text(
                                "1. Open the converted file in UR Setup on your G60 relay.",
                                size=13,
                                color=DIM,
                            ),
                            ft.Text(
                                "2. Review any warnings in the HTML report before commissioning."
                                if self._last_html
                                else "2. Verify settings in EnerVista before commissioning.",
                                size=13,
                                color=DIM,
                            ),
                            ft.Text(
                                "3. Confirm there are zero Invalid Settings after import.",
                                size=13,
                                color=DIM,
                            ),
                        ],
                    ),
                    padding=16,
                ),
                ft.Row(wrap=True, spacing=10, controls=actions),
                self._log_expansion(),
            ],
        )

    def _log_expansion(self) -> ft.ExpansionTile:
        return ft.ExpansionTile(
            title=ft.Text("Show conversion log", size=13, color=DIM),
            controls=[
                ft.Container(
                    bgcolor="#f0f3f8",
                    border_radius=6,
                    padding=12,
                    content=ft.Text(
                        self.log_text or "(no log output)",
                        font_family="Consolas",
                        size=11,
                        color=TEXT,
                        selectable=True,
                    ),
                ),
            ],
        )

    async def _back_from_failure(self, _event: ft.ControlEvent) -> None:
        if not self.busy:
            self.step = OUTPUT_STEP
            self.error_text = ""
            self._render()

    def _start_convert(self) -> None:
        g30 = Path(self.g30_path)
        out_dir = Path(self.output_dir.strip() or str(default_output_dir()))
        self.busy = True
        self.error_text = ""
        self.log_text = ""
        self._last_xml = None
        self._last_html = None
        self._last_urs = None
        self._render()

        if self.format_mode == "urs":
            template = self._selected_template()
            self.page.run_thread(self._run_urs_convert, g30, template, out_dir)
        else:
            template = self._selected_template()
            self.page.run_thread(self._run_xml_convert, g30, template.path, out_dir)

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
        self.page.run_task(self._xml_convert_done, out_dir, buffer.getvalue(), error)

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
        self.page.run_task(self._urs_convert_done, out_dir, buffer.getvalue(), error, output_path)

    async def _xml_convert_done(
        self,
        out_dir: Path,
        log_text: str,
        error: Exception | None,
    ) -> None:
        self.busy = False
        self.log_text = log_text
        if error:
            self.error_text = str(error)
            self._render()
            return

        xml_files = sorted(out_dir.glob("*.xml"), key=lambda p: p.stat().st_mtime, reverse=True)
        html_files = sorted(out_dir.glob("*_OR.html"), key=lambda p: p.stat().st_mtime, reverse=True)
        self._last_xml = xml_files[0] if xml_files else None
        self._last_html = html_files[0] if html_files else None
        self._render()

    async def _urs_convert_done(
        self,
        out_dir: Path,
        log_text: str,
        error: Exception | None,
        output_path: Path | None,
    ) -> None:
        self.busy = False
        self.log_text = log_text
        if error:
            self.error_text = str(error)
            self._render()
            return

        self._last_urs = output_path
        if self._last_urs is None or not self._last_urs.is_file():
            urs_files = sorted(out_dir.glob("*.urs"), key=lambda p: p.stat().st_mtime, reverse=True)
            self._last_urs = urs_files[0] if urs_files else None
        self._render()

    def _open_output(self) -> None:
        path = Path(self.output_dir.strip() or str(default_output_dir()))
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


async def main(page: ft.Page) -> None:
    ConverterWizard(page)


def main_entry() -> None:
    ft.run(main)


if __name__ == "__main__":
    main_entry()
