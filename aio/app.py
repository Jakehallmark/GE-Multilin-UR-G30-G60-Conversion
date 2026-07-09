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
import zipfile
from dataclasses import dataclass
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent
REPO_ROOT = APP_DIR.parent


def _bootstrap_flet_desktop_for_frozen() -> None:
    """Use bundled Flet desktop client from a writable app dir.

    PyInstaller builds still route through ``~/.flet/client`` by default, which
    can fail on locked-down PCs (WinError 5 on rename). Point FLET_VIEW_PATH
    at a copy under %LOCALAPPDATA% instead.
    """
    if not getattr(sys, "frozen", False) or os.environ.get("FLET_VIEW_PATH"):
        return

    bundle_root = Path(getattr(sys, "_MEIPASS", APP_DIR))
    archive = bundle_root / "flet_desktop" / "app" / "flet-windows.zip"
    if not archive.is_file():
        return

    try:
        import flet_desktop.version as flet_desktop_version  # type: ignore[import-untyped]
    except ImportError:
        return

    local_root = Path(
        os.environ.get("LOCALAPPDATA", os.environ.get("TEMP", "."))
    )
    cache_root = (
        local_root
        / "G30-to-G60-Converter"
        / f"flet-desktop-{flet_desktop_version.version}"
    )
    client_dir = cache_root / "flet"
    client_exe = client_dir / "flet.exe"
    ready_marker = cache_root / ".ready"

    if ready_marker.is_file() and client_exe.is_file():
        os.environ["FLET_VIEW_PATH"] = str(client_dir)
        return

    cache_root.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive, "r") as zf:
        zf.extractall(cache_root)

    if not client_exe.is_file():
        raise FileNotFoundError(
            f"Bundled Flet desktop client is missing flet.exe after extracting {archive}"
        )

    ready_marker.touch()
    os.environ["FLET_VIEW_PATH"] = str(client_dir)


if getattr(sys, "frozen", False):
    _bootstrap_flet_desktop_for_frozen()
    _bundle_root = Path(getattr(sys, "_MEIPASS", APP_DIR))
    for _path in (_bundle_root, APP_DIR):
        if str(_path) not in sys.path:
            sys.path.insert(0, str(_path))
else:
    if str(REPO_ROOT) not in sys.path:
        sys.path.insert(0, str(REPO_ROOT))
    if str(APP_DIR) not in sys.path:
        sys.path.insert(0, str(APP_DIR))

import flet as ft
from typing import Any, cast

from convert_g30_to_g60 import convert, validate_g30_settings_xml  # noqa: E402
from convert_g30_to_g60_urs import convert_urs  # noqa: E402
from verify_conversion import VerificationResult, write_verification_report  # noqa: E402
from urs_io import parse_urs_file, resolve_urs_template  # noqa: E402

from base_templates import BaseTemplateInfo, app_base_dir, discover_base_templates  # noqa: E402
from app_version import get_version_info  # noqa: E402


def _click(handler: Any) -> Any:
    """Bridge handler types for Flet's invariant ControlEventHandler stubs."""
    return handler


def _controls(controls: list[Any]) -> list[ft.Control]:
    return cast(list[ft.Control], controls)


@dataclass(frozen=True)
class Palette:
    navy: str
    background: str
    card: str
    border: str
    text: str
    dim: str
    accent: str
    ok: str
    warn: str
    error: str
    on_accent: str
    step_chip_bg: str
    selected_bg: str
    dropzone_bg: str
    badge_muted_bg: str
    badge_accent_bg: str
    disabled_bg: str
    log_bg: str


LIGHT_PALETTE = Palette(
    navy="#1a2744",
    background="#f4f6f9",
    card="#ffffff",
    border="#dde1e8",
    text="#1a1d23",
    dim="#6b7280",
    accent="#1d6fb8",
    ok="#1a7a44",
    warn="#b45309",
    error="#b91c1c",
    on_accent="#ffffff",
    step_chip_bg="#eef3fa",
    selected_bg="#f0f7ff",
    dropzone_bg="#fafbfc",
    badge_muted_bg="#f3f4f6",
    badge_accent_bg="#dbeafe",
    disabled_bg="#fafafa",
    log_bg="#f0f3f8",
)

