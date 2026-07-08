# Firmware assets for G30 → G60 conversion

## What belongs here

| Path | Purpose |
|------|---------|
| `g30/AnalogoperandTo61850_*.csv` | G30 / FW 7.x FlexAnalog → IEC61850 map (from URPC `Devices/`) |
| `g60/AnalogoperandTo61850_*.csv` | Matching G60 / FW 8.x map |
| `g30/*.SFD`, `*.000` *(optional, local only)* | Relay firmware images — **not** parsed by the converter |
| `g60/*.SFD` *(optional, local only)* | Same |

Encrypted firmware binaries (`.SFD` / `.000`) do **not** contain a plaintext signal dictionary. User-display remapping on the URS path joins the Analogoperand CSVs on IEC61850 path stems, then resolves names through the G60 Base EnumType `10013` table.

Bundled defaults:

- `g30/AnalogoperandTo61850_760.csv` — matches FW 7.60 projects (`7168` = SRC1 P)
- `g60/AnalogoperandTo61850_860.csv` — matches FW 8.60 bases (`6912` = SRC1 P)

Copy refreshed CSVs from:

`C:\ProgramData\GE Power Management\urpc\Devices\AnalogoperandTo61850_<rev>.csv`
