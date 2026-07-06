# G30 to G60 Relay Settings Converter

**Technical reference:** [Conversion Process — step-by-step guide](CONVERSION_PROCESS.md) 
Converts GE Multilin UR series **G30** relay settings XML files to **G60** format, producing a ready-to-import G60 XML and a detailed HTML conversion report.

## Repository layout

```
├── convert_g30_to_g60.py       # Desktop converter (source of truth)
├── Convert G30 to G60.bat      # Drag-and-drop launcher (Windows)
├── G60 Base.xml                # G60 template (required alongside the script)
├── azure/                      # Optional HTTP API for SharePoint / Power Automate
    └── function_app/
```

For cloud deployment, see [azure/README.md](azure/README.md).

---

## Files

| File | Purpose |
|------|---------|
| `convert_g30_to_g60.py` | Main conversion script |
| `Convert G30 to G60.bat` | Drag-and-drop launcher |
| `G60 Base.xml` | G60 template (must be in the same folder as the script) |
| `Converted\` | Output folder (created automatically, not committed) |

**Do not commit G30 source files** — they contain site-specific relay configuration. Keep inputs on your machine or internal storage only.

---

## Quick Start — Drag and Drop

1. Locate the G30 settings XML file you want to convert.
2. Drag it onto **`Convert G30 to G60.bat`**.
3. A console window will open, show progress, and close after you press a key.
4. Two output files appear in the `Converted\` subfolder:
   - `<DeviceName>.xml` — the converted G60 settings file
   - `<DeviceName>_OR.html` — the conversion report (open in any browser)

---

## Command-Line Usage

```
python convert_g30_to_g60.py  <g30_source.xml>  [output_dir]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `g30_source.xml` | Yes | Path to the G30 settings file to convert |
| `output_dir` | No | Folder for outputs (default: `Converted\` next to the script) |

The G60 base template (`G60 Base.xml`) must be in the **same folder** as the script.

**Examples:**

```batch
python convert_g30_to_g60.py "MySite G30 480V.xml"
python convert_g30_to_g60.py "relay-settings.xml"

:: Custom output directory
python convert_g30_to_g60.py "source.xml" "C:\Work\Converted"
```

---

## Requirements

- **Python 3.10+** — standard library only, no pip installs needed
- `G60 Base.xml` must remain in the **same folder** as the script
- G30 and G60 source files can be **UTF-8 or UTF-16 LE** encoded (the script auto-detects)

---

## How the Conversion Works

### 1. Parsing

Both the G30 source file and the G60 template are read as raw bytes. The script first attempts to parse as UTF-8 (allowing for XML encoding declarations), falling back to UTF-16 LE if needed. The G60 template provides the output structure; its `version` and `orderCode` attributes are always preserved unchanged.

### 2. Setting Matching

Every setting in the G60 template is matched against the G30 source using a five-part composite key:

```
(labelID, group, module, item, bit)
```

This uniquely identifies each register across both devices, regardless of firmware differences in display names or section layout. For example, two breaker modules that share the same `labelID` are distinguished by their `module` attribute.

### 3. Value Transfer Rules

| Setting Type | What is transferred | What is kept from G60 |
|---|---|---|
| **Number** | Numeric value, reformatted to match G60 decimal precision | `MinValue`, `MaxValue`, `Unit` |
| **Enum** | `value` (display text) + `EnumValue` (selection index) | `EnumFormatIndex` (G60 firmware's enum table) |
| **Flex** | Operand name string; FlexValue resolved to G60 firmware code | G60 FlexValue when G30 operand is hardware-unavailable |

**Number precision reformatting:** UR Setup rejects Number values whose decimal format doesn't match the register's expected precision. For example, if the G30 stored `1.00 Hz` but the G60 register expects `1.000 Hz`, the script reformats the value automatically. The numeric quantity is preserved; only the number of decimal places changes.

**Flex FlexValue firmware codes:** The `FlexValue` attribute in Flex settings is a firmware-internal operand identifier. These codes differ between G30 7.x and G60 8.x firmware for protection element outputs (`OVERFREQ 1 OP`, `DIR POWER 1 STG1 OP`, etc.) and system operands (`SETTING GROUP ACT 1`, etc.). The script builds a name-to-code lookup from the G60 template and substitutes the correct G60 code for every transferred Flex setting.

**Hardware-unavailable operands:** If a G30 Flex setting references a measurement signal that doesn't exist in the G60 hardware configuration (for example, `SRC4 Ia RMS` on a G60 that has no Source 4), the setting reverts to the G60 template's default (`OFF`) rather than writing an invalid code.

**FlexLogic syntax tokens (`AND(2)`, `OR(3)`, `TIMER 1`, `NOT`, etc.):** G30 exports use one of two encodings for gate/timer FlexValue codes:

| Export style | Example `AND(2)` code | Converter action |
|---|---|---|
| **Legacy packed** (older G30 files) | `10754` — opcode in bits 8–15, count in bits 0–7 | Shift to G60 wide form → `2752514` |
| **Wide** (newer G30 / native G60) | `2752514` — opcode in bits 16–23, count in bits 0–7 | Pass through unchanged |

The converter detects the format automatically: values above `65535` are already wide and are not shifted again. Double-shifting wide codes (e.g. `2752514` → `704643074`) produces invalid FlexLogic entries and causes UR Setup "FLEXLOGIC ENTRY" memory-map errors, often followed by cascading "token … is not connected" messages in the equation editor.

### 4. Unmatched Settings

| Case | Result |
|------|--------|
| G30 setting has a match in G60 | Value transferred (with rules above) |
| G30 setting has **no match** in G60 | Dropped — logged in HTML report |
| G60 setting has **no match** in G30 | Kept at G60 template default — logged in HTML report |

### 5. Output Naming

The output filename is derived automatically:

1. **Site prefix** — first word of the G30 `deviceName` (e.g. `publix`)
2. **G60 model** — first segment of the G60 `orderCode`, lowercased (e.g. `G60-V00-…` → `g60`)
3. **Specs suffix** — everything from the first `_` in the G30 `deviceName` onwards (e.g. `_208v4000a[86]`)
4. **Combined raw name** — `{prefix} {model}{suffix}` (e.g. `publix g60_208v4000a[86]`)
5. **UR Setup title-casing** applied:
   - Capitalize the first letter of each space-delimited token
   - Capitalize any letter that immediately follows a digit
   - Result: `Publix G60_208V4000A[86]`

The output XML's `deviceName` attribute is updated to match. The HTML report shares the same base name with `_OR` appended.

---

## Output Files

### Converted XML (`<DeviceName>.xml`)

A valid G60 settings file ready to import into GE UR Setup. Encoded as UTF-16 LE to match UR Setup's expectations. The G60 `version` and `orderCode` from the template are always preserved on line 2.

### Conversion Report (`<DeviceName>_OR.html`)

A self-contained HTML file (no external dependencies) with the following sections:

| Section | Contents |
|---------|----------|
| **Value Changes** | Settings where the G30 value differed from the G60 template default. Shows both the template value and the applied G30 value side by side. |
| **Setting Name Differences** | Settings matched by key where the display name differs between G30 and G60 firmware. Common with contact input labels and renamed virtual outputs. |
| **Range Warnings** | Number settings where the transferred G30 value falls outside the G60 register's `MinValue`/`MaxValue` bounds. These are applied but flagged for review. |
| **G60-Only Settings** | Settings present in the G60 template but absent in the G30 source. These retain the G60 template default. Typically G60-exclusive features. |
| **Dropped G30 Settings** | Settings from the G30 that have no matching register in the G60. These values are not carried over. |
| **Transferred Unchanged** | Settings that matched and had identical values in both files. Collapsed by default. |

All tables support live text filtering. The report can be printed directly from the browser.

---

## Important Notes

### Base Template File

**`G60 Base.xml`** provides the conversion base:

- Defines the complete G60 register structure
- Contains default values for G60-only settings
- Includes G60 firmware's FlexValue operand codes
- Carries the correct `version` and `orderCode` for every converted file

**Do not modify, rename, or move this file.** It defines the G60 register structure, firmware codes, and defaults used when a setting is not present in the G30 source.

### What the Script Does Not Change

- G60 `version` and `orderCode` — always from the template
- `EnumFormatIndex` — always from the G60 template (G30 and G60 use different enum tables)
- `MinValue`, `MaxValue`, `Unit` on Number settings — always from the G60 template

### Expected Differences After Import into UR Setup

When comparing the converted file against an expert-configured G60 reference in UR Setup's Device Comparison Report, some **Differences** are expected and intentional:

- **Contact / VO operand names** — G30 often uses custom labels (`Gen Aux On(H8a)`, `Main Trip On (VO4)`). UR Setup requires the **display name and FlexValue to match as a pair** from the G60 firmware operand table. The converter remaps these to canonical G60 names (`Cont Ip 3 On(H8a)`, `Virt Op 4 On (VO4)`) while preserving custom assign-VO labels (`= Parallel (VO1)`). Protection element outputs with identical names on both relays are unchanged.
- **G60-only settings** — Features that exist only in the G60 (e.g. SENS DIR POWER) will appear as "Missing Settings" since they were not present in the G30 to configure.
- **Intentional configuration differences** — Any setting where the expert G60 reference was deliberately configured differently from the G30 source will appear as a Difference.

**Zero Invalid Settings** is the target after a clean conversion. Invalid Settings indicate a value format or firmware-code problem that requires investigation.

---

## Recent Changes

- **2026-07-06**: Fixed FlexLogic **gate/timer** double-shift for newer G30 exports. Some G30 files (including recent UR Setup exports) already store syntax-token codes in the wide G60 form (`AND(2)` = 2752514). The converter now shifts only packed 16-bit codes (e.g. 10754 → 2752514) and passes wide values through unchanged. Double-shifting produced invalid codes (e.g. 704643074) that caused UR Setup "FLEXLOGIC ENTRY" memory-map errors and cascading "token … is not connected" failures.
- **2026-06-17**: Fixed FlexLogic **gate/timer** code translation for legacy packed G30 exports. Parameterized tokens (`AND(n)`, `OR(n)`, `NAND(n)`, `TIMER n`) encode as `(opcode << 16) | count` on G60, not a flat `× 256` shift.
- **2026-06-17**: Flex operand remapping writes canonical G60 names when resolving contacts/VOs by hardware address (UR Setup recomputes the display name from the contact label, so this is cosmetic but keeps the XML self-consistent).
- **2026-04-23**: Updated XML parsing to auto-detect encoding (UTF-8 first, then UTF-16 LE fallback). Added control character sanitization to handle G30 files with invalid characters in setting values or attributes.
- **2026-04-23**: Improved numeric range detection to parse lower-firmware G30 number values consistently, reducing missed out-of-range warnings.
- **2026-04-23**: Added automatic legacy scaling for IEC power factor threshold values from lower-firmware G30 files, with explicit reporting of the adjustment.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| `ERROR: File not found` | Wrong path or filename typo | Check the path passed to the script |
| `ERROR: Output path would overwrite an input file` | Output directory is the same folder as the template | Use the default `Converted\` folder or pass a different output path |
| Script opens and immediately closes | Python not on system PATH | Run from a terminal with `py convert_g30_to_g60.py ...` |
| UR Setup "FLEXLOGIC ENTRY" memory-map error or "token … is not connected" | Bad FlexLogic gate/timer FlexValue (often from double-shifting a wide-format G30 export), operand name/code mismatch, or G60 base template firmware differs from target relay | Re-run with the current script (detects packed vs wide syntax codes automatically); export a fresh `G60 Base.xml` from the **same firmware** as the target relay; check the HTML report for FlexLogic value changes |
| Output filename looks wrong | G30 `deviceName` doesn't follow the expected `prefix_specs` pattern | The raw and derived device names are printed to the console; verify the G30 source file's `deviceName` attribute on line 2 |
