# Firmware assets for G30 → G60 conversion

## What belongs here

| Path | Purpose |
|------|---------|
| `g30/AnalogoperandTo61850_*.csv` | G30 FlexAnalog → IEC61850 map (from URPC `Devices/`) |
| `g60/AnalogoperandTo61850_*.csv` | Matching G60 / FW 8.x map |
| `g30/*.SFD`, `*.000` *(optional, local only)* | Relay firmware images — **not** parsed by the converter |
| `g60/*.SFD` *(optional, local only)* | Same |

Encrypted firmware binaries (`.SFD` / `.000`) do **not** contain a plaintext signal dictionary. User-display remapping on the URS path joins the Analogoperand CSVs on IEC61850 path stems, then resolves names through the G60 Base EnumType `10013` table.

## G30 firmware archives → CSV

| Archive | Firmware line | CSV file |
|---------|---------------|----------|
| `A09ma590` | 5.9x | `AnalogoperandTo61850_590.csv` *(source required)* |
| `A09ma606` | 6.0x | `AnalogoperandTo61850_600.csv` *(source required; URS `version` is `600`)* |
| `A09ma766` | 7.6x | `AnalogoperandTo61850_760.csv` |
| `A09ma844` | 8.4x | `AnalogoperandTo61850_840.csv` |

## G60 firmware archives → CSV

| Archive | Firmware line | CSV file |
|---------|---------------|----------|
| `A09ma846` | 8.4x | `AnalogoperandTo61850_840.csv` |
| `A09ma851` | 8.5x | `AnalogoperandTo61850_850.csv` |
| `A09ma862` | 8.6x | `AnalogoperandTo61850_860.csv` |
| `A09ma871` | 8.7x | `AnalogoperandTo61850_870.csv` |

Copy refreshed CSVs from:

`C:\ProgramData\GE Power Management\urpc\Devices\AnalogoperandTo61850_<rev>.csv`

5.x/6.x builds use the exact suffix (`590`, `606`). 7.x/8.x builds floor to the line revision (`766` → `760`, `844` → `840`, `846` → `840`).

### Sourcing 5.9x / 6.0x CSVs

Current EnerVista / URPC installs (7.30+) only ship `AnalogoperandTo61850_730.csv` and newer. They do **not** include the 5.9x (`590`) or 6.0x (`600`) tables. Adding a device to EnerVista does not install these files — you still need to copy them from an older UR Setup `Devices` folder or GE media.

Reference URS exports (firmware in header field 5):

| File | `version` field |
|------|-----------------|
| `HCHPublix Firmware5-9_208V3000A 1-18-13.urs` | `590` |
| `Publix 1563 Cocoa Beach 6.06 208v 3000A.urs` | `600` |

To obtain the correct CSVs:

1. On a machine with **UR Setup 6.x** (or older) installed, copy from  
   `C:\ProgramData\GE Power Management\urpc\Devices\AnalogoperandTo61850_600.csv`  
   (and `…_590.csv` for the 5.9x line).
2. From **GE UR firmware / software media** for the matching release.
3. From a **URPC backup** or older workstation that still has the 6.x `Devices` folder.

Place the copied files in `firmware/g30/`. Until then the converter falls back to `AnalogoperandTo61850_740.csv` plus any `code (name)` annotations in the URS, and prints a warning.

**Companion XML:** If you download the device settings to EnerVista Offline, `TargetSettingFile.xml` in the matching folder is used automatically (full EnumType 10013 signal table, no CSV required for the G30 side).

## Converter selection

On URS conversion the converter reads:

1. **G30 firmware** from the source `.urs` header (or companion `.xml` `version` attribute)
2. **G60 firmware** from the selected base template

It then picks the matching `AnalogoperandTo61850_<rev>.csv` on each side. If the exact revision is missing, it uses the nearest lower bundled file and warns.

## Verify coverage

```powershell
python firmware/verify_csv_pairing.py
```

This checks each local SFD archive, each G60 base template, lists any 5.9x/6.0x CSVs still needed, and validates join pairs (including SRC P anchors).
