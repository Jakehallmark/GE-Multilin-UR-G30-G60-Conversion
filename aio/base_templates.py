"""G60 base template discovery for the standalone AiO converter app."""

from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

BASE_TEMPLATE_GLOB = "G60 Base*.xml"


@dataclass
class BaseTemplateInfo:
    path: Path
    version: str
    order_code: str
    device_name: str

    @property
    def label(self) -> str:
        fw = self.version or self.path.stem.removeprefix("G60 Base").strip() or "unknown"
        if self.order_code:
            return f"Firmware {fw} — {self.order_code}"
        return f"Firmware {fw}"

    @property
    def urs_path(self) -> Optional[Path]:
        """Paired .urs template with the same stem as this XML base, if present."""
        urs = self.path.with_suffix(".urs")
        return urs if urs.is_file() else None

    @property
    def has_urs_pair(self) -> bool:
        return self.urs_path is not None


def app_base_dir() -> Path:
    """Directory containing bundled base templates (dev or PyInstaller)."""
    if getattr(sys, "frozen", False):
        return Path(sys._MEIPASS) / "bases"
    return Path(__file__).resolve().parent.parent / "bases"


def _read_base_template_meta(path: Path) -> BaseTemplateInfo:
    with open(path, "rb") as f:
        for _event, elem in ET.iterparse(f, events=("start",)):
            return BaseTemplateInfo(
                path=path,
                version=elem.get("version", ""),
                order_code=elem.get("orderCode", ""),
                device_name=elem.get("deviceName", ""),
            )
    raise ValueError(f"Could not read base template metadata: {path}")


def discover_base_templates(base_dir: Path) -> list[BaseTemplateInfo]:
    templates: list[BaseTemplateInfo] = []
    if not base_dir.is_dir():
        return templates

    for path in sorted(base_dir.glob(BASE_TEMPLATE_GLOB)):
        if not path.is_file():
            continue
        try:
            templates.append(_read_base_template_meta(path))
        except (ET.ParseError, ValueError, OSError):
            continue

    def sort_key(info: BaseTemplateInfo) -> tuple:
        try:
            return (0, int(info.version))
        except ValueError:
            return (1, info.version.lower())

    return sorted(templates, key=sort_key)


def resolve_base_template(
    base_dir: Path, selection: Optional[str] = None
) -> BaseTemplateInfo:
    templates = discover_base_templates(base_dir)
    if not templates:
        raise FileNotFoundError(
            f"No G60 base templates found in {base_dir} (expected {BASE_TEMPLATE_GLOB})"
        )

    if selection is not None:
        return _match_base_template(templates, selection)

    default = base_dir / "G60 Base.xml"
    if default.is_file():
        for info in templates:
            if info.path.resolve() == default.resolve():
                return info

    if len(templates) == 1:
        return templates[0]

    labels = ", ".join(info.label for info in templates)
    raise FileNotFoundError(
        f"Multiple base templates found; select a target firmware ({labels})"
    )


def _match_base_template(
    templates: list[BaseTemplateInfo], selection: str
) -> BaseTemplateInfo:
    sel = selection.strip()
    sel_lower = sel.lower()
    sel_path = Path(sel)

    if sel_path.is_file():
        resolved = sel_path.resolve()
        for info in templates:
            if info.path.resolve() == resolved:
                return info

    for info in templates:
        if info.path.name.lower() == sel_lower:
            return info

    for info in templates:
        if info.version == sel:
            return info

    matches = [
        info for info in templates
        if sel in info.version or sel in info.path.stem
    ]
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        names = ", ".join(info.path.name for info in matches)
        raise FileNotFoundError(
            f"Ambiguous base template '{selection}' matches: {names}"
        )

    available = "\n".join(f"  {info.label}" for info in templates)
    raise FileNotFoundError(
        f"No G60 base template matches '{selection}'. Available:\n{available}"
    )
