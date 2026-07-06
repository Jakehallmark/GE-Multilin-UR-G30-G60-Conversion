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

## GitHub releases and Packages

Pushing a version tag triggers [`.github/workflows/release.yml`](.github/workflows/release.yml), which:

1. Builds `release/G30-to-G60-Converter.exe` from source (PyInstaller + `bases/`)
2. Publishes a **NuGet package** to **GitHub Packages** (shows under the repo **Packages** tab)
3. Creates a **GitHub Release** with auto-generated release notes and the exe attached for direct download

### Publish a new version

```powershell
# After your changes are committed on main:
git tag v1.0.1
git push origin main
git push origin v1.0.1
```

Or run the workflow manually: **Actions → Release → Run workflow** and enter a semver (e.g. `1.0.1`).

### Download for end users

| Location | Best for |
|----------|----------|
| **[Releases](https://github.com/Jakehallmark/GE-Multilin-UR-G30-G60-Conversion/releases)** | Direct `.exe` download (recommended) |
| **[Packages](https://github.com/Jakehallmark/GE-Multilin-UR-G30-G60-Conversion/packages)** | Versioned NuGet package (contains the same exe under `tools/`) |

You can rebuild locally with `.\aio\build.ps1` and commit `release/G30-to-G60-Converter.exe` if you want a copy in git, but the **tag push builds a fresh exe in CI** — that is the source of truth for published releases.

---

## Important notes

See [CONVERSION_PROCESS.md](CONVERSION_PROCESS.md) for matching rules, FlexLogic translation, HTML report sections, and troubleshooting.

**Zero Invalid Settings** in UR Setup after import is the target. Invalid Settings indicate a value format or firmware-code problem — check the HTML report and confirm the base template matches the target relay firmware.
