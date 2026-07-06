# G30 to G60 Relay Settings Converter

**Technical reference:** [Conversion Process — step-by-step guide](CONVERSION_PROCESS.md)

Converts GE Multilin UR series **G30** relay settings XML files to **G60** format, producing a ready-to-import G60 XML and a detailed HTML conversion report.

## Repository layout

```
├── convert_g30_to_g60.py          # CLI converter (source of truth)
├── Convert G30 to G60.bat         # Drag-and-drop launcher (Windows)
├── bases/                         # G60 firmware templates (committed)
│   ├── G60 Base.xml               #   default (firmware 860)
│   ├── G60 Base [8.4x].xml
│   ├── G60 Base [8.5x].xml
│   └── G60 Base [8.7x].xml
├── release/
│   └── G30-to-G60-Converter.exe   # Prebuilt GUI (tag on GitHub Releases)
├── aio/                           # GUI source + build.ps1 to rebuild release exe
├── azure/                         # Optional HTTP API for SharePoint / Power Automate
├── README.md
└── CONVERSION_PROCESS.md
```

For cloud deployment, see [azure/README.md](azure/README.md).

---

## Quick start — GUI (recommended)

1. Download **`G30-to-G60-Converter.exe`** from [GitHub Releases](https://github.com/Jakehallmark/GE-Multilin-UR-G30-G60-Conversion/releases) (recommended) or clone this repo and run `release/G30-to-G60-Converter.exe`.
2. Run the exe — no Python install required.
3. Select your G30 settings file, pick **target firmware** from the dropdown, and convert.
4. Output goes to **`Desktop\G60_Conversion\`** as `<DeviceName> FW<version>.xml` and `_OR.html`.

---

## Quick start — drag and drop (CLI)

1. Locate the G30 settings XML file you want to convert.
2. Drag it onto **`Convert G30 to G60.bat`**.
3. Output appears in the `Converted\` subfolder next to the script.

Uses **`bases/G60 Base.xml`** (firmware 860) by default.

---

## Command-line usage

```
python convert_g30_to_g60.py  <g30_source.xml>  [output_dir]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `g30_source.xml` | Yes | Path to the G30 settings file to convert |
| `output_dir` | No | Folder for outputs (default: `Converted\` next to the script) |

Output filenames include the target firmware, e.g. `Publix G60_208V4000A FW860.xml`, so conversions for different firmware versions do not overwrite each other.

**Examples:**

```batch
python convert_g30_to_g60.py "MySite G30 480V.xml"
python convert_g30_to_g60.py "source.xml" "C:\Work\Converted"
```

---

## Requirements

- **CLI:** Python 3.10+ — standard library only
- **GUI:** none (use `release/G30-to-G60-Converter.exe`)
- **`bases/G60 Base*.xml`** must be present — one template per supported target firmware
- G30 and G60 XML can be **UTF-8 or UTF-16 LE** (auto-detected)

**Do not commit G30 source files** — they contain site-specific relay configuration.

---

## Rebuilding the release exe

```powershell
pip install pyinstaller
.\aio\build.ps1
```

Writes `release/G30-to-G60-Converter.exe` with all templates from `bases/` bundled inside.

---

## Base templates

| File | Typical firmware |
|------|------------------|
| `bases/G60 Base.xml` | 860 (CLI / Azure default) |
| `bases/G60 Base [8.4x].xml` | 840 |
| `bases/G60 Base [8.5x].xml` | 850 |
| `bases/G60 Base [8.7x].xml` | 870 |

Export each blank template from UR Setup on the matching relay firmware. The converter preserves each template's `version` and `orderCode` in the output.

---

## GitHub Releases

Pushing a version tag runs [`.github/workflows/release.yml`](.github/workflows/release.yml), which builds the GUI exe and attaches it to a **GitHub Release** with auto-generated release notes.

### Publish a new version

```powershell
git add .
git commit -m "Your changes"
git push origin main

git tag v1.0.3
git push origin v1.0.3
```

When the Action finishes (green checkmark), open **Releases** — you should see `G30-to-G60-Converter.exe` as a downloadable asset (not just source zip/tar.gz).

### Fix a tag that has no exe

If a tag exists but the Action failed (red X), the tag page only shows source archives. After fixing the workflow:

```powershell
git tag -d v1.0.2
git push origin :refs/tags/v1.0.2
git tag v1.0.2
git push origin v1.0.2
```

Or push a new patch tag (`v1.0.3`).

### Download for end users

**[Releases](https://github.com/Jakehallmark/GE-Multilin-UR-G30-G60-Conversion/releases)** → pick a version → download **`G30-to-G60-Converter.exe`**.

### Rebuild locally (optional)

```powershell
pip install pyinstaller
.\aio\build.ps1
```

Writes `release/G30-to-G60-Converter.exe`. CI builds a fresh copy on each tag push — that is what gets attached to the Release.

---

## Important notes

See [CONVERSION_PROCESS.md](CONVERSION_PROCESS.md) for matching rules, FlexLogic translation, HTML report sections, and troubleshooting.

**Zero Invalid Settings** in UR Setup after import is the target. Invalid Settings indicate a value format or firmware-code problem — check the HTML report and confirm the base template matches the target relay firmware.