DARK_PALETTE = Palette(
    navy="#e8edf5",
    background="#12151c",
    card="#1e2430",
    border="#2d3548",
    text="#e8eaed",
    dim="#9aa3b2",
    accent="#4a9eed",
    ok="#3ecf7a",
    warn="#f0a050",
    error="#f07070",
    on_accent="#ffffff",
    step_chip_bg="#1a3050",
    selected_bg="#1a2a3d",
    dropzone_bg="#181d28",
    badge_muted_bg="#2a3140",
    badge_accent_bg="#1e3a5f",
    disabled_bg="#1a1f2a",
    log_bg="#161b26",
)

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
        self._verification: VerificationResult | None = None
        self._verification_report_path: Path | None = None
        self.about_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("About G30 → G60 Converter"),
            actions=_controls([ft.TextButton(content="Close", on_click=_click(self._close_about))]),
            actions_alignment=ft.MainAxisAlignment.END,
        )

        self.content_area = ft.Container(expand=True)
        self.header_area = ft.Container()
        self.next_btn = ft.FilledButton(content="Next", on_click=_click(self._on_next))
        self.back_btn = ft.OutlinedButton(content="Back", on_click=_click(self._on_back))
        self.step_row = ft.Row(alignment=ft.MainAxisAlignment.CENTER, spacing=8)

        self._configure_page()
        self._reload_bases()
        self._render()

    @property
    def _pal(self) -> Palette:
        return DARK_PALETTE if self._is_dark_effective() else LIGHT_PALETTE

    def _is_dark_effective(self) -> bool:
        mode = self.page.theme_mode
        if mode == ft.ThemeMode.DARK:
            return True
        if mode == ft.ThemeMode.LIGHT:
            return False
        brightness = getattr(self.page, "platform_brightness", ft.Brightness.LIGHT)
        return brightness == ft.Brightness.DARK

    def _configure_page(self) -> None:
        info = get_version_info()
        self.page.title = f"G30 → G60 Converter {info.version}"
        self.page.padding = 0
        self.page.theme_mode = ft.ThemeMode.SYSTEM
        self.page.window.width = 800
        self.page.window.height = 820
        self.page.window.min_width = 700
        self.page.window.min_height = 680
        self.page.on_platform_brightness_change = self._on_platform_brightness_change
        self._apply_theme()

    def _apply_theme(self) -> None:
        pal = self._pal
        self.page.bgcolor = pal.background
        self.page.theme = ft.Theme(font_family="Segoe UI", color_scheme_seed=pal.accent)
        self.page.dark_theme = ft.Theme(font_family="Segoe UI", color_scheme_seed=pal.accent)

    def _on_platform_brightness_change(self, _event: ft.PlatformBrightnessChangeEvent) -> None:
        if self.page.theme_mode != ft.ThemeMode.SYSTEM:
            return
        self._apply_theme()
        self._render()

    async def _toggle_theme(self, _event: ft.ControlEvent) -> None:
        self.page.theme_mode = (
            ft.ThemeMode.LIGHT if self._is_dark_effective() else ft.ThemeMode.DARK
        )
        self._apply_theme()
        self._render()

    def _close_about(self, _event: ft.ControlEvent) -> None:
        self.page.pop_dialog()

    async def _show_about(self, _event: ft.ControlEvent) -> None:
        info = get_version_info()
        pal = self._pal
        self.about_dialog.content = ft.Column(
            tight=True,
            spacing=10,
            controls=[
                ft.Text(f"Version {info.display}", size=15, weight=ft.FontWeight.W_600, color=pal.text),
                ft.Text(
                    "Converts GE Multilin UR G30 relay settings for G60 upgrades.",
                    size=13,
                    color=pal.dim,
                ),
                ft.Text(
                    "GitHub: github.com/Jakehallmark/GE-Multilin-UR-G30-G60-Conversion",
                    size=12,
                    color=pal.accent,
                    selectable=True,
                ),
                ft.Text(
                    "Built by Jacob Hallmark, Product Support",
                    size=12,
                    color=pal.dim,
                ),
            ],
        )
        self.page.show_dialog(self.about_dialog)

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
                padding=ft.Padding.symmetric(horizontal=28, vertical=16),
                content=ft.Column(
                    expand=True,
                    spacing=12,
                    controls=_controls([
                        self.header_area,
                        ft.Divider(height=1, color=self._pal.border),
                        self.step_row,
                        self.content_area,
                        ft.Row(
                            alignment=ft.MainAxisAlignment.END,
                            controls=_controls([self.back_btn, self.next_btn]),
                        ),
                    ]),
                ),
            )
            self.page.add(
                ft.Column(
                    expand=True,
                    spacing=0,
                    controls=_controls([body]),
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
                        bgcolor=self._pal.accent if idx <= self.step else self._pal.border,
                    )
                )
            done = idx < self.step
            active = idx == self.step
            circle_bg = self._pal.accent if done or active else self._pal.border
            circle_fg = self._pal.on_accent if done or active else self._pal.dim
            circle_content = (
                ft.Icon(ft.Icons.CHECK, size=14, color=self._pal.on_accent)
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
                            color=self._pal.accent if active else self._pal.dim,
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
                controls=_controls([
                    ft.Column(
                        spacing=2,
                        expand=True,
                        controls=[
                            ft.Text(
                                "G30 → G60 Converter",
                                size=18,
                                weight=ft.FontWeight.W_600,
                                color=self._pal.navy,
                            ),
                            ft.Text(
                                "Convert GE Multilin UR G30 relay settings for G60 import",
                                size=12,
                                color=self._pal.dim,
                            ),
                        ],
                    ),
                    ft.Row(
                        spacing=4,
                        controls=_controls([
                            ft.IconButton(
                                icon=ft.Icons.DARK_MODE
                                if not self._is_dark_effective()
                                else ft.Icons.LIGHT_MODE,
                                icon_size=20,
                                tooltip="Switch to dark mode"
                                if not self._is_dark_effective()
                                else "Switch to light mode",
                                style=ft.ButtonStyle(color=self._pal.dim),
                                on_click=_click(self._toggle_theme),
                            ),
                            ft.IconButton(
                                icon=ft.Icons.INFO_OUTLINE,
                                icon_size=20,
                                tooltip="About",
                                style=ft.ButtonStyle(color=self._pal.dim),
                                on_click=_click(self._show_about),
                            ),
                            ft.Container(
                                bgcolor=self._pal.step_chip_bg,
                                border_radius=16,
                                padding=ft.Padding.symmetric(horizontal=12, vertical=4),
                                content=ft.Text(
                                    f"Step {self.step + 1} of {len(STEP_LABELS)}",
                                    size=12,
                                    color=self._pal.accent,
                                    weight=ft.FontWeight.W_600,
                                ),
                            ),
                        ]),
                    ),
                ]),
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

    def _step_column(self, controls: list[ft.Control], *, scroll: bool = True) -> ft.Column:
        return ft.Column(
            spacing=12,
            expand=True,
            scroll=ft.ScrollMode.AUTO if scroll else ft.ScrollMode.HIDDEN,
            controls=controls,
        )

    def _card(self, content: ft.Control, *, padding: int = 20) -> ft.Container:
        return ft.Container(
            bgcolor=self._pal.card,
            border=ft.Border.all(1, self._pal.border),
            border_radius=8,
            padding=padding,
            content=content,
        )

    def _section_title(self, title: str, subtitle: str) -> ft.Column:
        return ft.Column(
            spacing=4,
            controls=[
                ft.Text(title, size=20, weight=ft.FontWeight.W_600, color=self._pal.text),
                ft.Text(subtitle, size=13, color=self._pal.dim),
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
                        ft.Icon(ft.Icons.ERROR_OUTLINE, color=self._pal.error, size=32),
                        ft.Text(
                            "No G60 base templates found in the bundled bases/ folder.",
                            color=self._pal.error,
                            size=14,
                        ),
                        ft.Text(
                            f"Expected location: {app_base_dir()}",
                            size=12,
                            color=self._pal.dim,
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
            fw_note: str = "",
        ) -> ft.Container:
            selected = self.format_mode == mode
            border_color = self._pal.accent if selected else self._pal.border
            bg = self._pal.selected_bg if selected else self._pal.card
            badge_row_controls: list[ft.Control] = [
                ft.Text(
                    title,
                    size=15,
                    weight=ft.FontWeight.W_600,
                    color=self._pal.text,
                ),
                ft.Container(
                    bgcolor=self._pal.badge_accent_bg if recommended else self._pal.badge_muted_bg,
                    border_radius=4,
                    padding=ft.Padding.symmetric(horizontal=8, vertical=2),
                    content=ft.Text(
                        badge,
                        size=10,
                        weight=ft.FontWeight.W_700,
                        color=self._pal.accent if recommended else self._pal.dim,
                    ),
                ),
            ]
            if fw_note:
                badge_row_controls.append(
                    ft.Container(
                        bgcolor=self._pal.step_chip_bg,
                        border_radius=4,
                        padding=ft.Padding.symmetric(horizontal=8, vertical=2),
                        content=ft.Text(
                            fw_note,
                            size=10,
                            weight=ft.FontWeight.W_600,
                            color=self._pal.dim,
                        ),
                    )
                )
            return ft.Container(
                border=ft.Border.all(2 if selected else 1, border_color),
                border_radius=8,
                bgcolor=bg,
                padding=14,
                on_click=lambda _e, m=mode: self._set_format_mode(m),
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Column(
                            spacing=4,
                            expand=True,
                            controls=[
                                ft.Row(
                                    controls=badge_row_controls,
                                    spacing=8,
                                    wrap=True,
                                ),
                                ft.Text(description, size=13, color=self._pal.dim),
                            ],
                        ),
                        ft.Icon(
                            ft.Icons.RADIO_BUTTON_CHECKED if selected else ft.Icons.RADIO_BUTTON_OFF,
                            color=self._pal.accent if selected else self._pal.dim,
                        ),
                    ],
                ),
            )

        return self._step_column(
            [
                self._section_title(
                    "Welcome",
                    "This wizard walks you through converting a G30 relay export into G60 format.",
                ),
                self._card(
                    ft.Column(
                        spacing=10,
                        controls=[
                            ft.Text("What are you converting?", size=14, weight=ft.FontWeight.W_600),
                            format_card(
                                "urs",
                                "URS device export",
                                "Produces a .urs file ready to import in EnerVista on the G60.",
                                "Recommended",
                                recommended=True,
                                fw_note="G30 FW 7.3x+",
                            ),
                            format_card(
                                "xml",
                                "XML settings export",
                                "Produces G60 .xml plus an HTML conversion report for review.",
                                "Advanced",
                                fw_note="G30 FW pre-7.3x",
                            ),
                            ft.Container(
                                bgcolor=self._pal.step_chip_bg,
                                border_radius=8,
                                padding=10,
                                content=ft.Row(
                                    spacing=8,
                                    vertical_alignment=ft.CrossAxisAlignment.START,
                                    controls=[
                                        ft.Icon(ft.Icons.INFO_OUTLINE, size=18, color=self._pal.dim),
                                        ft.Text(
                                            "Use URS for G30 firmware 7.3x and newer. For older firmware "
                                            "(5.x–7.2x), prefer the XML settings export — User Display "
                                            "Pages are mapped more reliably.",
                                            size=12,
                                            color=self._pal.dim,
                                            expand=True,
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                    padding=16,
                ),
                self._card(
                    ft.Column(
                        spacing=6,
                        controls=[
                            ft.Text("Before you begin", size=14, weight=ft.FontWeight.W_600),
                            ft.Text(
                                "1. Export your G30 settings from EnerVista (.urs for 7.3x+, or XML for older firmware).",
                                size=13,
                                color=self._pal.dim,
                            ),
                            ft.Text(
                                "2. Know the target G60 firmware version you will load the file onto.",
                                size=13,
                                color=self._pal.dim,
                            ),
                            ft.Text(
                                "3. After conversion, import the output into UR Setup on the G60.",
                                size=13,
                                color=self._pal.dim,
                            ),
                        ],
                    ),
                    padding=16,
                ),
            ],
            scroll=False,
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

        drop_border = self._pal.accent if valid else self._pal.border
        drop_bg = self._pal.selected_bg if valid else self._pal.dropzone_bg

        summary: list[ft.Control] = []
        if valid and path is not None:
            summary.append(
                self._card(
                    ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.INSERT_DRIVE_FILE, color=self._pal.accent),
                            ft.Column(
                                expand=True,
                                spacing=2,
                                controls=[
                                    ft.Text(path.name, size=14, weight=ft.FontWeight.W_600),
                                    ft.Text(
                                        f"{_human_size(path.stat().st_size)} · {path.parent}",
                                        size=12,
                                        color=self._pal.dim,
                                    ),
                                ],
                            ),
                            ft.Icon(ft.Icons.CHECK_CIRCLE, color=self._pal.ok),
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
                    color=self._pal.error,
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
                    on_click=_click(browse),
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10,
                        controls=[
                            ft.Icon(ft.Icons.UPLOAD_FILE, size=40, color=self._pal.accent),
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
                                color=self._pal.dim,
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
            border_color = self._pal.accent if selected else self._pal.border
            bg = self._pal.selected_bg if selected else self._pal.card

            status_icon = ft.Icons.CHECK_CIRCLE if urs_ok else ft.Icons.WARNING_AMBER_ROUNDED
            status_color = self._pal.ok if urs_ok else self._pal.warn
            urs_path = template.urs_path
            status_text = (
                f"URS base available ({urs_path.name})"
                if urs_ok and urs_path is not None
                else "No paired .urs base — URS conversion unavailable"
            )

            cards.append(
                ft.Container(
                    border=ft.Border.all(2 if selected else 1, border_color),
                    border_radius=8,
                    bgcolor=bg if not disabled else self._pal.disabled_bg,
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
                                        color=self._pal.dim,
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
                                color=self._pal.accent if selected else self._pal.dim,
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
            controls=_controls([
                self._section_title(
                    "Output location",
                    "Choose where the converted file should be saved.",
                ),
                ft.Row(
                    controls=_controls([
                        ft.TextField(
                            value=self.output_dir,
                            expand=True,
                            read_only=True,
                            border_color=self._pal.border,
                            on_change=lambda e: None,
                        ),
                        ft.OutlinedButton(content="Browse…", on_click=_click(browse_output)),
                    ]),
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
            ]),
        )

    def _review_row(self, label: str, value: str) -> ft.Row:
        return ft.Row(
            controls=[
                ft.Text(label, width=130, size=13, color=self._pal.dim),
                ft.Text(value, expand=True, size=13, color=self._pal.text),
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
                        ft.ProgressRing(width=48, height=48, color=self._pal.accent),
                        ft.Text("Converting settings…", size=18, weight=ft.FontWeight.W_600),
                        ft.Text("This may take a moment for large device files.", size=13, color=self._pal.dim),
                    ],
                ),
            )

        if self.error_text:
            return ft.Column(
                scroll=ft.ScrollMode.AUTO,
                spacing=16,
                controls=_controls([
                    ft.Container(
                        alignment=ft.Alignment.CENTER,
                        content=ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=8,
                            controls=[
                                ft.Icon(ft.Icons.ERROR_OUTLINE, size=48, color=self._pal.error),
                                ft.Text("Conversion failed", size=20, weight=ft.FontWeight.W_600, color=self._pal.error),
                                ft.Text(self.error_text, size=13, color=self._pal.dim, text_align=ft.TextAlign.CENTER),
                            ],
                        ),
                    ),
                    self._log_expansion(),
                    ft.Row(
                        controls=_controls([
                            ft.OutlinedButton(
                                content="Back to output",
                                on_click=_click(self._back_from_failure),
                            ),
                        ]),
                    ),
                ]),
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
        if self._verification_report_path and self._verification_report_path.is_file():
            actions.append(
                ft.OutlinedButton(
                    content="Open verification report",
                    on_click=lambda _e: self._open_verification_report(),
                )
            )

        verify_card = self._build_verification_card()
        return ft.Column(
            scroll=ft.ScrollMode.AUTO,
            spacing=16,
            controls=_controls([
                ft.Container(
                    alignment=ft.Alignment.CENTER,
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=8,
                        controls=[
                            ft.Icon(ft.Icons.CHECK_CIRCLE, size=56, color=self._pal.ok),
                            ft.Text("Conversion complete", size=22, weight=ft.FontWeight.W_600, color=self._pal.ok),
                            ft.Text(result_name, size=15, weight=ft.FontWeight.W_600),
                            ft.Text(f"Saved to {self.output_dir}", size=13, color=self._pal.dim),
                        ],
                    ),
                ),
                *([verify_card] if verify_card is not None else []),
                self._card(
                    ft.Column(
                        spacing=8,
                        controls=[
                            ft.Text("Next steps", size=14, weight=ft.FontWeight.W_600),
                            ft.Text(
                                "1. Open the converted file in UR Setup on your G60 relay.",
                                size=13,
                                color=self._pal.dim,
                            ),
                            ft.Text(
                                "2. Review any warnings in the HTML report before commissioning."
                                if self._last_html
                                else "2. Verify settings in EnerVista before commissioning.",
                                size=13,
                                color=self._pal.dim,
                            ),
                            ft.Text(
                                "3. Confirm there are zero Invalid Settings after import.",
                                size=13,
                                color=self._pal.dim,
                            ),
                        ],
                    ),
                    padding=16,
                ),
                ft.Row(wrap=True, spacing=10, controls=actions),
                self._log_expansion(),
            ]),
        )

    def _build_verification_card(self) -> ft.Control | None:
        verification = self._verification
        if verification is None:
            return None

        if verification.ok:
            return self._card(
                ft.Row(
                    spacing=10,
                    controls=[
                        ft.Icon(ft.Icons.VERIFIED, color=self._pal.ok),
                        ft.Column(
                            expand=True,
                            spacing=4,
                            controls=[
                                ft.Text(
                                    "Output verification passed",
                                    size=14,
                                    weight=ft.FontWeight.W_600,
                                    color=self._pal.ok,
                                ),
                                ft.Text(
                                    verification.format_short(),
                                    size=13,
                                    color=self._pal.dim,
                                ),
                            ],
                        ),
                    ],
                ),
                padding=14,
            )

        report_buttons: list[ft.Control] = [
            ft.OutlinedButton(
                content="Save verification report",
                icon=ft.Icons.SAVE_ALT,
                on_click=_click(self._save_verification_report),
            ),
        ]
        if self._verification_report_path and self._verification_report_path.is_file():
            report_buttons.append(
                ft.OutlinedButton(
                    content="Open saved report",
                    icon=ft.Icons.DESCRIPTION_OUTLINED,
                    on_click=_click(self._open_verification_report),
                )
            )

        return self._card(
            ft.Column(
                spacing=8,
                controls=[
                    ft.Row(
                        spacing=10,
                        controls=[
                            ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=self._pal.warn),
                            ft.Column(
                                expand=True,
                                spacing=4,
                                controls=[
                                    ft.Text(
                                        "Output verification found mismatches",
                                        size=14,
                                        weight=ft.FontWeight.W_600,
                                        color=self._pal.warn,
                                    ),
                                    ft.Text(
                                        verification.format_short(),
                                        size=13,
                                        color=self._pal.dim,
                                    ),
                                ],
                            ),
                        ],
                    ),
                    ft.Text(
                        "Some written values differ from what the converter expected. "
                        "Expand the list below or save a report before importing to the relay.",
                        size=13,
                        color=self._pal.dim,
                    ),
                    ft.ExpansionTile(
                        title=ft.Text(
                            f"Show all {len(verification.mismatches):,} mismatch(es)",
                            size=13,
                            color=self._pal.text,
                        ),
                        controls=[
                            ft.Container(
                                bgcolor=self._pal.log_bg,
                                border_radius=6,
                                padding=12,
                                content=ft.Column(
                                    scroll=ft.ScrollMode.AUTO,
                                    height=220,
                                    controls=[
                                        ft.Text(
                                            verification.format_mismatch_details(),
                                            font_family="Consolas",
                                            size=11,
                                            color=self._pal.text,
                                            selectable=True,
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                    ft.Row(wrap=True, spacing=10, controls=_controls(report_buttons)),
                ],
            ),
            padding=14,
        )

    def _converted_output_path(self) -> Path | None:
        if self._last_urs and self._last_urs.is_file():
            return self._last_urs
        if self._last_xml and self._last_xml.is_file():
            return self._last_xml
        return None

    def _verification_template_label(self) -> str:
        try:
            return self._selected_template().label
        except ValueError:
            return ""

    def _show_snackbar(self, message: str) -> None:
        self.page.show_dialog(ft.SnackBar(content=ft.Text(message)))

    def _save_verification_report(self, _event: ft.ControlEvent) -> None:
        verification = self._verification
        output_path = self._converted_output_path()
        if verification is None or output_path is None:
            self._show_snackbar("Nothing to save — run a conversion first.")
            return
        if verification.ok:
            self._show_snackbar("Verification passed — no mismatch report needed.")
            return
        try:
            source_path = Path(self.g30_path) if self.g30_path.strip() else None
            self._verification_report_path = write_verification_report(
                verification,
                output_path,
                source_path=source_path,
                template_label=self._verification_template_label(),
            )
        except OSError as exc:
            self._show_snackbar(f"Could not save report: {exc}")
            return
        self._show_snackbar(f"Saved {self._verification_report_path.name}")
        self._render()

    def _open_verification_report(self, _event: ft.ControlEvent | None = None) -> None:
        path = self._verification_report_path
        if path and path.is_file():
            os.startfile(path)

    def _log_expansion(self) -> ft.ExpansionTile:
        return ft.ExpansionTile(
            title=ft.Text("Show conversion log", size=13, color=self._pal.dim),
            controls=[
                ft.Container(
                    bgcolor=self._pal.log_bg,
                    border_radius=6,
                    padding=12,
                    content=ft.Text(
                        self.log_text or "(no log output)",
                        font_family="Consolas",
                        size=11,
                        color=self._pal.text,
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
        self._verification = None
        self._verification_report_path = None
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
        verification: VerificationResult | None = None
        try:
            verification = convert(g30, template, out_dir)
        except Exception as exc:
            error = exc
        finally:
            sys.stdout = old_stdout
        self.page.run_task(self._xml_convert_done, out_dir, buffer.getvalue(), error, verification)

    def _run_urs_convert(self, g30: Path, template: BaseTemplateInfo, out_dir: Path) -> None:
        out_dir.mkdir(parents=True, exist_ok=True)
        buffer = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = buffer
        error: Exception | None = None
        output_path: Path | None = None
        verification: VerificationResult | None = None
        try:
            urs_template = resolve_urs_template(template.path, app_base_dir())
            result = convert_urs(g30, urs_template, template.path, out_dir)
            output_path = result.output_path
            verification = result.verification
        except Exception as exc:
            error = exc
        finally:
            sys.stdout = old_stdout
        self.page.run_task(
            self._urs_convert_done,
            out_dir,
            buffer.getvalue(),
            error,
            output_path,
            verification,
        )

    async def _xml_convert_done(
        self,
        out_dir: Path,
        log_text: str,
        error: Exception | None,
        verification: VerificationResult | None,
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
        self._verification = verification
        self._render()

    async def _urs_convert_done(
        self,
        out_dir: Path,
        log_text: str,
        error: Exception | None,
        output_path: Path | None,
        verification: VerificationResult | None,
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
        self._verification = verification
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
    ft.run(main)  # type: ignore[reportUnknownMemberType]


if __name__ == "__main__":
    main_entry()
