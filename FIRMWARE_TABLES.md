# GE Multilin UR Firmware Enum Tables - G30 vs G60 Comparison

> Auto-generated reference comparing every `EnumType` table embedded in:
> - **G30 source:** Publix Store 1367 (firmware 7.6x)
> - **G60 template:** G60 Base (firmware 8.6x)

Regenerate: `powershell -File tools/generate_firmware_tables.ps1`

---

## How tables work in UR Setup XML

Each `<EnumType FormatIndex="..." Items="..."/>` element embeds a firmware enum dictionary.
Entries are semicolon-delimited: `code name` (e.g. `7168 SRC1       P`).

| Table | Purpose in conversion |
|-------|----------------------|
| **10012** | Flex operand remapping - logic, contacts, VOs, protection element outputs |
| **10013** | Signal operand remapping - measurements; user-display Item code lookup |
| **Other FormatIndex values** | Dropdown enums for `SettingType="Enum"` registers |

**Key difference:** FormatIndex numbers change between firmware generations for setting-specific enums.
Only **10012** and **10013** keep the same FormatIndex across G30 7.x and G60 8.x.

---

## Table inventory

| Source | EnumType count | Total entries |
|--------|---------------:|--------------:|
| G30 Publix 1367 | 68 | 2631 |
| G60 Base | 82 | 3662 |

### G30 tables

| FormatIndex | Entries | Role |
|-------------|--------:|------|
| 6386 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6385 | 4 | Setting-specific enum (dropdown choices for registers) |
| 6395 | 12 | Setting-specific enum (dropdown choices for registers) |
| 6396 | 3 | Setting-specific enum (dropdown choices for registers) |
| 6643 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6635 | 3 | Setting-specific enum (dropdown choices for registers) |
| 10012 | 1345 | Logic / Flex operand dictionary (contacts, VOs, protection outputs, FlexLogic tokens) |
| 10013 | 1032 | Signal / measurement operand dictionary (SRC1 Ia RMS, SRC1 P, etc.) |
| 6637 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6458 | 6 | Setting-specific enum (dropdown choices for registers) |
| 6666 | 12 | Setting-specific enum (dropdown choices for registers) |
| 6645 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6585 | 4 | Setting-specific enum (dropdown choices for registers) |
| 6586 | 4 | Setting-specific enum (dropdown choices for registers) |
| 6587 | 6 | Setting-specific enum (dropdown choices for registers) |
| 6408 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6397 | 3 | Setting-specific enum (dropdown choices for registers) |
| 6498 | 12 | Setting-specific enum (dropdown choices for registers) |
| 6499 | 7 | Setting-specific enum (dropdown choices for registers) |
| 6500 | 5 | Setting-specific enum (dropdown choices for registers) |
| 6401 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6464 | 5 | Setting-specific enum (dropdown choices for registers) |
| 6521 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6409 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6405 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6384 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6447 | 7 | Setting-specific enum (dropdown choices for registers) |
| 6390 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6448 | 4 | Setting-specific enum (dropdown choices for registers) |
| 6 | 4 | Setting-specific enum (dropdown choices for registers) |
| 10014 | 3 | Auxiliary enum |
| 10010 | 3 | Small flex-related enum |
| 6441 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6444 | 3 | Setting-specific enum (dropdown choices for registers) |
| 6445 | 2 | Setting-specific enum (dropdown choices for registers) |
| 10015 | 5 | Auxiliary enum |
| 10016 | 5 | Auxiliary enum |
| 6438 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6411 | 3 | Setting-specific enum (dropdown choices for registers) |
| 6577 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6578 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6579 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6580 | 3 | Setting-specific enum (dropdown choices for registers) |
| 6392 | 3 | Setting-specific enum (dropdown choices for registers) |
| 6581 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6449 | 3 | Setting-specific enum (dropdown choices for registers) |
| 6470 | 4 | Setting-specific enum (dropdown choices for registers) |
| 6450 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6404 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6387 | 17 | Setting-specific enum (dropdown choices for registers) |
| 6388 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6491 | 5 | Setting-specific enum (dropdown choices for registers) |
| 6492 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6477 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6486 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6460 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6467 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6394 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6399 | 4 | Setting-specific enum (dropdown choices for registers) |
| 6501 | 8 | Setting-specific enum (dropdown choices for registers) |
| 6474 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6367 | 2 | Setting-specific enum (dropdown choices for registers) |
| 6368 | 3 | Setting-specific enum (dropdown choices for registers) |
| 6457 | 6 | Setting-specific enum (dropdown choices for registers) |
| 6485 | 3 | Setting-specific enum (dropdown choices for registers) |
| 6410 | 4 | Setting-specific enum (dropdown choices for registers) |
| 6454 | 7 | Setting-specific enum (dropdown choices for registers) |
| 6584 | 3 | Setting-specific enum (dropdown choices for registers) |

### G60 Base tables

| FormatIndex | Entries | Role |
|-------------|--------:|------|
| 9779 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9778 | 4 | Setting-specific enum (dropdown choices for registers) |
| 10021 | 4 | Setting-specific enum (dropdown choices for registers) |
| 9789 | 12 | Setting-specific enum (dropdown choices for registers) |
| 9790 | 3 | Setting-specific enum (dropdown choices for registers) |
| 10051 | 2 | Setting-specific enum (dropdown choices for registers) |
| 10043 | 3 | Setting-specific enum (dropdown choices for registers) |
| 10012 | 2001 | Logic / Flex operand dictionary (contacts, VOs, protection outputs, FlexLogic tokens) |
| 10013 | 1170 | Signal / measurement operand dictionary (SRC1 Ia RMS, SRC1 P, etc.) |
| 10045 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9852 | 6 | Setting-specific enum (dropdown choices for registers) |
| 10074 | 12 | Setting-specific enum (dropdown choices for registers) |
| 10053 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9994 | 4 | Setting-specific enum (dropdown choices for registers) |
| 9995 | 4 | Setting-specific enum (dropdown choices for registers) |
| 9996 | 6 | Setting-specific enum (dropdown choices for registers) |
| 9802 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9791 | 3 | Setting-specific enum (dropdown choices for registers) |
| 9784 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9893 | 12 | Setting-specific enum (dropdown choices for registers) |
| 9894 | 7 | Setting-specific enum (dropdown choices for registers) |
| 9895 | 5 | Setting-specific enum (dropdown choices for registers) |
| 9795 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9858 | 5 | Setting-specific enum (dropdown choices for registers) |
| 9915 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9815 | 3 | Setting-specific enum (dropdown choices for registers) |
| 9808 | 6 | Setting-specific enum (dropdown choices for registers) |
| 9803 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9799 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9920 | 5 | Setting-specific enum (dropdown choices for registers) |
| 9921 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9777 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9841 | 7 | Setting-specific enum (dropdown choices for registers) |
| 9783 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9842 | 4 | Setting-specific enum (dropdown choices for registers) |
| 9931 | 5 | Setting-specific enum (dropdown choices for registers) |
| 9875 | 5 | Setting-specific enum (dropdown choices for registers) |
| 9932 | 4 | Setting-specific enum (dropdown choices for registers) |
| 6 | 4 | Setting-specific enum (dropdown choices for registers) |
| 10075 | 3 | Setting-specific enum (dropdown choices for registers) |
| 9929 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9832 | 2 | Setting-specific enum (dropdown choices for registers) |
| 10118 | 129 | Large G60-specific enum (130 entries) |
| 9805 | 3 | Setting-specific enum (dropdown choices for registers) |
| 9986 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9987 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9988 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9989 | 3 | Setting-specific enum (dropdown choices for registers) |
| 9786 | 3 | Setting-specific enum (dropdown choices for registers) |
| 9990 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9829 | 3 | Setting-specific enum (dropdown choices for registers) |
| 9797 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9828 | 13 | Setting-specific enum (dropdown choices for registers) |
| 9762 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9984 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9985 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9798 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9780 | 17 | Setting-specific enum (dropdown choices for registers) |
| 9781 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9886 | 5 | Setting-specific enum (dropdown choices for registers) |
| 9887 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9871 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9881 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9854 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9861 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9788 | 6 | Setting-specific enum (dropdown choices for registers) |
| 9793 | 4 | Setting-specific enum (dropdown choices for registers) |
| 9896 | 8 | Setting-specific enum (dropdown choices for registers) |
| 9868 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9826 | 49 | Setting-specific enum (dropdown choices for registers) |
| 9760 | 2 | Setting-specific enum (dropdown choices for registers) |
| 9761 | 3 | Setting-specific enum (dropdown choices for registers) |
| 10117 | 7 | Setting-specific enum (dropdown choices for registers) |
| 9851 | 6 | Setting-specific enum (dropdown choices for registers) |
| 10112 | 2 | Setting-specific enum (dropdown choices for registers) |
| 10096 | 6 | Setting-specific enum (dropdown choices for registers) |
| 10103 | 4 | Setting-specific enum (dropdown choices for registers) |
| 9880 | 3 | Setting-specific enum (dropdown choices for registers) |
| 9804 | 4 | Setting-specific enum (dropdown choices for registers) |
| 9848 | 7 | Setting-specific enum (dropdown choices for registers) |
| 9993 | 3 | Setting-specific enum (dropdown choices for registers) |
| 10092 | 3 | Setting-specific enum (dropdown choices for registers) |

---

## FormatIndex 10012 - Logic / Flex Operand Table

Used by `SettingType="Flex"` for LED assignments, oscillography triggers, FlexLogic operands, contact/virtual-output picks, and protection element outputs.
The converter builds a **name-to-G60-code** map from this table (`build_flex_operand_map`).

**Why codes differ:** G30 7.x and G60 8.x assign different internal numeric IDs to the same logical operand. Matching is by **operand name** (or hardware address suffix for contacts/VOs), not by copying the G30 code.

### Summary

| Metric | Count |
|--------|------:|
| G30 entries | 1345 |
| G60 entries | 2001 |
| Same name **and** same code | 295 |
| Same name, **different code** | 956 |
| G30 only (name absent on G60) | 94 |
| G60 only (name absent on G30) | 750 |

### Full entry comparison

| Name | G30 Code | G60 Code | Status |
|------|----------|----------|--------|
| 100 STATOR DPO | - | 2149581179 | G60 only |
| 100 STATOR OP | - | 2148794747 | G60 only |
| 100 STATOR PKP | - | 2148532603 | G60 only |
| 100 STATOR STG1 DPO | - | 2149056891 | G60 only |
| 100 STATOR STG1 OP | - | 2148008315 | G60 only |
| 100 STATOR STG1 PKP | - | 2147484027 | G60 only |
| 100 STATOR STG2 DPO | - | 2149319035 | G60 only |
| 100 STATOR STG2 OP | - | 2148270459 | G60 only |
| 100 STATOR STG2 PKP | - | 2147746171 | G60 only |
| 3RD HARM NTRL UV DPO | 2148008266 | 2148008469 | Code changed |
| 3RD HARM NTRL UV OP | 2147746122 | 2147746325 | Code changed |
| 3RD HARM NTRL UV PKP | 2147483978 | 2147484181 | Code changed |
| 50-3 (FE 1) DPO | 2148008336 | - | G30 only |
| 50-3 (FE 1) OP | 2147746192 | - | G30 only |
| 50-3 (FE 1) PKP | 2147484048 | - | G30 only |
| ACCDNT ENRG ARMED | 2147483944 | 2147484147 | Code changed |
| ACCDNT ENRG DPO | 2148008232 | 2148008435 | Code changed |
| ACCDNT ENRG OP | 2147746088 | 2147746291 | Code changed |
| ACCESS LOC CMND OFF | 1572886 | 1572886 | Identical |
| ACCESS LOC CMND ON | 1572885 | 1572885 | Identical |
| ACCESS LOC SETG OFF | 1572884 | 1572884 | Identical |
| ACCESS LOC SETG ON | 1572883 | 1572883 | Identical |
| ACCESS REM CMND OFF | 1572890 | 1572890 | Identical |
| ACCESS REM CMND ON | 1572889 | 1572889 | Identical |
| ACCESS REM SETG OFF | 1572888 | 1572888 | Identical |
| ACCESS REM SETG ON | 1572887 | 1572887 | Identical |
| Active Freq Ref=Main | - | 1572926 | G60 only |
| ANY MAJOR ERROR | 3538975 | 3538975 | Identical |
| ANY MINOR ERROR | 3538974 | 3538974 | Identical |
| ANY SELF TESTS | 3538944 | 3538944 | Identical |
| AUX OV 1 DPO | 2148008084 | 2148008235 | Code changed |
| AUX OV 1 OP | 2147745940 | 2147746091 | Code changed |
| AUX OV 1 PKP | 2147483796 | 2147483947 | Code changed |
| AUX OV 2 DPO | 2148008085 | 2148008236 | Code changed |
| AUX OV 2 OP | 2147745941 | 2147746092 | Code changed |
| AUX OV 2 PKP | 2147483797 | 2147483948 | Code changed |
| AUX UV 1 DPO | 2148008076 | 2148008651 | Code changed |
| AUX UV 1 OP | 2147745932 | 2147746507 | Code changed |
| AUX UV 1 PKP | 2147483788 | 2147484363 | Code changed |
| AUX UV 2 DPO | 2148008077 | 2148008652 | Code changed |
| AUX UV 2 OP | 2147745933 | 2147746508 | Code changed |
| AUX UV 2 PKP | 2147483789 | 2147484364 | Code changed |
| AUX UV 3 DPO | 2148008078 | 2148008653 | Code changed |
| AUX UV 3 OP | 2147745934 | 2147746509 | Code changed |
| AUX UV 3 PKP | 2147483790 | 2147484365 | Code changed |
| BATTERY FAIL | 3538963 | 3538963 | Identical |
| BKR 1 FLSHOVR DPO | - | 2150368528 | G60 only |
| BKR 1 FLSHOVR DPO A | - | 2149582096 | G60 only |
| BKR 1 FLSHOVR DPO B | - | 2149844240 | G60 only |
| BKR 1 FLSHOVR DPO C | - | 2150106384 | G60 only |
| BKR 1 FLSHOVR OP | - | 2149319952 | G60 only |
| BKR 1 FLSHOVR OP A | - | 2148533520 | G60 only |
| BKR 1 FLSHOVR OP B | - | 2148795664 | G60 only |
| BKR 1 FLSHOVR OP C | - | 2149057808 | G60 only |
| BKR 1 FLSHOVR PKP | - | 2148271376 | G60 only |
| BKR 1 FLSHOVR PKP A | - | 2147484944 | G60 only |
| BKR 1 FLSHOVR PKP B | - | 2147747088 | G60 only |
| BKR 1 FLSHOVR PKP C | - | 2148009232 | G60 only |
| BKR 2 FLSHOVR DPO | - | 2150368529 | G60 only |
| BKR 2 FLSHOVR DPO A | - | 2149582097 | G60 only |
| BKR 2 FLSHOVR DPO B | - | 2149844241 | G60 only |
| BKR 2 FLSHOVR DPO C | - | 2150106385 | G60 only |
| BKR 2 FLSHOVR OP | - | 2149319953 | G60 only |
| BKR 2 FLSHOVR OP A | - | 2148533521 | G60 only |
| BKR 2 FLSHOVR OP B | - | 2148795665 | G60 only |
| BKR 2 FLSHOVR OP C | - | 2149057809 | G60 only |
| BKR 2 FLSHOVR PKP | - | 2148271377 | G60 only |
| BKR 2 FLSHOVR PKP A | - | 2147484945 | G60 only |
| BKR 2 FLSHOVR PKP B | - | 2147747089 | G60 only |
| BKR 2 FLSHOVR PKP C | - | 2148009233 | G60 only |
| BKR ARC 1 DPO | 2147746080 | 2147746285 | Code changed |
| BKR ARC 1 MAX DPO | 2148270368 | 2148270573 | Code changed |
| BKR ARC 1 MAX OP | 2148008224 | 2148008429 | Code changed |
| BKR ARC 1 OP | 2147483936 | 2147484141 | Code changed |
| BKR ARC 2 DPO | 2147746081 | 2147746286 | Code changed |
| BKR ARC 2 MAX DPO | 2148270369 | 2148270574 | Code changed |
| BKR ARC 2 MAX OP | 2148008225 | 2148008430 | Code changed |
| BKR ARC 2 OP | 2147483937 | 2147484142 | Code changed |
| BKR FAIL 1 RETRIP | - | 2148532687 | G60 only |
| BKR FAIL 1 RETRIPA | - | 2149319119 | G60 only |
| BKR FAIL 1 RETRIPB | - | 2149056975 | G60 only |
| BKR FAIL 1 RETRIPC | - | 2148794831 | G60 only |
| BKR FAIL 1 T1 OP | - | 2148270543 | G60 only |
| BKR FAIL 1 T2 OP | - | 2148008399 | G60 only |
| BKR FAIL 1 T3 OP | - | 2147746255 | G60 only |
| BKR FAIL 1 TRIP OP | - | 2147484111 | G60 only |
| BKR FAIL 2 RETRIP | - | 2148532688 | G60 only |
| BKR FAIL 2 RETRIPA | - | 2149319120 | G60 only |
| BKR FAIL 2 RETRIPB | - | 2149056976 | G60 only |
| BKR FAIL 2 RETRIPC | - | 2148794832 | G60 only |
| BKR FAIL 2 T1 OP | - | 2148270544 | G60 only |
| BKR FAIL 2 T2 OP | - | 2148008400 | G60 only |
| BKR FAIL 2 T3 OP | - | 2147746256 | G60 only |
| BKR FAIL 2 TRIP OP | - | 2147484112 | G60 only |
| BREAKER 1 ANY P OPEN | 2150368200 | 2150368463 | Code changed |
| BREAKER 1 BAD STATUS | 2147484622 | 2147484885 | Code changed |
| BREAKER 1 BLK RCLS | 2149057492 | 2148533467 | Code changed |
| BREAKER 1 BYPASS OFF | 2148795348 | - | G30 only |
| BREAKER 1 BYPASS ON | 2148533204 | - | G30 only |
| BREAKER 1 CLOSED | 2148008904 | 2148009167 | Code changed |
| BREAKER 1 DISCREP | 2148795336 | 2148795599 | Code changed |
| BREAKER 1 ENA RCLS | 2149319636 | 2148795611 | Code changed |
| BREAKER 1 MNL CLS | 2149319624 | 2149319887 | Code changed |
| BREAKER 1 MNL OPEN | 2149057480 | 2149057743 | Code changed |
| BREAKER 1 OFF CMD | 2147484616 | 2147484879 | Code changed |
| BREAKER 1 ON CMD | 2147746760 | 2147747023 | Code changed |
| BREAKER 1 ONE P OPEN | 2150630344 | 2150630607 | Code changed |
| BREAKER 1 OOS | 2150892488 | 2150892751 | Code changed |
| BREAKER 1 OPEN | 2148271048 | 2148271311 | Code changed |
| BREAKER 1 Phase A BAD STATUS | 2147746766 | 2147747029 | Code changed |
| BREAKER 1 Phase A CLOSED | 2148533198 | 2148533461 | Code changed |
| BREAKER 1 Phase A INTERM | 2150106062 | 2150106325 | Code changed |
| BREAKER 1 Phase A OPEN | 2149319630 | 2149319893 | Code changed |
| BREAKER 1 Phase B BAD STATUS | 2148008910 | 2148009173 | Code changed |
| BREAKER 1 Phase B CLOSED | 2148795342 | 2148795605 | Code changed |
| BREAKER 1 Phase B INTERM | 2150368206 | 2150368469 | Code changed |
| BREAKER 1 Phase B OPEN | 2149581774 | 2149582037 | Code changed |
| BREAKER 1 Phase C BAD STATUS | 2148271054 | 2148271317 | Code changed |
| BREAKER 1 Phase C CLOSED | 2149057486 | 2149057749 | Code changed |
| BREAKER 1 Phase C INTERM | 2150630350 | 2150630613 | Code changed |
| BREAKER 1 Phase C OPEN | 2149843918 | 2149844181 | Code changed |
| BREAKER 1 SUBD CLSD | 2148008916 | 2148009179 | Code changed |
| BREAKER 1 SUBD OPEN | 2148271060 | 2148271323 | Code changed |
| BREAKER 1 TAG OFF | 2147746772 | 2147747035 | Code changed |
| BREAKER 1 TAG ON | 2147484628 | 2147484891 | Code changed |
| BREAKER 1 TRIP A | 2149581768 | 2149582031 | Code changed |
| BREAKER 1 TRIP B | 2149843912 | 2149844175 | Code changed |
| BREAKER 1 TRIP C | 2150106056 | 2150106319 | Code changed |
| BREAKER 1 TROUBLE | 2148533192 | 2148533455 | Code changed |
| BREAKER 2 ANY P OPEN | 2150368201 | 2150368464 | Code changed |
| BREAKER 2 BAD STATUS | 2147484623 | 2147484886 | Code changed |
| BREAKER 2 BLK RCLS | 2149057493 | 2148533468 | Code changed |
| BREAKER 2 BYPASS OFF | 2148795349 | - | G30 only |
| BREAKER 2 BYPASS ON | 2148533205 | - | G30 only |
| BREAKER 2 CLOSED | 2148008905 | 2148009168 | Code changed |
| BREAKER 2 DISCREP | 2148795337 | 2148795600 | Code changed |
| BREAKER 2 ENA RCLS | 2149319637 | 2148795612 | Code changed |
| BREAKER 2 MNL CLS | 2149319625 | 2149319888 | Code changed |
| BREAKER 2 MNL OPEN | 2149057481 | 2149057744 | Code changed |
| BREAKER 2 OFF CMD | 2147484617 | 2147484880 | Code changed |
| BREAKER 2 ON CMD | 2147746761 | 2147747024 | Code changed |
| BREAKER 2 ONE P OPEN | 2150630345 | 2150630608 | Code changed |
| BREAKER 2 OOS | 2150892489 | 2150892752 | Code changed |
| BREAKER 2 OPEN | 2148271049 | 2148271312 | Code changed |
| BREAKER 2 Phase A BAD STATUS | 2147746767 | 2147747030 | Code changed |
| BREAKER 2 Phase A CLOSED | 2148533199 | 2148533462 | Code changed |
| BREAKER 2 Phase A INTERM | 2150106063 | 2150106326 | Code changed |
| BREAKER 2 Phase A OPEN | 2149319631 | 2149319894 | Code changed |
| BREAKER 2 Phase B BAD STATUS | 2148008911 | 2148009174 | Code changed |
| BREAKER 2 Phase B CLOSED | 2148795343 | 2148795606 | Code changed |
| BREAKER 2 Phase B INTERM | 2150368207 | 2150368470 | Code changed |
| BREAKER 2 Phase B OPEN | 2149581775 | 2149582038 | Code changed |
| BREAKER 2 Phase C BAD STATUS | 2148271055 | 2148271318 | Code changed |
| BREAKER 2 Phase C CLOSED | 2149057487 | 2149057750 | Code changed |
| BREAKER 2 Phase C INTERM | 2150630351 | 2150630614 | Code changed |
| BREAKER 2 Phase C OPEN | 2149843919 | 2149844182 | Code changed |
| BREAKER 2 SUBD CLSD | 2148008917 | 2148009180 | Code changed |
| BREAKER 2 SUBD OPEN | 2148271061 | 2148271324 | Code changed |
| BREAKER 2 TAG OFF | 2147746773 | 2147747036 | Code changed |
| BREAKER 2 TAG ON | 2147484629 | 2147484892 | Code changed |
| BREAKER 2 TRIP A | 2149581769 | 2149582032 | Code changed |
| BREAKER 2 TRIP B | 2149843913 | 2149844176 | Code changed |
| BREAKER 2 TRIP C | 2150106057 | 2150106320 | Code changed |
| BREAKER 2 TROUBLE | 2148533193 | 2148533456 | Code changed |
| BRK RESTRIKE 1 OP | - | 2148271370 | G60 only |
| BRK RESTRIKE 1 OP A | - | 2147484938 | G60 only |
| BRK RESTRIKE 1 OP B | - | 2147747082 | G60 only |
| BRK RESTRIKE 1 OP C | - | 2148009226 | G60 only |
| BRK RESTRIKE 2 OP | - | 2148271371 | G60 only |
| BRK RESTRIKE 2 OP A | - | 2147484939 | G60 only |
| BRK RESTRIKE 2 OP B | - | 2147747083 | G60 only |
| BRK RESTRIKE 2 OP C | - | 2148009227 | G60 only |
| CHANGE PH ROT | 2147483749 | 2147483895 | Code changed |
| CLOCK UNSYNCHRONIZED | 1572896 | 1572896 | Identical |
| Cont Ip 1 Off(H7a) | - | 196609 | G60 only |
| Cont Ip 1 On(H7a) | - | 131073 | G60 only |
| Cont Ip 2 Off(H7c) | - | 196610 | G60 only |
| Cont Ip 2 On(H7c) | - | 131074 | G60 only |
| Cont Ip 3 Off(H8a) | - | 196611 | G60 only |
| Cont Ip 3 On(H8a) | - | 131075 | G60 only |
| Cont Ip 4 Off(H8c) | - | 196612 | G60 only |
| Cont Ip 4 On(H8c) | - | 131076 | G60 only |
| Cont Op 1 Closed (H1) | - | 524289 | G60 only |
| Cont Op 1 IOn (H1) | - | 786433 | G60 only |
| Cont Op 1 VOff (H1) | - | 720897 | G60 only |
| Cont Op 1 VOn (H1) | - | 655361 | G60 only |
| Cont Op 2 Closed (H2) | - | 524290 | G60 only |
| Cont Op 2 IOn (H2) | - | 786434 | G60 only |
| Cont Op 2 VOff (H2) | - | 720898 | G60 only |
| Cont Op 2 VOn (H2) | - | 655362 | G60 only |
| Cont Op 3 Closed (H3) | - | 524291 | G60 only |
| Cont Op 3 IOn (H3) | - | 786435 | G60 only |
| Cont Op 3 VOff (H3) | - | 720899 | G60 only |
| Cont Op 3 VOn (H3) | - | 655363 | G60 only |
| Cont Op 4 Closed (H4) | - | 524292 | G60 only |
| Cont Op 4 IOn (H4) | - | 786436 | G60 only |
| Cont Op 4 VOff (H4) | - | 720900 | G60 only |
| Cont Op 4 VOn (H4) | - | 655364 | G60 only |
| Cont Op 5 Closed (H5) | - | 524293 | G60 only |
| Cont Op 5 IOn (H5) | - | 786437 | G60 only |
| Cont Op 5 VOff (H5) | - | 720901 | G60 only |
| Cont Op 5 VOn (H5) | - | 655365 | G60 only |
| Cont Op 6 Closed (H6) | - | 524294 | G60 only |
| Cont Op 6 IOn (H6) | - | 786438 | G60 only |
| Cont Op 6 VOff (H6) | - | 720902 | G60 only |
| Cont Op 6 VOn (H6) | - | 655366 | G60 only |
| CONTROL PUSHBUTTON 1 ON | 2147484038 | 2147484241 | Code changed |
| CONTROL PUSHBUTTON 2 ON | 2147484039 | 2147484242 | Code changed |
| CONTROL PUSHBUTTON 3 ON | 2147484040 | 2147484243 | Code changed |
| COP PROTSUPR | - | 12189697 | G60 only |
| Counter 1 (CNT 1) EQL | 2147746336 | 2147746952 | Code changed |
| Counter 1 (CNT 1) HI | 2147484192 | 2147484808 | Code changed |
| Counter 1 (CNT 1) LO | 2148008480 | 2148009096 | Code changed |
| Counter 2 (CNT 2) EQL | 2147746337 | 2147746953 | Code changed |
| Counter 2 (CNT 2) HI | 2147484193 | 2147484809 | Code changed |
| Counter 2 (CNT 2) LO | 2148008481 | 2148009097 | Code changed |
| Counter 3 (CNT 3) EQL | 2147746338 | 2147746954 | Code changed |
| Counter 3 (CNT 3) HI | 2147484194 | 2147484810 | Code changed |
| Counter 3 (CNT 3) LO | 2148008482 | 2148009098 | Code changed |
| Counter 4 (CNT 4) EQL | 2147746339 | 2147746955 | Code changed |
| Counter 4 (CNT 4) HI | 2147484195 | 2147484811 | Code changed |
| Counter 4 (CNT 4) LO | 2148008483 | 2148009099 | Code changed |
| Counter 5 (CNT 5) EQL | 2147746340 | 2147746956 | Code changed |
| Counter 5 (CNT 5) HI | 2147484196 | 2147484812 | Code changed |
| Counter 5 (CNT 5) LO | 2148008484 | 2148009100 | Code changed |
| Counter 6 (CNT 6) EQL | 2147746341 | 2147746957 | Code changed |
| Counter 6 (CNT 6) HI | 2147484197 | 2147484813 | Code changed |
| Counter 6 (CNT 6) LO | 2148008485 | 2148009101 | Code changed |
| Counter 7 (CNT 7) EQL | 2147746342 | 2147746958 | Code changed |
| Counter 7 (CNT 7) HI | 2147484198 | 2147484814 | Code changed |
| Counter 7 (CNT 7) LO | 2148008486 | 2148009102 | Code changed |
| Counter 8 (CNT 8) EQL | 2147746343 | 2147746959 | Code changed |
| Counter 8 (CNT 8) HI | 2147484199 | 2147484815 | Code changed |
| Counter 8 (CNT 8) LO | 2148008487 | 2148009103 | Code changed |
| CT FAIL 1 OP | 2147746064 | 2147746247 | Code changed |
| CT FAIL 1 PKP | 2147483920 | 2147484103 | Code changed |
| CT FAIL 2 OP | 2147746065 | 2147746248 | Code changed |
| CT FAIL 2 PKP | 2147483921 | 2147484104 | Code changed |
| CT FAIL 3 OP | 2147746066 | 2147746249 | Code changed |
| CT FAIL 3 PKP | 2147483922 | 2147484105 | Code changed |
| CT FAIL 4 OP | 2147746067 | 2147746250 | Code changed |
| CT FAIL 4 PKP | 2147483923 | 2147484106 | Code changed |
| Dig Element 1(DE1) DPO | 2148008628 | 2148008843 | Code changed |
| Dig Element 1(DE1) OP | 2147746484 | 2147746699 | Code changed |
| Dig Element 1(DE1) PKP | 2147484340 | 2147484555 | Code changed |
| Dig Element 10(DE10) DPO | 2148008637 | 2148008852 | Code changed |
| Dig Element 10(DE10) OP | 2147746493 | 2147746708 | Code changed |
| Dig Element 10(DE10) PKP | 2147484349 | 2147484564 | Code changed |
| Dig Element 11(DE11) DPO | 2148008638 | 2148008853 | Code changed |
| Dig Element 11(DE11) OP | 2147746494 | 2147746709 | Code changed |
| Dig Element 11(DE11) PKP | 2147484350 | 2147484565 | Code changed |
| Dig Element 12(DE12) DPO | 2148008639 | 2148008854 | Code changed |
| Dig Element 12(DE12) OP | 2147746495 | 2147746710 | Code changed |
| Dig Element 12(DE12) PKP | 2147484351 | 2147484566 | Code changed |
| Dig Element 13(DE13) DPO | 2148008640 | 2148008855 | Code changed |
| Dig Element 13(DE13) OP | 2147746496 | 2147746711 | Code changed |
| Dig Element 13(DE13) PKP | 2147484352 | 2147484567 | Code changed |
| Dig Element 14(DE14) DPO | 2148008641 | 2148008856 | Code changed |
| Dig Element 14(DE14) OP | 2147746497 | 2147746712 | Code changed |
| Dig Element 14(DE14) PKP | 2147484353 | 2147484568 | Code changed |
| Dig Element 15(DE15) DPO | 2148008642 | 2148008857 | Code changed |
| Dig Element 15(DE15) OP | 2147746498 | 2147746713 | Code changed |
| Dig Element 15(DE15) PKP | 2147484354 | 2147484569 | Code changed |
| Dig Element 16(DE16) DPO | 2148008643 | 2148008858 | Code changed |
| Dig Element 16(DE16) OP | 2147746499 | 2147746714 | Code changed |
| Dig Element 16(DE16) PKP | 2147484355 | 2147484570 | Code changed |
| Dig Element 17(DE17) DPO | 2148008644 | 2148008859 | Code changed |
| Dig Element 17(DE17) OP | 2147746500 | 2147746715 | Code changed |
| Dig Element 17(DE17) PKP | 2147484356 | 2147484571 | Code changed |
| Dig Element 18(DE18) DPO | 2148008645 | 2148008860 | Code changed |
| Dig Element 18(DE18) OP | 2147746501 | 2147746716 | Code changed |
| Dig Element 18(DE18) PKP | 2147484357 | 2147484572 | Code changed |
| Dig Element 19(DE19) DPO | 2148008646 | 2148008861 | Code changed |
| Dig Element 19(DE19) OP | 2147746502 | 2147746717 | Code changed |
| Dig Element 19(DE19) PKP | 2147484358 | 2147484573 | Code changed |
| Dig Element 2(DE2) DPO | 2148008629 | 2148008844 | Code changed |
| Dig Element 2(DE2) OP | 2147746485 | 2147746700 | Code changed |
| Dig Element 2(DE2) PKP | 2147484341 | 2147484556 | Code changed |
| Dig Element 20(DE20) DPO | 2148008647 | 2148008862 | Code changed |
| Dig Element 20(DE20) OP | 2147746503 | 2147746718 | Code changed |
| Dig Element 20(DE20) PKP | 2147484359 | 2147484574 | Code changed |
| Dig Element 21(DE21) DPO | 2148008648 | 2148008863 | Code changed |
| Dig Element 21(DE21) OP | 2147746504 | 2147746719 | Code changed |
| Dig Element 21(DE21) PKP | 2147484360 | 2147484575 | Code changed |
| Dig Element 22(DE22) DPO | 2148008649 | 2148008864 | Code changed |
| Dig Element 22(DE22) OP | 2147746505 | 2147746720 | Code changed |
| Dig Element 22(DE22) PKP | 2147484361 | 2147484576 | Code changed |
| Dig Element 23(DE23) DPO | 2148008650 | 2148008865 | Code changed |
| Dig Element 23(DE23) OP | 2147746506 | 2147746721 | Code changed |
| Dig Element 23(DE23) PKP | 2147484362 | 2147484577 | Code changed |
| Dig Element 24(DE24) DPO | 2148008651 | 2148008866 | Code changed |
| Dig Element 24(DE24) OP | 2147746507 | 2147746722 | Code changed |
| Dig Element 24(DE24) PKP | 2147484363 | 2147484578 | Code changed |
| Dig Element 25(DE25) DPO | 2148008652 | 2148008867 | Code changed |
| Dig Element 25(DE25) OP | 2147746508 | 2147746723 | Code changed |
| Dig Element 25(DE25) PKP | 2147484364 | 2147484579 | Code changed |
| Dig Element 26(DE26) DPO | 2148008653 | 2148008868 | Code changed |
| Dig Element 26(DE26) OP | 2147746509 | 2147746724 | Code changed |
| Dig Element 26(DE26) PKP | 2147484365 | 2147484580 | Code changed |
| Dig Element 27(DE27) DPO | 2148008654 | 2148008869 | Code changed |
| Dig Element 27(DE27) OP | 2147746510 | 2147746725 | Code changed |
| Dig Element 27(DE27) PKP | 2147484366 | 2147484581 | Code changed |
| Dig Element 28(DE28) DPO | 2148008655 | 2148008870 | Code changed |
| Dig Element 28(DE28) OP | 2147746511 | 2147746726 | Code changed |
| Dig Element 28(DE28) PKP | 2147484367 | 2147484582 | Code changed |
| Dig Element 29(DE29) DPO | 2148008656 | 2148008871 | Code changed |
| Dig Element 29(DE29) OP | 2147746512 | 2147746727 | Code changed |
| Dig Element 29(DE29) PKP | 2147484368 | 2147484583 | Code changed |
| Dig Element 3(DE3) DPO | 2148008630 | 2148008845 | Code changed |
| Dig Element 3(DE3) OP | 2147746486 | 2147746701 | Code changed |
| Dig Element 3(DE3) PKP | 2147484342 | 2147484557 | Code changed |
| Dig Element 30(DE30) DPO | 2148008657 | 2148008872 | Code changed |
| Dig Element 30(DE30) OP | 2147746513 | 2147746728 | Code changed |
| Dig Element 30(DE30) PKP | 2147484369 | 2147484584 | Code changed |
| Dig Element 31(DE31) DPO | 2148008658 | 2148008873 | Code changed |
| Dig Element 31(DE31) OP | 2147746514 | 2147746729 | Code changed |
| Dig Element 31(DE31) PKP | 2147484370 | 2147484585 | Code changed |
| Dig Element 32(DE32) DPO | 2148008659 | 2148008874 | Code changed |
| Dig Element 32(DE32) OP | 2147746515 | 2147746730 | Code changed |
| Dig Element 32(DE32) PKP | 2147484371 | 2147484586 | Code changed |
| Dig Element 33(DE33) DPO | 2148008660 | 2148008875 | Code changed |
| Dig Element 33(DE33) OP | 2147746516 | 2147746731 | Code changed |
| Dig Element 33(DE33) PKP | 2147484372 | 2147484587 | Code changed |
| Dig Element 34(DE34) DPO | 2148008661 | 2148008876 | Code changed |
| Dig Element 34(DE34) OP | 2147746517 | 2147746732 | Code changed |
| Dig Element 34(DE34) PKP | 2147484373 | 2147484588 | Code changed |
| Dig Element 35(DE35) DPO | 2148008662 | 2148008877 | Code changed |
| Dig Element 35(DE35) OP | 2147746518 | 2147746733 | Code changed |
| Dig Element 35(DE35) PKP | 2147484374 | 2147484589 | Code changed |
| Dig Element 36(DE36) DPO | 2148008663 | 2148008878 | Code changed |
| Dig Element 36(DE36) OP | 2147746519 | 2147746734 | Code changed |
| Dig Element 36(DE36) PKP | 2147484375 | 2147484590 | Code changed |
| Dig Element 37(DE37) DPO | 2148008664 | 2148008879 | Code changed |
| Dig Element 37(DE37) OP | 2147746520 | 2147746735 | Code changed |
| Dig Element 37(DE37) PKP | 2147484376 | 2147484591 | Code changed |
| Dig Element 38(DE38) DPO | 2148008665 | 2148008880 | Code changed |
| Dig Element 38(DE38) OP | 2147746521 | 2147746736 | Code changed |
| Dig Element 38(DE38) PKP | 2147484377 | 2147484592 | Code changed |
| Dig Element 39(DE39) DPO | 2148008666 | 2148008881 | Code changed |
| Dig Element 39(DE39) OP | 2147746522 | 2147746737 | Code changed |
| Dig Element 39(DE39) PKP | 2147484378 | 2147484593 | Code changed |
| Dig Element 4(DE4) DPO | 2148008631 | 2148008846 | Code changed |
| Dig Element 4(DE4) OP | 2147746487 | 2147746702 | Code changed |
| Dig Element 4(DE4) PKP | 2147484343 | 2147484558 | Code changed |
| Dig Element 40(DE40) DPO | 2148008667 | 2148008882 | Code changed |
| Dig Element 40(DE40) OP | 2147746523 | 2147746738 | Code changed |
| Dig Element 40(DE40) PKP | 2147484379 | 2147484594 | Code changed |
| Dig Element 41(DE41) DPO | 2148008668 | 2148008883 | Code changed |
| Dig Element 41(DE41) OP | 2147746524 | 2147746739 | Code changed |
| Dig Element 41(DE41) PKP | 2147484380 | 2147484595 | Code changed |
| Dig Element 42(DE42) DPO | 2148008669 | 2148008884 | Code changed |
| Dig Element 42(DE42) OP | 2147746525 | 2147746740 | Code changed |
| Dig Element 42(DE42) PKP | 2147484381 | 2147484596 | Code changed |
| Dig Element 43(DE43) DPO | 2148008670 | 2148008885 | Code changed |
| Dig Element 43(DE43) OP | 2147746526 | 2147746741 | Code changed |
| Dig Element 43(DE43) PKP | 2147484382 | 2147484597 | Code changed |
| Dig Element 44(DE44) DPO | 2148008671 | 2148008886 | Code changed |
| Dig Element 44(DE44) OP | 2147746527 | 2147746742 | Code changed |
| Dig Element 44(DE44) PKP | 2147484383 | 2147484598 | Code changed |
| Dig Element 45(DE45) DPO | 2148008672 | 2148008887 | Code changed |
| Dig Element 45(DE45) OP | 2147746528 | 2147746743 | Code changed |
| Dig Element 45(DE45) PKP | 2147484384 | 2147484599 | Code changed |
| Dig Element 46(DE46) DPO | 2148008673 | 2148008888 | Code changed |
| Dig Element 46(DE46) OP | 2147746529 | 2147746744 | Code changed |
| Dig Element 46(DE46) PKP | 2147484385 | 2147484600 | Code changed |
| Dig Element 47(DE47) DPO | 2148008674 | 2148008889 | Code changed |
| Dig Element 47(DE47) OP | 2147746530 | 2147746745 | Code changed |
| Dig Element 47(DE47) PKP | 2147484386 | 2147484601 | Code changed |
| Dig Element 48(DE48) DPO | 2148008675 | 2148008890 | Code changed |
| Dig Element 48(DE48) OP | 2147746531 | 2147746746 | Code changed |
| Dig Element 48(DE48) PKP | 2147484387 | 2147484602 | Code changed |
| Dig Element 49(DE49) DPO | - | 2148008891 | G60 only |
| Dig Element 49(DE49) OP | - | 2147746747 | G60 only |
| Dig Element 49(DE49) PKP | - | 2147484603 | G60 only |
| Dig Element 5(DE5) DPO | 2148008632 | 2148008847 | Code changed |
| Dig Element 5(DE5) OP | 2147746488 | 2147746703 | Code changed |
| Dig Element 5(DE5) PKP | 2147484344 | 2147484559 | Code changed |
| Dig Element 50(DE50) DPO | - | 2148008892 | G60 only |
| Dig Element 50(DE50) OP | - | 2147746748 | G60 only |
| Dig Element 50(DE50) PKP | - | 2147484604 | G60 only |
| Dig Element 51(DE51) DPO | - | 2148008893 | G60 only |
| Dig Element 51(DE51) OP | - | 2147746749 | G60 only |
| Dig Element 51(DE51) PKP | - | 2147484605 | G60 only |
| Dig Element 52(DE52) DPO | - | 2148008894 | G60 only |
| Dig Element 52(DE52) OP | - | 2147746750 | G60 only |
| Dig Element 52(DE52) PKP | - | 2147484606 | G60 only |
| Dig Element 53(DE53) DPO | - | 2148008895 | G60 only |
| Dig Element 53(DE53) OP | - | 2147746751 | G60 only |
| Dig Element 53(DE53) PKP | - | 2147484607 | G60 only |
| Dig Element 54(DE54) DPO | - | 2148008896 | G60 only |
| Dig Element 54(DE54) OP | - | 2147746752 | G60 only |
| Dig Element 54(DE54) PKP | - | 2147484608 | G60 only |
| Dig Element 55(DE55) DPO | - | 2148008897 | G60 only |
| Dig Element 55(DE55) OP | - | 2147746753 | G60 only |
| Dig Element 55(DE55) PKP | - | 2147484609 | G60 only |
| Dig Element 56(DE56) DPO | - | 2148008898 | G60 only |
| Dig Element 56(DE56) OP | - | 2147746754 | G60 only |
| Dig Element 56(DE56) PKP | - | 2147484610 | G60 only |
| Dig Element 57(DE57) DPO | - | 2148008899 | G60 only |
| Dig Element 57(DE57) OP | - | 2147746755 | G60 only |
| Dig Element 57(DE57) PKP | - | 2147484611 | G60 only |
| Dig Element 58(DE58) DPO | - | 2148008900 | G60 only |
| Dig Element 58(DE58) OP | - | 2147746756 | G60 only |
| Dig Element 58(DE58) PKP | - | 2147484612 | G60 only |
| Dig Element 59(DE59) DPO | - | 2148008901 | G60 only |
| Dig Element 59(DE59) OP | - | 2147746757 | G60 only |
| Dig Element 59(DE59) PKP | - | 2147484613 | G60 only |
| Dig Element 6(DE6) DPO | 2148008633 | 2148008848 | Code changed |
| Dig Element 6(DE6) OP | 2147746489 | 2147746704 | Code changed |
| Dig Element 6(DE6) PKP | 2147484345 | 2147484560 | Code changed |
| Dig Element 60(DE60) DPO | - | 2148008902 | G60 only |
| Dig Element 60(DE60) OP | - | 2147746758 | G60 only |
| Dig Element 60(DE60) PKP | - | 2147484614 | G60 only |
| Dig Element 61(DE61) DPO | - | 2148008903 | G60 only |
| Dig Element 61(DE61) OP | - | 2147746759 | G60 only |
| Dig Element 61(DE61) PKP | - | 2147484615 | G60 only |
| Dig Element 62(DE62) DPO | - | 2148008904 | G60 only |
| Dig Element 62(DE62) OP | - | 2147746760 | G60 only |
| Dig Element 62(DE62) PKP | - | 2147484616 | G60 only |
| Dig Element 63(DE63) DPO | - | 2148008905 | G60 only |
| Dig Element 63(DE63) OP | - | 2147746761 | G60 only |
| Dig Element 63(DE63) PKP | - | 2147484617 | G60 only |
| Dig Element 64(DE64) DPO | - | 2148008906 | G60 only |
| Dig Element 64(DE64) OP | - | 2147746762 | G60 only |
| Dig Element 64(DE64) PKP | - | 2147484618 | G60 only |
| Dig Element 65(DE65) DPO | - | 2148008907 | G60 only |
| Dig Element 65(DE65) OP | - | 2147746763 | G60 only |
| Dig Element 65(DE65) PKP | - | 2147484619 | G60 only |
| Dig Element 66(DE66) DPO | - | 2148008908 | G60 only |
| Dig Element 66(DE66) OP | - | 2147746764 | G60 only |
| Dig Element 66(DE66) PKP | - | 2147484620 | G60 only |
| Dig Element 67(DE67) DPO | - | 2148008909 | G60 only |
| Dig Element 67(DE67) OP | - | 2147746765 | G60 only |
| Dig Element 67(DE67) PKP | - | 2147484621 | G60 only |
| Dig Element 68(DE68) DPO | - | 2148008910 | G60 only |
| Dig Element 68(DE68) OP | - | 2147746766 | G60 only |
| Dig Element 68(DE68) PKP | - | 2147484622 | G60 only |
| Dig Element 69(DE69) DPO | - | 2148008911 | G60 only |
| Dig Element 69(DE69) OP | - | 2147746767 | G60 only |
| Dig Element 69(DE69) PKP | - | 2147484623 | G60 only |
| Dig Element 7(DE7) DPO | 2148008634 | 2148008849 | Code changed |
| Dig Element 7(DE7) OP | 2147746490 | 2147746705 | Code changed |
| Dig Element 7(DE7) PKP | 2147484346 | 2147484561 | Code changed |
| Dig Element 70(DE70) DPO | - | 2148008912 | G60 only |
| Dig Element 70(DE70) OP | - | 2147746768 | G60 only |
| Dig Element 70(DE70) PKP | - | 2147484624 | G60 only |
| Dig Element 71(DE71) DPO | - | 2148008913 | G60 only |
| Dig Element 71(DE71) OP | - | 2147746769 | G60 only |
| Dig Element 71(DE71) PKP | - | 2147484625 | G60 only |
| Dig Element 72(DE72) DPO | - | 2148008914 | G60 only |
| Dig Element 72(DE72) OP | - | 2147746770 | G60 only |
| Dig Element 72(DE72) PKP | - | 2147484626 | G60 only |
| Dig Element 73(DE73) DPO | - | 2148008915 | G60 only |
| Dig Element 73(DE73) OP | - | 2147746771 | G60 only |
| Dig Element 73(DE73) PKP | - | 2147484627 | G60 only |
| Dig Element 74(DE74) DPO | - | 2148008916 | G60 only |
| Dig Element 74(DE74) OP | - | 2147746772 | G60 only |
| Dig Element 74(DE74) PKP | - | 2147484628 | G60 only |
| Dig Element 75(DE75) DPO | - | 2148008917 | G60 only |
| Dig Element 75(DE75) OP | - | 2147746773 | G60 only |
| Dig Element 75(DE75) PKP | - | 2147484629 | G60 only |
| Dig Element 76(DE76) DPO | - | 2148008918 | G60 only |
| Dig Element 76(DE76) OP | - | 2147746774 | G60 only |
| Dig Element 76(DE76) PKP | - | 2147484630 | G60 only |
| Dig Element 77(DE77) DPO | - | 2148008919 | G60 only |
| Dig Element 77(DE77) OP | - | 2147746775 | G60 only |
| Dig Element 77(DE77) PKP | - | 2147484631 | G60 only |
| Dig Element 78(DE78) DPO | - | 2148008920 | G60 only |
| Dig Element 78(DE78) OP | - | 2147746776 | G60 only |
| Dig Element 78(DE78) PKP | - | 2147484632 | G60 only |
| Dig Element 79(DE79) DPO | - | 2148008921 | G60 only |
| Dig Element 79(DE79) OP | - | 2147746777 | G60 only |
| Dig Element 79(DE79) PKP | - | 2147484633 | G60 only |
| Dig Element 8(DE8) DPO | 2148008635 | 2148008850 | Code changed |
| Dig Element 8(DE8) OP | 2147746491 | 2147746706 | Code changed |
| Dig Element 8(DE8) PKP | 2147484347 | 2147484562 | Code changed |
| Dig Element 80(DE80) DPO | - | 2148008922 | G60 only |
| Dig Element 80(DE80) OP | - | 2147746778 | G60 only |
| Dig Element 80(DE80) PKP | - | 2147484634 | G60 only |
| Dig Element 81(DE81) DPO | - | 2148008923 | G60 only |
| Dig Element 81(DE81) OP | - | 2147746779 | G60 only |
| Dig Element 81(DE81) PKP | - | 2147484635 | G60 only |
| Dig Element 82(DE82) DPO | - | 2148008924 | G60 only |
| Dig Element 82(DE82) OP | - | 2147746780 | G60 only |
| Dig Element 82(DE82) PKP | - | 2147484636 | G60 only |
| Dig Element 83(DE83) DPO | - | 2148008925 | G60 only |
| Dig Element 83(DE83) OP | - | 2147746781 | G60 only |
| Dig Element 83(DE83) PKP | - | 2147484637 | G60 only |
| Dig Element 84(DE84) DPO | - | 2148008926 | G60 only |
| Dig Element 84(DE84) OP | - | 2147746782 | G60 only |
| Dig Element 84(DE84) PKP | - | 2147484638 | G60 only |
| Dig Element 85(DE85) DPO | - | 2148008927 | G60 only |
| Dig Element 85(DE85) OP | - | 2147746783 | G60 only |
| Dig Element 85(DE85) PKP | - | 2147484639 | G60 only |
| Dig Element 86(DE86) DPO | - | 2148008928 | G60 only |
| Dig Element 86(DE86) OP | - | 2147746784 | G60 only |
| Dig Element 86(DE86) PKP | - | 2147484640 | G60 only |
| Dig Element 87(DE87) DPO | - | 2148008929 | G60 only |
| Dig Element 87(DE87) OP | - | 2147746785 | G60 only |
| Dig Element 87(DE87) PKP | - | 2147484641 | G60 only |
| Dig Element 88(DE88) DPO | - | 2148008930 | G60 only |
| Dig Element 88(DE88) OP | - | 2147746786 | G60 only |
| Dig Element 88(DE88) PKP | - | 2147484642 | G60 only |
| Dig Element 89(DE89) DPO | - | 2148008931 | G60 only |
| Dig Element 89(DE89) OP | - | 2147746787 | G60 only |
| Dig Element 89(DE89) PKP | - | 2147484643 | G60 only |
| Dig Element 9(DE9) DPO | 2148008636 | 2148008851 | Code changed |
| Dig Element 9(DE9) OP | 2147746492 | 2147746707 | Code changed |
| Dig Element 9(DE9) PKP | 2147484348 | 2147484563 | Code changed |
| Dig Element 90(DE90) DPO | - | 2148008932 | G60 only |
| Dig Element 90(DE90) OP | - | 2147746788 | G60 only |
| Dig Element 90(DE90) PKP | - | 2147484644 | G60 only |
| Dig Element 91(DE91) DPO | - | 2148008933 | G60 only |
| Dig Element 91(DE91) OP | - | 2147746789 | G60 only |
| Dig Element 91(DE91) PKP | - | 2147484645 | G60 only |
| Dig Element 92(DE92) DPO | - | 2148008934 | G60 only |
| Dig Element 92(DE92) OP | - | 2147746790 | G60 only |
| Dig Element 92(DE92) PKP | - | 2147484646 | G60 only |
| Dig Element 93(DE93) DPO | - | 2148008935 | G60 only |
| Dig Element 93(DE93) OP | - | 2147746791 | G60 only |
| Dig Element 93(DE93) PKP | - | 2147484647 | G60 only |
| Dig Element 94(DE94) DPO | - | 2148008936 | G60 only |
| Dig Element 94(DE94) OP | - | 2147746792 | G60 only |
| Dig Element 94(DE94) PKP | - | 2147484648 | G60 only |
| Dig Element 95(DE95) DPO | - | 2148008937 | G60 only |
| Dig Element 95(DE95) OP | - | 2147746793 | G60 only |
| Dig Element 95(DE95) PKP | - | 2147484649 | G60 only |
| Dig Element 96(DE96) DPO | - | 2148008938 | G60 only |
| Dig Element 96(DE96) OP | - | 2147746794 | G60 only |
| Dig Element 96(DE96) PKP | - | 2147484650 | G60 only |
| DIR POWER 1 DPO | 2149581014 | 2149581172 | Code changed |
| DIR POWER 1 OP | 2149318870 | 2149319028 | Code changed |
| DIR POWER 1 PKP | 2149056726 | 2149056884 | Code changed |
| DIR POWER 1 STG1 DPO | 2148532438 | 2148532596 | Code changed |
| DIR POWER 1 STG1 OP | 2148008150 | 2148008308 | Code changed |
| DIR POWER 1 STG1 PKP | 2147483862 | 2147484020 | Code changed |
| DIR POWER 1 STG2 DPO | 2148794582 | 2148794740 | Code changed |
| DIR POWER 1 STG2 OP | 2148270294 | 2148270452 | Code changed |
| DIR POWER 1 STG2 PKP | 2147746006 | 2147746164 | Code changed |
| DIR POWER 2 DPO | 2149581015 | 2149581173 | Code changed |
| DIR POWER 2 OP | 2149318871 | 2149319029 | Code changed |
| DIR POWER 2 PKP | 2149056727 | 2149056885 | Code changed |
| DIR POWER 2 STG1 DPO | 2148532439 | 2148532597 | Code changed |
| DIR POWER 2 STG1 OP | 2148008151 | 2148008309 | Code changed |
| DIR POWER 2 STG1 PKP | 2147483863 | 2147484021 | Code changed |
| DIR POWER 2 STG2 DPO | 2148794583 | 2148794741 | Code changed |
| DIR POWER 2 STG2 OP | 2148270295 | 2148270453 | Code changed |
| DIR POWER 2 STG2 PKP | 2147746007 | 2147746165 | Code changed |
| EQUIPMENT MISMATCH | 3538955 | 3538955 | Identical |
| FACTORY MODE ACT | - | 3539002 | G60 only |
| FIELD CURRENT OC DPO | - | 2148009210 | G60 only |
| FIELD CURRENT OC OP | - | 2147747066 | G60 only |
| FIELD CURRENT OC PKP | - | 2147484922 | G60 only |
| FIELD CURRENT UC DPO | - | 2148795642 | G60 only |
| FIELD CURRENT UC OP | - | 2148533498 | G60 only |
| FIELD CURRENT UC PKP | - | 2148271354 | G60 only |
| FIELD GND INJ UC DPO | - | 2149319929 | G60 only |
| FIELD GND INJ UC OP | - | 2149582073 | G60 only |
| FIELD GND INJ UC PKP | - | 2149057785 | G60 only |
| FIELD GND STG1 DPO | - | 2148009209 | G60 only |
| FIELD GND STG1 OP | - | 2148533497 | G60 only |
| FIELD GND STG1 PKP | - | 2147484921 | G60 only |
| FIELD GND STG2 DPO | - | 2148271353 | G60 only |
| FIELD GND STG2 OP | - | 2148795641 | G60 only |
| FIELD GND STG2 PKP | - | 2147747065 | G60 only |
| FIRST ETHERNET FAIL | 3538964 | 3538964 | Identical |
| FLEXLOGIC ERR TOKEN | 3538954 | 3538954 | Identical |
| FREQ OOB ACCUM OP | 2149319573 | 2149319836 | Code changed |
| FREQ OOB ACCUM PKP | 2149057429 | 2149057692 | Code changed |
| FREQ OOB BAND 1 DPO | 2147484564 | 2147484827 | Code changed |
| FREQ OOB BAND 1 OP | 2148008852 | 2148009115 | Code changed |
| FREQ OOB BAND 1 PKP | 2147746708 | 2147746971 | Code changed |
| FREQ OOB BAND 2 DPO | 2148270996 | 2148271259 | Code changed |
| FREQ OOB BAND 2 OP | 2148795284 | 2148795547 | Code changed |
| FREQ OOB BAND 2 PKP | 2148533140 | 2148533403 | Code changed |
| FREQ OOB BAND 3 DPO | 2149057428 | 2149057691 | Code changed |
| FREQ OOB BAND 3 OP | 2149581716 | 2149581979 | Code changed |
| FREQ OOB BAND 3 PKP | 2149319572 | 2149319835 | Code changed |
| FREQ OOB BAND 4 DPO | 2149843860 | 2149844123 | Code changed |
| FREQ OOB BAND 4 OP | 2150368148 | 2150368411 | Code changed |
| FREQ OOB BAND 4 PKP | 2150106004 | 2150106267 | Code changed |
| FREQ OOB BAND 5 DPO | 2150630292 | 2150630555 | Code changed |
| FREQ OOB BAND 5 OP | 2151154580 | 2151154843 | Code changed |
| FREQ OOB BAND 5 PKP | 2150892436 | 2150892699 | Code changed |
| FREQ OOB BAND 6 DPO | 2147484565 | 2147484828 | Code changed |
| FREQ OOB BAND 6 OP | 2148008853 | 2148009116 | Code changed |
| FREQ OOB BAND 6 PKP | 2147746709 | 2147746972 | Code changed |
| FREQ OOB BAND 7 DPO | 2148270997 | 2148271260 | Code changed |
| FREQ OOB BAND 7 OP | 2148795285 | 2148795548 | Code changed |
| FREQ OOB BAND 7 PKP | 2148533141 | 2148533404 | Code changed |
| FREQ RATE 1 DPO | 2148008466 | 2148008669 | Code changed |
| FREQ RATE 1 OP | 2147746322 | 2147746525 | Code changed |
| FREQ RATE 1 PKP | 2147484178 | 2147484381 | Code changed |
| FREQ RATE 2 DPO | 2148008467 | 2148008670 | Code changed |
| FREQ RATE 2 OP | 2147746323 | 2147746526 | Code changed |
| FREQ RATE 2 PKP | 2147484179 | 2147484382 | Code changed |
| FREQ RATE 3 DPO | 2148008468 | 2148008671 | Code changed |
| FREQ RATE 3 OP | 2147746324 | 2147746527 | Code changed |
| FREQ RATE 3 PKP | 2147484180 | 2147484383 | Code changed |
| FREQ RATE 4 DPO | 2148008469 | 2148008672 | Code changed |
| FREQ RATE 4 OP | 2147746325 | 2147746528 | Code changed |
| FREQ RATE 4 PKP | 2147484181 | 2147484384 | Code changed |
| FxE 1 (FE 1) DPO | - | 2148008539 | G60 only |
| FxE 1 (FE 1) OP | - | 2147746395 | G60 only |
| FxE 1 (FE 1) PKP | - | 2147484251 | G60 only |
| FxE 10 (FE 10) DPO | 2148008345 | 2148008548 | Code changed |
| FxE 10 (FE 10) OP | 2147746201 | 2147746404 | Code changed |
| FxE 10 (FE 10) PKP | 2147484057 | 2147484260 | Code changed |
| FxE 11 (FE 11) DPO | 2148008346 | 2148008549 | Code changed |
| FxE 11 (FE 11) OP | 2147746202 | 2147746405 | Code changed |
| FxE 11 (FE 11) PKP | 2147484058 | 2147484261 | Code changed |
| FxE 12 (FE 12) DPO | 2148008347 | 2148008550 | Code changed |
| FxE 12 (FE 12) OP | 2147746203 | 2147746406 | Code changed |
| FxE 12 (FE 12) PKP | 2147484059 | 2147484262 | Code changed |
| FxE 13 (FE 13) DPO | 2148008348 | 2148008551 | Code changed |
| FxE 13 (FE 13) OP | 2147746204 | 2147746407 | Code changed |
| FxE 13 (FE 13) PKP | 2147484060 | 2147484263 | Code changed |
| FxE 14 (FE 14) DPO | 2148008349 | 2148008552 | Code changed |
| FxE 14 (FE 14) OP | 2147746205 | 2147746408 | Code changed |
| FxE 14 (FE 14) PKP | 2147484061 | 2147484264 | Code changed |
| FxE 15 (FE 15) DPO | 2148008350 | 2148008553 | Code changed |
| FxE 15 (FE 15) OP | 2147746206 | 2147746409 | Code changed |
| FxE 15 (FE 15) PKP | 2147484062 | 2147484265 | Code changed |
| FxE 16 (FE 16) DPO | 2148008351 | 2148008554 | Code changed |
| FxE 16 (FE 16) OP | 2147746207 | 2147746410 | Code changed |
| FxE 16 (FE 16) PKP | 2147484063 | 2147484266 | Code changed |
| FxE 2 (FE 2) DPO | 2148008337 | 2148008540 | Code changed |
| FxE 2 (FE 2) OP | 2147746193 | 2147746396 | Code changed |
| FxE 2 (FE 2) PKP | 2147484049 | 2147484252 | Code changed |
| FxE 3 (FE 3) DPO | 2148008338 | 2148008541 | Code changed |
| FxE 3 (FE 3) OP | 2147746194 | 2147746397 | Code changed |
| FxE 3 (FE 3) PKP | 2147484050 | 2147484253 | Code changed |
| FxE 4 (FE 4) DPO | 2148008339 | 2148008542 | Code changed |
| FxE 4 (FE 4) OP | 2147746195 | 2147746398 | Code changed |
| FxE 4 (FE 4) PKP | 2147484051 | 2147484254 | Code changed |
| FxE 5 (FE 5) DPO | 2148008340 | 2148008543 | Code changed |
| FxE 5 (FE 5) OP | 2147746196 | 2147746399 | Code changed |
| FxE 5 (FE 5) PKP | 2147484052 | 2147484255 | Code changed |
| FxE 6 (FE 6) DPO | 2148008341 | 2148008544 | Code changed |
| FxE 6 (FE 6) OP | 2147746197 | 2147746400 | Code changed |
| FxE 6 (FE 6) PKP | 2147484053 | 2147484256 | Code changed |
| FxE 7 (FE 7) DPO | 2148008342 | 2148008545 | Code changed |
| FxE 7 (FE 7) OP | 2147746198 | 2147746401 | Code changed |
| FxE 7 (FE 7) PKP | 2147484054 | 2147484257 | Code changed |
| FxE 8 (FE 8) DPO | 2148008343 | 2148008546 | Code changed |
| FxE 8 (FE 8) OP | 2147746199 | 2147746402 | Code changed |
| FxE 8 (FE 8) PKP | 2147484055 | 2147484258 | Code changed |
| FxE 9 (FE 9) DPO | 2148008344 | 2148008547 | Code changed |
| FxE 9 (FE 9) OP | 2147746200 | 2147746403 | Code changed |
| FxE 9 (FE 9) PKP | 2147484056 | 2147484259 | Code changed |
| Gen Aux Off(H8a) | 196611 | - | G30 only |
| Gen Aux On(H8a) | 131075 | - | G30 only |
| Gen Only On (VO3) | 393219 | - | G30 only |
| Gen Sync Closed (H6) | 524294 | - | G30 only |
| Gen Sync IOn (H6) | 786438 | - | G30 only |
| Gen Sync On (VO8) | 393224 | - | G30 only |
| Gen Sync VOff (H6) | 720902 | - | G30 only |
| Gen Sync VOn (H6) | 655366 | - | G30 only |
| Gen Trip Closed (H2) | 524290 | - | G30 only |
| Gen Trip IOn (H2) | 786434 | - | G30 only |
| Gen Trip On (VO5) | 393221 | - | G30 only |
| Gen Trip VOff (H2) | 720898 | - | G30 only |
| Gen Trip VOn (H2) | 655362 | - | G30 only |
| GEN UNBAL DPO | 2149318781 | 2149318927 | Code changed |
| GEN UNBAL OP | 2149580925 | 2149581071 | Code changed |
| GEN UNBAL PKP | 2149056637 | 2149056783 | Code changed |
| GEN UNBAL STG1 DPO | 2147745917 | 2147746063 | Code changed |
| GEN UNBAL STG1 OP | 2148008061 | 2148008207 | Code changed |
| GEN UNBAL STG1 PKP | 2147483773 | 2147483919 | Code changed |
| GEN UNBAL STG2 DPO | 2148532349 | 2148532495 | Code changed |
| GEN UNBAL STG2 OP | 2148794493 | 2148794639 | Code changed |
| GEN UNBAL STG2 PKP | 2148270205 | 2148270351 | Code changed |
| GPM-F FAILURE | - | 1572897 | G60 only |
| GROUND IOC1 DPO | 2148008000 | 2148008112 | Code changed |
| GROUND IOC1 OP | 2147745856 | 2147745968 | Code changed |
| GROUND IOC1 PKP | 2147483712 | 2147483824 | Code changed |
| GROUND TOC1 DPO | 2148008016 | 2148008140 | Code changed |
| GROUND TOC1 OP | 2147745872 | 2147745996 | Code changed |
| GROUND TOC1 PKP | 2147483728 | 2147483852 | Code changed |
| GX Off(H7c) | 196610 | - | G30 only |
| GX On(H7c) | 131074 | - | G30 only |
| HARMONIC DET 1 OP | - | 2148795784 | G60 only |
| HARMONIC DET 1 OP A | - | 2149057928 | G60 only |
| HARMONIC DET 1 OP B | - | 2149320072 | G60 only |
| HARMONIC DET 1 OP C | - | 2149582216 | G60 only |
| HARMONIC DET 1 OP G | - | 2149844360 | G60 only |
| HARMONIC DET 1 PKP | - | 2147485064 | G60 only |
| HARMONIC DET 1 PKP A | - | 2147747208 | G60 only |
| HARMONIC DET 1 PKP B | - | 2148009352 | G60 only |
| HARMONIC DET 1 PKP C | - | 2148271496 | G60 only |
| HARMONIC DET 1 PKP G | - | 2148533640 | G60 only |
| HARMONIC DET 2 OP | - | 2148795785 | G60 only |
| HARMONIC DET 2 OP A | - | 2149057929 | G60 only |
| HARMONIC DET 2 OP B | - | 2149320073 | G60 only |
| HARMONIC DET 2 OP C | - | 2149582217 | G60 only |
| HARMONIC DET 2 OP G | - | 2149844361 | G60 only |
| HARMONIC DET 2 PKP | - | 2147485065 | G60 only |
| HARMONIC DET 2 PKP A | - | 2147747209 | G60 only |
| HARMONIC DET 2 PKP B | - | 2148009353 | G60 only |
| HARMONIC DET 2 PKP C | - | 2148271497 | G60 only |
| HARMONIC DET 2 PKP G | - | 2148533641 | G60 only |
| HARMONIC DET 3 OP | - | 2148795786 | G60 only |
| HARMONIC DET 3 OP A | - | 2149057930 | G60 only |
| HARMONIC DET 3 OP B | - | 2149320074 | G60 only |
| HARMONIC DET 3 OP C | - | 2149582218 | G60 only |
| HARMONIC DET 3 OP G | - | 2149844362 | G60 only |
| HARMONIC DET 3 PKP | - | 2147485066 | G60 only |
| HARMONIC DET 3 PKP A | - | 2147747210 | G60 only |
| HARMONIC DET 3 PKP B | - | 2148009354 | G60 only |
| HARMONIC DET 3 PKP C | - | 2148271498 | G60 only |
| HARMONIC DET 3 PKP G | - | 2148533642 | G60 only |
| HARMONIC DET 4 OP | - | 2148795787 | G60 only |
| HARMONIC DET 4 OP A | - | 2149057931 | G60 only |
| HARMONIC DET 4 OP B | - | 2149320075 | G60 only |
| HARMONIC DET 4 OP C | - | 2149582219 | G60 only |
| HARMONIC DET 4 OP G | - | 2149844363 | G60 only |
| HARMONIC DET 4 PKP | - | 2147485067 | G60 only |
| HARMONIC DET 4 PKP A | - | 2147747211 | G60 only |
| HARMONIC DET 4 PKP B | - | 2148009355 | G60 only |
| HARMONIC DET 4 PKP C | - | 2148271499 | G60 only |
| HARMONIC DET 4 PKP G | - | 2148533643 | G60 only |
| IED Beh On | - | 1572921 | G60 only |
| IED Beh Test | - | 1572922 | G60 only |
| IED Beh Test-Blocked | - | 1572923 | G60 only |
| IED in Local | - | 1572924 | G60 only |
| IED in Remote | - | 1572925 | G60 only |
| IED IN SIM MODE OFF | - | 1572916 | G60 only |
| IED IN SIM MODE ON | - | 1572915 | G60 only |
| IOC2_Block On (VO10) | 393226 | - | G30 only |
| IRIG-b FAILURE | 3538945 | 3538945 | Identical |
| LATCH  1 OFF | 2147746212 | 2147746973 | Code changed |
| LATCH  1 ON | 2147484068 | 2147484829 | Code changed |
| LATCH  2 OFF | 2147746213 | 2147746974 | Code changed |
| LATCH  2 ON | 2147484069 | 2147484830 | Code changed |
| LATCH  3 OFF | 2147746214 | 2147746975 | Code changed |
| LATCH  3 ON | 2147484070 | 2147484831 | Code changed |
| LATCH  4 OFF | 2147746215 | 2147746976 | Code changed |
| LATCH  4 ON | 2147484071 | 2147484832 | Code changed |
| LATCH  5 OFF | 2147746216 | 2147746977 | Code changed |
| LATCH  5 ON | 2147484072 | 2147484833 | Code changed |
| LATCH  6 OFF | 2147746217 | 2147746978 | Code changed |
| LATCH  6 ON | 2147484073 | 2147484834 | Code changed |
| LATCH  7 OFF | 2147746218 | 2147746979 | Code changed |
| LATCH  7 ON | 2147484074 | 2147484835 | Code changed |
| LATCH  8 OFF | 2147746219 | 2147746980 | Code changed |
| LATCH  8 ON | 2147484075 | 2147484836 | Code changed |
| LATCH  9 OFF | 2147746220 | 2147746981 | Code changed |
| LATCH  9 ON | 2147484076 | 2147484837 | Code changed |
| LATCH 10 OFF | 2147746221 | 2147746982 | Code changed |
| LATCH 10 ON | 2147484077 | 2147484838 | Code changed |
| LATCH 11 OFF | 2147746222 | 2147746983 | Code changed |
| LATCH 11 ON | 2147484078 | 2147484839 | Code changed |
| LATCH 12 OFF | 2147746223 | 2147746984 | Code changed |
| LATCH 12 ON | 2147484079 | 2147484840 | Code changed |
| LATCH 13 OFF | 2147746224 | 2147746985 | Code changed |
| LATCH 13 ON | 2147484080 | 2147484841 | Code changed |
| LATCH 14 OFF | 2147746225 | 2147746986 | Code changed |
| LATCH 14 ON | 2147484081 | 2147484842 | Code changed |
| LATCH 15 OFF | 2147746226 | 2147746987 | Code changed |
| LATCH 15 ON | 2147484082 | 2147484843 | Code changed |
| LATCH 16 OFF | 2147746227 | 2147746988 | Code changed |
| LATCH 16 ON | 2147484083 | 2147484844 | Code changed |
| Leap Second Added | - | 1572928 | G60 only |
| Leap Second Detected | - | 1572927 | G60 only |
| LED ALARM | 5242885 | 5242885 | Identical |
| LED CURRENT | 5242888 | 5242888 | Identical |
| LED FREQUENCY | 5242889 | 5242889 | Identical |
| LED IN SERVICE | 5242881 | 5242881 | Identical |
| LED NEUTRAL/GROUND | 5242894 | 5242894 | Identical |
| LED OTHER | 5242890 | 5242890 | Identical |
| LED PHASE A | 5242891 | 5242891 | Identical |
| LED PHASE B | 5242892 | 5242892 | Identical |
| LED PHASE C | 5242893 | 5242893 | Identical |
| LED PICKUP | 5242886 | 5242886 | Identical |
| LED TEST IN PROGRESS | 1572865 | 1572865 | Identical |
| LED TEST MODE | 5242883 | 5242883 | Identical |
| LED TRIP | 5242884 | 5242884 | Identical |
| LED TROUBLE | 5242882 | 5242882 | Identical |
| LED USER 1 | 5242895 | 5242895 | Identical |
| LED USER 10 | 5242904 | 5242904 | Identical |
| LED USER 11 | 5242905 | 5242905 | Identical |
| LED USER 12 | 5242906 | 5242906 | Identical |
| LED USER 13 | 5242907 | 5242907 | Identical |
| LED USER 14 | 5242908 | 5242908 | Identical |
| LED USER 15 | 5242909 | 5242909 | Identical |
| LED USER 16 | 5242910 | 5242910 | Identical |
| LED USER 17 | 5242911 | 5242911 | Identical |
| LED USER 18 | 5242912 | 5242912 | Identical |
| LED USER 19 | 5242913 | 5242913 | Identical |
| LED USER 2 | 5242896 | 5242896 | Identical |
| LED USER 20 | 5242914 | 5242914 | Identical |
| LED USER 21 | 5242915 | 5242915 | Identical |
| LED USER 22 | 5242916 | 5242916 | Identical |
| LED USER 23 | 5242917 | 5242917 | Identical |
| LED USER 24 | 5242918 | 5242918 | Identical |
| LED USER 25 | 5242919 | 5242919 | Identical |
| LED USER 26 | 5242920 | 5242920 | Identical |
| LED USER 27 | 5242921 | 5242921 | Identical |
| LED USER 28 | 5242922 | 5242922 | Identical |
| LED USER 29 | 5242923 | 5242923 | Identical |
| LED USER 3 | 5242897 | 5242897 | Identical |
| LED USER 30 | 5242924 | 5242924 | Identical |
| LED USER 31 | 5242925 | 5242925 | Identical |
| LED USER 32 | 5242926 | 5242926 | Identical |
| LED USER 33 | 5242927 | 5242927 | Identical |
| LED USER 34 | 5242928 | 5242928 | Identical |
| LED USER 35 | 5242929 | 5242929 | Identical |
| LED USER 36 | 5242930 | 5242930 | Identical |
| LED USER 37 | 5242931 | 5242931 | Identical |
| LED USER 38 | 5242932 | 5242932 | Identical |
| LED USER 39 | 5242933 | 5242933 | Identical |
| LED USER 4 | 5242898 | 5242898 | Identical |
| LED USER 40 | 5242934 | 5242934 | Identical |
| LED USER 41 | 5242935 | 5242935 | Identical |
| LED USER 42 | 5242936 | 5242936 | Identical |
| LED USER 43 | 5242937 | 5242937 | Identical |
| LED USER 44 | 5242938 | 5242938 | Identical |
| LED USER 45 | 5242939 | 5242939 | Identical |
| LED USER 46 | 5242940 | 5242940 | Identical |
| LED USER 47 | 5242941 | 5242941 | Identical |
| LED USER 48 | 5242942 | 5242942 | Identical |
| LED USER 5 | 5242899 | 5242899 | Identical |
| LED USER 6 | 5242900 | 5242900 | Identical |
| LED USER 7 | 5242901 | 5242901 | Identical |
| LED USER 8 | 5242902 | 5242902 | Identical |
| LED USER 9 | 5242903 | 5242903 | Identical |
| LED VOLTAGE | 5242887 | 5242887 | Identical |
| LOC SET ACCS AUT OFF | 1572891 | 1572891 | Identical |
| LOC SET ACCS AUT ON | 1572892 | 1572892 | Identical |
| LOCAL ACCESS DENIED | 1572872 | 1572872 | Identical |
| LOSS EXCIT DPO | 2149581100 | 2149581303 | Code changed |
| LOSS EXCIT OP | 2148794668 | 2148794871 | Code changed |
| LOSS EXCIT PKP | 2148532524 | 2148532727 | Code changed |
| LOSS EXCIT STG1 DPO | 2149056812 | 2149057015 | Code changed |
| LOSS EXCIT STG1 OP | 2148008236 | 2148008439 | Code changed |
| LOSS EXCIT STG1 PKP | 2147483948 | 2147484151 | Code changed |
| LOSS EXCIT STG2 DPO | 2149318956 | 2149319159 | Code changed |
| LOSS EXCIT STG2 OP | 2148270380 | 2148270583 | Code changed |
| LOSS EXCIT STG2 PKP | 2147746092 | 2147746295 | Code changed |
| Main Aux Off(H8c) | 196612 | - | G30 only |
| Main Aux On(H8c) | 131076 | - | G30 only |
| Main Only On (VO2) | 393218 | - | G30 only |
| Main Sync Closed (H5) | 524293 | - | G30 only |
| Main Sync IOn (H5) | 786437 | - | G30 only |
| Main Sync On (VO7) | 393223 | - | G30 only |
| Main Sync VOff (H5) | 720901 | - | G30 only |
| Main Sync VOn (H5) | 655365 | - | G30 only |
| Main Trip Closed (H1) | 524289 | - | G30 only |
| Main Trip IOn (H1) | 786433 | - | G30 only |
| Main Trip On (VO4) | 393220 | - | G30 only |
| Main Trip VOff (H1) | 720897 | - | G30 only |
| Main Trip VOn (H1) | 655361 | - | G30 only |
| MX Off(H7a) | 196609 | - | G30 only |
| MX On(H7a) | 131073 | - | G30 only |
| N_IOC1_Block On (VO11) | 393227 | - | G30 only |
| NEG SEQ DIR OC1 FWD | 2147483708 | 2147483820 | Code changed |
| NEG SEQ DIR OC1 REV | 2147745852 | 2147745964 | Code changed |
| NEG SEQ DIR OC2 FWD | 2147483709 | 2147483821 | Code changed |
| NEG SEQ DIR OC2 REV | 2147745853 | 2147745965 | Code changed |
| NEG SEQ OV1 DPO | 2148008056 | 2148008202 | Code changed |
| NEG SEQ OV1 OP | 2147745912 | 2147746058 | Code changed |
| NEG SEQ OV1 PKP | 2147483768 | 2147483914 | Code changed |
| NEG SEQ OV2 DPO | 2148008057 | 2148008203 | Code changed |
| NEG SEQ OV2 OP | 2147745913 | 2147746059 | Code changed |
| NEG SEQ OV2 PKP | 2147483769 | 2147483915 | Code changed |
| NEG SEQ OV3 DPO | 2148008058 | 2148008204 | Code changed |
| NEG SEQ OV3 OP | 2147745914 | 2147746060 | Code changed |
| NEG SEQ OV3 PKP | 2147483770 | 2147483916 | Code changed |
| NEUTRAL IOC1 DPO | 2148007968 | 2148008048 | Code changed |
| NEUTRAL IOC1 OP | 2147745824 | 2147745904 | Code changed |
| NEUTRAL IOC1 PKP | 2147483680 | 2147483760 | Code changed |
| NEUTRAL OV1 DPO | 2148008092 | 2148008248 | Code changed |
| NEUTRAL OV1 OP | 2147745948 | 2147746104 | Code changed |
| NEUTRAL OV1 PKP | 2147483804 | 2147483960 | Code changed |
| NEUTRAL OV2 DPO | 2148008093 | 2148008249 | Code changed |
| NEUTRAL OV2 OP | 2147745949 | 2147746105 | Code changed |
| NEUTRAL OV2 PKP | 2147483805 | 2147483961 | Code changed |
| NEUTRAL OV3 DPO | 2148008094 | 2148008250 | Code changed |
| NEUTRAL OV3 OP | 2147745950 | 2147746106 | Code changed |
| NEUTRAL OV3 PKP | 2147483806 | 2147483962 | Code changed |
| NEUTRAL TOC1 DPO | 2148007984 | 2148008076 | Code changed |
| NEUTRAL TOC1 OP | 2147745840 | 2147745932 | Code changed |
| NEUTRAL TOC1 PKP | 2147483696 | 2147483788 | Code changed |
| NEUTRAL TOC2 DPO | 2148007985 | 2148008077 | Code changed |
| NEUTRAL TOC2 OP | 2147745841 | 2147745933 | Code changed |
| NEUTRAL TOC2 PKP | 2147483697 | 2147483789 | Code changed |
| Not_Parallel On (VO9) | 393225 | - | G30 only |
| NTRL DIR OC1 FWD | 2147483704 | 2147483750 | Code changed |
| NTRL DIR OC1 REV | 2147745848 | 2147745894 | Code changed |
| NTRL DIR OC2 FWD | 2147483705 | 2147483751 | Code changed |
| NTRL DIR OC2 REV | 2147745849 | 2147745895 | Code changed |
| OFF | 0 | 0 | Identical |
| ON | 1 | 1 | Identical |
| OVERFREQ 1 DPO | 2148008280 | 2148008483 | Code changed |
| OVERFREQ 1 OP | 2147746136 | 2147746339 | Code changed |
| OVERFREQ 1 PKP | 2147483992 | 2147484195 | Code changed |
| OVERFREQ 2 DPO | 2148008281 | 2148008484 | Code changed |
| OVERFREQ 2 OP | 2147746137 | 2147746340 | Code changed |
| OVERFREQ 2 PKP | 2147483993 | 2147484196 | Code changed |
| OVERFREQ 3 DPO | 2148008282 | 2148008485 | Code changed |
| OVERFREQ 3 OP | 2147746138 | 2147746341 | Code changed |
| OVERFREQ 3 PKP | 2147483994 | 2147484197 | Code changed |
| OVERFREQ 4 DPO | 2148008283 | 2148008486 | Code changed |
| OVERFREQ 4 OP | 2147746139 | 2147746342 | Code changed |
| OVERFREQ 4 PKP | 2147483995 | 2147484198 | Code changed |
| Parallel On (VO1) | 393217 | - | G30 only |
| PH DIR1 BLK | 2148270104 | 2148270164 | Code changed |
| PH DIR1 BLK A | 2147483672 | 2147483732 | Code changed |
| PH DIR1 BLK B | 2147745816 | 2147745876 | Code changed |
| PH DIR1 BLK C | 2148007960 | 2148008020 | Code changed |
| PH DIST Z1 DPO AB | - | 2150367550 | G60 only |
| PH DIST Z1 DPO BC | - | 2150629694 | G60 only |
| PH DIST Z1 DPO CA | - | 2150891838 | G60 only |
| PH DIST Z1 OP | - | 2147746110 | G60 only |
| PH DIST Z1 OP AB | - | 2148794686 | G60 only |
| PH DIST Z1 OP BC | - | 2149056830 | G60 only |
| PH DIST Z1 OP CA | - | 2149318974 | G60 only |
| PH DIST Z1 PKP | - | 2147483966 | G60 only |
| PH DIST Z1 PKP AB | - | 2148008254 | G60 only |
| PH DIST Z1 PKP BC | - | 2148270398 | G60 only |
| PH DIST Z1 PKP CA | - | 2148532542 | G60 only |
| PH DIST Z1 SUPN IAB | - | 2149581118 | G60 only |
| PH DIST Z1 SUPN IBC | - | 2149843262 | G60 only |
| PH DIST Z1 SUPN ICA | - | 2150105406 | G60 only |
| PH DIST Z2 DPO AB | - | 2150367551 | G60 only |
| PH DIST Z2 DPO BC | - | 2150629695 | G60 only |
| PH DIST Z2 DPO CA | - | 2150891839 | G60 only |
| PH DIST Z2 OP | - | 2147746111 | G60 only |
| PH DIST Z2 OP AB | - | 2148794687 | G60 only |
| PH DIST Z2 OP BC | - | 2149056831 | G60 only |
| PH DIST Z2 OP CA | - | 2149318975 | G60 only |
| PH DIST Z2 PKP | - | 2147483967 | G60 only |
| PH DIST Z2 PKP AB | - | 2148008255 | G60 only |
| PH DIST Z2 PKP BC | - | 2148270399 | G60 only |
| PH DIST Z2 PKP CA | - | 2148532543 | G60 only |
| PH DIST Z2 SUPN IAB | - | 2149581119 | G60 only |
| PH DIST Z2 SUPN IBC | - | 2149843263 | G60 only |
| PH DIST Z2 SUPN ICA | - | 2150105407 | G60 only |
| PH DIST Z3 DPO AB | - | 2150367552 | G60 only |
| PH DIST Z3 DPO BC | - | 2150629696 | G60 only |
| PH DIST Z3 DPO CA | - | 2150891840 | G60 only |
| PH DIST Z3 OP | - | 2147746112 | G60 only |
| PH DIST Z3 OP AB | - | 2148794688 | G60 only |
| PH DIST Z3 OP BC | - | 2149056832 | G60 only |
| PH DIST Z3 OP CA | - | 2149318976 | G60 only |
| PH DIST Z3 PKP | - | 2147483968 | G60 only |
| PH DIST Z3 PKP AB | - | 2148008256 | G60 only |
| PH DIST Z3 PKP BC | - | 2148270400 | G60 only |
| PH DIST Z3 PKP CA | - | 2148532544 | G60 only |
| PH DIST Z3 SUPN IAB | - | 2149581120 | G60 only |
| PH DIST Z3 SUPN IBC | - | 2149843264 | G60 only |
| PH DIST Z3 SUPN ICA | - | 2150105408 | G60 only |
| PHASE IOC1 DPO | 2149580800 | 2149580800 | Identical |
| PHASE IOC1 DPO A | 2149842944 | 2149842944 | Identical |
| PHASE IOC1 DPO B | 2150105088 | 2150105088 | Identical |
| PHASE IOC1 DPO C | 2150367232 | 2150367232 | Identical |
| PHASE IOC1 OP | 2147745792 | 2147745792 | Identical |
| PHASE IOC1 OP A | 2148794368 | 2148794368 | Identical |
| PHASE IOC1 OP B | 2149056512 | 2149056512 | Identical |
| PHASE IOC1 OP C | 2149318656 | 2149318656 | Identical |
| PHASE IOC1 PKP | 2147483648 | 2147483648 | Identical |
| PHASE IOC1 PKP A | 2148007936 | 2148007936 | Identical |
| PHASE IOC1 PKP B | 2148270080 | 2148270080 | Identical |
| PHASE IOC1 PKP C | 2148532224 | 2148532224 | Identical |
| PHASE IOC2 DPO | 2149580801 | 2149580801 | Identical |
| PHASE IOC2 DPO A | 2149842945 | 2149842945 | Identical |
| PHASE IOC2 DPO B | 2150105089 | 2150105089 | Identical |
| PHASE IOC2 DPO C | 2150367233 | 2150367233 | Identical |
| PHASE IOC2 OP | 2147745793 | 2147745793 | Identical |
| PHASE IOC2 OP A | 2148794369 | 2148794369 | Identical |
| PHASE IOC2 OP B | 2149056513 | 2149056513 | Identical |
| PHASE IOC2 OP C | 2149318657 | 2149318657 | Identical |
| PHASE IOC2 PKP | 2147483649 | 2147483649 | Identical |
| PHASE IOC2 PKP A | 2148007937 | 2148007937 | Identical |
| PHASE IOC2 PKP B | 2148270081 | 2148270081 | Identical |
| PHASE IOC2 PKP C | 2148532225 | 2148532225 | Identical |
| PHASE IOC3 DPO | 2149580802 | 2149580802 | Identical |
| PHASE IOC3 DPO A | 2149842946 | 2149842946 | Identical |
| PHASE IOC3 DPO B | 2150105090 | 2150105090 | Identical |
| PHASE IOC3 DPO C | 2150367234 | 2150367234 | Identical |
| PHASE IOC3 OP | 2147745794 | 2147745794 | Identical |
| PHASE IOC3 OP A | 2148794370 | 2148794370 | Identical |
| PHASE IOC3 OP B | 2149056514 | 2149056514 | Identical |
| PHASE IOC3 OP C | 2149318658 | 2149318658 | Identical |
| PHASE IOC3 PKP | 2147483650 | 2147483650 | Identical |
| PHASE IOC3 PKP A | 2148007938 | 2148007938 | Identical |
| PHASE IOC3 PKP B | 2148270082 | 2148270082 | Identical |
| PHASE IOC3 PKP C | 2148532226 | 2148532226 | Identical |
| PHASE IOC4 DPO | 2149580803 | 2149580803 | Identical |
| PHASE IOC4 DPO A | 2149842947 | 2149842947 | Identical |
| PHASE IOC4 DPO B | 2150105091 | 2150105091 | Identical |
| PHASE IOC4 DPO C | 2150367235 | 2150367235 | Identical |
| PHASE IOC4 OP | 2147745795 | 2147745795 | Identical |
| PHASE IOC4 OP A | 2148794371 | 2148794371 | Identical |
| PHASE IOC4 OP B | 2149056515 | 2149056515 | Identical |
| PHASE IOC4 OP C | 2149318659 | 2149318659 | Identical |
| PHASE IOC4 PKP | 2147483651 | 2147483651 | Identical |
| PHASE IOC4 PKP A | 2148007939 | 2148007939 | Identical |
| PHASE IOC4 PKP B | 2148270083 | 2148270083 | Identical |
| PHASE IOC4 PKP C | 2148532227 | 2148532227 | Identical |
| PHASE OV1 DPO | 2149580951 | 2149581105 | Code changed |
| PHASE OV1 DPO A | 2149843095 | 2149843249 | Code changed |
| PHASE OV1 DPO B | 2150105239 | 2150105393 | Code changed |
| PHASE OV1 DPO C | 2150367383 | 2150367537 | Code changed |
| PHASE OV1 OP | 2147745943 | 2147746097 | Code changed |
| PHASE OV1 OP A | 2148794519 | 2148794673 | Code changed |
| PHASE OV1 OP B | 2149056663 | 2149056817 | Code changed |
| PHASE OV1 OP C | 2149318807 | 2149318961 | Code changed |
| PHASE OV1 PKP | 2147483799 | 2147483953 | Code changed |
| PHASE OV1 PKP A | 2148008087 | 2148008241 | Code changed |
| PHASE OV1 PKP B | 2148270231 | 2148270385 | Code changed |
| PHASE OV1 PKP C | 2148532375 | 2148532529 | Code changed |
| PHASE OV2 DPO | 2149580952 | 2149581106 | Code changed |
| PHASE OV2 DPO A | 2149843096 | 2149843250 | Code changed |
| PHASE OV2 DPO B | 2150105240 | 2150105394 | Code changed |
| PHASE OV2 DPO C | 2150367384 | 2150367538 | Code changed |
| PHASE OV2 OP | 2147745944 | 2147746098 | Code changed |
| PHASE OV2 OP A | 2148794520 | 2148794674 | Code changed |
| PHASE OV2 OP B | 2149056664 | 2149056818 | Code changed |
| PHASE OV2 OP C | 2149318808 | 2149318962 | Code changed |
| PHASE OV2 PKP | 2147483800 | 2147483954 | Code changed |
| PHASE OV2 PKP A | 2148008088 | 2148008242 | Code changed |
| PHASE OV2 PKP B | 2148270232 | 2148270386 | Code changed |
| PHASE OV2 PKP C | 2148532376 | 2148532530 | Code changed |
| PHASE OV3 DPO | 2149580953 | 2149581107 | Code changed |
| PHASE OV3 DPO A | 2149843097 | 2149843251 | Code changed |
| PHASE OV3 DPO B | 2150105241 | 2150105395 | Code changed |
| PHASE OV3 DPO C | 2150367385 | 2150367539 | Code changed |
| PHASE OV3 OP | 2147745945 | 2147746099 | Code changed |
| PHASE OV3 OP A | 2148794521 | 2148794675 | Code changed |
| PHASE OV3 OP B | 2149056665 | 2149056819 | Code changed |
| PHASE OV3 OP C | 2149318809 | 2149318963 | Code changed |
| PHASE OV3 PKP | 2147483801 | 2147483955 | Code changed |
| PHASE OV3 PKP A | 2148008089 | 2148008243 | Code changed |
| PHASE OV3 PKP B | 2148270233 | 2148270387 | Code changed |
| PHASE OV3 PKP C | 2148532377 | 2148532531 | Code changed |
| PHASE TOC1 DPO | 2149580816 | 2149580856 | Code changed |
| PHASE TOC1 DPO A | 2149842960 | 2149843000 | Code changed |
| PHASE TOC1 DPO B | 2150105104 | 2150105144 | Code changed |
| PHASE TOC1 DPO C | 2150367248 | 2150367288 | Code changed |
| PHASE TOC1 OP | 2147745808 | 2147745848 | Code changed |
| PHASE TOC1 OP A | 2148794384 | 2148794424 | Code changed |
| PHASE TOC1 OP B | 2149056528 | 2149056568 | Code changed |
| PHASE TOC1 OP C | 2149318672 | 2149318712 | Code changed |
| PHASE TOC1 PKP | 2147483664 | 2147483704 | Code changed |
| PHASE TOC1 PKP A | 2148007952 | 2148007992 | Code changed |
| PHASE TOC1 PKP B | 2148270096 | 2148270136 | Code changed |
| PHASE TOC1 PKP C | 2148532240 | 2148532280 | Code changed |
| PHASE TOC2 DPO | 2149580817 | 2149580857 | Code changed |
| PHASE TOC2 DPO A | 2149842961 | 2149843001 | Code changed |
| PHASE TOC2 DPO B | 2150105105 | 2150105145 | Code changed |
| PHASE TOC2 DPO C | 2150367249 | 2150367289 | Code changed |
| PHASE TOC2 OP | 2147745809 | 2147745849 | Code changed |
| PHASE TOC2 OP A | 2148794385 | 2148794425 | Code changed |
| PHASE TOC2 OP B | 2149056529 | 2149056569 | Code changed |
| PHASE TOC2 OP C | 2149318673 | 2149318713 | Code changed |
| PHASE TOC2 PKP | 2147483665 | 2147483705 | Code changed |
| PHASE TOC2 PKP A | 2148007953 | 2148007993 | Code changed |
| PHASE TOC2 PKP B | 2148270097 | 2148270137 | Code changed |
| PHASE TOC2 PKP C | 2148532241 | 2148532281 | Code changed |
| PHASE TOC3 DPO | 2149580818 | 2149580858 | Code changed |
| PHASE TOC3 DPO A | 2149842962 | 2149843002 | Code changed |
| PHASE TOC3 DPO B | 2150105106 | 2150105146 | Code changed |
| PHASE TOC3 DPO C | 2150367250 | 2150367290 | Code changed |
| PHASE TOC3 OP | 2147745810 | 2147745850 | Code changed |
| PHASE TOC3 OP A | 2148794386 | 2148794426 | Code changed |
| PHASE TOC3 OP B | 2149056530 | 2149056570 | Code changed |
| PHASE TOC3 OP C | 2149318674 | 2149318714 | Code changed |
| PHASE TOC3 PKP | 2147483666 | 2147483706 | Code changed |
| PHASE TOC3 PKP A | 2148007954 | 2148007994 | Code changed |
| PHASE TOC3 PKP B | 2148270098 | 2148270138 | Code changed |
| PHASE TOC3 PKP C | 2148532242 | 2148532282 | Code changed |
| PHASE TOC4 DPO | 2149580819 | 2149580859 | Code changed |
| PHASE TOC4 DPO A | 2149842963 | 2149843003 | Code changed |
| PHASE TOC4 DPO B | 2150105107 | 2150105147 | Code changed |
| PHASE TOC4 DPO C | 2150367251 | 2150367291 | Code changed |
| PHASE TOC4 OP | 2147745811 | 2147745851 | Code changed |
| PHASE TOC4 OP A | 2148794387 | 2148794427 | Code changed |
| PHASE TOC4 OP B | 2149056531 | 2149056571 | Code changed |
| PHASE TOC4 OP C | 2149318675 | 2149318715 | Code changed |
| PHASE TOC4 PKP | 2147483667 | 2147483707 | Code changed |
| PHASE TOC4 PKP A | 2148007955 | 2148007995 | Code changed |
| PHASE TOC4 PKP B | 2148270099 | 2148270139 | Code changed |
| PHASE TOC4 PKP C | 2148532243 | 2148532283 | Code changed |
| PHASE UV1 DPO | 2149580944 | 2149581093 | Code changed |
| PHASE UV1 DPO A | 2149843088 | 2149843237 | Code changed |
| PHASE UV1 DPO B | 2150105232 | 2150105381 | Code changed |
| PHASE UV1 DPO C | 2150367376 | 2150367525 | Code changed |
| PHASE UV1 OP | 2147745936 | 2147746085 | Code changed |
| PHASE UV1 OP A | 2148794512 | 2148794661 | Code changed |
| PHASE UV1 OP B | 2149056656 | 2149056805 | Code changed |
| PHASE UV1 OP C | 2149318800 | 2149318949 | Code changed |
| PHASE UV1 PKP | 2147483792 | 2147483941 | Code changed |
| PHASE UV1 PKP A | 2148008080 | 2148008229 | Code changed |
| PHASE UV1 PKP B | 2148270224 | 2148270373 | Code changed |
| PHASE UV1 PKP C | 2148532368 | 2148532517 | Code changed |
| PHASE UV2 DPO | 2149580945 | 2149581094 | Code changed |
| PHASE UV2 DPO A | 2149843089 | 2149843238 | Code changed |
| PHASE UV2 DPO B | 2150105233 | 2150105382 | Code changed |
| PHASE UV2 DPO C | 2150367377 | 2150367526 | Code changed |
| PHASE UV2 OP | 2147745937 | 2147746086 | Code changed |
| PHASE UV2 OP A | 2148794513 | 2148794662 | Code changed |
| PHASE UV2 OP B | 2149056657 | 2149056806 | Code changed |
| PHASE UV2 OP C | 2149318801 | 2149318950 | Code changed |
| PHASE UV2 PKP | 2147483793 | 2147483942 | Code changed |
| PHASE UV2 PKP A | 2148008081 | 2148008230 | Code changed |
| PHASE UV2 PKP B | 2148270225 | 2148270374 | Code changed |
| PHASE UV2 PKP C | 2148532369 | 2148532518 | Code changed |
| PHASE UV3 DPO | 2149580946 | 2149581095 | Code changed |
| PHASE UV3 DPO A | 2149843090 | 2149843239 | Code changed |
| PHASE UV3 DPO B | 2150105234 | 2150105383 | Code changed |
| PHASE UV3 DPO C | 2150367378 | 2150367527 | Code changed |
| PHASE UV3 OP | 2147745938 | 2147746087 | Code changed |
| PHASE UV3 OP A | 2148794514 | 2148794663 | Code changed |
| PHASE UV3 OP B | 2149056658 | 2149056807 | Code changed |
| PHASE UV3 OP C | 2149318802 | 2149318951 | Code changed |
| PHASE UV3 PKP | 2147483794 | 2147483943 | Code changed |
| PHASE UV3 PKP A | 2148008082 | 2148008231 | Code changed |
| PHASE UV3 PKP B | 2148270226 | 2148270375 | Code changed |
| PHASE UV3 PKP C | 2148532370 | 2148532519 | Code changed |
| PLC Trip Closed (H3) | 524291 | - | G30 only |
| PLC Trip IOn (H3) | 786435 | - | G30 only |
| PLC Trip On (VO6) | 393222 | - | G30 only |
| PLC Trip VOff (H3) | 720899 | - | G30 only |
| PLC Trip VOn (H3) | 655363 | - | G30 only |
| POWER SWING 50DD | - | 2149581148 | G60 only |
| POWER SWING BLOCK | - | 2148270428 | G60 only |
| POWER SWING INCOMING | - | 2150105436 | G60 only |
| POWER SWING INNER | - | 2148008284 | G60 only |
| POWER SWING MIDDLE | - | 2147746140 | G60 only |
| POWER SWING OUTER | - | 2147483996 | G60 only |
| POWER SWING OUTGOING | - | 2150367580 | G60 only |
| POWER SWING TMR2 PKP | - | 2148794716 | G60 only |
| POWER SWING TMR3 PKP | - | 2149056860 | G60 only |
| POWER SWING TMR4 PKP | - | 2149319004 | G60 only |
| POWER SWING TRIP | - | 2148532572 | G60 only |
| POWER SWING UN/BLOCK | - | 2149843292 | G60 only |
| PROTSUPR | 1572906 | 1572906 | Identical |
| REM SET ACCS AUT OFF | 1572893 | 1572893 | Identical |
| REM SET ACCS AUT ON | 1572894 | 1572894 | Identical |
| REMOTE ACCESS DENIED | 1572881 | 1572881 | Identical |
| RESET OP | 2147483985 | 2147484188 | Code changed |
| RESET OP (COMMS) | 2148008273 | 2148008476 | Code changed |
| RESET OP (OPERAND) | 2148270417 | 2148270620 | Code changed |
| RESET OP (PUSHBUTTON) | 2147746129 | 2147746332 | Code changed |
| RESTD GND FT1 DPO | 2148008022 | 2148008168 | Code changed |
| RESTD GND FT1 OP | 2147745878 | 2147746024 | Code changed |
| RESTD GND FT1 PKP | 2147483734 | 2147483880 | Code changed |
| RESTD GND FT2 DPO | 2148008023 | 2148008169 | Code changed |
| RESTD GND FT2 OP | 2147745879 | 2147746025 | Code changed |
| RESTD GND FT2 PKP | 2147483735 | 2147483881 | Code changed |
| RRTD 1  ALARM DPO | - | 2149057766 | G60 only |
| RRTD 1  ALARM OP | - | 2148271334 | G60 only |
| RRTD 1  ALARM PKP | - | 2148009190 | G60 only |
| RRTD 1  OPEN | - | 2147747046 | G60 only |
| RRTD 1  SHORTED | - | 2147484902 | G60 only |
| RRTD 1  TRIP DPO | - | 2149319910 | G60 only |
| RRTD 1  TRIP OP | - | 2148795622 | G60 only |
| RRTD 1  TRIP PKP | - | 2148533478 | G60 only |
| RRTD 10  ALARM DPO | - | 2149057775 | G60 only |
| RRTD 10  ALARM OP | - | 2148271343 | G60 only |
| RRTD 10  ALARM PKP | - | 2148009199 | G60 only |
| RRTD 10  OPEN | - | 2147747055 | G60 only |
| RRTD 10  SHORTED | - | 2147484911 | G60 only |
| RRTD 10  TRIP DPO | - | 2149319919 | G60 only |
| RRTD 10  TRIP OP | - | 2148795631 | G60 only |
| RRTD 10  TRIP PKP | - | 2148533487 | G60 only |
| RRTD 11  ALARM DPO | - | 2149057776 | G60 only |
| RRTD 11  ALARM OP | - | 2148271344 | G60 only |
| RRTD 11  ALARM PKP | - | 2148009200 | G60 only |
| RRTD 11  OPEN | - | 2147747056 | G60 only |
| RRTD 11  SHORTED | - | 2147484912 | G60 only |
| RRTD 11  TRIP DPO | - | 2149319920 | G60 only |
| RRTD 11  TRIP OP | - | 2148795632 | G60 only |
| RRTD 11  TRIP PKP | - | 2148533488 | G60 only |
| RRTD 12  ALARM DPO | - | 2149057777 | G60 only |
| RRTD 12  ALARM OP | - | 2148271345 | G60 only |
| RRTD 12  ALARM PKP | - | 2148009201 | G60 only |
| RRTD 12  OPEN | - | 2147747057 | G60 only |
| RRTD 12  SHORTED | - | 2147484913 | G60 only |
| RRTD 12  TRIP DPO | - | 2149319921 | G60 only |
| RRTD 12  TRIP OP | - | 2148795633 | G60 only |
| RRTD 12  TRIP PKP | - | 2148533489 | G60 only |
| RRTD 2  ALARM DPO | - | 2149057767 | G60 only |
| RRTD 2  ALARM OP | - | 2148271335 | G60 only |
| RRTD 2  ALARM PKP | - | 2148009191 | G60 only |
| RRTD 2  OPEN | - | 2147747047 | G60 only |
| RRTD 2  SHORTED | - | 2147484903 | G60 only |
| RRTD 2  TRIP DPO | - | 2149319911 | G60 only |
| RRTD 2  TRIP OP | - | 2148795623 | G60 only |
| RRTD 2  TRIP PKP | - | 2148533479 | G60 only |
| RRTD 3  ALARM DPO | - | 2149057768 | G60 only |
| RRTD 3  ALARM OP | - | 2148271336 | G60 only |
| RRTD 3  ALARM PKP | - | 2148009192 | G60 only |
| RRTD 3  OPEN | - | 2147747048 | G60 only |
| RRTD 3  SHORTED | - | 2147484904 | G60 only |
| RRTD 3  TRIP DPO | - | 2149319912 | G60 only |
| RRTD 3  TRIP OP | - | 2148795624 | G60 only |
| RRTD 3  TRIP PKP | - | 2148533480 | G60 only |
| RRTD 4  ALARM DPO | - | 2149057769 | G60 only |
| RRTD 4  ALARM OP | - | 2148271337 | G60 only |
| RRTD 4  ALARM PKP | - | 2148009193 | G60 only |
| RRTD 4  OPEN | - | 2147747049 | G60 only |
| RRTD 4  SHORTED | - | 2147484905 | G60 only |
| RRTD 4  TRIP DPO | - | 2149319913 | G60 only |
| RRTD 4  TRIP OP | - | 2148795625 | G60 only |
| RRTD 4  TRIP PKP | - | 2148533481 | G60 only |
| RRTD 5  ALARM DPO | - | 2149057770 | G60 only |
| RRTD 5  ALARM OP | - | 2148271338 | G60 only |
| RRTD 5  ALARM PKP | - | 2148009194 | G60 only |
| RRTD 5  OPEN | - | 2147747050 | G60 only |
| RRTD 5  SHORTED | - | 2147484906 | G60 only |
| RRTD 5  TRIP DPO | - | 2149319914 | G60 only |
| RRTD 5  TRIP OP | - | 2148795626 | G60 only |
| RRTD 5  TRIP PKP | - | 2148533482 | G60 only |
| RRTD 6  ALARM DPO | - | 2149057771 | G60 only |
| RRTD 6  ALARM OP | - | 2148271339 | G60 only |
| RRTD 6  ALARM PKP | - | 2148009195 | G60 only |
| RRTD 6  OPEN | - | 2147747051 | G60 only |
| RRTD 6  SHORTED | - | 2147484907 | G60 only |
| RRTD 6  TRIP DPO | - | 2149319915 | G60 only |
| RRTD 6  TRIP OP | - | 2148795627 | G60 only |
| RRTD 6  TRIP PKP | - | 2148533483 | G60 only |
| RRTD 7  ALARM DPO | - | 2149057772 | G60 only |
| RRTD 7  ALARM OP | - | 2148271340 | G60 only |
| RRTD 7  ALARM PKP | - | 2148009196 | G60 only |
| RRTD 7  OPEN | - | 2147747052 | G60 only |
| RRTD 7  SHORTED | - | 2147484908 | G60 only |
| RRTD 7  TRIP DPO | - | 2149319916 | G60 only |
| RRTD 7  TRIP OP | - | 2148795628 | G60 only |
| RRTD 7  TRIP PKP | - | 2148533484 | G60 only |
| RRTD 8  ALARM DPO | - | 2149057773 | G60 only |
| RRTD 8  ALARM OP | - | 2148271341 | G60 only |
| RRTD 8  ALARM PKP | - | 2148009197 | G60 only |
| RRTD 8  OPEN | - | 2147747053 | G60 only |
| RRTD 8  SHORTED | - | 2147484909 | G60 only |
| RRTD 8  TRIP DPO | - | 2149319917 | G60 only |
| RRTD 8  TRIP OP | - | 2148795629 | G60 only |
| RRTD 8  TRIP PKP | - | 2148533485 | G60 only |
| RRTD 9  ALARM DPO | - | 2149057774 | G60 only |
| RRTD 9  ALARM OP | - | 2148271342 | G60 only |
| RRTD 9  ALARM PKP | - | 2148009198 | G60 only |
| RRTD 9  OPEN | - | 2147747054 | G60 only |
| RRTD 9  SHORTED | - | 2147484910 | G60 only |
| RRTD 9  TRIP DPO | - | 2149319918 | G60 only |
| RRTD 9  TRIP OP | - | 2148795630 | G60 only |
| RRTD 9  TRIP PKP | - | 2148533486 | G60 only |
| RRTD COMM FAILURE | - | 3538952 | G60 only |
| RxGOOSE INVLD ON | - | 1572917 | G60 only |
| RxGOOSE QUES ON | - | 1572918 | G60 only |
| SECOND ETHERNET FAIL | 3538965 | 3538965 | Identical |
| SELECTOR 1 ALARM | 2150629764 | 2150629967 | Code changed |
| SELECTOR 1 BIT 0 | 2149319044 | 2149319247 | Code changed |
| SELECTOR 1 BIT 1 | 2149581188 | 2149581391 | Code changed |
| SELECTOR 1 BIT 2 | 2149843332 | 2149843535 | Code changed |
| SELECTOR 1 BIT ALARM | 2150367620 | 2150367823 | Code changed |
| SELECTOR 1 POS 1 | 2147484036 | 2147484239 | Code changed |
| SELECTOR 1 POS 2 | 2147746180 | 2147746383 | Code changed |
| SELECTOR 1 POS 3 | 2148008324 | 2148008527 | Code changed |
| SELECTOR 1 POS 4 | 2148270468 | 2148270671 | Code changed |
| SELECTOR 1 POS 5 | 2148532612 | 2148532815 | Code changed |
| SELECTOR 1 POS 6 | 2148794756 | 2148794959 | Code changed |
| SELECTOR 1 POS 7 | 2149056900 | 2149057103 | Code changed |
| SELECTOR 1 PWR ALARM | 2150891908 | 2150892111 | Code changed |
| SELECTOR 1 STP ALARM | 2150105476 | 2150105679 | Code changed |
| SELECTOR 2 ALARM | 2150629765 | 2150629968 | Code changed |
| SELECTOR 2 BIT 0 | 2149319045 | 2149319248 | Code changed |
| SELECTOR 2 BIT 1 | 2149581189 | 2149581392 | Code changed |
| SELECTOR 2 BIT 2 | 2149843333 | 2149843536 | Code changed |
| SELECTOR 2 BIT ALARM | 2150367621 | 2150367824 | Code changed |
| SELECTOR 2 POS 1 | 2147484037 | 2147484240 | Code changed |
| SELECTOR 2 POS 2 | 2147746181 | 2147746384 | Code changed |
| SELECTOR 2 POS 3 | 2148008325 | 2148008528 | Code changed |
| SELECTOR 2 POS 4 | 2148270469 | 2148270672 | Code changed |
| SELECTOR 2 POS 5 | 2148532613 | 2148532816 | Code changed |
| SELECTOR 2 POS 6 | 2148794757 | 2148794960 | Code changed |
| SELECTOR 2 POS 7 | 2149056901 | 2149057104 | Code changed |
| SELECTOR 2 PWR ALARM | 2150891909 | 2150892112 | Code changed |
| SELECTOR 2 STP ALARM | 2150105477 | 2150105680 | Code changed |
| SETTING CHANGED | 1572907 | 1572907 | Identical |
| SETTING GROUP ACT 1 | 2147483984 | 2147484187 | Code changed |
| SETTING GROUP ACT 2 | 2147746128 | 2147746331 | Code changed |
| SETTING GROUP ACT 3 | 2148008272 | 2148008475 | Code changed |
| SETTING GROUP ACT 4 | 2148270416 | 2148270619 | Code changed |
| SETTING GROUP ACT 5 | 2148532560 | 2148532763 | Code changed |
| SETTING GROUP ACT 6 | 2148794704 | 2148794907 | Code changed |
| SH STAT GND OC DPO | - | 2149582072 | G60 only |
| SH STAT GND OC OP | - | 2149319928 | G60 only |
| SH STAT GND OC PKP | - | 2149057784 | G60 only |
| SH STAT GND STG1 DPO | - | 2148533496 | G60 only |
| SH STAT GND STG1 OP | - | 2148009208 | G60 only |
| SH STAT GND STG1 PKP | - | 2147484920 | G60 only |
| SH STAT GND STG2 DPO | - | 2148795640 | G60 only |
| SH STAT GND STG2 OP | - | 2148271352 | G60 only |
| SH STAT GND STG2 PKP | - | 2147747064 | G60 only |
| SH STAT GND TRB OP | - | 2149844216 | G60 only |
| SNTP FAILURE | 3538962 | 3538962 | Identical |
| Spare Closed (H4) | 524292 | - | G30 only |
| Spare IOn (H4) | 786436 | - | G30 only |
| Spare VOff (H4) | 720900 | - | G30 only |
| Spare VOn (H4) | 655364 | - | G30 only |
| SPLIT PHASE DPO | 2149581022 | 2149581180 | Code changed |
| SPLIT PHASE DPO A | 2149843166 | 2149843324 | Code changed |
| SPLIT PHASE DPO B | 2150105310 | 2150105468 | Code changed |
| SPLIT PHASE DPO C | 2150367454 | 2150367612 | Code changed |
| SPLIT PHASE OP | 2147746014 | 2147746172 | Code changed |
| SPLIT PHASE OP A | 2148794590 | 2148794748 | Code changed |
| SPLIT PHASE OP B | 2149056734 | 2149056892 | Code changed |
| SPLIT PHASE OP C | 2149318878 | 2149319036 | Code changed |
| SPLIT PHASE PKP | 2147483870 | 2147484028 | Code changed |
| SPLIT PHASE PKP A | 2148008158 | 2148008316 | Code changed |
| SPLIT PHASE PKP B | 2148270302 | 2148270460 | Code changed |
| SPLIT PHASE PKP C | 2148532446 | 2148532604 | Code changed |
| Src 1 CT Alt Bank On | - | 11927553 | G60 only |
| Src 1 CT Sw Prot Blk | - | 11272193 | G60 only |
| Src 1 VT Alt Bank On | - | 12058625 | G60 only |
| Src 1 VT Sw Prot Blk | - | 11403265 | G60 only |
| Src 2 CT Alt Bank On | - | 11927554 | G60 only |
| Src 2 CT Sw Prot Blk | - | 11272194 | G60 only |
| Src 2 VT Alt Bank On | - | 12058626 | G60 only |
| Src 2 VT Sw Prot Blk | - | 11403266 | G60 only |
| Src 3 CT Alt Bank On | - | 11927555 | G60 only |
| Src 3 CT Sw Prot Blk | - | 11272195 | G60 only |
| Src 3 VT Alt Bank On | - | 12058627 | G60 only |
| Src 3 VT Sw Prot Blk | - | 11403267 | G60 only |
| Src 4 CT Alt Bank On | - | 11927556 | G60 only |
| Src 4 CT Sw Prot Blk | - | 11272196 | G60 only |
| Src 4 VT Alt Bank On | - | 12058628 | G60 only |
| Src 4 VT Sw Prot Blk | - | 11403268 | G60 only |
| SRC1 50DD OP | 2147483880 | 2147484038 | Code changed |
| SRC1 VT FUSE FAIL ALARM | 2148532448 | 2148532606 | Code changed |
| SRC1 VT FUSE FAIL DPO | 2147746016 | 2147746174 | Code changed |
| SRC1 VT FUSE FAIL NTRL WIRE OPEN | 2148270304 | 2148270462 | Code changed |
| SRC1 VT FUSE FAIL OP | 2147483872 | 2147484030 | Code changed |
| SRC1 VT FUSE FAIL VOL LOSS | 2148008160 | 2148008318 | Code changed |
| SRC2 50DD OP | 2147483881 | 2147484039 | Code changed |
| SRC2 VT FUSE FAIL ALARM | 2148532449 | 2148532607 | Code changed |
| SRC2 VT FUSE FAIL DPO | 2147746017 | 2147746175 | Code changed |
| SRC2 VT FUSE FAIL NTRL WIRE OPEN | 2148270305 | 2148270463 | Code changed |
| SRC2 VT FUSE FAIL OP | 2147483873 | 2147484031 | Code changed |
| SRC2 VT FUSE FAIL VOL LOSS | 2148008161 | 2148008319 | Code changed |
| SRC3 50DD OP | 2147483882 | 2147484040 | Code changed |
| SRC3 VT FUSE FAIL ALARM | 2148532450 | 2148532608 | Code changed |
| SRC3 VT FUSE FAIL DPO | 2147746018 | 2147746176 | Code changed |
| SRC3 VT FUSE FAIL NTRL WIRE OPEN | 2148270306 | 2148270464 | Code changed |
| SRC3 VT FUSE FAIL OP | 2147483874 | 2147484032 | Code changed |
| SRC3 VT FUSE FAIL VOL LOSS | 2148008162 | 2148008320 | Code changed |
| SRC4 50DD OP | 2147483883 | 2147484041 | Code changed |
| SRC4 VT FUSE FAIL ALARM | 2148532451 | 2148532609 | Code changed |
| SRC4 VT FUSE FAIL DPO | 2147746019 | 2147746177 | Code changed |
| SRC4 VT FUSE FAIL NTRL WIRE OPEN | 2148270307 | 2148270465 | Code changed |
| SRC4 VT FUSE FAIL OP | 2147483875 | 2147484033 | Code changed |
| SRC4 VT FUSE FAIL VOL LOSS | 2148008163 | 2148008321 | Code changed |
| STATOR DIFF DIR A | - | 2149319104 | G60 only |
| STATOR DIFF DIR B | - | 2149581248 | G60 only |
| STATOR DIFF DIR C | - | 2149843392 | G60 only |
| STATOR DIFF DPO A | - | 2150891968 | G60 only |
| STATOR DIFF DPO B | - | 2151154112 | G60 only |
| STATOR DIFF DPO C | - | 2151416256 | G60 only |
| STATOR DIFF OP | - | 2147484096 | G60 only |
| STATOR DIFF OP A | - | 2147746240 | G60 only |
| STATOR DIFF OP B | - | 2148008384 | G60 only |
| STATOR DIFF OP C | - | 2148270528 | G60 only |
| STATOR DIFF PKP A | - | 2148532672 | G60 only |
| STATOR DIFF PKP B | - | 2148794816 | G60 only |
| STATOR DIFF PKP C | - | 2149056960 | G60 only |
| STATOR DIFF SAT A | - | 2150105536 | G60 only |
| STATOR DIFF SAT B | - | 2150367680 | G60 only |
| STATOR DIFF SAT C | - | 2150629824 | G60 only |
| SWITCH 1 BAD STATUS | 2147484592 | 2147485126 | Code changed |
| SWITCH 1 BYPASS OFF | 2150368152 | - | G30 only |
| SWITCH 1 BYPASS ON | 2150106008 | - | G30 only |
| SWITCH 1 CLOSED | 2148008856 | 2148009390 | Code changed |
| SWITCH 1 DISCREP | 2148533144 | 2148533678 | Code changed |
| SWITCH 1 OFF CMD | 2147484568 | 2147485102 | Code changed |
| SWITCH 1 ON CMD | 2147746712 | 2147747246 | Code changed |
| SWITCH 1 OPEN | 2148271000 | 2148271534 | Code changed |
| SWITCH 1 Phase A BAD STATUS | 2147746736 | 2147747270 | Code changed |
| SWITCH 1 Phase A CLOSED | 2148008880 | 2148009414 | Code changed |
| SWITCH 1 Phase A INTERM | 2148533168 | 2148533702 | Code changed |
| SWITCH 1 Phase A OPEN | 2148271024 | 2148271558 | Code changed |
| SWITCH 1 Phase B BAD STATUS | 2148795312 | 2148795846 | Code changed |
| SWITCH 1 Phase B CLOSED | 2149057456 | 2149057990 | Code changed |
| SWITCH 1 Phase B INTERM | 2149581744 | 2149582278 | Code changed |
| SWITCH 1 Phase B OPEN | 2149319600 | 2149320134 | Code changed |
| SWITCH 1 Phase C BAD STATUS | 2149843888 | 2149844422 | Code changed |
| SWITCH 1 Phase C CLOSED | 2150106032 | 2150106566 | Code changed |
| SWITCH 1 Phase C INTERM | 2150630320 | 2150630854 | Code changed |
| SWITCH 1 Phase C OPEN | 2150368176 | 2150368710 | Code changed |
| SWITCH 1 SUBD CLSD | 2149581720 | 2149582254 | Code changed |
| SWITCH 1 SUBD OPEN | 2149843864 | 2149844398 | Code changed |
| SWITCH 1 TAG OFF | 2149319576 | 2149320110 | Code changed |
| SWITCH 1 TAG ON | 2149057432 | 2149057966 | Code changed |
| SWITCH 1 TROUBLE | 2148795288 | 2148795822 | Code changed |
| SWITCH 2 BAD STATUS | 2147484593 | 2147485127 | Code changed |
| SWITCH 2 BYPASS OFF | 2150368153 | - | G30 only |
| SWITCH 2 BYPASS ON | 2150106009 | - | G30 only |
| SWITCH 2 CLOSED | 2148008857 | 2148009391 | Code changed |
| SWITCH 2 DISCREP | 2148533145 | 2148533679 | Code changed |
| SWITCH 2 OFF CMD | 2147484569 | 2147485103 | Code changed |
| SWITCH 2 ON CMD | 2147746713 | 2147747247 | Code changed |
| SWITCH 2 OPEN | 2148271001 | 2148271535 | Code changed |
| SWITCH 2 Phase A BAD STATUS | 2147746737 | 2147747271 | Code changed |
| SWITCH 2 Phase A CLOSED | 2148008881 | 2148009415 | Code changed |
| SWITCH 2 Phase A INTERM | 2148533169 | 2148533703 | Code changed |
| SWITCH 2 Phase A OPEN | 2148271025 | 2148271559 | Code changed |
| SWITCH 2 Phase B BAD STATUS | 2148795313 | 2148795847 | Code changed |
| SWITCH 2 Phase B CLOSED | 2149057457 | 2149057991 | Code changed |
| SWITCH 2 Phase B INTERM | 2149581745 | 2149582279 | Code changed |
| SWITCH 2 Phase B OPEN | 2149319601 | 2149320135 | Code changed |
| SWITCH 2 Phase C BAD STATUS | 2149843889 | 2149844423 | Code changed |
| SWITCH 2 Phase C CLOSED | 2150106033 | 2150106567 | Code changed |
| SWITCH 2 Phase C INTERM | 2150630321 | 2150630855 | Code changed |
| SWITCH 2 Phase C OPEN | 2150368177 | 2150368711 | Code changed |
| SWITCH 2 SUBD CLSD | 2149581721 | 2149582255 | Code changed |
| SWITCH 2 SUBD OPEN | 2149843865 | 2149844399 | Code changed |
| SWITCH 2 TAG OFF | 2149319577 | 2149320111 | Code changed |
| SWITCH 2 TAG ON | 2149057433 | 2149057967 | Code changed |
| SWITCH 2 TROUBLE | 2148795289 | 2148795823 | Code changed |
| SWITCH 3 BAD STATUS | 2147484594 | 2147485128 | Code changed |
| SWITCH 3 BYPASS OFF | 2150368154 | - | G30 only |
| SWITCH 3 BYPASS ON | 2150106010 | - | G30 only |
| SWITCH 3 CLOSED | 2148008858 | 2148009392 | Code changed |
| SWITCH 3 DISCREP | 2148533146 | 2148533680 | Code changed |
| SWITCH 3 OFF CMD | 2147484570 | 2147485104 | Code changed |
| SWITCH 3 ON CMD | 2147746714 | 2147747248 | Code changed |
| SWITCH 3 OPEN | 2148271002 | 2148271536 | Code changed |
| SWITCH 3 Phase A BAD STATUS | 2147746738 | 2147747272 | Code changed |
| SWITCH 3 Phase A CLOSED | 2148008882 | 2148009416 | Code changed |
| SWITCH 3 Phase A INTERM | 2148533170 | 2148533704 | Code changed |
| SWITCH 3 Phase A OPEN | 2148271026 | 2148271560 | Code changed |
| SWITCH 3 Phase B BAD STATUS | 2148795314 | 2148795848 | Code changed |
| SWITCH 3 Phase B CLOSED | 2149057458 | 2149057992 | Code changed |
| SWITCH 3 Phase B INTERM | 2149581746 | 2149582280 | Code changed |
| SWITCH 3 Phase B OPEN | 2149319602 | 2149320136 | Code changed |
| SWITCH 3 Phase C BAD STATUS | 2149843890 | 2149844424 | Code changed |
| SWITCH 3 Phase C CLOSED | 2150106034 | 2150106568 | Code changed |
| SWITCH 3 Phase C INTERM | 2150630322 | 2150630856 | Code changed |
| SWITCH 3 Phase C OPEN | 2150368178 | 2150368712 | Code changed |
| SWITCH 3 SUBD CLSD | 2149581722 | 2149582256 | Code changed |
| SWITCH 3 SUBD OPEN | 2149843866 | 2149844400 | Code changed |
| SWITCH 3 TAG OFF | 2149319578 | 2149320112 | Code changed |
| SWITCH 3 TAG ON | 2149057434 | 2149057968 | Code changed |
| SWITCH 3 TROUBLE | 2148795290 | 2148795824 | Code changed |
| SWITCH 4 BAD STATUS | 2147484595 | 2147485129 | Code changed |
| SWITCH 4 BYPASS OFF | 2150368155 | - | G30 only |
| SWITCH 4 BYPASS ON | 2150106011 | - | G30 only |
| SWITCH 4 CLOSED | 2148008859 | 2148009393 | Code changed |
| SWITCH 4 DISCREP | 2148533147 | 2148533681 | Code changed |
| SWITCH 4 OFF CMD | 2147484571 | 2147485105 | Code changed |
| SWITCH 4 ON CMD | 2147746715 | 2147747249 | Code changed |
| SWITCH 4 OPEN | 2148271003 | 2148271537 | Code changed |
| SWITCH 4 Phase A BAD STATUS | 2147746739 | 2147747273 | Code changed |
| SWITCH 4 Phase A CLOSED | 2148008883 | 2148009417 | Code changed |
| SWITCH 4 Phase A INTERM | 2148533171 | 2148533705 | Code changed |
| SWITCH 4 Phase A OPEN | 2148271027 | 2148271561 | Code changed |
| SWITCH 4 Phase B BAD STATUS | 2148795315 | 2148795849 | Code changed |
| SWITCH 4 Phase B CLOSED | 2149057459 | 2149057993 | Code changed |
| SWITCH 4 Phase B INTERM | 2149581747 | 2149582281 | Code changed |
| SWITCH 4 Phase B OPEN | 2149319603 | 2149320137 | Code changed |
| SWITCH 4 Phase C BAD STATUS | 2149843891 | 2149844425 | Code changed |
| SWITCH 4 Phase C CLOSED | 2150106035 | 2150106569 | Code changed |
| SWITCH 4 Phase C INTERM | 2150630323 | 2150630857 | Code changed |
| SWITCH 4 Phase C OPEN | 2150368179 | 2150368713 | Code changed |
| SWITCH 4 SUBD CLSD | 2149581723 | 2149582257 | Code changed |
| SWITCH 4 SUBD OPEN | 2149843867 | 2149844401 | Code changed |
| SWITCH 4 TAG OFF | 2149319579 | 2149320113 | Code changed |
| SWITCH 4 TAG ON | 2149057435 | 2149057969 | Code changed |
| SWITCH 4 TROUBLE | 2148795291 | 2148795825 | Code changed |
| SWITCH 5 BAD STATUS | 2147484596 | 2147485130 | Code changed |
| SWITCH 5 BYPASS OFF | 2150368156 | - | G30 only |
| SWITCH 5 BYPASS ON | 2150106012 | - | G30 only |
| SWITCH 5 CLOSED | 2148008860 | 2148009394 | Code changed |
| SWITCH 5 DISCREP | 2148533148 | 2148533682 | Code changed |
| SWITCH 5 OFF CMD | 2147484572 | 2147485106 | Code changed |
| SWITCH 5 ON CMD | 2147746716 | 2147747250 | Code changed |
| SWITCH 5 OPEN | 2148271004 | 2148271538 | Code changed |
| SWITCH 5 Phase A BAD STATUS | 2147746740 | 2147747274 | Code changed |
| SWITCH 5 Phase A CLOSED | 2148008884 | 2148009418 | Code changed |
| SWITCH 5 Phase A INTERM | 2148533172 | 2148533706 | Code changed |
| SWITCH 5 Phase A OPEN | 2148271028 | 2148271562 | Code changed |
| SWITCH 5 Phase B BAD STATUS | 2148795316 | 2148795850 | Code changed |
| SWITCH 5 Phase B CLOSED | 2149057460 | 2149057994 | Code changed |
| SWITCH 5 Phase B INTERM | 2149581748 | 2149582282 | Code changed |
| SWITCH 5 Phase B OPEN | 2149319604 | 2149320138 | Code changed |
| SWITCH 5 Phase C BAD STATUS | 2149843892 | 2149844426 | Code changed |
| SWITCH 5 Phase C CLOSED | 2150106036 | 2150106570 | Code changed |
| SWITCH 5 Phase C INTERM | 2150630324 | 2150630858 | Code changed |
| SWITCH 5 Phase C OPEN | 2150368180 | 2150368714 | Code changed |
| SWITCH 5 SUBD CLSD | 2149581724 | 2149582258 | Code changed |
| SWITCH 5 SUBD OPEN | 2149843868 | 2149844402 | Code changed |
| SWITCH 5 TAG OFF | 2149319580 | 2149320114 | Code changed |
| SWITCH 5 TAG ON | 2149057436 | 2149057970 | Code changed |
| SWITCH 5 TROUBLE | 2148795292 | 2148795826 | Code changed |
| SWITCH 6 BAD STATUS | 2147484597 | 2147485131 | Code changed |
| SWITCH 6 BYPASS OFF | 2150368157 | - | G30 only |
| SWITCH 6 BYPASS ON | 2150106013 | - | G30 only |
| SWITCH 6 CLOSED | 2148008861 | 2148009395 | Code changed |
| SWITCH 6 DISCREP | 2148533149 | 2148533683 | Code changed |
| SWITCH 6 OFF CMD | 2147484573 | 2147485107 | Code changed |
| SWITCH 6 ON CMD | 2147746717 | 2147747251 | Code changed |
| SWITCH 6 OPEN | 2148271005 | 2148271539 | Code changed |
| SWITCH 6 Phase A BAD STATUS | 2147746741 | 2147747275 | Code changed |
| SWITCH 6 Phase A CLOSED | 2148008885 | 2148009419 | Code changed |
| SWITCH 6 Phase A INTERM | 2148533173 | 2148533707 | Code changed |
| SWITCH 6 Phase A OPEN | 2148271029 | 2148271563 | Code changed |
| SWITCH 6 Phase B BAD STATUS | 2148795317 | 2148795851 | Code changed |
| SWITCH 6 Phase B CLOSED | 2149057461 | 2149057995 | Code changed |
| SWITCH 6 Phase B INTERM | 2149581749 | 2149582283 | Code changed |
| SWITCH 6 Phase B OPEN | 2149319605 | 2149320139 | Code changed |
| SWITCH 6 Phase C BAD STATUS | 2149843893 | 2149844427 | Code changed |
| SWITCH 6 Phase C CLOSED | 2150106037 | 2150106571 | Code changed |
| SWITCH 6 Phase C INTERM | 2150630325 | 2150630859 | Code changed |
| SWITCH 6 Phase C OPEN | 2150368181 | 2150368715 | Code changed |
| SWITCH 6 SUBD CLSD | 2149581725 | 2149582259 | Code changed |
| SWITCH 6 SUBD OPEN | 2149843869 | 2149844403 | Code changed |
| SWITCH 6 TAG OFF | 2149319581 | 2149320115 | Code changed |
| SWITCH 6 TAG ON | 2149057437 | 2149057971 | Code changed |
| SWITCH 6 TROUBLE | 2148795293 | 2148795827 | Code changed |
| SWITCH 7 BAD STATUS | 2147484598 | 2147485132 | Code changed |
| SWITCH 7 BYPASS OFF | 2150368158 | - | G30 only |
| SWITCH 7 BYPASS ON | 2150106014 | - | G30 only |
| SWITCH 7 CLOSED | 2148008862 | 2148009396 | Code changed |
| SWITCH 7 DISCREP | 2148533150 | 2148533684 | Code changed |
| SWITCH 7 OFF CMD | 2147484574 | 2147485108 | Code changed |
| SWITCH 7 ON CMD | 2147746718 | 2147747252 | Code changed |
| SWITCH 7 OPEN | 2148271006 | 2148271540 | Code changed |
| SWITCH 7 Phase A BAD STATUS | 2147746742 | 2147747276 | Code changed |
| SWITCH 7 Phase A CLOSED | 2148008886 | 2148009420 | Code changed |
| SWITCH 7 Phase A INTERM | 2148533174 | 2148533708 | Code changed |
| SWITCH 7 Phase A OPEN | 2148271030 | 2148271564 | Code changed |
| SWITCH 7 Phase B BAD STATUS | 2148795318 | 2148795852 | Code changed |
| SWITCH 7 Phase B CLOSED | 2149057462 | 2149057996 | Code changed |
| SWITCH 7 Phase B INTERM | 2149581750 | 2149582284 | Code changed |
| SWITCH 7 Phase B OPEN | 2149319606 | 2149320140 | Code changed |
| SWITCH 7 Phase C BAD STATUS | 2149843894 | 2149844428 | Code changed |
| SWITCH 7 Phase C CLOSED | 2150106038 | 2150106572 | Code changed |
| SWITCH 7 Phase C INTERM | 2150630326 | 2150630860 | Code changed |
| SWITCH 7 Phase C OPEN | 2150368182 | 2150368716 | Code changed |
| SWITCH 7 SUBD CLSD | 2149581726 | 2149582260 | Code changed |
| SWITCH 7 SUBD OPEN | 2149843870 | 2149844404 | Code changed |
| SWITCH 7 TAG OFF | 2149319582 | 2149320116 | Code changed |
| SWITCH 7 TAG ON | 2149057438 | 2149057972 | Code changed |
| SWITCH 7 TROUBLE | 2148795294 | 2148795828 | Code changed |
| SWITCH 8 BAD STATUS | 2147484599 | 2147485133 | Code changed |
| SWITCH 8 BYPASS OFF | 2150368159 | - | G30 only |
| SWITCH 8 BYPASS ON | 2150106015 | - | G30 only |
| SWITCH 8 CLOSED | 2148008863 | 2148009397 | Code changed |
| SWITCH 8 DISCREP | 2148533151 | 2148533685 | Code changed |
| SWITCH 8 OFF CMD | 2147484575 | 2147485109 | Code changed |
| SWITCH 8 ON CMD | 2147746719 | 2147747253 | Code changed |
| SWITCH 8 OPEN | 2148271007 | 2148271541 | Code changed |
| SWITCH 8 Phase A BAD STATUS | 2147746743 | 2147747277 | Code changed |
| SWITCH 8 Phase A CLOSED | 2148008887 | 2148009421 | Code changed |
| SWITCH 8 Phase A INTERM | 2148533175 | 2148533709 | Code changed |
| SWITCH 8 Phase A OPEN | 2148271031 | 2148271565 | Code changed |
| SWITCH 8 Phase B BAD STATUS | 2148795319 | 2148795853 | Code changed |
| SWITCH 8 Phase B CLOSED | 2149057463 | 2149057997 | Code changed |
| SWITCH 8 Phase B INTERM | 2149581751 | 2149582285 | Code changed |
| SWITCH 8 Phase B OPEN | 2149319607 | 2149320141 | Code changed |
| SWITCH 8 Phase C BAD STATUS | 2149843895 | 2149844429 | Code changed |
| SWITCH 8 Phase C CLOSED | 2150106039 | 2150106573 | Code changed |
| SWITCH 8 Phase C INTERM | 2150630327 | 2150630861 | Code changed |
| SWITCH 8 Phase C OPEN | 2150368183 | 2150368717 | Code changed |
| SWITCH 8 SUBD CLSD | 2149581727 | 2149582261 | Code changed |
| SWITCH 8 SUBD OPEN | 2149843871 | 2149844405 | Code changed |
| SWITCH 8 TAG OFF | 2149319583 | 2149320117 | Code changed |
| SWITCH 8 TAG ON | 2149057439 | 2149057973 | Code changed |
| SWITCH 8 TROUBLE | 2148795295 | 2148795829 | Code changed |
| SYNC 1 ANG DIFF PKP | - | 2151416323 | G60 only |
| SYNC 1 CLS DPO | 2149843256 | 2149843459 | Code changed |
| SYNC 1 CLS OP | 2148008248 | 2148008451 | Code changed |
| SYNC 1 DEAD S DPO | 2149318968 | 2149319171 | Code changed |
| SYNC 1 DEAD S OP | 2147483960 | 2147484163 | Code changed |
| SYNC 1 FREQ DIFF PKP | - | 2151154179 | G60 only |
| SYNC 1 S-CLOSE ARMD | 2150629688 | 2150629891 | Code changed |
| SYNC 1 S-CLOSE OP | 2150105400 | 2150105603 | Code changed |
| SYNC 1 S-CLOSE OP DPO | 2150367544 | 2150367747 | Code changed |
| SYNC 1 SYNC DPO | 2149581112 | 2149581315 | Code changed |
| SYNC 1 SYNC OP | 2147746104 | 2147746307 | Code changed |
| SYNC 1 V1 ABOVE MIN | 2148270392 | 2148270595 | Code changed |
| SYNC 1 V1 BELOW MAX | 2148794680 | 2148794883 | Code changed |
| SYNC 1 V2 ABOVE MIN | 2148532536 | 2148532739 | Code changed |
| SYNC 1 V2 BELOW MAX | 2149056824 | 2149057027 | Code changed |
| SYNC 1 VOLT DIFF PKP | - | 2150892035 | G60 only |
| SYNC 2 ANG DIFF PKP | - | 2151416324 | G60 only |
| SYNC 2 CLS DPO | 2149843257 | 2149843460 | Code changed |
| SYNC 2 CLS OP | 2148008249 | 2148008452 | Code changed |
| SYNC 2 DEAD S DPO | 2149318969 | 2149319172 | Code changed |
| SYNC 2 DEAD S OP | 2147483961 | 2147484164 | Code changed |
| SYNC 2 FREQ DIFF PKP | - | 2151154180 | G60 only |
| SYNC 2 S-CLOSE ARMD | 2150629689 | 2150629892 | Code changed |
| SYNC 2 S-CLOSE OP | 2150105401 | 2150105604 | Code changed |
| SYNC 2 S-CLOSE OP DPO | 2150367545 | 2150367748 | Code changed |
| SYNC 2 SYNC DPO | 2149581113 | 2149581316 | Code changed |
| SYNC 2 SYNC OP | 2147746105 | 2147746308 | Code changed |
| SYNC 2 V1 ABOVE MIN | 2148270393 | 2148270596 | Code changed |
| SYNC 2 V1 BELOW MAX | 2148794681 | 2148794884 | Code changed |
| SYNC 2 V2 ABOVE MIN | 2148532537 | 2148532740 | Code changed |
| SYNC 2 V2 BELOW MAX | 2149056825 | 2149057028 | Code changed |
| SYNC 2 VOLT DIFF PKP | - | 2150892036 | G60 only |
| SYNC 3 ANG DIFF PKP | - | 2151416325 | G60 only |
| SYNC 3 CLS DPO | 2149843258 | 2149843461 | Code changed |
| SYNC 3 CLS OP | 2148008250 | 2148008453 | Code changed |
| SYNC 3 DEAD S DPO | 2149318970 | 2149319173 | Code changed |
| SYNC 3 DEAD S OP | 2147483962 | 2147484165 | Code changed |
| SYNC 3 FREQ DIFF PKP | - | 2151154181 | G60 only |
| SYNC 3 S-CLOSE ARMD | 2150629690 | 2150629893 | Code changed |
| SYNC 3 S-CLOSE OP | 2150105402 | 2150105605 | Code changed |
| SYNC 3 S-CLOSE OP DPO | 2150367546 | 2150367749 | Code changed |
| SYNC 3 SYNC DPO | 2149581114 | 2149581317 | Code changed |
| SYNC 3 SYNC OP | 2147746106 | 2147746309 | Code changed |
| SYNC 3 V1 ABOVE MIN | 2148270394 | 2148270597 | Code changed |
| SYNC 3 V1 BELOW MAX | 2148794682 | 2148794885 | Code changed |
| SYNC 3 V2 ABOVE MIN | 2148532538 | 2148532741 | Code changed |
| SYNC 3 V2 BELOW MAX | 2149056826 | 2149057029 | Code changed |
| SYNC 3 VOLT DIFF PKP | - | 2150892037 | G60 only |
| SYNC 4 ANG DIFF PKP | - | 2151416326 | G60 only |
| SYNC 4 CLS DPO | 2149843259 | 2149843462 | Code changed |
| SYNC 4 CLS OP | 2148008251 | 2148008454 | Code changed |
| SYNC 4 DEAD S DPO | 2149318971 | 2149319174 | Code changed |
| SYNC 4 DEAD S OP | 2147483963 | 2147484166 | Code changed |
| SYNC 4 FREQ DIFF PKP | - | 2151154182 | G60 only |
| SYNC 4 S-CLOSE ARMD | 2150629691 | 2150629894 | Code changed |
| SYNC 4 S-CLOSE OP | 2150105403 | 2150105606 | Code changed |
| SYNC 4 S-CLOSE OP DPO | 2150367547 | 2150367750 | Code changed |
| SYNC 4 SYNC DPO | 2149581115 | 2149581318 | Code changed |
| SYNC 4 SYNC OP | 2147746107 | 2147746310 | Code changed |
| SYNC 4 V1 ABOVE MIN | 2148270395 | 2148270598 | Code changed |
| SYNC 4 V1 BELOW MAX | 2148794683 | 2148794886 | Code changed |
| SYNC 4 V2 ABOVE MIN | 2148532539 | 2148532742 | Code changed |
| SYNC 4 V2 BELOW MAX | 2149056827 | 2149057030 | Code changed |
| SYNC 4 VOLT DIFF PKP | - | 2150892038 | G60 only |
| SYSTEM EXCEPTION | 3538958 | 3538958 | Identical |
| TEMP MONITOR | 3538966 | 3538966 | Identical |
| Thermal Prot 1 ALARM | - | 2148008030 | G60 only |
| Thermal Prot 1 OP | 2147746804 | 2147745886 | Code changed |
| Thermal Prot 1 PKP | 2147484660 | 2147483742 | Code changed |
| Thermal Prot 2 ALARM | - | 2148008031 | G60 only |
| Thermal Prot 2 OP | 2147746805 | 2147745887 | Code changed |
| Thermal Prot 2 PKP | 2147484661 | 2147483743 | Code changed |
| THIRD ETHERNET FAIL | 3539008 | 3539008 | Identical |
| TRIPBUS 1 OP | 2147746634 | 2147746897 | Code changed |
| TRIPBUS 1 PKP | 2147484490 | 2147484753 | Code changed |
| TRIPBUS 2 OP | 2147746635 | 2147746898 | Code changed |
| TRIPBUS 2 PKP | 2147484491 | 2147484754 | Code changed |
| TRIPBUS 3 OP | 2147746636 | 2147746899 | Code changed |
| TRIPBUS 3 PKP | 2147484492 | 2147484755 | Code changed |
| TRIPBUS 4 OP | 2147746637 | 2147746900 | Code changed |
| TRIPBUS 4 PKP | 2147484493 | 2147484756 | Code changed |
| TRIPBUS 5 OP | 2147746638 | 2147746901 | Code changed |
| TRIPBUS 5 PKP | 2147484494 | 2147484757 | Code changed |
| TRIPBUS 6 OP | 2147746639 | 2147746902 | Code changed |
| TRIPBUS 6 PKP | 2147484495 | 2147484758 | Code changed |
| TxGOOSE SIM ON | - | 1572914 | G60 only |
| UNAUTH  FW ATTEMPT | - | 3539003 | G60 only |
| UNAUTHORIZED ACCESS | 1572864 | 1572864 | Identical |
| UNDERFREQ 1 DPO | 2148008288 | 2148008487 | Code changed |
| UNDERFREQ 1 OP | 2147746144 | 2147746343 | Code changed |
| UNDERFREQ 1 PKP | 2147484000 | 2147484199 | Code changed |
| UNDERFREQ 2 DPO | 2148008289 | 2148008488 | Code changed |
| UNDERFREQ 2 OP | 2147746145 | 2147746344 | Code changed |
| UNDERFREQ 2 PKP | 2147484001 | 2147484200 | Code changed |
| UNDERFREQ 3 DPO | 2148008290 | 2148008489 | Code changed |
| UNDERFREQ 3 OP | 2147746146 | 2147746345 | Code changed |
| UNDERFREQ 3 PKP | 2147484002 | 2147484201 | Code changed |
| UNDERFREQ 4 DPO | 2148008291 | 2148008490 | Code changed |
| UNDERFREQ 4 OP | 2147746147 | 2147746346 | Code changed |
| UNDERFREQ 4 PKP | 2147484003 | 2147484202 | Code changed |
| UNDERFREQ 5 DPO | 2148008292 | 2148008491 | Code changed |
| UNDERFREQ 5 OP | 2147746148 | 2147746347 | Code changed |
| UNDERFREQ 5 PKP | 2147484004 | 2147484203 | Code changed |
| UNDERFREQ 6 DPO | 2148008293 | 2148008492 | Code changed |
| UNDERFREQ 6 OP | 2147746149 | 2147746348 | Code changed |
| UNDERFREQ 6 PKP | 2147484005 | 2147484204 | Code changed |
| UNIT NOT PROGRAMMED | 3538957 | 3538957 | Identical |
| Virt Ip 1 On (VI1) | 262145 | 262145 | Identical |
| Virt Ip 10 On (VI10) | 262154 | 262154 | Identical |
| Virt Ip 100 On (VI100) | - | 262244 | G60 only |
| Virt Ip 101 On (VI101) | - | 262245 | G60 only |
| Virt Ip 102 On (VI102) | - | 262246 | G60 only |
| Virt Ip 103 On (VI103) | - | 262247 | G60 only |
| Virt Ip 104 On (VI104) | - | 262248 | G60 only |
| Virt Ip 105 On (VI105) | - | 262249 | G60 only |
| Virt Ip 106 On (VI106) | - | 262250 | G60 only |
| Virt Ip 107 On (VI107) | - | 262251 | G60 only |
| Virt Ip 108 On (VI108) | - | 262252 | G60 only |
| Virt Ip 109 On (VI109) | - | 262253 | G60 only |
| Virt Ip 11 On (VI11) | 262155 | 262155 | Identical |
| Virt Ip 110 On (VI110) | - | 262254 | G60 only |
| Virt Ip 111 On (VI111) | - | 262255 | G60 only |
| Virt Ip 112 On (VI112) | - | 262256 | G60 only |
| Virt Ip 113 On (VI113) | - | 262257 | G60 only |
| Virt Ip 114 On (VI114) | - | 262258 | G60 only |
| Virt Ip 115 On (VI115) | - | 262259 | G60 only |
| Virt Ip 116 On (VI116) | - | 262260 | G60 only |
| Virt Ip 117 On (VI117) | - | 262261 | G60 only |
| Virt Ip 118 On (VI118) | - | 262262 | G60 only |
| Virt Ip 119 On (VI119) | - | 262263 | G60 only |
| Virt Ip 12 On (VI12) | 262156 | 262156 | Identical |
| Virt Ip 120 On (VI120) | - | 262264 | G60 only |
| Virt Ip 121 On (VI121) | - | 262265 | G60 only |
| Virt Ip 122 On (VI122) | - | 262266 | G60 only |
| Virt Ip 123 On (VI123) | - | 262267 | G60 only |
| Virt Ip 124 On (VI124) | - | 262268 | G60 only |
| Virt Ip 125 On (VI125) | - | 262269 | G60 only |
| Virt Ip 126 On (VI126) | - | 262270 | G60 only |
| Virt Ip 127 On (VI127) | - | 262271 | G60 only |
| Virt Ip 128 On (VI128) | - | 262272 | G60 only |
| Virt Ip 13 On (VI13) | 262157 | 262157 | Identical |
| Virt Ip 14 On (VI14) | 262158 | 262158 | Identical |
| Virt Ip 15 On (VI15) | 262159 | 262159 | Identical |
| Virt Ip 16 On (VI16) | 262160 | 262160 | Identical |
| Virt Ip 17 On (VI17) | 262161 | 262161 | Identical |
| Virt Ip 18 On (VI18) | 262162 | 262162 | Identical |
| Virt Ip 19 On (VI19) | 262163 | 262163 | Identical |
| Virt Ip 2 On (VI2) | 262146 | 262146 | Identical |
| Virt Ip 20 On (VI20) | 262164 | 262164 | Identical |
| Virt Ip 21 On (VI21) | 262165 | 262165 | Identical |
| Virt Ip 22 On (VI22) | 262166 | 262166 | Identical |
| Virt Ip 23 On (VI23) | 262167 | 262167 | Identical |
| Virt Ip 24 On (VI24) | 262168 | 262168 | Identical |
| Virt Ip 25 On (VI25) | 262169 | 262169 | Identical |
| Virt Ip 26 On (VI26) | 262170 | 262170 | Identical |
| Virt Ip 27 On (VI27) | 262171 | 262171 | Identical |
| Virt Ip 28 On (VI28) | 262172 | 262172 | Identical |
| Virt Ip 29 On (VI29) | 262173 | 262173 | Identical |
| Virt Ip 3 On (VI3) | 262147 | 262147 | Identical |
| Virt Ip 30 On (VI30) | 262174 | 262174 | Identical |
| Virt Ip 31 On (VI31) | 262175 | 262175 | Identical |
| Virt Ip 32 On (VI32) | 262176 | 262176 | Identical |
| Virt Ip 33 On (VI33) | 262177 | 262177 | Identical |
| Virt Ip 34 On (VI34) | 262178 | 262178 | Identical |
| Virt Ip 35 On (VI35) | 262179 | 262179 | Identical |
| Virt Ip 36 On (VI36) | 262180 | 262180 | Identical |
| Virt Ip 37 On (VI37) | 262181 | 262181 | Identical |
| Virt Ip 38 On (VI38) | 262182 | 262182 | Identical |
| Virt Ip 39 On (VI39) | 262183 | 262183 | Identical |
| Virt Ip 4 On (VI4) | 262148 | 262148 | Identical |
| Virt Ip 40 On (VI40) | 262184 | 262184 | Identical |
| Virt Ip 41 On (VI41) | 262185 | 262185 | Identical |
| Virt Ip 42 On (VI42) | 262186 | 262186 | Identical |
| Virt Ip 43 On (VI43) | 262187 | 262187 | Identical |
| Virt Ip 44 On (VI44) | 262188 | 262188 | Identical |
| Virt Ip 45 On (VI45) | 262189 | 262189 | Identical |
| Virt Ip 46 On (VI46) | 262190 | 262190 | Identical |
| Virt Ip 47 On (VI47) | 262191 | 262191 | Identical |
| Virt Ip 48 On (VI48) | 262192 | 262192 | Identical |
| Virt Ip 49 On (VI49) | 262193 | 262193 | Identical |
| Virt Ip 5 On (VI5) | 262149 | 262149 | Identical |
| Virt Ip 50 On (VI50) | 262194 | 262194 | Identical |
| Virt Ip 51 On (VI51) | 262195 | 262195 | Identical |
| Virt Ip 52 On (VI52) | 262196 | 262196 | Identical |
| Virt Ip 53 On (VI53) | 262197 | 262197 | Identical |
| Virt Ip 54 On (VI54) | 262198 | 262198 | Identical |
| Virt Ip 55 On (VI55) | 262199 | 262199 | Identical |
| Virt Ip 56 On (VI56) | 262200 | 262200 | Identical |
| Virt Ip 57 On (VI57) | 262201 | 262201 | Identical |
| Virt Ip 58 On (VI58) | 262202 | 262202 | Identical |
| Virt Ip 59 On (VI59) | 262203 | 262203 | Identical |
| Virt Ip 6 On (VI6) | 262150 | 262150 | Identical |
| Virt Ip 60 On (VI60) | 262204 | 262204 | Identical |
| Virt Ip 61 On (VI61) | 262205 | 262205 | Identical |
| Virt Ip 62 On (VI62) | 262206 | 262206 | Identical |
| Virt Ip 63 On (VI63) | 262207 | 262207 | Identical |
| Virt Ip 64 On (VI64) | 262208 | 262208 | Identical |
| Virt Ip 65 On (VI65) | - | 262209 | G60 only |
| Virt Ip 66 On (VI66) | - | 262210 | G60 only |
| Virt Ip 67 On (VI67) | - | 262211 | G60 only |
| Virt Ip 68 On (VI68) | - | 262212 | G60 only |
| Virt Ip 69 On (VI69) | - | 262213 | G60 only |
| Virt Ip 7 On (VI7) | 262151 | 262151 | Identical |
| Virt Ip 70 On (VI70) | - | 262214 | G60 only |
| Virt Ip 71 On (VI71) | - | 262215 | G60 only |
| Virt Ip 72 On (VI72) | - | 262216 | G60 only |
| Virt Ip 73 On (VI73) | - | 262217 | G60 only |
| Virt Ip 74 On (VI74) | - | 262218 | G60 only |
| Virt Ip 75 On (VI75) | - | 262219 | G60 only |
| Virt Ip 76 On (VI76) | - | 262220 | G60 only |
| Virt Ip 77 On (VI77) | - | 262221 | G60 only |
| Virt Ip 78 On (VI78) | - | 262222 | G60 only |
| Virt Ip 79 On (VI79) | - | 262223 | G60 only |
| Virt Ip 8 On (VI8) | 262152 | 262152 | Identical |
| Virt Ip 80 On (VI80) | - | 262224 | G60 only |
| Virt Ip 81 On (VI81) | - | 262225 | G60 only |
| Virt Ip 82 On (VI82) | - | 262226 | G60 only |
| Virt Ip 83 On (VI83) | - | 262227 | G60 only |
| Virt Ip 84 On (VI84) | - | 262228 | G60 only |
| Virt Ip 85 On (VI85) | - | 262229 | G60 only |
| Virt Ip 86 On (VI86) | - | 262230 | G60 only |
| Virt Ip 87 On (VI87) | - | 262231 | G60 only |
| Virt Ip 88 On (VI88) | - | 262232 | G60 only |
| Virt Ip 89 On (VI89) | - | 262233 | G60 only |
| Virt Ip 9 On (VI9) | 262153 | 262153 | Identical |
| Virt Ip 90 On (VI90) | - | 262234 | G60 only |
| Virt Ip 91 On (VI91) | - | 262235 | G60 only |
| Virt Ip 92 On (VI92) | - | 262236 | G60 only |
| Virt Ip 93 On (VI93) | - | 262237 | G60 only |
| Virt Ip 94 On (VI94) | - | 262238 | G60 only |
| Virt Ip 95 On (VI95) | - | 262239 | G60 only |
| Virt Ip 96 On (VI96) | - | 262240 | G60 only |
| Virt Ip 97 On (VI97) | - | 262241 | G60 only |
| Virt Ip 98 On (VI98) | - | 262242 | G60 only |
| Virt Ip 99 On (VI99) | - | 262243 | G60 only |
| Virt Op 1 On (VO1) | - | 393217 | G60 only |
| Virt Op 10 On (VO10) | - | 393226 | G60 only |
| Virt Op 100 On (VO100) | - | 393316 | G60 only |
| Virt Op 101 On (VO101) | - | 393317 | G60 only |
| Virt Op 102 On (VO102) | - | 393318 | G60 only |
| Virt Op 103 On (VO103) | - | 393319 | G60 only |
| Virt Op 104 On (VO104) | - | 393320 | G60 only |
| Virt Op 105 On (VO105) | - | 393321 | G60 only |
| Virt Op 106 On (VO106) | - | 393322 | G60 only |
| Virt Op 107 On (VO107) | - | 393323 | G60 only |
| Virt Op 108 On (VO108) | - | 393324 | G60 only |
| Virt Op 109 On (VO109) | - | 393325 | G60 only |
| Virt Op 11 On (VO11) | - | 393227 | G60 only |
| Virt Op 110 On (VO110) | - | 393326 | G60 only |
| Virt Op 111 On (VO111) | - | 393327 | G60 only |
| Virt Op 112 On (VO112) | - | 393328 | G60 only |
| Virt Op 113 On (VO113) | - | 393329 | G60 only |
| Virt Op 114 On (VO114) | - | 393330 | G60 only |
| Virt Op 115 On (VO115) | - | 393331 | G60 only |
| Virt Op 116 On (VO116) | - | 393332 | G60 only |
| Virt Op 117 On (VO117) | - | 393333 | G60 only |
| Virt Op 118 On (VO118) | - | 393334 | G60 only |
| Virt Op 119 On (VO119) | - | 393335 | G60 only |
| Virt Op 12 On (VO12) | 393228 | 393228 | Identical |
| Virt Op 120 On (VO120) | - | 393336 | G60 only |
| Virt Op 121 On (VO121) | - | 393337 | G60 only |
| Virt Op 122 On (VO122) | - | 393338 | G60 only |
| Virt Op 123 On (VO123) | - | 393339 | G60 only |
| Virt Op 124 On (VO124) | - | 393340 | G60 only |
| Virt Op 125 On (VO125) | - | 393341 | G60 only |
| Virt Op 126 On (VO126) | - | 393342 | G60 only |
| Virt Op 127 On (VO127) | - | 393343 | G60 only |
| Virt Op 128 On (VO128) | - | 393344 | G60 only |
| Virt Op 129 On (VO129) | - | 393345 | G60 only |
| Virt Op 13 On (VO13) | 393229 | 393229 | Identical |
| Virt Op 130 On (VO130) | - | 393346 | G60 only |
| Virt Op 131 On (VO131) | - | 393347 | G60 only |
| Virt Op 132 On (VO132) | - | 393348 | G60 only |
| Virt Op 133 On (VO133) | - | 393349 | G60 only |
| Virt Op 134 On (VO134) | - | 393350 | G60 only |
| Virt Op 135 On (VO135) | - | 393351 | G60 only |
| Virt Op 136 On (VO136) | - | 393352 | G60 only |
| Virt Op 137 On (VO137) | - | 393353 | G60 only |
| Virt Op 138 On (VO138) | - | 393354 | G60 only |
| Virt Op 139 On (VO139) | - | 393355 | G60 only |
| Virt Op 14 On (VO14) | 393230 | 393230 | Identical |
| Virt Op 140 On (VO140) | - | 393356 | G60 only |
| Virt Op 141 On (VO141) | - | 393357 | G60 only |
| Virt Op 142 On (VO142) | - | 393358 | G60 only |
| Virt Op 143 On (VO143) | - | 393359 | G60 only |
| Virt Op 144 On (VO144) | - | 393360 | G60 only |
| Virt Op 145 On (VO145) | - | 393361 | G60 only |
| Virt Op 146 On (VO146) | - | 393362 | G60 only |
| Virt Op 147 On (VO147) | - | 393363 | G60 only |
| Virt Op 148 On (VO148) | - | 393364 | G60 only |
| Virt Op 149 On (VO149) | - | 393365 | G60 only |
| Virt Op 15 On (VO15) | 393231 | 393231 | Identical |
| Virt Op 150 On (VO150) | - | 393366 | G60 only |
| Virt Op 151 On (VO151) | - | 393367 | G60 only |
| Virt Op 152 On (VO152) | - | 393368 | G60 only |
| Virt Op 153 On (VO153) | - | 393369 | G60 only |
| Virt Op 154 On (VO154) | - | 393370 | G60 only |
| Virt Op 155 On (VO155) | - | 393371 | G60 only |
| Virt Op 156 On (VO156) | - | 393372 | G60 only |
| Virt Op 157 On (VO157) | - | 393373 | G60 only |
| Virt Op 158 On (VO158) | - | 393374 | G60 only |
| Virt Op 159 On (VO159) | - | 393375 | G60 only |
| Virt Op 16 On (VO16) | 393232 | 393232 | Identical |
| Virt Op 160 On (VO160) | - | 393376 | G60 only |
| Virt Op 161 On (VO161) | - | 393377 | G60 only |
| Virt Op 162 On (VO162) | - | 393378 | G60 only |
| Virt Op 163 On (VO163) | - | 393379 | G60 only |
| Virt Op 164 On (VO164) | - | 393380 | G60 only |
| Virt Op 165 On (VO165) | - | 393381 | G60 only |
| Virt Op 166 On (VO166) | - | 393382 | G60 only |
| Virt Op 167 On (VO167) | - | 393383 | G60 only |
| Virt Op 168 On (VO168) | - | 393384 | G60 only |
| Virt Op 169 On (VO169) | - | 393385 | G60 only |
| Virt Op 17 On (VO17) | 393233 | 393233 | Identical |
| Virt Op 170 On (VO170) | - | 393386 | G60 only |
| Virt Op 171 On (VO171) | - | 393387 | G60 only |
| Virt Op 172 On (VO172) | - | 393388 | G60 only |
| Virt Op 173 On (VO173) | - | 393389 | G60 only |
| Virt Op 174 On (VO174) | - | 393390 | G60 only |
| Virt Op 175 On (VO175) | - | 393391 | G60 only |
| Virt Op 176 On (VO176) | - | 393392 | G60 only |
| Virt Op 177 On (VO177) | - | 393393 | G60 only |
| Virt Op 178 On (VO178) | - | 393394 | G60 only |
| Virt Op 179 On (VO179) | - | 393395 | G60 only |
| Virt Op 18 On (VO18) | 393234 | 393234 | Identical |
| Virt Op 180 On (VO180) | - | 393396 | G60 only |
| Virt Op 181 On (VO181) | - | 393397 | G60 only |
| Virt Op 182 On (VO182) | - | 393398 | G60 only |
| Virt Op 183 On (VO183) | - | 393399 | G60 only |
| Virt Op 184 On (VO184) | - | 393400 | G60 only |
| Virt Op 185 On (VO185) | - | 393401 | G60 only |
| Virt Op 186 On (VO186) | - | 393402 | G60 only |
| Virt Op 187 On (VO187) | - | 393403 | G60 only |
| Virt Op 188 On (VO188) | - | 393404 | G60 only |
| Virt Op 189 On (VO189) | - | 393405 | G60 only |
| Virt Op 19 On (VO19) | 393235 | 393235 | Identical |
| Virt Op 190 On (VO190) | - | 393406 | G60 only |
| Virt Op 191 On (VO191) | - | 393407 | G60 only |
| Virt Op 192 On (VO192) | - | 393408 | G60 only |
| Virt Op 193 On (VO193) | - | 393409 | G60 only |
| Virt Op 194 On (VO194) | - | 393410 | G60 only |
| Virt Op 195 On (VO195) | - | 393411 | G60 only |
| Virt Op 196 On (VO196) | - | 393412 | G60 only |
| Virt Op 197 On (VO197) | - | 393413 | G60 only |
| Virt Op 198 On (VO198) | - | 393414 | G60 only |
| Virt Op 199 On (VO199) | - | 393415 | G60 only |
| Virt Op 2 On (VO2) | - | 393218 | G60 only |
| Virt Op 20 On (VO20) | 393236 | 393236 | Identical |
| Virt Op 200 On (VO200) | - | 393416 | G60 only |
| Virt Op 201 On (VO201) | - | 393417 | G60 only |
| Virt Op 202 On (VO202) | - | 393418 | G60 only |
| Virt Op 203 On (VO203) | - | 393419 | G60 only |
| Virt Op 204 On (VO204) | - | 393420 | G60 only |
| Virt Op 205 On (VO205) | - | 393421 | G60 only |
| Virt Op 206 On (VO206) | - | 393422 | G60 only |
| Virt Op 207 On (VO207) | - | 393423 | G60 only |
| Virt Op 208 On (VO208) | - | 393424 | G60 only |
| Virt Op 209 On (VO209) | - | 393425 | G60 only |
| Virt Op 21 On (VO21) | 393237 | 393237 | Identical |
| Virt Op 210 On (VO210) | - | 393426 | G60 only |
| Virt Op 211 On (VO211) | - | 393427 | G60 only |
| Virt Op 212 On (VO212) | - | 393428 | G60 only |
| Virt Op 213 On (VO213) | - | 393429 | G60 only |
| Virt Op 214 On (VO214) | - | 393430 | G60 only |
| Virt Op 215 On (VO215) | - | 393431 | G60 only |
| Virt Op 216 On (VO216) | - | 393432 | G60 only |
| Virt Op 217 On (VO217) | - | 393433 | G60 only |
| Virt Op 218 On (VO218) | - | 393434 | G60 only |
| Virt Op 219 On (VO219) | - | 393435 | G60 only |
| Virt Op 22 On (VO22) | 393238 | 393238 | Identical |
| Virt Op 220 On (VO220) | - | 393436 | G60 only |
| Virt Op 221 On (VO221) | - | 393437 | G60 only |
| Virt Op 222 On (VO222) | - | 393438 | G60 only |
| Virt Op 223 On (VO223) | - | 393439 | G60 only |
| Virt Op 224 On (VO224) | - | 393440 | G60 only |
| Virt Op 225 On (VO225) | - | 393441 | G60 only |
| Virt Op 226 On (VO226) | - | 393442 | G60 only |
| Virt Op 227 On (VO227) | - | 393443 | G60 only |
| Virt Op 228 On (VO228) | - | 393444 | G60 only |
| Virt Op 229 On (VO229) | - | 393445 | G60 only |
| Virt Op 23 On (VO23) | 393239 | 393239 | Identical |
| Virt Op 230 On (VO230) | - | 393446 | G60 only |
| Virt Op 231 On (VO231) | - | 393447 | G60 only |
| Virt Op 232 On (VO232) | - | 393448 | G60 only |
| Virt Op 233 On (VO233) | - | 393449 | G60 only |
| Virt Op 234 On (VO234) | - | 393450 | G60 only |
| Virt Op 235 On (VO235) | - | 393451 | G60 only |
| Virt Op 236 On (VO236) | - | 393452 | G60 only |
| Virt Op 237 On (VO237) | - | 393453 | G60 only |
| Virt Op 238 On (VO238) | - | 393454 | G60 only |
| Virt Op 239 On (VO239) | - | 393455 | G60 only |
| Virt Op 24 On (VO24) | 393240 | 393240 | Identical |
| Virt Op 240 On (VO240) | - | 393456 | G60 only |
| Virt Op 241 On (VO241) | - | 393457 | G60 only |
| Virt Op 242 On (VO242) | - | 393458 | G60 only |
| Virt Op 243 On (VO243) | - | 393459 | G60 only |
| Virt Op 244 On (VO244) | - | 393460 | G60 only |
| Virt Op 245 On (VO245) | - | 393461 | G60 only |
| Virt Op 246 On (VO246) | - | 393462 | G60 only |
| Virt Op 247 On (VO247) | - | 393463 | G60 only |
| Virt Op 248 On (VO248) | - | 393464 | G60 only |
| Virt Op 249 On (VO249) | - | 393465 | G60 only |
| Virt Op 25 On (VO25) | 393241 | 393241 | Identical |
| Virt Op 250 On (VO250) | - | 393466 | G60 only |
| Virt Op 251 On (VO251) | - | 393467 | G60 only |
| Virt Op 252 On (VO252) | - | 393468 | G60 only |
| Virt Op 253 On (VO253) | - | 393469 | G60 only |
| Virt Op 254 On (VO254) | - | 393470 | G60 only |
| Virt Op 255 On (VO255) | - | 393471 | G60 only |
| Virt Op 256 On (VO256) | - | 393472 | G60 only |
| Virt Op 26 On (VO26) | 393242 | 393242 | Identical |
| Virt Op 27 On (VO27) | 393243 | 393243 | Identical |
| Virt Op 28 On (VO28) | 393244 | 393244 | Identical |
| Virt Op 29 On (VO29) | 393245 | 393245 | Identical |
| Virt Op 3 On (VO3) | - | 393219 | G60 only |
| Virt Op 30 On (VO30) | 393246 | 393246 | Identical |
| Virt Op 31 On (VO31) | 393247 | 393247 | Identical |
| Virt Op 32 On (VO32) | 393248 | 393248 | Identical |
| Virt Op 33 On (VO33) | 393249 | 393249 | Identical |
| Virt Op 34 On (VO34) | 393250 | 393250 | Identical |
| Virt Op 35 On (VO35) | 393251 | 393251 | Identical |
| Virt Op 36 On (VO36) | 393252 | 393252 | Identical |
| Virt Op 37 On (VO37) | 393253 | 393253 | Identical |
| Virt Op 38 On (VO38) | 393254 | 393254 | Identical |
| Virt Op 39 On (VO39) | 393255 | 393255 | Identical |
| Virt Op 4 On (VO4) | - | 393220 | G60 only |
| Virt Op 40 On (VO40) | 393256 | 393256 | Identical |
| Virt Op 41 On (VO41) | 393257 | 393257 | Identical |
| Virt Op 42 On (VO42) | 393258 | 393258 | Identical |
| Virt Op 43 On (VO43) | 393259 | 393259 | Identical |
| Virt Op 44 On (VO44) | 393260 | 393260 | Identical |
| Virt Op 45 On (VO45) | 393261 | 393261 | Identical |
| Virt Op 46 On (VO46) | 393262 | 393262 | Identical |
| Virt Op 47 On (VO47) | 393263 | 393263 | Identical |
| Virt Op 48 On (VO48) | 393264 | 393264 | Identical |
| Virt Op 49 On (VO49) | 393265 | 393265 | Identical |
| Virt Op 5 On (VO5) | - | 393221 | G60 only |
| Virt Op 50 On (VO50) | 393266 | 393266 | Identical |
| Virt Op 51 On (VO51) | 393267 | 393267 | Identical |
| Virt Op 52 On (VO52) | 393268 | 393268 | Identical |
| Virt Op 53 On (VO53) | 393269 | 393269 | Identical |
| Virt Op 54 On (VO54) | 393270 | 393270 | Identical |
| Virt Op 55 On (VO55) | 393271 | 393271 | Identical |
| Virt Op 56 On (VO56) | 393272 | 393272 | Identical |
| Virt Op 57 On (VO57) | 393273 | 393273 | Identical |
| Virt Op 58 On (VO58) | 393274 | 393274 | Identical |
| Virt Op 59 On (VO59) | 393275 | 393275 | Identical |
| Virt Op 6 On (VO6) | - | 393222 | G60 only |
| Virt Op 60 On (VO60) | 393276 | 393276 | Identical |
| Virt Op 61 On (VO61) | 393277 | 393277 | Identical |
| Virt Op 62 On (VO62) | 393278 | 393278 | Identical |
| Virt Op 63 On (VO63) | 393279 | 393279 | Identical |
| Virt Op 64 On (VO64) | 393280 | 393280 | Identical |
| Virt Op 65 On (VO65) | 393281 | 393281 | Identical |
| Virt Op 66 On (VO66) | 393282 | 393282 | Identical |
| Virt Op 67 On (VO67) | 393283 | 393283 | Identical |
| Virt Op 68 On (VO68) | 393284 | 393284 | Identical |
| Virt Op 69 On (VO69) | 393285 | 393285 | Identical |
| Virt Op 7 On (VO7) | - | 393223 | G60 only |
| Virt Op 70 On (VO70) | 393286 | 393286 | Identical |
| Virt Op 71 On (VO71) | 393287 | 393287 | Identical |
| Virt Op 72 On (VO72) | 393288 | 393288 | Identical |
| Virt Op 73 On (VO73) | 393289 | 393289 | Identical |
| Virt Op 74 On (VO74) | 393290 | 393290 | Identical |
| Virt Op 75 On (VO75) | 393291 | 393291 | Identical |
| Virt Op 76 On (VO76) | 393292 | 393292 | Identical |
| Virt Op 77 On (VO77) | 393293 | 393293 | Identical |
| Virt Op 78 On (VO78) | 393294 | 393294 | Identical |
| Virt Op 79 On (VO79) | 393295 | 393295 | Identical |
| Virt Op 8 On (VO8) | - | 393224 | G60 only |
| Virt Op 80 On (VO80) | 393296 | 393296 | Identical |
| Virt Op 81 On (VO81) | 393297 | 393297 | Identical |
| Virt Op 82 On (VO82) | 393298 | 393298 | Identical |
| Virt Op 83 On (VO83) | 393299 | 393299 | Identical |
| Virt Op 84 On (VO84) | 393300 | 393300 | Identical |
| Virt Op 85 On (VO85) | 393301 | 393301 | Identical |
| Virt Op 86 On (VO86) | 393302 | 393302 | Identical |
| Virt Op 87 On (VO87) | 393303 | 393303 | Identical |
| Virt Op 88 On (VO88) | 393304 | 393304 | Identical |
| Virt Op 89 On (VO89) | 393305 | 393305 | Identical |
| Virt Op 9 On (VO9) | - | 393225 | G60 only |
| Virt Op 90 On (VO90) | 393306 | 393306 | Identical |
| Virt Op 91 On (VO91) | 393307 | 393307 | Identical |
| Virt Op 92 On (VO92) | 393308 | 393308 | Identical |
| Virt Op 93 On (VO93) | 393309 | 393309 | Identical |
| Virt Op 94 On (VO94) | 393310 | 393310 | Identical |
| Virt Op 95 On (VO95) | 393311 | 393311 | Identical |
| Virt Op 96 On (VO96) | 393312 | 393312 | Identical |
| Virt Op 97 On (VO97) | - | 393313 | G60 only |
| Virt Op 98 On (VO98) | - | 393314 | G60 only |
| Virt Op 99 On (VO99) | - | 393315 | G60 only |
| VOLTAGE MONITOR | 3538953 | 3538953 | Identical |
| VOLTS PER HERTZ 1 DPO | 2148008146 | 2148008304 | Code changed |
| VOLTS PER HERTZ 1 OP | 2147746002 | 2147746160 | Code changed |
| VOLTS PER HERTZ 1 PKP | 2147483858 | 2147484016 | Code changed |
| VOLTS PER HERTZ 2 DPO | 2148008147 | 2148008305 | Code changed |
| VOLTS PER HERTZ 2 OP | 2147746003 | 2147746161 | Code changed |
| VOLTS PER HERTZ 2 PKP | 2147483859 | 2147484017 | Code changed |
| XFMR AGING FCTR DPO | 2148008139 | - | G30 only |
| XFMR AGING FCTR OP | 2147745995 | - | G30 only |
| XFMR AGING FCTR PKP | 2147483851 | - | G30 only |
| XFMR HST-SPOT C DPO | 2148008138 | - | G30 only |
| XFMR HST-SPOT C OP | 2147745994 | - | G30 only |
| XFMR HST-SPOT C PKP | 2147483850 | - | G30 only |
| XFMR LIFE LOST OP | 2147745996 | - | G30 only |
| XFMR LIFE LOST PKP | 2147483852 | - | G30 only |
| XFMR PCNT DIFF 2ND A | 2149318865 | - | G30 only |
| XFMR PCNT DIFF 2ND B | 2149581009 | - | G30 only |
| XFMR PCNT DIFF 2ND C | 2149843153 | - | G30 only |
| XFMR PCNT DIFF 5TH A | 2150105297 | - | G30 only |
| XFMR PCNT DIFF 5TH B | 2150367441 | - | G30 only |
| XFMR PCNT DIFF 5TH C | 2150629585 | - | G30 only |
| XFMR PCNT DIFF DIR A | 2148271100 | - | G30 only |
| XFMR PCNT DIFF DIR B | 2148533244 | - | G30 only |
| XFMR PCNT DIFF DIR C | 2148795388 | - | G30 only |
| XFMR PCNT DIFF OP | 2149056721 | - | G30 only |
| XFMR PCNT DIFF OP A | 2148270289 | - | G30 only |
| XFMR PCNT DIFF OP B | 2148532433 | - | G30 only |
| XFMR PCNT DIFF OP C | 2148794577 | - | G30 only |
| XFMR PCNT DIFF PKP A | 2147483857 | - | G30 only |
| XFMR PCNT DIFF PKP B | 2147746001 | - | G30 only |
| XFMR PCNT DIFF PKP C | 2148008145 | - | G30 only |
| XFMR PCNT DIFF SAT A | 2147484668 | - | G30 only |
| XFMR PCNT DIFF SAT B | 2147746812 | - | G30 only |
| XFMR PCNT DIFF SAT C | 2148008956 | - | G30 only |
| XFMR PCNT DIFF WARN | 2149057532 | - | G30 only |

---

## FormatIndex 10013 - Signal / Measurement Operand Table

Used for measurement signal picks (SRC1 P, Ia RMS, etc.). Also the lookup source for **user-definable display Item codes**.

| Platform | User-display Item encoding |
|----------|---------------------------|
| G30 | Raw table-10013 code (e.g. `7168` = SRC1 P) |
| G60 | G60 table-10013 code **+ 262144** (e.g. `6912 + 262144 = 269056`) |

### Summary

| Metric | Count |
|--------|------:|
| G30 entries | 1032 |
| G60 entries | 1170 |
| Same name **and** same code | 707 |
| Same name, **different code** | 294 |
| G30 only (name absent on G60) | 31 |
| G60 only (name absent on G30) | 169 |

### Full entry comparison

| Name | G30 Code | G60 Code | Status |
|------|----------|----------|--------|
| Active Setting Group | 24447 | 24447 | Identical |
| Alt Ref Freq | - | 32770 | G60 only |
| Bkr 1 Acc Arc Amp A | 12032 | 53248 | Code changed |
| Bkr 1 Acc Arc Amp B | 12034 | 53250 | Code changed |
| Bkr 1 Acc Arc Amp C | 12036 | 53252 | Code changed |
| Bkr 1 Amp Max A | 12048 | 53264 | Code changed |
| Bkr 1 Amp Max B | 12050 | 53266 | Code changed |
| Bkr 1 Amp Max C | 12052 | 53268 | Code changed |
| Bkr 1 Arc Amp A | 12042 | 53258 | Code changed |
| Bkr 1 Arc Amp B | 12044 | 53260 | Code changed |
| Bkr 1 Arc Amp C | 12046 | 53262 | Code changed |
| Bkr 1 Op Time | 12041 | 53257 | Code changed |
| Bkr 1 Op Time A | 12038 | 53254 | Code changed |
| Bkr 1 Op Time B | 12039 | 53255 | Code changed |
| Bkr 1 Op Time C | 12040 | 53256 | Code changed |
| Bkr 2 Acc Arc Amp A | 12054 | 53270 | Code changed |
| Bkr 2 Acc Arc Amp B | 12056 | 53272 | Code changed |
| Bkr 2 Acc Arc Amp C | 12058 | 53274 | Code changed |
| Bkr 2 Amp Max A | 12070 | 53286 | Code changed |
| Bkr 2 Amp Max B | 12072 | 53288 | Code changed |
| Bkr 2 Amp Max C | 12074 | 53290 | Code changed |
| Bkr 2 Arc Amp A | 12064 | 53280 | Code changed |
| Bkr 2 Arc Amp B | 12066 | 53282 | Code changed |
| Bkr 2 Arc Amp C | 12068 | 53284 | Code changed |
| Bkr 2 Op Time | 12063 | 53279 | Code changed |
| Bkr 2 Op Time A | 12060 | 53276 | Code changed |
| Bkr 2 Op Time B | 12061 | 53277 | Code changed |
| Bkr 2 Op Time C | 12062 | 53278 | Code changed |
| Communications Group | 24432 | - | G30 only |
| DCMA Ip1 | 13504 | 14352 | Code changed |
| DCMA Ip2 | 13506 | 14354 | Code changed |
| DCMA Ip3 | 13508 | 14356 | Code changed |
| DCMA Ip4 | 13510 | 14358 | Code changed |
| DigCounter 1 Frozen | - | 2146 | G60 only |
| DigCounter 1 Value | - | 2144 | G60 only |
| DigCounter 2 Frozen | - | 2150 | G60 only |
| DigCounter 2 Value | - | 2148 | G60 only |
| DigCounter 3 Frozen | - | 2154 | G60 only |
| DigCounter 3 Value | - | 2152 | G60 only |
| DigCounter 4 Frozen | - | 2158 | G60 only |
| DigCounter 4 Value | - | 2156 | G60 only |
| DigCounter 5 Frozen | - | 2162 | G60 only |
| DigCounter 5 Value | - | 2160 | G60 only |
| DigCounter 6 Frozen | - | 2166 | G60 only |
| DigCounter 6 Value | - | 2164 | G60 only |
| DigCounter 7 Frozen | - | 2170 | G60 only |
| DigCounter 7 Value | - | 2168 | G60 only |
| DigCounter 8 Frozen | - | 2174 | G60 only |
| DigCounter 8 Value | - | 2172 | G60 only |
| Dist Zab Ang | - | 32449 | G60 only |
| Dist Zab Mag | - | 32448 | G60 only |
| Dist Zag Ang | - | 32455 | G60 only |
| Dist Zag Mag | - | 32454 | G60 only |
| Dist Zbc Ang | - | 32451 | G60 only |
| Dist Zbc Mag | - | 32450 | G60 only |
| Dist Zbg Ang | - | 32457 | G60 only |
| Dist Zbg Mag | - | 32456 | G60 only |
| Dist Zca Ang | - | 32453 | G60 only |
| Dist Zca Mag | - | 32452 | G60 only |
| Dist Zcg Ang | - | 32459 | G60 only |
| Dist Zcg Mag | - | 32458 | G60 only |
| Fault Location | - | 26180 | G60 only |
| Fault1        Analog [1 ] | - | 22168 | G60 only |
| Fault1        Analog [10 ] | - | 22186 | G60 only |
| Fault1        Analog [11 ] | - | 22188 | G60 only |
| Fault1        Analog [12 ] | - | 22190 | G60 only |
| Fault1        Analog [13 ] | - | 22192 | G60 only |
| Fault1        Analog [14 ] | - | 22194 | G60 only |
| Fault1        Analog [15 ] | - | 22196 | G60 only |
| Fault1        Analog [16 ] | - | 22198 | G60 only |
| Fault1        Analog [17 ] | - | 22200 | G60 only |
| Fault1        Analog [18 ] | - | 22202 | G60 only |
| Fault1        Analog [19 ] | - | 22204 | G60 only |
| Fault1        Analog [2 ] | - | 22170 | G60 only |
| Fault1        Analog [20 ] | - | 22206 | G60 only |
| Fault1        Analog [21 ] | - | 22208 | G60 only |
| Fault1        Analog [22 ] | - | 22210 | G60 only |
| Fault1        Analog [23 ] | - | 22212 | G60 only |
| Fault1        Analog [24 ] | - | 22214 | G60 only |
| Fault1        Analog [25 ] | - | 22216 | G60 only |
| Fault1        Analog [26 ] | - | 22218 | G60 only |
| Fault1        Analog [27 ] | - | 22220 | G60 only |
| Fault1        Analog [28 ] | - | 22222 | G60 only |
| Fault1        Analog [29 ] | - | 22224 | G60 only |
| Fault1        Analog [3 ] | - | 22172 | G60 only |
| Fault1        Analog [30 ] | - | 22226 | G60 only |
| Fault1        Analog [31 ] | - | 22228 | G60 only |
| Fault1        Analog [32 ] | - | 22230 | G60 only |
| Fault1        Analog [4 ] | - | 22174 | G60 only |
| Fault1        Analog [5 ] | - | 22176 | G60 only |
| Fault1        Analog [6 ] | - | 22178 | G60 only |
| Fault1        Analog [7 ] | - | 22180 | G60 only |
| Fault1        Analog [8 ] | - | 22182 | G60 only |
| Fault1        Analog [9 ] | - | 22184 | G60 only |
| Fault2        Analog [1 ] | - | 22232 | G60 only |
| Fault2        Analog [10 ] | - | 22250 | G60 only |
| Fault2        Analog [11 ] | - | 22252 | G60 only |
| Fault2        Analog [12 ] | - | 22254 | G60 only |
| Fault2        Analog [13 ] | - | 22256 | G60 only |
| Fault2        Analog [14 ] | - | 22258 | G60 only |
| Fault2        Analog [15 ] | - | 22260 | G60 only |
| Fault2        Analog [16 ] | - | 22262 | G60 only |
| Fault2        Analog [17 ] | - | 22264 | G60 only |
| Fault2        Analog [18 ] | - | 22266 | G60 only |
| Fault2        Analog [19 ] | - | 22268 | G60 only |
| Fault2        Analog [2 ] | - | 22234 | G60 only |
| Fault2        Analog [20 ] | - | 22270 | G60 only |
| Fault2        Analog [21 ] | - | 22272 | G60 only |
| Fault2        Analog [22 ] | - | 22274 | G60 only |
| Fault2        Analog [23 ] | - | 22276 | G60 only |
| Fault2        Analog [24 ] | - | 22278 | G60 only |
| Fault2        Analog [25 ] | - | 22280 | G60 only |
| Fault2        Analog [26 ] | - | 22282 | G60 only |
| Fault2        Analog [27 ] | - | 22284 | G60 only |
| Fault2        Analog [28 ] | - | 22286 | G60 only |
| Fault2        Analog [29 ] | - | 22288 | G60 only |
| Fault2        Analog [3 ] | - | 22236 | G60 only |
| Fault2        Analog [30 ] | - | 22290 | G60 only |
| Fault2        Analog [31 ] | - | 22292 | G60 only |
| Fault2        Analog [32 ] | - | 22294 | G60 only |
| Fault2        Analog [4 ] | - | 22238 | G60 only |
| Fault2        Analog [5 ] | - | 22240 | G60 only |
| Fault2        Analog [6 ] | - | 22242 | G60 only |
| Fault2        Analog [7 ] | - | 22244 | G60 only |
| Fault2        Analog [8 ] | - | 22246 | G60 only |
| Fault2        Analog [9 ] | - | 22248 | G60 only |
| Field Current | - | 26182 | G60 only |
| Field Ground Current | - | 26178 | G60 only |
| Field Ground Resist | - | 26176 | G60 only |
| Field Voltage | - | 26181 | G60 only |
| FlexElement 1  Value | 39168 | 39168 | Identical |
| FlexElement 10  Value | 39186 | 39186 | Identical |
| FlexElement 11  Value | 39188 | 39188 | Identical |
| FlexElement 12  Value | 39190 | 39190 | Identical |
| FlexElement 13  Value | 39192 | 39192 | Identical |
| FlexElement 14  Value | 39194 | 39194 | Identical |
| FlexElement 15  Value | 39196 | 39196 | Identical |
| FlexElement 16  Value | 39198 | 39198 | Identical |
| FlexElement 2  Value | 39170 | 39170 | Identical |
| FlexElement 3  Value | 39172 | 39172 | Identical |
| FlexElement 4  Value | 39174 | 39174 | Identical |
| FlexElement 5  Value | 39176 | 39176 | Identical |
| FlexElement 6  Value | 39178 | 39178 | Identical |
| FlexElement 7  Value | 39180 | 39180 | Identical |
| FlexElement 8  Value | 39182 | 39182 | Identical |
| FlexElement 9  Value | 39184 | 39184 | Identical |
| Freq Rate 1 Value | 5856 | 5856 | Identical |
| Freq Rate 2 Value | 5860 | 5860 | Identical |
| Freq Rate 3 Value | 5864 | 5864 | Identical |
| Freq Rate 4 Value | 5868 | 5868 | Identical |
| Harmonic Det 1 IA | - | 14032 | G60 only |
| Harmonic Det 1 IAVG | - | 14035 | G60 only |
| Harmonic Det 1 IB | - | 14033 | G60 only |
| Harmonic Det 1 IC | - | 14034 | G60 only |
| Harmonic Det 1 IG | - | 14036 | G60 only |
| Harmonic Det 2 IA | - | 14037 | G60 only |
| Harmonic Det 2 IAVG | - | 14040 | G60 only |
| Harmonic Det 2 IB | - | 14038 | G60 only |
| Harmonic Det 2 IC | - | 14039 | G60 only |
| Harmonic Det 2 IG | - | 14041 | G60 only |
| Harmonic Det 3 IA | - | 14042 | G60 only |
| Harmonic Det 3 IAVG | - | 14045 | G60 only |
| Harmonic Det 3 IB | - | 14043 | G60 only |
| Harmonic Det 3 IC | - | 14044 | G60 only |
| Harmonic Det 3 IG | - | 14046 | G60 only |
| Harmonic Det 4 IA | - | 14047 | G60 only |
| Harmonic Det 4 IAVG | - | 14050 | G60 only |
| Harmonic Det 4 IB | - | 14048 | G60 only |
| Harmonic Det 4 IC | - | 14049 | G60 only |
| Harmonic Det 4 IG | - | 14051 | G60 only |
| Injected Voltage | - | 26179 | G60 only |
| Last Fault Rpt Date | - | 22296 | G60 only |
| Last Fault Rpt Time | - | 22298 | G60 only |
| Main Ref Freq | - | 32769 | G60 only |
| OFF | 0 | 0 | Identical |
| Oscill Num Triggers | 12306 | 12306 | Identical |
| RGF 1      Igd Mag | 5792 | 5792 | Identical |
| RGF 1      Igr Mag | 5794 | 5794 | Identical |
| RGF 2      Igd Mag | 5796 | 5796 | Identical |
| RGF 2      Igr Mag | 5798 | 5798 | Identical |
| RRTD 1 Value | - | 34752 | G60 only |
| RRTD 10 Value | - | 34761 | G60 only |
| RRTD 11 Value | - | 34762 | G60 only |
| RRTD 12 Value | - | 34763 | G60 only |
| RRTD 2 Value | - | 34753 | G60 only |
| RRTD 3 Value | - | 34754 | G60 only |
| RRTD 4 Value | - | 34755 | G60 only |
| RRTD 5 Value | - | 34756 | G60 only |
| RRTD 6 Value | - | 34757 | G60 only |
| RRTD 7 Value | - | 34758 | G60 only |
| RRTD 8 Value | - | 34759 | G60 only |
| RRTD 9 Value | - | 34760 | G60 only |
| SH Current angle | - | 5759 | G60 only |
| Sh Injection Current | - | 5754 | G60 only |
| Sh Injection Voltage | - | 5752 | G60 only |
| Sns Dir Power 1 | 5760 | 5760 | Identical |
| Sns Dir Power 2 | 5762 | 5762 | Identical |
| SRC1       Demand Ia | - | 7680 | G60 only |
| SRC1       Demand Ib | - | 7682 | G60 only |
| SRC1       Demand Ic | - | 7684 | G60 only |
| SRC1       Demand VA | - | 7690 | G60 only |
| SRC1       Demand var | - | 7688 | G60 only |
| SRC1       Demand Watt | - | 7686 | G60 only |
| SRC1       Frequency | 7552 | 7552 | Identical |
| SRC1       I_0 Angle | 6171 | 20347 | Code changed |
| SRC1       I_0 Mag | 6169 | 20345 | Code changed |
| SRC1       I_1 Angle | 6174 | 20350 | Code changed |
| SRC1       I_1 Mag | 6172 | 20348 | Code changed |
| SRC1       I_2 Angle | 6177 | 20353 | Code changed |
| SRC1       I_2 Mag | 6175 | 20351 | Code changed |
| SRC1       Ia Angle | 6154 | 20330 | Code changed |
| SRC1       Ia Harm[10 ] | 10249 | 10249 | Identical |
| SRC1       Ia Harm[11 ] | 10250 | 10250 | Identical |
| SRC1       Ia Harm[12 ] | 10251 | 10251 | Identical |
| SRC1       Ia Harm[13 ] | 10252 | 10252 | Identical |
| SRC1       Ia Harm[14 ] | 10253 | 10253 | Identical |
| SRC1       Ia Harm[15 ] | 10254 | 10254 | Identical |
| SRC1       Ia Harm[16 ] | 10255 | 10255 | Identical |
| SRC1       Ia Harm[17 ] | 10256 | 10256 | Identical |
| SRC1       Ia Harm[18 ] | 10257 | 10257 | Identical |
| SRC1       Ia Harm[19 ] | 10258 | 10258 | Identical |
| SRC1       Ia Harm[2 ] | 10241 | 10241 | Identical |
| SRC1       Ia Harm[20 ] | 10259 | 10259 | Identical |
| SRC1       Ia Harm[21 ] | 10260 | 10260 | Identical |
| SRC1       Ia Harm[22 ] | 10261 | 10261 | Identical |
| SRC1       Ia Harm[23 ] | 10262 | 10262 | Identical |
| SRC1       Ia Harm[24 ] | 10263 | 10263 | Identical |
| SRC1       Ia Harm[25 ] | 10264 | 10264 | Identical |
| SRC1       Ia Harm[3 ] | 10242 | 10242 | Identical |
| SRC1       Ia Harm[4 ] | 10243 | 10243 | Identical |
| SRC1       Ia Harm[5 ] | 10244 | 10244 | Identical |
| SRC1       Ia Harm[6 ] | 10245 | 10245 | Identical |
| SRC1       Ia Harm[7 ] | 10246 | 10246 | Identical |
| SRC1       Ia Harm[8 ] | 10247 | 10247 | Identical |
| SRC1       Ia Harm[9 ] | 10248 | 10248 | Identical |
| SRC1       Ia Mag | 6152 | 20328 | Code changed |
| SRC1       Ia RMS | 6144 | 20320 | Code changed |
| SRC1       Ia THD | 10240 | 10240 | Identical |
| SRC1       Ib Angle | 6157 | 20333 | Code changed |
| SRC1       Ib Harm[10 ] | 10282 | 10282 | Identical |
| SRC1       Ib Harm[11 ] | 10283 | 10283 | Identical |
| SRC1       Ib Harm[12 ] | 10284 | 10284 | Identical |
| SRC1       Ib Harm[13 ] | 10285 | 10285 | Identical |
| SRC1       Ib Harm[14 ] | 10286 | 10286 | Identical |
| SRC1       Ib Harm[15 ] | 10287 | 10287 | Identical |
| SRC1       Ib Harm[16 ] | 10288 | 10288 | Identical |
| SRC1       Ib Harm[17 ] | 10289 | 10289 | Identical |
| SRC1       Ib Harm[18 ] | 10290 | 10290 | Identical |
| SRC1       Ib Harm[19 ] | 10291 | 10291 | Identical |
| SRC1       Ib Harm[2 ] | 10274 | 10274 | Identical |
| SRC1       Ib Harm[20 ] | 10292 | 10292 | Identical |
| SRC1       Ib Harm[21 ] | 10293 | 10293 | Identical |
| SRC1       Ib Harm[22 ] | 10294 | 10294 | Identical |
| SRC1       Ib Harm[23 ] | 10295 | 10295 | Identical |
| SRC1       Ib Harm[24 ] | 10296 | 10296 | Identical |
| SRC1       Ib Harm[25 ] | 10297 | 10297 | Identical |
| SRC1       Ib Harm[3 ] | 10275 | 10275 | Identical |
| SRC1       Ib Harm[4 ] | 10276 | 10276 | Identical |
| SRC1       Ib Harm[5 ] | 10277 | 10277 | Identical |
| SRC1       Ib Harm[6 ] | 10278 | 10278 | Identical |
| SRC1       Ib Harm[7 ] | 10279 | 10279 | Identical |
| SRC1       Ib Harm[8 ] | 10280 | 10280 | Identical |
| SRC1       Ib Harm[9 ] | 10281 | 10281 | Identical |
| SRC1       Ib Mag | 6155 | 20331 | Code changed |
| SRC1       Ib RMS | 6146 | 20322 | Code changed |
| SRC1       Ib THD | 10273 | 10273 | Identical |
| SRC1       Ic Angle | 6160 | 20336 | Code changed |
| SRC1       Ic Harm[10 ] | 10315 | 10315 | Identical |
| SRC1       Ic Harm[11 ] | 10316 | 10316 | Identical |
| SRC1       Ic Harm[12 ] | 10317 | 10317 | Identical |
| SRC1       Ic Harm[13 ] | 10318 | 10318 | Identical |
| SRC1       Ic Harm[14 ] | 10319 | 10319 | Identical |
| SRC1       Ic Harm[15 ] | 10320 | 10320 | Identical |
| SRC1       Ic Harm[16 ] | 10321 | 10321 | Identical |
| SRC1       Ic Harm[17 ] | 10322 | 10322 | Identical |
| SRC1       Ic Harm[18 ] | 10323 | 10323 | Identical |
| SRC1       Ic Harm[19 ] | 10324 | 10324 | Identical |
| SRC1       Ic Harm[2 ] | 10307 | 10307 | Identical |
| SRC1       Ic Harm[20 ] | 10325 | 10325 | Identical |
| SRC1       Ic Harm[21 ] | 10326 | 10326 | Identical |
| SRC1       Ic Harm[22 ] | 10327 | 10327 | Identical |
| SRC1       Ic Harm[23 ] | 10328 | 10328 | Identical |
| SRC1       Ic Harm[24 ] | 10329 | 10329 | Identical |
| SRC1       Ic Harm[25 ] | 10330 | 10330 | Identical |
| SRC1       Ic Harm[3 ] | 10308 | 10308 | Identical |
| SRC1       Ic Harm[4 ] | 10309 | 10309 | Identical |
| SRC1       Ic Harm[5 ] | 10310 | 10310 | Identical |
| SRC1       Ic Harm[6 ] | 10311 | 10311 | Identical |
| SRC1       Ic Harm[7 ] | 10312 | 10312 | Identical |
| SRC1       Ic Harm[8 ] | 10313 | 10313 | Identical |
| SRC1       Ic Harm[9 ] | 10314 | 10314 | Identical |
| SRC1       Ic Mag | 6158 | 20334 | Code changed |
| SRC1       Ic RMS | 6148 | 20324 | Code changed |
| SRC1       Ic THD | 10306 | 10306 | Identical |
| SRC1       Ig Angle | 6168 | 20344 | Code changed |
| SRC1       Ig Mag | 6166 | 20342 | Code changed |
| SRC1       Ig RMS | 6164 | 20340 | Code changed |
| SRC1       Igd Angle | 6180 | 22152 | Code changed |
| SRC1       Igd Mag | 6178 | 22150 | Code changed |
| SRC1       In Angle | 6163 | 20339 | Code changed |
| SRC1       In Mag | 6161 | 20337 | Code changed |
| SRC1       In RMS | 6150 | 20326 | Code changed |
| SRC1       Neg varh | 7430 | 7430 | Identical |
| SRC1       Neg Watthour | 7426 | 7426 | Identical |
| SRC1       P | 7168 | 6912 | Code changed |
| SRC1       Pa | 7170 | 6914 | Code changed |
| SRC1       Pb | 7172 | 6916 | Code changed |
| SRC1       Pc | 7174 | 6918 | Code changed |
| SRC1       PF | 7192 | 6936 | Code changed |
| SRC1       Phase A PF | 7193 | 6937 | Code changed |
| SRC1       Phase B PF | 7194 | 6938 | Code changed |
| SRC1       Phase C PF | 7195 | 6939 | Code changed |
| SRC1       Pos varh | 7428 | 7428 | Identical |
| SRC1       Pos Watthour | 7424 | 7424 | Identical |
| SRC1       Q | 7176 | 6920 | Code changed |
| SRC1       Qa | 7178 | 6922 | Code changed |
| SRC1       Qb | 7180 | 6924 | Code changed |
| SRC1       Qc | 7182 | 6926 | Code changed |
| SRC1       S | 7184 | 6928 | Code changed |
| SRC1       Sa | 7186 | 6930 | Code changed |
| SRC1       Sb | 7188 | 6932 | Code changed |
| SRC1       Sc | 7190 | 6934 | Code changed |
| SRC1       V_0 Angle | 6693 | 5925 | Code changed |
| SRC1       V_0 Mag | 6691 | 5923 | Code changed |
| SRC1       V_1 Angle | 6696 | 5928 | Code changed |
| SRC1       V_1 Mag | 6694 | 5926 | Code changed |
| SRC1       V_2 Angle | 6699 | 5931 | Code changed |
| SRC1       V_2 Mag | 6697 | 5929 | Code changed |
| SRC1       Va Harm[10 ] | 8073 | 8073 | Identical |
| SRC1       Va Harm[11 ] | 8074 | 8074 | Identical |
| SRC1       Va Harm[12 ] | 8075 | 8075 | Identical |
| SRC1       Va Harm[13 ] | 8076 | 8076 | Identical |
| SRC1       Va Harm[14 ] | 8077 | 8077 | Identical |
| SRC1       Va Harm[15 ] | 8078 | 8078 | Identical |
| SRC1       Va Harm[16 ] | 8079 | 8079 | Identical |
| SRC1       Va Harm[17 ] | 8080 | 8080 | Identical |
| SRC1       Va Harm[18 ] | 8081 | 8081 | Identical |
| SRC1       Va Harm[19 ] | 8082 | 8082 | Identical |
| SRC1       Va Harm[2 ] | 8065 | 8065 | Identical |
| SRC1       Va Harm[20 ] | 8083 | 8083 | Identical |
| SRC1       Va Harm[21 ] | 8084 | 8084 | Identical |
| SRC1       Va Harm[22 ] | 8085 | 8085 | Identical |
| SRC1       Va Harm[23 ] | 8086 | 8086 | Identical |
| SRC1       Va Harm[24 ] | 8087 | 8087 | Identical |
| SRC1       Va Harm[25 ] | 8088 | 8088 | Identical |
| SRC1       Va Harm[3 ] | 8066 | 8066 | Identical |
| SRC1       Va Harm[4 ] | 8067 | 8067 | Identical |
| SRC1       Va Harm[5 ] | 8068 | 8068 | Identical |
| SRC1       Va Harm[6 ] | 8069 | 8069 | Identical |
| SRC1       Va Harm[7 ] | 8070 | 8070 | Identical |
| SRC1       Va Harm[8 ] | 8071 | 8071 | Identical |
| SRC1       Va Harm[9 ] | 8072 | 8072 | Identical |
| SRC1       Va THD | 8064 | 8064 | Identical |
| SRC1       Vab Angle | 6679 | 5911 | Code changed |
| SRC1       Vab Mag | 6677 | 5909 | Code changed |
| SRC1       Vab RMS | 6671 | 5903 | Code changed |
| SRC1       Vag Angle | 6664 | 5896 | Code changed |
| SRC1       Vag Mag | 6662 | 5894 | Code changed |
| SRC1       Vag RMS | 6656 | 5888 | Code changed |
| SRC1       Vb Harm[10 ] | 8098 | 8098 | Identical |
| SRC1       Vb Harm[11 ] | 8099 | 8099 | Identical |
| SRC1       Vb Harm[12 ] | 8100 | 8100 | Identical |
| SRC1       Vb Harm[13 ] | 8101 | 8101 | Identical |
| SRC1       Vb Harm[14 ] | 8102 | 8102 | Identical |
| SRC1       Vb Harm[15 ] | 8103 | 8103 | Identical |
| SRC1       Vb Harm[16 ] | 8104 | 8104 | Identical |
| SRC1       Vb Harm[17 ] | 8105 | 8105 | Identical |
| SRC1       Vb Harm[18 ] | 8106 | 8106 | Identical |
| SRC1       Vb Harm[19 ] | 8107 | 8107 | Identical |
| SRC1       Vb Harm[2 ] | 8090 | 8090 | Identical |
| SRC1       Vb Harm[20 ] | 8108 | 8108 | Identical |
| SRC1       Vb Harm[21 ] | 8109 | 8109 | Identical |
| SRC1       Vb Harm[22 ] | 8110 | 8110 | Identical |
| SRC1       Vb Harm[23 ] | 8111 | 8111 | Identical |
| SRC1       Vb Harm[24 ] | 8112 | 8112 | Identical |
| SRC1       Vb Harm[25 ] | 8113 | 8113 | Identical |
| SRC1       Vb Harm[3 ] | 8091 | 8091 | Identical |
| SRC1       Vb Harm[4 ] | 8092 | 8092 | Identical |
| SRC1       Vb Harm[5 ] | 8093 | 8093 | Identical |
| SRC1       Vb Harm[6 ] | 8094 | 8094 | Identical |
| SRC1       Vb Harm[7 ] | 8095 | 8095 | Identical |
| SRC1       Vb Harm[8 ] | 8096 | 8096 | Identical |
| SRC1       Vb Harm[9 ] | 8097 | 8097 | Identical |
| SRC1       Vb THD | 8089 | 8089 | Identical |
| SRC1       Vbc Angle | 6682 | 5914 | Code changed |
| SRC1       Vbc Mag | 6680 | 5912 | Code changed |
| SRC1       Vbc RMS | 6673 | 5905 | Code changed |
| SRC1       Vbg Angle | 6667 | 5899 | Code changed |
| SRC1       Vbg Mag | 6665 | 5897 | Code changed |
| SRC1       Vbg RMS | 6658 | 5890 | Code changed |
| SRC1       Vc Harm[10 ] | 8123 | 8123 | Identical |
| SRC1       Vc Harm[11 ] | 8124 | 8124 | Identical |
| SRC1       Vc Harm[12 ] | 8125 | 8125 | Identical |
| SRC1       Vc Harm[13 ] | 8126 | 8126 | Identical |
| SRC1       Vc Harm[14 ] | 8127 | 8127 | Identical |
| SRC1       Vc Harm[15 ] | 8128 | 8128 | Identical |
| SRC1       Vc Harm[16 ] | 8129 | 8129 | Identical |
| SRC1       Vc Harm[17 ] | 8130 | 8130 | Identical |
| SRC1       Vc Harm[18 ] | 8131 | 8131 | Identical |
| SRC1       Vc Harm[19 ] | 8132 | 8132 | Identical |
| SRC1       Vc Harm[2 ] | 8115 | 8115 | Identical |
| SRC1       Vc Harm[20 ] | 8133 | 8133 | Identical |
| SRC1       Vc Harm[21 ] | 8134 | 8134 | Identical |
| SRC1       Vc Harm[22 ] | 8135 | 8135 | Identical |
| SRC1       Vc Harm[23 ] | 8136 | 8136 | Identical |
| SRC1       Vc Harm[24 ] | 8137 | 8137 | Identical |
| SRC1       Vc Harm[25 ] | 8138 | 8138 | Identical |
| SRC1       Vc Harm[3 ] | 8116 | 8116 | Identical |
| SRC1       Vc Harm[4 ] | 8117 | 8117 | Identical |
| SRC1       Vc Harm[5 ] | 8118 | 8118 | Identical |
| SRC1       Vc Harm[6 ] | 8119 | 8119 | Identical |
| SRC1       Vc Harm[7 ] | 8120 | 8120 | Identical |
| SRC1       Vc Harm[8 ] | 8121 | 8121 | Identical |
| SRC1       Vc Harm[9 ] | 8122 | 8122 | Identical |
| SRC1       Vc THD | 8114 | 8114 | Identical |
| SRC1       Vca Angle | 6685 | 5917 | Code changed |
| SRC1       Vca Mag | 6683 | 5915 | Code changed |
| SRC1       Vca RMS | 6675 | 5907 | Code changed |
| SRC1       Vcg Angle | 6670 | 5902 | Code changed |
| SRC1       Vcg Mag | 6668 | 5900 | Code changed |
| SRC1       Vcg RMS | 6660 | 5892 | Code changed |
| SRC1       Vx Angle | 6690 | 5922 | Code changed |
| SRC1       Vx Mag | 6688 | 5920 | Code changed |
| SRC1       Vx RMS | 6686 | 5918 | Code changed |
| SRC2       Demand Ia | - | 7696 | G60 only |
| SRC2       Demand Ib | - | 7698 | G60 only |
| SRC2       Demand Ic | - | 7700 | G60 only |
| SRC2       Demand VA | - | 7706 | G60 only |
| SRC2       Demand var | - | 7704 | G60 only |
| SRC2       Demand Watt | - | 7702 | G60 only |
| SRC2       Frequency | 7554 | 7554 | Identical |
| SRC2       I_0 Angle | 6235 | 20408 | Code changed |
| SRC2       I_0 Mag | 6233 | 20406 | Code changed |
| SRC2       I_1 Angle | 6238 | 20411 | Code changed |
| SRC2       I_1 Mag | 6236 | 20409 | Code changed |
| SRC2       I_2 Angle | 6241 | 20414 | Code changed |
| SRC2       I_2 Mag | 6239 | 20412 | Code changed |
| SRC2       Ia Angle | 6218 | 20391 | Code changed |
| SRC2       Ia Harm[10 ] | 10348 | 10348 | Identical |
| SRC2       Ia Harm[11 ] | 10349 | 10349 | Identical |
| SRC2       Ia Harm[12 ] | 10350 | 10350 | Identical |
| SRC2       Ia Harm[13 ] | 10351 | 10351 | Identical |
| SRC2       Ia Harm[14 ] | 10352 | 10352 | Identical |
| SRC2       Ia Harm[15 ] | 10353 | 10353 | Identical |
| SRC2       Ia Harm[16 ] | 10354 | 10354 | Identical |
| SRC2       Ia Harm[17 ] | 10355 | 10355 | Identical |
| SRC2       Ia Harm[18 ] | 10356 | 10356 | Identical |
| SRC2       Ia Harm[19 ] | 10357 | 10357 | Identical |
| SRC2       Ia Harm[2 ] | 10340 | 10340 | Identical |
| SRC2       Ia Harm[20 ] | 10358 | 10358 | Identical |
| SRC2       Ia Harm[21 ] | 10359 | 10359 | Identical |
| SRC2       Ia Harm[22 ] | 10360 | 10360 | Identical |
| SRC2       Ia Harm[23 ] | 10361 | 10361 | Identical |
| SRC2       Ia Harm[24 ] | 10362 | 10362 | Identical |
| SRC2       Ia Harm[25 ] | 10363 | 10363 | Identical |
| SRC2       Ia Harm[3 ] | 10341 | 10341 | Identical |
| SRC2       Ia Harm[4 ] | 10342 | 10342 | Identical |
| SRC2       Ia Harm[5 ] | 10343 | 10343 | Identical |
| SRC2       Ia Harm[6 ] | 10344 | 10344 | Identical |
| SRC2       Ia Harm[7 ] | 10345 | 10345 | Identical |
| SRC2       Ia Harm[8 ] | 10346 | 10346 | Identical |
| SRC2       Ia Harm[9 ] | 10347 | 10347 | Identical |
| SRC2       Ia Mag | 6216 | 20389 | Code changed |
| SRC2       Ia RMS | 6208 | 20381 | Code changed |
| SRC2       Ia THD | 10339 | 10339 | Identical |
| SRC2       Ib Angle | 6221 | 20394 | Code changed |
| SRC2       Ib Harm[10 ] | 10381 | 10381 | Identical |
| SRC2       Ib Harm[11 ] | 10382 | 10382 | Identical |
| SRC2       Ib Harm[12 ] | 10383 | 10383 | Identical |
| SRC2       Ib Harm[13 ] | 10384 | 10384 | Identical |
| SRC2       Ib Harm[14 ] | 10385 | 10385 | Identical |
| SRC2       Ib Harm[15 ] | 10386 | 10386 | Identical |
| SRC2       Ib Harm[16 ] | 10387 | 10387 | Identical |
| SRC2       Ib Harm[17 ] | 10388 | 10388 | Identical |
| SRC2       Ib Harm[18 ] | 10389 | 10389 | Identical |
| SRC2       Ib Harm[19 ] | 10390 | 10390 | Identical |
| SRC2       Ib Harm[2 ] | 10373 | 10373 | Identical |
| SRC2       Ib Harm[20 ] | 10391 | 10391 | Identical |
| SRC2       Ib Harm[21 ] | 10392 | 10392 | Identical |
| SRC2       Ib Harm[22 ] | 10393 | 10393 | Identical |
| SRC2       Ib Harm[23 ] | 10394 | 10394 | Identical |
| SRC2       Ib Harm[24 ] | 10395 | 10395 | Identical |
| SRC2       Ib Harm[25 ] | 10396 | 10396 | Identical |
| SRC2       Ib Harm[3 ] | 10374 | 10374 | Identical |
| SRC2       Ib Harm[4 ] | 10375 | 10375 | Identical |
| SRC2       Ib Harm[5 ] | 10376 | 10376 | Identical |
| SRC2       Ib Harm[6 ] | 10377 | 10377 | Identical |
| SRC2       Ib Harm[7 ] | 10378 | 10378 | Identical |
| SRC2       Ib Harm[8 ] | 10379 | 10379 | Identical |
| SRC2       Ib Harm[9 ] | 10380 | 10380 | Identical |
| SRC2       Ib Mag | 6219 | 20392 | Code changed |
| SRC2       Ib RMS | 6210 | 20383 | Code changed |
| SRC2       Ib THD | 10372 | 10372 | Identical |
| SRC2       Ic Angle | 6224 | 20397 | Code changed |
| SRC2       Ic Harm[10 ] | 10414 | 10414 | Identical |
| SRC2       Ic Harm[11 ] | 10415 | 10415 | Identical |
| SRC2       Ic Harm[12 ] | 10416 | 10416 | Identical |
| SRC2       Ic Harm[13 ] | 10417 | 10417 | Identical |
| SRC2       Ic Harm[14 ] | 10418 | 10418 | Identical |
| SRC2       Ic Harm[15 ] | 10419 | 10419 | Identical |
| SRC2       Ic Harm[16 ] | 10420 | 10420 | Identical |
| SRC2       Ic Harm[17 ] | 10421 | 10421 | Identical |
| SRC2       Ic Harm[18 ] | 10422 | 10422 | Identical |
| SRC2       Ic Harm[19 ] | 10423 | 10423 | Identical |
| SRC2       Ic Harm[2 ] | 10406 | 10406 | Identical |
| SRC2       Ic Harm[20 ] | 10424 | 10424 | Identical |
| SRC2       Ic Harm[21 ] | 10425 | 10425 | Identical |
| SRC2       Ic Harm[22 ] | 10426 | 10426 | Identical |
| SRC2       Ic Harm[23 ] | 10427 | 10427 | Identical |
| SRC2       Ic Harm[24 ] | 10428 | 10428 | Identical |
| SRC2       Ic Harm[25 ] | 10429 | 10429 | Identical |
| SRC2       Ic Harm[3 ] | 10407 | 10407 | Identical |
| SRC2       Ic Harm[4 ] | 10408 | 10408 | Identical |
| SRC2       Ic Harm[5 ] | 10409 | 10409 | Identical |
| SRC2       Ic Harm[6 ] | 10410 | 10410 | Identical |
| SRC2       Ic Harm[7 ] | 10411 | 10411 | Identical |
| SRC2       Ic Harm[8 ] | 10412 | 10412 | Identical |
| SRC2       Ic Harm[9 ] | 10413 | 10413 | Identical |
| SRC2       Ic Mag | 6222 | 20395 | Code changed |
| SRC2       Ic RMS | 6212 | 20385 | Code changed |
| SRC2       Ic THD | 10405 | 10405 | Identical |
| SRC2       Ig Angle | 6232 | 20405 | Code changed |
| SRC2       Ig Mag | 6230 | 20403 | Code changed |
| SRC2       Ig RMS | 6228 | 20401 | Code changed |
| SRC2       Igd Angle | 6244 | 22155 | Code changed |
| SRC2       Igd Mag | 6242 | 22153 | Code changed |
| SRC2       In Angle | 6227 | 20400 | Code changed |
| SRC2       In Mag | 6225 | 20398 | Code changed |
| SRC2       In RMS | 6214 | 20387 | Code changed |
| SRC2       Neg varh | 7446 | 7446 | Identical |
| SRC2       Neg Watthour | 7442 | 7442 | Identical |
| SRC2       P | 7200 | 6944 | Code changed |
| SRC2       Pa | 7202 | 6946 | Code changed |
| SRC2       Pb | 7204 | 6948 | Code changed |
| SRC2       Pc | 7206 | 6950 | Code changed |
| SRC2       PF | 7224 | 6968 | Code changed |
| SRC2       Phase A PF | 7225 | 6969 | Code changed |
| SRC2       Phase B PF | 7226 | 6970 | Code changed |
| SRC2       Phase C PF | 7227 | 6971 | Code changed |
| SRC2       Pos varh | 7444 | 7444 | Identical |
| SRC2       Pos Watthour | 7440 | 7440 | Identical |
| SRC2       Q | 7208 | 6952 | Code changed |
| SRC2       Qa | 7210 | 6954 | Code changed |
| SRC2       Qb | 7212 | 6956 | Code changed |
| SRC2       Qc | 7214 | 6958 | Code changed |
| SRC2       S | 7216 | 6960 | Code changed |
| SRC2       Sa | 7218 | 6962 | Code changed |
| SRC2       Sb | 7220 | 6964 | Code changed |
| SRC2       Sc | 7222 | 6966 | Code changed |
| SRC2       V_0 Angle | 6757 | 5989 | Code changed |
| SRC2       V_0 Mag | 6755 | 5987 | Code changed |
| SRC2       V_1 Angle | 6760 | 5992 | Code changed |
| SRC2       V_1 Mag | 6758 | 5990 | Code changed |
| SRC2       V_2 Angle | 6763 | 5995 | Code changed |
| SRC2       V_2 Mag | 6761 | 5993 | Code changed |
| SRC2       Va Harm[10 ] | 8148 | 8148 | Identical |
| SRC2       Va Harm[11 ] | 8149 | 8149 | Identical |
| SRC2       Va Harm[12 ] | 8150 | 8150 | Identical |
| SRC2       Va Harm[13 ] | 8151 | 8151 | Identical |
| SRC2       Va Harm[14 ] | 8152 | 8152 | Identical |
| SRC2       Va Harm[15 ] | 8153 | 8153 | Identical |
| SRC2       Va Harm[16 ] | 8154 | 8154 | Identical |
| SRC2       Va Harm[17 ] | 8155 | 8155 | Identical |
| SRC2       Va Harm[18 ] | 8156 | 8156 | Identical |
| SRC2       Va Harm[19 ] | 8157 | 8157 | Identical |
| SRC2       Va Harm[2 ] | 8140 | 8140 | Identical |
| SRC2       Va Harm[20 ] | 8158 | 8158 | Identical |
| SRC2       Va Harm[21 ] | 8159 | 8159 | Identical |
| SRC2       Va Harm[22 ] | 8160 | 8160 | Identical |
| SRC2       Va Harm[23 ] | 8161 | 8161 | Identical |
| SRC2       Va Harm[24 ] | 8162 | 8162 | Identical |
| SRC2       Va Harm[25 ] | 8163 | 8163 | Identical |
| SRC2       Va Harm[3 ] | 8141 | 8141 | Identical |
| SRC2       Va Harm[4 ] | 8142 | 8142 | Identical |
| SRC2       Va Harm[5 ] | 8143 | 8143 | Identical |
| SRC2       Va Harm[6 ] | 8144 | 8144 | Identical |
| SRC2       Va Harm[7 ] | 8145 | 8145 | Identical |
| SRC2       Va Harm[8 ] | 8146 | 8146 | Identical |
| SRC2       Va Harm[9 ] | 8147 | 8147 | Identical |
| SRC2       Va THD | 8139 | 8139 | Identical |
| SRC2       Vab Angle | 6743 | 5975 | Code changed |
| SRC2       Vab Mag | 6741 | 5973 | Code changed |
| SRC2       Vab RMS | 6735 | 5967 | Code changed |
| SRC2       Vag Angle | 6728 | 5960 | Code changed |
| SRC2       Vag Mag | 6726 | 5958 | Code changed |
| SRC2       Vag RMS | 6720 | 5952 | Code changed |
| SRC2       Vb Harm[10 ] | 8173 | 8173 | Identical |
| SRC2       Vb Harm[11 ] | 8174 | 8174 | Identical |
| SRC2       Vb Harm[12 ] | 8175 | 8175 | Identical |
| SRC2       Vb Harm[13 ] | 8176 | 8176 | Identical |
| SRC2       Vb Harm[14 ] | 8177 | 8177 | Identical |
| SRC2       Vb Harm[15 ] | 8178 | 8178 | Identical |
| SRC2       Vb Harm[16 ] | 8179 | 8179 | Identical |
| SRC2       Vb Harm[17 ] | 8180 | 8180 | Identical |
| SRC2       Vb Harm[18 ] | 8181 | 8181 | Identical |
| SRC2       Vb Harm[19 ] | 8182 | 8182 | Identical |
| SRC2       Vb Harm[2 ] | 8165 | 8165 | Identical |
| SRC2       Vb Harm[20 ] | 8183 | 8183 | Identical |
| SRC2       Vb Harm[21 ] | 8184 | 8184 | Identical |
| SRC2       Vb Harm[22 ] | 8185 | 8185 | Identical |
| SRC2       Vb Harm[23 ] | 8186 | 8186 | Identical |
| SRC2       Vb Harm[24 ] | 8187 | 8187 | Identical |
| SRC2       Vb Harm[25 ] | 8188 | 8188 | Identical |
| SRC2       Vb Harm[3 ] | 8166 | 8166 | Identical |
| SRC2       Vb Harm[4 ] | 8167 | 8167 | Identical |
| SRC2       Vb Harm[5 ] | 8168 | 8168 | Identical |
| SRC2       Vb Harm[6 ] | 8169 | 8169 | Identical |
| SRC2       Vb Harm[7 ] | 8170 | 8170 | Identical |
| SRC2       Vb Harm[8 ] | 8171 | 8171 | Identical |
| SRC2       Vb Harm[9 ] | 8172 | 8172 | Identical |
| SRC2       Vb THD | 8164 | 8164 | Identical |
| SRC2       Vbc Angle | 6746 | 5978 | Code changed |
| SRC2       Vbc Mag | 6744 | 5976 | Code changed |
| SRC2       Vbc RMS | 6737 | 5969 | Code changed |
| SRC2       Vbg Angle | 6731 | 5963 | Code changed |
| SRC2       Vbg Mag | 6729 | 5961 | Code changed |
| SRC2       Vbg RMS | 6722 | 5954 | Code changed |
| SRC2       Vc Harm[10 ] | 8198 | 8198 | Identical |
| SRC2       Vc Harm[11 ] | 8199 | 8199 | Identical |
| SRC2       Vc Harm[12 ] | 8200 | 8200 | Identical |
| SRC2       Vc Harm[13 ] | 8201 | 8201 | Identical |
| SRC2       Vc Harm[14 ] | 8202 | 8202 | Identical |
| SRC2       Vc Harm[15 ] | 8203 | 8203 | Identical |
| SRC2       Vc Harm[16 ] | 8204 | 8204 | Identical |
| SRC2       Vc Harm[17 ] | 8205 | 8205 | Identical |
| SRC2       Vc Harm[18 ] | 8206 | 8206 | Identical |
| SRC2       Vc Harm[19 ] | 8207 | 8207 | Identical |
| SRC2       Vc Harm[2 ] | 8190 | 8190 | Identical |
| SRC2       Vc Harm[20 ] | 8208 | 8208 | Identical |
| SRC2       Vc Harm[21 ] | 8209 | 8209 | Identical |
| SRC2       Vc Harm[22 ] | 8210 | 8210 | Identical |
| SRC2       Vc Harm[23 ] | 8211 | 8211 | Identical |
| SRC2       Vc Harm[24 ] | 8212 | 8212 | Identical |
| SRC2       Vc Harm[25 ] | 8213 | 8213 | Identical |
| SRC2       Vc Harm[3 ] | 8191 | 8191 | Identical |
| SRC2       Vc Harm[4 ] | 8192 | 8192 | Identical |
| SRC2       Vc Harm[5 ] | 8193 | 8193 | Identical |
| SRC2       Vc Harm[6 ] | 8194 | 8194 | Identical |
| SRC2       Vc Harm[7 ] | 8195 | 8195 | Identical |
| SRC2       Vc Harm[8 ] | 8196 | 8196 | Identical |
| SRC2       Vc Harm[9 ] | 8197 | 8197 | Identical |
| SRC2       Vc THD | 8189 | 8189 | Identical |
| SRC2       Vca Angle | 6749 | 5981 | Code changed |
| SRC2       Vca Mag | 6747 | 5979 | Code changed |
| SRC2       Vca RMS | 6739 | 5971 | Code changed |
| SRC2       Vcg Angle | 6734 | 5966 | Code changed |
| SRC2       Vcg Mag | 6732 | 5964 | Code changed |
| SRC2       Vcg RMS | 6724 | 5956 | Code changed |
| SRC2       Vx Angle | 6754 | 5986 | Code changed |
| SRC2       Vx Mag | 6752 | 5984 | Code changed |
| SRC2       Vx RMS | 6750 | 5982 | Code changed |
| SRC3       Demand Ia | - | 7712 | G60 only |
| SRC3       Demand Ib | - | 7714 | G60 only |
| SRC3       Demand Ic | - | 7716 | G60 only |
| SRC3       Demand VA | - | 7722 | G60 only |
| SRC3       Demand var | - | 7720 | G60 only |
| SRC3       Demand Watt | - | 7718 | G60 only |
| SRC3       Frequency | 7556 | 7556 | Identical |
| SRC3       I_0 Angle | 6299 | 20469 | Code changed |
| SRC3       I_0 Mag | 6297 | 20467 | Code changed |
| SRC3       I_1 Angle | 6302 | 20472 | Code changed |
| SRC3       I_1 Mag | 6300 | 20470 | Code changed |
| SRC3       I_2 Angle | 6305 | 20475 | Code changed |
| SRC3       I_2 Mag | 6303 | 20473 | Code changed |
| SRC3       Ia Angle | 6282 | 20452 | Code changed |
| SRC3       Ia Harm[10 ] | 10447 | 10447 | Identical |
| SRC3       Ia Harm[11 ] | 10448 | 10448 | Identical |
| SRC3       Ia Harm[12 ] | 10449 | 10449 | Identical |
| SRC3       Ia Harm[13 ] | 10450 | 10450 | Identical |
| SRC3       Ia Harm[14 ] | 10451 | 10451 | Identical |
| SRC3       Ia Harm[15 ] | 10452 | 10452 | Identical |
| SRC3       Ia Harm[16 ] | 10453 | 10453 | Identical |
| SRC3       Ia Harm[17 ] | 10454 | 10454 | Identical |
| SRC3       Ia Harm[18 ] | 10455 | 10455 | Identical |
| SRC3       Ia Harm[19 ] | 10456 | 10456 | Identical |
| SRC3       Ia Harm[2 ] | 10439 | 10439 | Identical |
| SRC3       Ia Harm[20 ] | 10457 | 10457 | Identical |
| SRC3       Ia Harm[21 ] | 10458 | 10458 | Identical |
| SRC3       Ia Harm[22 ] | 10459 | 10459 | Identical |
| SRC3       Ia Harm[23 ] | 10460 | 10460 | Identical |
| SRC3       Ia Harm[24 ] | 10461 | 10461 | Identical |
| SRC3       Ia Harm[25 ] | 10462 | 10462 | Identical |
| SRC3       Ia Harm[3 ] | 10440 | 10440 | Identical |
| SRC3       Ia Harm[4 ] | 10441 | 10441 | Identical |
| SRC3       Ia Harm[5 ] | 10442 | 10442 | Identical |
| SRC3       Ia Harm[6 ] | 10443 | 10443 | Identical |
| SRC3       Ia Harm[7 ] | 10444 | 10444 | Identical |
| SRC3       Ia Harm[8 ] | 10445 | 10445 | Identical |
| SRC3       Ia Harm[9 ] | 10446 | 10446 | Identical |
| SRC3       Ia Mag | 6280 | 20450 | Code changed |
| SRC3       Ia RMS | 6272 | 20442 | Code changed |
| SRC3       Ia THD | 10438 | 10438 | Identical |
| SRC3       Ib Angle | 6285 | 20455 | Code changed |
| SRC3       Ib Harm[10 ] | 10480 | 10480 | Identical |
| SRC3       Ib Harm[11 ] | 10481 | 10481 | Identical |
| SRC3       Ib Harm[12 ] | 10482 | 10482 | Identical |
| SRC3       Ib Harm[13 ] | 10483 | 10483 | Identical |
| SRC3       Ib Harm[14 ] | 10484 | 10484 | Identical |
| SRC3       Ib Harm[15 ] | 10485 | 10485 | Identical |
| SRC3       Ib Harm[16 ] | 10486 | 10486 | Identical |
| SRC3       Ib Harm[17 ] | 10487 | 10487 | Identical |
| SRC3       Ib Harm[18 ] | 10488 | 10488 | Identical |
| SRC3       Ib Harm[19 ] | 10489 | 10489 | Identical |
| SRC3       Ib Harm[2 ] | 10472 | 10472 | Identical |
| SRC3       Ib Harm[20 ] | 10490 | 10490 | Identical |
| SRC3       Ib Harm[21 ] | 10491 | 10491 | Identical |
| SRC3       Ib Harm[22 ] | 10492 | 10492 | Identical |
| SRC3       Ib Harm[23 ] | 10493 | 10493 | Identical |
| SRC3       Ib Harm[24 ] | 10494 | 10494 | Identical |
| SRC3       Ib Harm[25 ] | 10495 | 10495 | Identical |
| SRC3       Ib Harm[3 ] | 10473 | 10473 | Identical |
| SRC3       Ib Harm[4 ] | 10474 | 10474 | Identical |
| SRC3       Ib Harm[5 ] | 10475 | 10475 | Identical |
| SRC3       Ib Harm[6 ] | 10476 | 10476 | Identical |
| SRC3       Ib Harm[7 ] | 10477 | 10477 | Identical |
| SRC3       Ib Harm[8 ] | 10478 | 10478 | Identical |
| SRC3       Ib Harm[9 ] | 10479 | 10479 | Identical |
| SRC3       Ib Mag | 6283 | 20453 | Code changed |
| SRC3       Ib RMS | 6274 | 20444 | Code changed |
| SRC3       Ib THD | 10471 | 10471 | Identical |
| SRC3       Ic Angle | 6288 | 20458 | Code changed |
| SRC3       Ic Harm[10 ] | 10513 | 10513 | Identical |
| SRC3       Ic Harm[11 ] | 10514 | 10514 | Identical |
| SRC3       Ic Harm[12 ] | 10515 | 10515 | Identical |
| SRC3       Ic Harm[13 ] | 10516 | 10516 | Identical |
| SRC3       Ic Harm[14 ] | 10517 | 10517 | Identical |
| SRC3       Ic Harm[15 ] | 10518 | 10518 | Identical |
| SRC3       Ic Harm[16 ] | 10519 | 10519 | Identical |
| SRC3       Ic Harm[17 ] | 10520 | 10520 | Identical |
| SRC3       Ic Harm[18 ] | 10521 | 10521 | Identical |
| SRC3       Ic Harm[19 ] | 10522 | 10522 | Identical |
| SRC3       Ic Harm[2 ] | 10505 | 10505 | Identical |
| SRC3       Ic Harm[20 ] | 10523 | 10523 | Identical |
| SRC3       Ic Harm[21 ] | 10524 | 10524 | Identical |
| SRC3       Ic Harm[22 ] | 10525 | 10525 | Identical |
| SRC3       Ic Harm[23 ] | 10526 | 10526 | Identical |
| SRC3       Ic Harm[24 ] | 10527 | 10527 | Identical |
| SRC3       Ic Harm[25 ] | 10528 | 10528 | Identical |
| SRC3       Ic Harm[3 ] | 10506 | 10506 | Identical |
| SRC3       Ic Harm[4 ] | 10507 | 10507 | Identical |
| SRC3       Ic Harm[5 ] | 10508 | 10508 | Identical |
| SRC3       Ic Harm[6 ] | 10509 | 10509 | Identical |
| SRC3       Ic Harm[7 ] | 10510 | 10510 | Identical |
| SRC3       Ic Harm[8 ] | 10511 | 10511 | Identical |
| SRC3       Ic Harm[9 ] | 10512 | 10512 | Identical |
| SRC3       Ic Mag | 6286 | 20456 | Code changed |
| SRC3       Ic RMS | 6276 | 20446 | Code changed |
| SRC3       Ic THD | 10504 | 10504 | Identical |
| SRC3       Ig Angle | 6296 | 20466 | Code changed |
| SRC3       Ig Mag | 6294 | 20464 | Code changed |
| SRC3       Ig RMS | 6292 | 20462 | Code changed |
| SRC3       Igd Angle | 6308 | 22158 | Code changed |
| SRC3       Igd Mag | 6306 | 22156 | Code changed |
| SRC3       In Angle | 6291 | 20461 | Code changed |
| SRC3       In Mag | 6289 | 20459 | Code changed |
| SRC3       In RMS | 6278 | 20448 | Code changed |
| SRC3       Neg varh | 7462 | 7462 | Identical |
| SRC3       Neg Watthour | 7458 | 7458 | Identical |
| SRC3       P | 7232 | 6976 | Code changed |
| SRC3       Pa | 7234 | 6978 | Code changed |
| SRC3       Pb | 7236 | 6980 | Code changed |
| SRC3       Pc | 7238 | 6982 | Code changed |
| SRC3       PF | 7256 | 7000 | Code changed |
| SRC3       Phase A PF | 7257 | 7001 | Code changed |
| SRC3       Phase B PF | 7258 | 7002 | Code changed |
| SRC3       Phase C PF | 7259 | 7003 | Code changed |
| SRC3       Pos varh | 7460 | 7460 | Identical |
| SRC3       Pos Watthour | 7456 | 7456 | Identical |
| SRC3       Q | 7240 | 6984 | Code changed |
| SRC3       Qa | 7242 | 6986 | Code changed |
| SRC3       Qb | 7244 | 6988 | Code changed |
| SRC3       Qc | 7246 | 6990 | Code changed |
| SRC3       S | 7248 | 6992 | Code changed |
| SRC3       Sa | 7250 | 6994 | Code changed |
| SRC3       Sb | 7252 | 6996 | Code changed |
| SRC3       Sc | 7254 | 6998 | Code changed |
| SRC3       V_0 Angle | 6821 | 6053 | Code changed |
| SRC3       V_0 Mag | 6819 | 6051 | Code changed |
| SRC3       V_1 Angle | 6824 | 6056 | Code changed |
| SRC3       V_1 Mag | 6822 | 6054 | Code changed |
| SRC3       V_2 Angle | 6827 | 6059 | Code changed |
| SRC3       V_2 Mag | 6825 | 6057 | Code changed |
| SRC3       Va Harm[10 ] | 8223 | 8223 | Identical |
| SRC3       Va Harm[11 ] | 8224 | 8224 | Identical |
| SRC3       Va Harm[12 ] | 8225 | 8225 | Identical |
| SRC3       Va Harm[13 ] | 8226 | 8226 | Identical |
| SRC3       Va Harm[14 ] | 8227 | 8227 | Identical |
| SRC3       Va Harm[15 ] | 8228 | 8228 | Identical |
| SRC3       Va Harm[16 ] | 8229 | 8229 | Identical |
| SRC3       Va Harm[17 ] | 8230 | 8230 | Identical |
| SRC3       Va Harm[18 ] | 8231 | 8231 | Identical |
| SRC3       Va Harm[19 ] | 8232 | 8232 | Identical |
| SRC3       Va Harm[2 ] | 8215 | 8215 | Identical |
| SRC3       Va Harm[20 ] | 8233 | 8233 | Identical |
| SRC3       Va Harm[21 ] | 8234 | 8234 | Identical |
| SRC3       Va Harm[22 ] | 8235 | 8235 | Identical |
| SRC3       Va Harm[23 ] | 8236 | 8236 | Identical |
| SRC3       Va Harm[24 ] | 8237 | 8237 | Identical |
| SRC3       Va Harm[25 ] | 8238 | 8238 | Identical |
| SRC3       Va Harm[3 ] | 8216 | 8216 | Identical |
| SRC3       Va Harm[4 ] | 8217 | 8217 | Identical |
| SRC3       Va Harm[5 ] | 8218 | 8218 | Identical |
| SRC3       Va Harm[6 ] | 8219 | 8219 | Identical |
| SRC3       Va Harm[7 ] | 8220 | 8220 | Identical |
| SRC3       Va Harm[8 ] | 8221 | 8221 | Identical |
| SRC3       Va Harm[9 ] | 8222 | 8222 | Identical |
| SRC3       Va THD | 8214 | 8214 | Identical |
| SRC3       Vab Angle | 6807 | 6039 | Code changed |
| SRC3       Vab Mag | 6805 | 6037 | Code changed |
| SRC3       Vab RMS | 6799 | 6031 | Code changed |
| SRC3       Vag Angle | 6792 | 6024 | Code changed |
| SRC3       Vag Mag | 6790 | 6022 | Code changed |
| SRC3       Vag RMS | 6784 | 6016 | Code changed |
| SRC3       Vb Harm[10 ] | 8248 | 8248 | Identical |
| SRC3       Vb Harm[11 ] | 8249 | 8249 | Identical |
| SRC3       Vb Harm[12 ] | 8250 | 8250 | Identical |
| SRC3       Vb Harm[13 ] | 8251 | 8251 | Identical |
| SRC3       Vb Harm[14 ] | 8252 | 8252 | Identical |
| SRC3       Vb Harm[15 ] | 8253 | 8253 | Identical |
| SRC3       Vb Harm[16 ] | 8254 | 8254 | Identical |
| SRC3       Vb Harm[17 ] | 8255 | 8255 | Identical |
| SRC3       Vb Harm[18 ] | 8256 | 8256 | Identical |
| SRC3       Vb Harm[19 ] | 8257 | 8257 | Identical |
| SRC3       Vb Harm[2 ] | 8240 | 8240 | Identical |
| SRC3       Vb Harm[20 ] | 8258 | 8258 | Identical |
| SRC3       Vb Harm[21 ] | 8259 | 8259 | Identical |
| SRC3       Vb Harm[22 ] | 8260 | 8260 | Identical |
| SRC3       Vb Harm[23 ] | 8261 | 8261 | Identical |
| SRC3       Vb Harm[24 ] | 8262 | 8262 | Identical |
| SRC3       Vb Harm[25 ] | 8263 | 8263 | Identical |
| SRC3       Vb Harm[3 ] | 8241 | 8241 | Identical |
| SRC3       Vb Harm[4 ] | 8242 | 8242 | Identical |
| SRC3       Vb Harm[5 ] | 8243 | 8243 | Identical |
| SRC3       Vb Harm[6 ] | 8244 | 8244 | Identical |
| SRC3       Vb Harm[7 ] | 8245 | 8245 | Identical |
| SRC3       Vb Harm[8 ] | 8246 | 8246 | Identical |
| SRC3       Vb Harm[9 ] | 8247 | 8247 | Identical |
| SRC3       Vb THD | 8239 | 8239 | Identical |
| SRC3       Vbc Angle | 6810 | 6042 | Code changed |
| SRC3       Vbc Mag | 6808 | 6040 | Code changed |
| SRC3       Vbc RMS | 6801 | 6033 | Code changed |
| SRC3       Vbg Angle | 6795 | 6027 | Code changed |
| SRC3       Vbg Mag | 6793 | 6025 | Code changed |
| SRC3       Vbg RMS | 6786 | 6018 | Code changed |
| SRC3       Vc Harm[10 ] | 8273 | 8273 | Identical |
| SRC3       Vc Harm[11 ] | 8274 | 8274 | Identical |
| SRC3       Vc Harm[12 ] | 8275 | 8275 | Identical |
| SRC3       Vc Harm[13 ] | 8276 | 8276 | Identical |
| SRC3       Vc Harm[14 ] | 8277 | 8277 | Identical |
| SRC3       Vc Harm[15 ] | 8278 | 8278 | Identical |
| SRC3       Vc Harm[16 ] | 8279 | 8279 | Identical |
| SRC3       Vc Harm[17 ] | 8280 | 8280 | Identical |
| SRC3       Vc Harm[18 ] | 8281 | 8281 | Identical |
| SRC3       Vc Harm[19 ] | 8282 | 8282 | Identical |
| SRC3       Vc Harm[2 ] | 8265 | 8265 | Identical |
| SRC3       Vc Harm[20 ] | 8283 | 8283 | Identical |
| SRC3       Vc Harm[21 ] | 8284 | 8284 | Identical |
| SRC3       Vc Harm[22 ] | 8285 | 8285 | Identical |
| SRC3       Vc Harm[23 ] | 8286 | 8286 | Identical |
| SRC3       Vc Harm[24 ] | 8287 | 8287 | Identical |
| SRC3       Vc Harm[25 ] | 8288 | 8288 | Identical |
| SRC3       Vc Harm[3 ] | 8266 | 8266 | Identical |
| SRC3       Vc Harm[4 ] | 8267 | 8267 | Identical |
| SRC3       Vc Harm[5 ] | 8268 | 8268 | Identical |
| SRC3       Vc Harm[6 ] | 8269 | 8269 | Identical |
| SRC3       Vc Harm[7 ] | 8270 | 8270 | Identical |
| SRC3       Vc Harm[8 ] | 8271 | 8271 | Identical |
| SRC3       Vc Harm[9 ] | 8272 | 8272 | Identical |
| SRC3       Vc THD | 8264 | 8264 | Identical |
| SRC3       Vca Angle | 6813 | 6045 | Code changed |
| SRC3       Vca Mag | 6811 | 6043 | Code changed |
| SRC3       Vca RMS | 6803 | 6035 | Code changed |
| SRC3       Vcg Angle | 6798 | 6030 | Code changed |
| SRC3       Vcg Mag | 6796 | 6028 | Code changed |
| SRC3       Vcg RMS | 6788 | 6020 | Code changed |
| SRC3       Vx Angle | 6818 | 6050 | Code changed |
| SRC3       Vx Mag | 6816 | 6048 | Code changed |
| SRC3       Vx RMS | 6814 | 6046 | Code changed |
| SRC4       Demand Ia | - | 7728 | G60 only |
| SRC4       Demand Ib | - | 7730 | G60 only |
| SRC4       Demand Ic | - | 7732 | G60 only |
| SRC4       Demand VA | - | 7738 | G60 only |
| SRC4       Demand var | - | 7736 | G60 only |
| SRC4       Demand Watt | - | 7734 | G60 only |
| SRC4       Frequency | 7558 | 7558 | Identical |
| SRC4       I_0 Angle | 6363 | 20530 | Code changed |
| SRC4       I_0 Mag | 6361 | 20528 | Code changed |
| SRC4       I_1 Angle | 6366 | 20533 | Code changed |
| SRC4       I_1 Mag | 6364 | 20531 | Code changed |
| SRC4       I_2 Angle | 6369 | 20536 | Code changed |
| SRC4       I_2 Mag | 6367 | 20534 | Code changed |
| SRC4       Ia Angle | 6346 | 20513 | Code changed |
| SRC4       Ia Harm[10 ] | 10546 | 10546 | Identical |
| SRC4       Ia Harm[11 ] | 10547 | 10547 | Identical |
| SRC4       Ia Harm[12 ] | 10548 | 10548 | Identical |
| SRC4       Ia Harm[13 ] | 10549 | 10549 | Identical |
| SRC4       Ia Harm[14 ] | 10550 | 10550 | Identical |
| SRC4       Ia Harm[15 ] | 10551 | 10551 | Identical |
| SRC4       Ia Harm[16 ] | 10552 | 10552 | Identical |
| SRC4       Ia Harm[17 ] | 10553 | 10553 | Identical |
| SRC4       Ia Harm[18 ] | 10554 | 10554 | Identical |
| SRC4       Ia Harm[19 ] | 10555 | 10555 | Identical |
| SRC4       Ia Harm[2 ] | 10538 | 10538 | Identical |
| SRC4       Ia Harm[20 ] | 10556 | 10556 | Identical |
| SRC4       Ia Harm[21 ] | 10557 | 10557 | Identical |
| SRC4       Ia Harm[22 ] | 10558 | 10558 | Identical |
| SRC4       Ia Harm[23 ] | 10559 | 10559 | Identical |
| SRC4       Ia Harm[24 ] | 10560 | 10560 | Identical |
| SRC4       Ia Harm[25 ] | 10561 | 10561 | Identical |
| SRC4       Ia Harm[3 ] | 10539 | 10539 | Identical |
| SRC4       Ia Harm[4 ] | 10540 | 10540 | Identical |
| SRC4       Ia Harm[5 ] | 10541 | 10541 | Identical |
| SRC4       Ia Harm[6 ] | 10542 | 10542 | Identical |
| SRC4       Ia Harm[7 ] | 10543 | 10543 | Identical |
| SRC4       Ia Harm[8 ] | 10544 | 10544 | Identical |
| SRC4       Ia Harm[9 ] | 10545 | 10545 | Identical |
| SRC4       Ia Mag | 6344 | 20511 | Code changed |
| SRC4       Ia RMS | 6336 | 20503 | Code changed |
| SRC4       Ia THD | 10537 | 10537 | Identical |
| SRC4       Ib Angle | 6349 | 20516 | Code changed |
| SRC4       Ib Harm[10 ] | 10579 | 10579 | Identical |
| SRC4       Ib Harm[11 ] | 10580 | 10580 | Identical |
| SRC4       Ib Harm[12 ] | 10581 | 10581 | Identical |
| SRC4       Ib Harm[13 ] | 10582 | 10582 | Identical |
| SRC4       Ib Harm[14 ] | 10583 | 10583 | Identical |
| SRC4       Ib Harm[15 ] | 10584 | 10584 | Identical |
| SRC4       Ib Harm[16 ] | 10585 | 10585 | Identical |
| SRC4       Ib Harm[17 ] | 10586 | 10586 | Identical |
| SRC4       Ib Harm[18 ] | 10587 | 10587 | Identical |
| SRC4       Ib Harm[19 ] | 10588 | 10588 | Identical |
| SRC4       Ib Harm[2 ] | 10571 | 10571 | Identical |
| SRC4       Ib Harm[20 ] | 10589 | 10589 | Identical |
| SRC4       Ib Harm[21 ] | 10590 | 10590 | Identical |
| SRC4       Ib Harm[22 ] | 10591 | 10591 | Identical |
| SRC4       Ib Harm[23 ] | 10592 | 10592 | Identical |
| SRC4       Ib Harm[24 ] | 10593 | 10593 | Identical |
| SRC4       Ib Harm[25 ] | 10594 | 10594 | Identical |
| SRC4       Ib Harm[3 ] | 10572 | 10572 | Identical |
| SRC4       Ib Harm[4 ] | 10573 | 10573 | Identical |
| SRC4       Ib Harm[5 ] | 10574 | 10574 | Identical |
| SRC4       Ib Harm[6 ] | 10575 | 10575 | Identical |
| SRC4       Ib Harm[7 ] | 10576 | 10576 | Identical |
| SRC4       Ib Harm[8 ] | 10577 | 10577 | Identical |
| SRC4       Ib Harm[9 ] | 10578 | 10578 | Identical |
| SRC4       Ib Mag | 6347 | 20514 | Code changed |
| SRC4       Ib RMS | 6338 | 20505 | Code changed |
| SRC4       Ib THD | 10570 | 10570 | Identical |
| SRC4       Ic Angle | 6352 | 20519 | Code changed |
| SRC4       Ic Harm[10 ] | 10612 | 10612 | Identical |
| SRC4       Ic Harm[11 ] | 10613 | 10613 | Identical |
| SRC4       Ic Harm[12 ] | 10614 | 10614 | Identical |
| SRC4       Ic Harm[13 ] | 10615 | 10615 | Identical |
| SRC4       Ic Harm[14 ] | 10616 | 10616 | Identical |
| SRC4       Ic Harm[15 ] | 10617 | 10617 | Identical |
| SRC4       Ic Harm[16 ] | 10618 | 10618 | Identical |
| SRC4       Ic Harm[17 ] | 10619 | 10619 | Identical |
| SRC4       Ic Harm[18 ] | 10620 | 10620 | Identical |
| SRC4       Ic Harm[19 ] | 10621 | 10621 | Identical |
| SRC4       Ic Harm[2 ] | 10604 | 10604 | Identical |
| SRC4       Ic Harm[20 ] | 10622 | 10622 | Identical |
| SRC4       Ic Harm[21 ] | 10623 | 10623 | Identical |
| SRC4       Ic Harm[22 ] | 10624 | 10624 | Identical |
| SRC4       Ic Harm[23 ] | 10625 | 10625 | Identical |
| SRC4       Ic Harm[24 ] | 10626 | 10626 | Identical |
| SRC4       Ic Harm[25 ] | 10627 | 10627 | Identical |
| SRC4       Ic Harm[3 ] | 10605 | 10605 | Identical |
| SRC4       Ic Harm[4 ] | 10606 | 10606 | Identical |
| SRC4       Ic Harm[5 ] | 10607 | 10607 | Identical |
| SRC4       Ic Harm[6 ] | 10608 | 10608 | Identical |
| SRC4       Ic Harm[7 ] | 10609 | 10609 | Identical |
| SRC4       Ic Harm[8 ] | 10610 | 10610 | Identical |
| SRC4       Ic Harm[9 ] | 10611 | 10611 | Identical |
| SRC4       Ic Mag | 6350 | 20517 | Code changed |
| SRC4       Ic RMS | 6340 | 20507 | Code changed |
| SRC4       Ic THD | 10603 | 10603 | Identical |
| SRC4       Ig Angle | 6360 | 20527 | Code changed |
| SRC4       Ig Mag | 6358 | 20525 | Code changed |
| SRC4       Ig RMS | 6356 | 20523 | Code changed |
| SRC4       Igd Angle | 6372 | 22161 | Code changed |
| SRC4       Igd Mag | 6370 | 22159 | Code changed |
| SRC4       In Angle | 6355 | 20522 | Code changed |
| SRC4       In Mag | 6353 | 20520 | Code changed |
| SRC4       In RMS | 6342 | 20509 | Code changed |
| SRC4       Neg varh | 7478 | 7478 | Identical |
| SRC4       Neg Watthour | 7474 | 7474 | Identical |
| SRC4       P | 7264 | 7008 | Code changed |
| SRC4       Pa | 7266 | 7010 | Code changed |
| SRC4       Pb | 7268 | 7012 | Code changed |
| SRC4       Pc | 7270 | 7014 | Code changed |
| SRC4       PF | 7288 | 7032 | Code changed |
| SRC4       Phase A PF | 7289 | 7033 | Code changed |
| SRC4       Phase B PF | 7290 | 7034 | Code changed |
| SRC4       Phase C PF | 7291 | 7035 | Code changed |
| SRC4       Pos varh | 7476 | 7476 | Identical |
| SRC4       Pos Watthour | 7472 | 7472 | Identical |
| SRC4       Q | 7272 | 7016 | Code changed |
| SRC4       Qa | 7274 | 7018 | Code changed |
| SRC4       Qb | 7276 | 7020 | Code changed |
| SRC4       Qc | 7278 | 7022 | Code changed |
| SRC4       S | 7280 | 7024 | Code changed |
| SRC4       Sa | 7282 | 7026 | Code changed |
| SRC4       Sb | 7284 | 7028 | Code changed |
| SRC4       Sc | 7286 | 7030 | Code changed |
| SRC4       V_0 Angle | 6885 | 6117 | Code changed |
| SRC4       V_0 Mag | 6883 | 6115 | Code changed |
| SRC4       V_1 Angle | 6888 | 6120 | Code changed |
| SRC4       V_1 Mag | 6886 | 6118 | Code changed |
| SRC4       V_2 Angle | 6891 | 6123 | Code changed |
| SRC4       V_2 Mag | 6889 | 6121 | Code changed |
| SRC4       Va Harm[10 ] | 8298 | 8298 | Identical |
| SRC4       Va Harm[11 ] | 8299 | 8299 | Identical |
| SRC4       Va Harm[12 ] | 8300 | 8300 | Identical |
| SRC4       Va Harm[13 ] | 8301 | 8301 | Identical |
| SRC4       Va Harm[14 ] | 8302 | 8302 | Identical |
| SRC4       Va Harm[15 ] | 8303 | 8303 | Identical |
| SRC4       Va Harm[16 ] | 8304 | 8304 | Identical |
| SRC4       Va Harm[17 ] | 8305 | 8305 | Identical |
| SRC4       Va Harm[18 ] | 8306 | 8306 | Identical |
| SRC4       Va Harm[19 ] | 8307 | 8307 | Identical |
| SRC4       Va Harm[2 ] | 8290 | 8290 | Identical |
| SRC4       Va Harm[20 ] | 8308 | 8308 | Identical |
| SRC4       Va Harm[21 ] | 8309 | 8309 | Identical |
| SRC4       Va Harm[22 ] | 8310 | 8310 | Identical |
| SRC4       Va Harm[23 ] | 8311 | 8311 | Identical |
| SRC4       Va Harm[24 ] | 8312 | 8312 | Identical |
| SRC4       Va Harm[25 ] | 8313 | 8313 | Identical |
| SRC4       Va Harm[3 ] | 8291 | 8291 | Identical |
| SRC4       Va Harm[4 ] | 8292 | 8292 | Identical |
| SRC4       Va Harm[5 ] | 8293 | 8293 | Identical |
| SRC4       Va Harm[6 ] | 8294 | 8294 | Identical |
| SRC4       Va Harm[7 ] | 8295 | 8295 | Identical |
| SRC4       Va Harm[8 ] | 8296 | 8296 | Identical |
| SRC4       Va Harm[9 ] | 8297 | 8297 | Identical |
| SRC4       Va THD | 8289 | 8289 | Identical |
| SRC4       Vab Angle | 6871 | 6103 | Code changed |
| SRC4       Vab Mag | 6869 | 6101 | Code changed |
| SRC4       Vab RMS | 6863 | 6095 | Code changed |
| SRC4       Vag Angle | 6856 | 6088 | Code changed |
| SRC4       Vag Mag | 6854 | 6086 | Code changed |
| SRC4       Vag RMS | 6848 | 6080 | Code changed |
| SRC4       Vb Harm[10 ] | 8323 | 8323 | Identical |
| SRC4       Vb Harm[11 ] | 8324 | 8324 | Identical |
| SRC4       Vb Harm[12 ] | 8325 | 8325 | Identical |
| SRC4       Vb Harm[13 ] | 8326 | 8326 | Identical |
| SRC4       Vb Harm[14 ] | 8327 | 8327 | Identical |
| SRC4       Vb Harm[15 ] | 8328 | 8328 | Identical |
| SRC4       Vb Harm[16 ] | 8329 | 8329 | Identical |
| SRC4       Vb Harm[17 ] | 8330 | 8330 | Identical |
| SRC4       Vb Harm[18 ] | 8331 | 8331 | Identical |
| SRC4       Vb Harm[19 ] | 8332 | 8332 | Identical |
| SRC4       Vb Harm[2 ] | 8315 | 8315 | Identical |
| SRC4       Vb Harm[20 ] | 8333 | 8333 | Identical |
| SRC4       Vb Harm[21 ] | 8334 | 8334 | Identical |
| SRC4       Vb Harm[22 ] | 8335 | 8335 | Identical |
| SRC4       Vb Harm[23 ] | 8336 | 8336 | Identical |
| SRC4       Vb Harm[24 ] | 8337 | 8337 | Identical |
| SRC4       Vb Harm[25 ] | 8338 | 8338 | Identical |
| SRC4       Vb Harm[3 ] | 8316 | 8316 | Identical |
| SRC4       Vb Harm[4 ] | 8317 | 8317 | Identical |
| SRC4       Vb Harm[5 ] | 8318 | 8318 | Identical |
| SRC4       Vb Harm[6 ] | 8319 | 8319 | Identical |
| SRC4       Vb Harm[7 ] | 8320 | 8320 | Identical |
| SRC4       Vb Harm[8 ] | 8321 | 8321 | Identical |
| SRC4       Vb Harm[9 ] | 8322 | 8322 | Identical |
| SRC4       Vb THD | 8314 | 8314 | Identical |
| SRC4       Vbc Angle | 6874 | 6106 | Code changed |
| SRC4       Vbc Mag | 6872 | 6104 | Code changed |
| SRC4       Vbc RMS | 6865 | 6097 | Code changed |
| SRC4       Vbg Angle | 6859 | 6091 | Code changed |
| SRC4       Vbg Mag | 6857 | 6089 | Code changed |
| SRC4       Vbg RMS | 6850 | 6082 | Code changed |
| SRC4       Vc Harm[10 ] | 8348 | 8348 | Identical |
| SRC4       Vc Harm[11 ] | 8349 | 8349 | Identical |
| SRC4       Vc Harm[12 ] | 8350 | 8350 | Identical |
| SRC4       Vc Harm[13 ] | 8351 | 8351 | Identical |
| SRC4       Vc Harm[14 ] | 8352 | 8352 | Identical |
| SRC4       Vc Harm[15 ] | 8353 | 8353 | Identical |
| SRC4       Vc Harm[16 ] | 8354 | 8354 | Identical |
| SRC4       Vc Harm[17 ] | 8355 | 8355 | Identical |
| SRC4       Vc Harm[18 ] | 8356 | 8356 | Identical |
| SRC4       Vc Harm[19 ] | 8357 | 8357 | Identical |
| SRC4       Vc Harm[2 ] | 8340 | 8340 | Identical |
| SRC4       Vc Harm[20 ] | 8358 | 8358 | Identical |
| SRC4       Vc Harm[21 ] | 8359 | 8359 | Identical |
| SRC4       Vc Harm[22 ] | 8360 | 8360 | Identical |
| SRC4       Vc Harm[23 ] | 8361 | 8361 | Identical |
| SRC4       Vc Harm[24 ] | 8362 | 8362 | Identical |
| SRC4       Vc Harm[25 ] | 8363 | 8363 | Identical |
| SRC4       Vc Harm[3 ] | 8341 | 8341 | Identical |
| SRC4       Vc Harm[4 ] | 8342 | 8342 | Identical |
| SRC4       Vc Harm[5 ] | 8343 | 8343 | Identical |
| SRC4       Vc Harm[6 ] | 8344 | 8344 | Identical |
| SRC4       Vc Harm[7 ] | 8345 | 8345 | Identical |
| SRC4       Vc Harm[8 ] | 8346 | 8346 | Identical |
| SRC4       Vc Harm[9 ] | 8347 | 8347 | Identical |
| SRC4       Vc THD | 8339 | 8339 | Identical |
| SRC4       Vca Angle | 6877 | 6109 | Code changed |
| SRC4       Vca Mag | 6875 | 6107 | Code changed |
| SRC4       Vca RMS | 6867 | 6099 | Code changed |
| SRC4       Vcg Angle | 6862 | 6094 | Code changed |
| SRC4       Vcg Mag | 6860 | 6092 | Code changed |
| SRC4       Vcg RMS | 6852 | 6084 | Code changed |
| SRC4       Vx Angle | 6882 | 6114 | Code changed |
| SRC4       Vx Mag | 6880 | 6112 | Code changed |
| SRC4       Vx RMS | 6878 | 6110 | Code changed |
| Stat Gnd Resistance | - | 5756 | G60 only |
| Stator Diff CT Prim. | - | 5740 | G60 only |
| Stator Diff Iad | - | 5728 | G60 only |
| Stator Diff Ibd | - | 5732 | G60 only |
| Stator Diff Icd | - | 5736 | G60 only |
| Stator Gnd V0 3rd | 5748 | 5748 | Identical |
| Stator Gnd Vn 3rd | 5744 | 5744 | Identical |
| Stator Gnd Vn+V0 3rd | 5746 | 5746 | Identical |
| Stator Rest Iar | - | 5730 | G60 only |
| Stator Rest Ibr | - | 5734 | G60 only |
| Stator Rest Icr | - | 5738 | G60 only |
| Synchchk 1 Delta F | 10852 | 10852 | Identical |
| Synchchk 1 Delta Phs | 10850 | 10850 | Identical |
| Synchchk 1 Delta V | 10848 | 10848 | Identical |
| Synchchk 1 SSCP DPh | 10851 | 10851 | Identical |
| Synchchk 1 SSCP DPh' | 10863 | 10863 | Identical |
| Synchchk 1 V1 Ang | 10855 | 10855 | Identical |
| Synchchk 1 V1 Mag | 10853 | 10853 | Identical |
| Synchchk 1 V2 Ang | 10858 | 10858 | Identical |
| Synchchk 1 V2' Ang | 10861 | 10861 | Identical |
| Synchchk 1 V2 Mag | 10856 | 10856 | Identical |
| Synchchk 1 V2' Mag | 10859 | 10859 | Identical |
| Synchchk 2 Delta F | 10868 | 10868 | Identical |
| Synchchk 2 Delta Phs | 10866 | 10866 | Identical |
| Synchchk 2 Delta V | 10864 | 10864 | Identical |
| Synchchk 2 SSCP DPh | 10867 | 10867 | Identical |
| Synchchk 2 SSCP DPh' | 10879 | 10879 | Identical |
| Synchchk 2 V1 Ang | 10871 | 10871 | Identical |
| Synchchk 2 V1 Mag | 10869 | 10869 | Identical |
| Synchchk 2 V2 Ang | 10874 | 10874 | Identical |
| Synchchk 2 V2' Ang | 10877 | 10877 | Identical |
| Synchchk 2 V2 Mag | 10872 | 10872 | Identical |
| Synchchk 2 V2' Mag | 10875 | 10875 | Identical |
| Synchchk 3 Delta F | 10884 | 10884 | Identical |
| Synchchk 3 Delta Phs | 10882 | 10882 | Identical |
| Synchchk 3 Delta V | 10880 | 10880 | Identical |
| Synchchk 3 SSCP DPh | 10883 | 10883 | Identical |
| Synchchk 3 SSCP DPh' | 10895 | 10895 | Identical |
| Synchchk 3 V1 Ang | 10887 | 10887 | Identical |
| Synchchk 3 V1 Mag | 10885 | 10885 | Identical |
| Synchchk 3 V2 Ang | 10890 | 10890 | Identical |
| Synchchk 3 V2' Ang | 10893 | 10893 | Identical |
| Synchchk 3 V2 Mag | 10888 | 10888 | Identical |
| Synchchk 3 V2' Mag | 10891 | 10891 | Identical |
| Synchchk 4 Delta F | 10900 | 10900 | Identical |
| Synchchk 4 Delta Phs | 10898 | 10898 | Identical |
| Synchchk 4 Delta V | 10896 | 10896 | Identical |
| Synchchk 4 SSCP DPh | 10899 | 10899 | Identical |
| Synchchk 4 SSCP DPh' | 10911 | 10911 | Identical |
| Synchchk 4 V1 Ang | 10903 | 10903 | Identical |
| Synchchk 4 V1 Mag | 10901 | 10901 | Identical |
| Synchchk 4 V2 Ang | 10906 | 10906 | Identical |
| Synchchk 4 V2' Ang | 10909 | 10909 | Identical |
| Synchchk 4 V2 Mag | 10904 | 10904 | Identical |
| Synchchk 4 V2' Mag | 10907 | 10907 | Identical |
| Synchck 1 Delta Ph' | 10862 | 10862 | Identical |
| Synchck 2 Delta Ph' | 10878 | 10878 | Identical |
| Synchck 3 Delta Ph' | 10894 | 10894 | Identical |
| Synchck 4 Delta Ph' | 10910 | 10910 | Identical |
| Tracking Frequency | 32768 | 32768 | Identical |
| V0 3rd Harmonic 1 | 41138 | 41138 | Identical |
| V0 3rd Harmonic 2 | 41140 | 41140 | Identical |
| V0 3rd Harmonic 3 | 41142 | 41142 | Identical |
| V0 3rd Harmonic 4 | 41144 | 41144 | Identical |
| Volts Per Hertz 1 | 42400 | 42400 | Identical |
| Volts Per Hertz 2 | 42401 | 42401 | Identical |
| Xfmr acc LOL | 9013 | - | G30 only |
| Xfmr agng fctr | 9010 | - | G30 only |
| Xfmr daily LOL | 9011 | - | G30 only |
| Xfmr Harm2 Iad Angle | 8966 | - | G30 only |
| Xfmr Harm2 Iad Mag | 8965 | - | G30 only |
| Xfmr Harm2 Ibd Angle | 8974 | - | G30 only |
| Xfmr Harm2 Ibd Mag | 8973 | - | G30 only |
| Xfmr Harm2 Icd Angle | 8982 | - | G30 only |
| Xfmr Harm2 Icd Mag | 8981 | - | G30 only |
| Xfmr Harm5 Iad Angle | 8968 | - | G30 only |
| Xfmr Harm5 Iad Mag | 8967 | - | G30 only |
| Xfmr Harm5 Ibd Angle | 8976 | - | G30 only |
| Xfmr Harm5 Ibd Mag | 8975 | - | G30 only |
| Xfmr Harm5 Icd Angle | 8984 | - | G30 only |
| Xfmr Harm5 Icd Mag | 8983 | - | G30 only |
| Xfmr hst-spot tC | 9009 | - | G30 only |
| Xfmr Iad Angle | 8962 | - | G30 only |
| Xfmr Iad Mag | 8961 | - | G30 only |
| Xfmr Iar Angle | 8964 | - | G30 only |
| Xfmr Iar Mag | 8963 | - | G30 only |
| Xfmr Ibd Angle | 8970 | - | G30 only |
| Xfmr Ibd Mag | 8969 | - | G30 only |
| Xfmr Ibr Angle | 8972 | - | G30 only |
| Xfmr Ibr Mag | 8971 | - | G30 only |
| Xfmr Icd Angle | 8978 | - | G30 only |
| Xfmr Icd Mag | 8977 | - | G30 only |
| Xfmr Icr Angle | 8980 | - | G30 only |
| Xfmr Icr Mag | 8979 | - | G30 only |
| Xfmr Ref Winding | 8960 | - | G30 only |
| Xfmr top-oil tC | 9008 | - | G30 only |

---

## Setting-specific enum tables (FormatIndex != 10012/10013)

These tables provide dropdown choices for `SettingType="Enum"` registers.
The converter copies G30 `value` + `EnumValue` but **always keeps** the G60 `EnumFormatIndex`.

FormatIndex numbers differ between G30 7.x and G60 8.x even when the dropdown choices are logically the same.
Tables below are listed in full per file.

### G30 - all setting enum tables

### G30 FormatIndex 6386 (2 entries)

| Code | Name |
|------|------|
| 0 | Disabled |
| 1 | Enabled |

### G30 FormatIndex 6385 (4 entries)

| Code | Name |
|------|------|
| 0 | 25 % |
| 1 | 50 % |
| 2 | 75 % |
| 3 | 100 % |

### G30 FormatIndex 6395 (12 entries)

| Code | Name |
|------|------|
| 0 | 300 |
| 1 | 1200 |
| 2 | 2400 |
| 3 | 4800 |
| 4 | 9600 |
| 5 | 19200 |
| 6 | 38400 |
| 7 | 57600 |
| 8 | 115200 |
| 9 | 14400 |
| 10 | 28800 |
| 11 | 33600 |

### G30 FormatIndex 6396 (3 entries)

| Code | Name |
|------|------|
| 0 | None |
| 1 | Odd |
| 2 | Even |

### G30 FormatIndex 6643 (2 entries)

| Code | Name |
|------|------|
| 0 | 19200 |
| 1 | 115200 |

### G30 FormatIndex 6635 (3 entries)

| Code | Name |
|------|------|
| 0 | None |
| 1 | Failover |
| 2 | PRP |

### G30 FormatIndex 6637 (2 entries)

| Code | Name |
|------|------|
| 0 | DNP 3.0 |
| 1 | IEC 60870-5-104 |

### G30 FormatIndex 6458 (6 entries)

| Code | Name |
|------|------|
| 0 | NONE |
| 1 | COM1 - RS485 |
| 2 | COM2 - RS485 |
| 3 | FRONT PANEL - RS232 |
| 4 | NETWORK - TCP |
| 5 | NETWORK - UDP |

### G30 FormatIndex 6666 (12 entries)

| Code | Name |
|------|------|
| 0 | 0.01 |
| 1 | 0.1 |
| 2 | 1 |
| 3 | 10 |
| 4 | 100 |
| 5 | 1000 |
| 6 | 10000 |
| 7 | 100000 |
| 8 | 0.001 |
| 9 | 1000000 |
| 10 | 10000000 |
| 11 | 100000000 |

### G30 FormatIndex 6645 (2 entries)

| Code | Name |
|------|------|
| 0 | UTC |
| 1 | LOCAL |

### G30 FormatIndex 6585 (4 entries)

| Code | Name |
|------|------|
| 0 | 1 |
| 1 | 2 |
| 2 | 5 |
| 3 | 6 |

### G30 FormatIndex 6586 (4 entries)

| Code | Name |
|------|------|
| 0 | 1 |
| 1 | 2 |
| 2 | 9 |
| 3 | 10 |

### G30 FormatIndex 6587 (6 entries)

| Code | Name |
|------|------|
| 0 | 1 |
| 1 | 2 |
| 2 | 3 |
| 3 | 4 |
| 4 | 5 |
| 5 | 7 |

### G30 FormatIndex 6408 (2 entries)

| Code | Name |
|------|------|
| 0 | No |
| 1 | Yes |

### G30 FormatIndex 6397 (3 entries)

| Code | Name |
|------|------|
| 0 | None |
| 1 | DC Shift |
| 2 | Amplitude Modulated |

### G30 FormatIndex 6498 (12 entries)

| Code | Name |
|------|------|
| 0 | January |
| 1 | February |
| 2 | March |
| 3 | April |
| 4 | May |
| 5 | June |
| 6 | July |
| 7 | August |
| 8 | September |
| 9 | October |
| 10 | November |
| 11 | December |

### G30 FormatIndex 6499 (7 entries)

| Code | Name |
|------|------|
| 0 | Sunday |
| 1 | Monday |
| 2 | Tuesday |
| 3 | Wednesday |
| 4 | Thursday |
| 5 | Friday |
| 6 | Saturday |

### G30 FormatIndex 6500 (5 entries)

| Code | Name |
|------|------|
| 0 | First |
| 1 | Second |
| 2 | Third |
| 3 | Fourth |
| 4 | Last |

### G30 FormatIndex 6401 (2 entries)

| Code | Name |
|------|------|
| 0 | Automatic Overwrite |
| 1 | Protected |

### G30 FormatIndex 6464 (5 entries)

| Code | Name |
|------|------|
| 0 | Off |
| 1 | 8 samples/cycle |
| 2 | 16 samples/cycle |
| 3 | 32 samples/cycle |
| 4 | 64 samples/cycle |

### G30 FormatIndex 6521 (2 entries)

| Code | Name |
|------|------|
| 0 | Continuous |
| 1 | Trigger |

### G30 FormatIndex 6409 (2 entries)

| Code | Name |
|------|------|
| 0 | Latched |
| 1 | Self-Reset |

### G30 FormatIndex 6405 (2 entries)

| Code | Name |
|------|------|
| 0 | 1 A |
| 1 | 5 A |

### G30 FormatIndex 6384 (2 entries)

| Code | Name |
|------|------|
| 0 | Wye |
| 1 | Delta |

### G30 FormatIndex 6447 (7 entries)

| Code | Name |
|------|------|
| 0 | Vn |
| 1 | Vag |
| 2 | Vbg |
| 3 | Vcg |
| 4 | Vab |
| 5 | Vbc |
| 6 | Vca |

### G30 FormatIndex 6390 (2 entries)

| Code | Name |
|------|------|
| 0 | ABC |
| 1 | ACB |

### G30 FormatIndex 6448 (4 entries)

| Code | Name |
|------|------|
| 0 | Util (SRC 1) |
| 1 | Gen (SRC 2) |
| 2 | Load (SRC 3) |
| 3 | Sync (SRC 4) |

### G30 FormatIndex 6 (4 entries)

| Code | Name |
|------|------|
| 0 | None |
| 1 | F1 |
| 4 | M1 |
| 5 | F1+M1 |

### G30 FormatIndex 10014 (3 entries)

| Code | Name |
|------|------|
| 0 | None |
| 2 | F5 |
| 8 | M5 |

### G30 FormatIndex 10010 (3 entries)

| Code | Name |
|------|------|
| 0 | Automatic Selection |
| 1 | Winding 1 |
| 2 | Winding 2 |

### G30 FormatIndex 6441 (2 entries)

| Code | Name |
|------|------|
| 0 | Internal (software) |
| 1 | External (with CTs) |

### G30 FormatIndex 6444 (3 entries)

| Code | Name |
|------|------|
| 0 | Wye |
| 1 | Delta |
| 2 | Zig-zag |

### G30 FormatIndex 6445 (2 entries)

| Code | Name |
|------|------|
| 0 | Not within zone |
| 1 | Within zone |

### G30 FormatIndex 10015 (5 entries)

| Code | Name |
|------|------|
| 0 | dcma Input 1 |
| 1 | dcma Input 2 |
| 2 | dcma Input 3 |
| 3 | dcma Input 4 |
| 4 | Monthly Average |

### G30 FormatIndex 10016 (5 entries)

| Code | Name |
|------|------|
| 0 | dcma Input 1 |
| 1 | dcma Input 2 |
| 2 | dcma Input 3 |
| 3 | dcma Input 4 |
| 4 | Computed |

### G30 FormatIndex 6438 (2 entries)

| Code | Name |
|------|------|
| 0 | 3-Pole |
| 1 | 1-Pole |

### G30 FormatIndex 6411 (3 entries)

| Code | Name |
|------|------|
| 0 | millisecond |
| 1 | second |
| 2 | minute |

### G30 FormatIndex 6577 (2 entries)

| Code | Name |
|------|------|
| 0 | SIGNED |
| 1 | ABSOLUTE |

### G30 FormatIndex 6578 (2 entries)

| Code | Name |
|------|------|
| 0 | LEVEL |
| 1 | DELTA |

### G30 FormatIndex 6579 (2 entries)

| Code | Name |
|------|------|
| 0 | OVER |
| 1 | UNDER |

### G30 FormatIndex 6580 (3 entries)

| Code | Name |
|------|------|
| 0 | Milliseconds |
| 1 | Seconds |
| 2 | Minutes |

### G30 FormatIndex 6392 (3 entries)

| Code | Name |
|------|------|
| 0 | Self-reset |
| 1 | Latched |
| 2 | Disabled |

### G30 FormatIndex 6581 (2 entries)

| Code | Name |
|------|------|
| 0 | Reset Dominant |
| 1 | Set Dominant |

### G30 FormatIndex 6449 (3 entries)

| Code | Name |
|------|------|
| 0 | Disabled |
| 1 | Adapt. 2nd |
| 2 | Trad. 2nd |

### G30 FormatIndex 6470 (4 entries)

| Code | Name |
|------|------|
| 0 | Per phase |
| 1 | 2-out-of-3 |
| 2 | Average |
| 3 | 1-out-of-3 |

### G30 FormatIndex 6450 (2 entries)

| Code | Name |
|------|------|
| 0 | Disabled |
| 1 | 5th |

### G30 FormatIndex 6404 (2 entries)

| Code | Name |
|------|------|
| 0 | Phasor |
| 1 | RMS |

### G30 FormatIndex 6387 (17 entries)

| Code | Name |
|------|------|
| 0 | IEEE Mod Inv |
| 1 | IEEE Very Inv |
| 2 | IEEE Ext Inv |
| 3 | IEC Curve A |
| 4 | IEC Curve B |
| 5 | IEC Curve C |
| 6 | IEC Short Inv |
| 7 | IAC Ext Inv |
| 8 | IAC Very Inv |
| 9 | IAC Inverse |
| 10 | IAC Short Inv |
| 11 | I2t |
| 12 | Definite Time |
| 13 | Flexcurve A |
| 14 | Flexcurve B |
| 15 | Flexcurve C |
| 16 | Flexcurve D |

### G30 FormatIndex 6388 (2 entries)

| Code | Name |
|------|------|
| 0 | Instantaneous |
| 1 | Timed |

### G30 FormatIndex 6491 (5 entries)

| Code | Name |
|------|------|
| 0 | Voltage |
| 1 | Current |
| 2 | Dual |
| 3 | Dual-V |
| 4 | Dual-I |

### G30 FormatIndex 6492 (2 entries)

| Code | Name |
|------|------|
| 0 | Calculated V0 |
| 1 | Measured VX |

### G30 FormatIndex 6477 (2 entries)

| Code | Name |
|------|------|
| 0 | Calculated 3I0 |
| 1 | Measured IG |

### G30 FormatIndex 6486 (2 entries)

| Code | Name |
|------|------|
| 0 | Over |
| 1 | Over-Under |

### G30 FormatIndex 6460 (2 entries)

| Code | Name |
|------|------|
| 0 | Neg Sequence |
| 1 | Zero Sequence |

### G30 FormatIndex 6467 (2 entries)

| Code | Name |
|------|------|
| 0 | Phase to Ground |
| 1 | Phase to Phase |

### G30 FormatIndex 6394 (2 entries)

| Code | Name |
|------|------|
| 0 | Definite Time |
| 1 | Inverse Time |

### G30 FormatIndex 6399 (4 entries)

| Code | Name |
|------|------|
| 0 | Definite Time |
| 1 | Flexcurve A |
| 2 | Flexcurve B |
| 3 | Flexcurve C |

### G30 FormatIndex 6501 (8 entries)

| Code | Name |
|------|------|
| 0 | Definite Time |
| 1 | Inverse A |
| 2 | Inverse B |
| 3 | Inverse C |
| 4 | Flexcurve A |
| 5 | Flexcurve B |
| 6 | Flexcurve C |
| 7 | Flexcurve D |

### G30 FormatIndex 6474 (2 entries)

| Code | Name |
|------|------|
| 0 | UV AND OFFLINE |
| 1 | UV OR OFFLINE |

### G30 FormatIndex 6367 (2 entries)

| Code | Name |
|------|------|
| 0 | Time-out |
| 1 | Acknowledge |

### G30 FormatIndex 6368 (3 entries)

| Code | Name |
|------|------|
| 0 | Restore |
| 1 | Synchronize |
| 2 | Sync/Restore |

### G30 FormatIndex 6457 (6 entries)

| Code | Name |
|------|------|
| 0 | None |
| 1 | LV1 and DV2 |
| 2 | DV1 and LV2 |
| 3 | DV1 or DV2 |
| 4 | DV1 Xor DV2 |
| 5 | DV1 and DV2 |

### G30 FormatIndex 6485 (3 entries)

| Code | Name |
|------|------|
| 0 | Increasing |
| 1 | Decreasing |
| 2 | Bidirectional |

### G30 FormatIndex 6410 (4 entries)

| Code | Name |
|------|------|
| 0 | 17 Vdc |
| 1 | 33 Vdc |
| 2 | 84 Vdc |
| 3 | 166 Vdc |

### G30 FormatIndex 6454 (7 entries)

| Code | Name |
|------|------|
| 0 | 0 to -1 mA |
| 1 | 0 to 1 mA |
| 2 | -1 to 1 mA |
| 3 | 0 to 5 mA |
| 4 | 0 to 10 mA |
| 5 | 0 to 20 mA |
| 6 | 4 to 20 mA |

### G30 FormatIndex 6584 (3 entries)

| Code | Name |
|------|------|
| 0 | -1 to 1 mA |
| 1 | 0 to 1 mA |
| 2 | 4 to 20 mA |

### G60 Base - all setting enum tables

### G60 FormatIndex 9779 (2 entries)

| Code | Name |
|------|------|
| 0 | Disabled |
| 1 | Enabled |

### G60 FormatIndex 9778 (4 entries)

| Code | Name |
|------|------|
| 0 | 25 % |
| 1 | 50 % |
| 2 | 75 % |
| 3 | 100 % |

### G60 FormatIndex 10021 (4 entries)

| Code | Name |
|------|------|
| 0 | RS485 |
| 1 | RRTD |
| 2 | GPM-F |
| 3 | RRTD & GPM-F |

### G60 FormatIndex 9789 (12 entries)

| Code | Name |
|------|------|
| 0 | 300 |
| 1 | 1200 |
| 2 | 2400 |
| 3 | 4800 |
| 4 | 9600 |
| 5 | 19200 |
| 6 | 38400 |
| 7 | 57600 |
| 8 | 115200 |
| 9 | 14400 |
| 10 | 28800 |
| 11 | 33600 |

### G60 FormatIndex 9790 (3 entries)

| Code | Name |
|------|------|
| 0 | None |
| 1 | Odd |
| 2 | Even |

### G60 FormatIndex 10051 (2 entries)

| Code | Name |
|------|------|
| 0 | 19200 |
| 1 | 115200 |

### G60 FormatIndex 10043 (3 entries)

| Code | Name |
|------|------|
| 0 | None |
| 1 | Failover |
| 2 | PRP |

### G60 FormatIndex 10045 (2 entries)

| Code | Name |
|------|------|
| 0 | DNP 3.0 |
| 1 | IEC 60870-5-104 |

### G60 FormatIndex 9852 (6 entries)

| Code | Name |
|------|------|
| 0 | NONE |
| 1 | COM1 - RS485 |
| 2 | COM2 - RS485 |
| 3 | FRONT PANEL - RS232 |
| 4 | NETWORK - TCP |
| 5 | NETWORK - UDP |

### G60 FormatIndex 10074 (12 entries)

| Code | Name |
|------|------|
| 0 | 0.01 |
| 1 | 0.1 |
| 2 | 1 |
| 3 | 10 |
| 4 | 100 |
| 5 | 1000 |
| 6 | 10000 |
| 7 | 100000 |
| 8 | 0.001 |
| 9 | 1000000 |
| 10 | 10000000 |
| 11 | 100000000 |

### G60 FormatIndex 10053 (2 entries)

| Code | Name |
|------|------|
| 0 | UTC |
| 1 | LOCAL |

### G60 FormatIndex 9994 (4 entries)

| Code | Name |
|------|------|
| 0 | 1 |
| 1 | 2 |
| 2 | 5 |
| 3 | 6 |

### G60 FormatIndex 9995 (4 entries)

| Code | Name |
|------|------|
| 0 | 1 |
| 1 | 2 |
| 2 | 9 |
| 3 | 10 |

### G60 FormatIndex 9996 (6 entries)

| Code | Name |
|------|------|
| 0 | 1 |
| 1 | 2 |
| 2 | 3 |
| 3 | 4 |
| 4 | 5 |
| 5 | 7 |

### G60 FormatIndex 9802 (2 entries)

| Code | Name |
|------|------|
| 0 | No |
| 1 | Yes |

### G60 FormatIndex 9791 (3 entries)

| Code | Name |
|------|------|
| 0 | None |
| 1 | DC Shift |
| 2 | Amplitude Modulated |

### G60 FormatIndex 9784 (2 entries)

| Code | Name |
|------|------|
| 0 | Local Time Settings |
| 1 | IRIG-B Time |

### G60 FormatIndex 9893 (12 entries)

| Code | Name |
|------|------|
| 0 | January |
| 1 | February |
| 2 | March |
| 3 | April |
| 4 | May |
| 5 | June |
| 6 | July |
| 7 | August |
| 8 | September |
| 9 | October |
| 10 | November |
| 11 | December |

### G60 FormatIndex 9894 (7 entries)

| Code | Name |
|------|------|
| 0 | Sunday |
| 1 | Monday |
| 2 | Tuesday |
| 3 | Wednesday |
| 4 | Thursday |
| 5 | Friday |
| 6 | Saturday |

### G60 FormatIndex 9895 (5 entries)

| Code | Name |
|------|------|
| 0 | First |
| 1 | Second |
| 2 | Third |
| 3 | Fourth |
| 4 | Last |

### G60 FormatIndex 9795 (2 entries)

| Code | Name |
|------|------|
| 0 | Automatic Overwrite |
| 1 | Protected |

### G60 FormatIndex 9858 (5 entries)

| Code | Name |
|------|------|
| 0 | Off |
| 1 | 8 samples/cycle |
| 2 | 16 samples/cycle |
| 3 | 32 samples/cycle |
| 4 | 64 samples/cycle |

### G60 FormatIndex 9915 (2 entries)

| Code | Name |
|------|------|
| 0 | Continuous |
| 1 | Trigger |

### G60 FormatIndex 9815 (3 entries)

| Code | Name |
|------|------|
| 0 | Thermal Exponential |
| 1 | Block Interval |
| 2 | Rolling Demand |

### G60 FormatIndex 9808 (6 entries)

| Code | Name |
|------|------|
| 0 | 5 MIN |
| 1 | 10 MIN |
| 2 | 15 MIN |
| 3 | 20 MIN |
| 4 | 30 MIN |
| 5 | 60 MIN |

### G60 FormatIndex 9803 (2 entries)

| Code | Name |
|------|------|
| 0 | Latched |
| 1 | Self-Reset |

### G60 FormatIndex 9799 (2 entries)

| Code | Name |
|------|------|
| 0 | 1 A |
| 1 | 5 A |

### G60 FormatIndex 9920 (5 entries)

| Code | Name |
|------|------|
| 0 | Standard |
| 1 | Inverted-3Ph |
| 2 | Inverted Ph-A |
| 3 | Inverted Ph-B |
| 4 | Inverted Ph-C |

### G60 FormatIndex 9921 (2 entries)

| Code | Name |
|------|------|
| 0 | Standard |
| 1 | Inverted |

### G60 FormatIndex 9777 (2 entries)

| Code | Name |
|------|------|
| 0 | Wye |
| 1 | Delta |

### G60 FormatIndex 9841 (7 entries)

| Code | Name |
|------|------|
| 0 | Vn |
| 1 | Vag |
| 2 | Vbg |
| 3 | Vcg |
| 4 | Vab |
| 5 | Vbc |
| 6 | Vca |

### G60 FormatIndex 9783 (2 entries)

| Code | Name |
|------|------|
| 0 | ABC |
| 1 | ACB |

### G60 FormatIndex 9842 (4 entries)

| Code | Name |
|------|------|
| 0 | SRC 1 (SRC 1) |
| 1 | SRC 2 (SRC 2) |
| 2 | SRC 3 (SRC 3) |
| 3 | SRC 4 (SRC 4) |

### G60 FormatIndex 9931 (5 entries)

| Code | Name |
|------|------|
| 0 | AUTO |
| 1 | 3PH_VT |
| 2 | 1PH_VT |
| 3 | 3PH_CT |
| 4 | 1PH_CT |

### G60 FormatIndex 9875 (5 entries)

| Code | Name |
|------|------|
| 0 | None |
| 1 | SRC 1 (SRC 1) |
| 2 | SRC 2 (SRC 2) |
| 3 | SRC 3 (SRC 3) |
| 4 | SRC 4 (SRC 4) |

### G60 FormatIndex 9932 (4 entries)

| Code | Name |
|------|------|
| 0 | 3PH_VT |
| 1 | 1PH_VT |
| 2 | 3PH_CT |
| 3 | 1PH_CT |

### G60 FormatIndex 6 (4 entries)

| Code | Name |
|------|------|
| 0 | None |
| 1 | F1 |
| 4 | M1 |
| 5 | F1+M1 |

### G60 FormatIndex 10075 (3 entries)

| Code | Name |
|------|------|
| 0 | None |
| 2 | F5 |
| 8 | M5 |

### G60 FormatIndex 9929 (2 entries)

| Code | Name |
|------|------|
| 0 | Common |
| 1 | Distinct |

### G60 FormatIndex 9832 (2 entries)

| Code | Name |
|------|------|
| 0 | 3-Pole |
| 1 | 1-Pole |

### G60 FormatIndex 10118 (129 entries)

| Code | Name |
|------|------|
| 0 | OFF |
| 1 | RxGOOSE DPS 1 |
| 2 | RxGOOSE DPS 2 |
| 3 | RxGOOSE DPS 3 |
| 4 | RxGOOSE DPS 4 |
| 5 | RxGOOSE DPS 5 |
| 6 | RxGOOSE DPS 6 |
| 7 | RxGOOSE DPS 7 |
| 8 | RxGOOSE DPS 8 |
| 9 | RxGOOSE DPS 9 |
| 10 | RxGOOSE DPS 10 |
| 11 | RxGOOSE DPS 11 |
| 12 | RxGOOSE DPS 12 |
| 13 | RxGOOSE DPS 13 |
| 14 | RxGOOSE DPS 14 |
| 15 | RxGOOSE DPS 15 |
| 16 | RxGOOSE DPS 16 |
| 17 | RxGOOSE DPS 17 |
| 18 | RxGOOSE DPS 18 |
| 19 | RxGOOSE DPS 19 |
| 20 | RxGOOSE DPS 20 |
| 21 | RxGOOSE DPS 21 |
| 22 | RxGOOSE DPS 22 |
| 23 | RxGOOSE DPS 23 |
| 24 | RxGOOSE DPS 24 |
| 25 | RxGOOSE DPS 25 |
| 26 | RxGOOSE DPS 26 |
| 27 | RxGOOSE DPS 27 |
| 28 | RxGOOSE DPS 28 |
| 29 | RxGOOSE DPS 29 |
| 30 | RxGOOSE DPS 30 |
| 31 | RxGOOSE DPS 31 |
| 32 | RxGOOSE DPS 32 |
| 33 | RxGOOSE DPS 33 |
| 34 | RxGOOSE DPS 34 |
| 35 | RxGOOSE DPS 35 |
| 36 | RxGOOSE DPS 36 |
| 37 | RxGOOSE DPS 37 |
| 38 | RxGOOSE DPS 38 |
| 39 | RxGOOSE DPS 39 |
| 40 | RxGOOSE DPS 40 |
| 41 | RxGOOSE DPS 41 |
| 42 | RxGOOSE DPS 42 |
| 43 | RxGOOSE DPS 43 |
| 44 | RxGOOSE DPS 44 |
| 45 | RxGOOSE DPS 45 |
| 46 | RxGOOSE DPS 46 |
| 47 | RxGOOSE DPS 47 |
| 48 | RxGOOSE DPS 48 |
| 49 | RxGOOSE DPS 49 |
| 50 | RxGOOSE DPS 50 |
| 51 | RxGOOSE DPS 51 |
| 52 | RxGOOSE DPS 52 |
| 53 | RxGOOSE DPS 53 |
| 54 | RxGOOSE DPS 54 |
| 55 | RxGOOSE DPS 55 |
| 56 | RxGOOSE DPS 56 |
| 57 | RxGOOSE DPS 57 |
| 58 | RxGOOSE DPS 58 |
| 59 | RxGOOSE DPS 59 |
| 60 | RxGOOSE DPS 60 |
| 61 | RxGOOSE DPS 61 |
| 62 | RxGOOSE DPS 62 |
| 63 | RxGOOSE DPS 63 |
| 64 | RxGOOSE DPS 64 |
| 65 | RxGOOSE DPS 65 |
| 66 | RxGOOSE DPS 66 |
| 67 | RxGOOSE DPS 67 |
| 68 | RxGOOSE DPS 68 |
| 69 | RxGOOSE DPS 69 |
| 70 | RxGOOSE DPS 70 |
| 71 | RxGOOSE DPS 71 |
| 72 | RxGOOSE DPS 72 |
| 73 | RxGOOSE DPS 73 |
| 74 | RxGOOSE DPS 74 |
| 75 | RxGOOSE DPS 75 |
| 76 | RxGOOSE DPS 76 |
| 77 | RxGOOSE DPS 77 |
| 78 | RxGOOSE DPS 78 |
| 79 | RxGOOSE DPS 79 |
| 80 | RxGOOSE DPS 80 |
| 81 | RxGOOSE DPS 81 |
| 82 | RxGOOSE DPS 82 |
| 83 | RxGOOSE DPS 83 |
| 84 | RxGOOSE DPS 84 |
| 85 | RxGOOSE DPS 85 |
| 86 | RxGOOSE DPS 86 |
| 87 | RxGOOSE DPS 87 |
| 88 | RxGOOSE DPS 88 |
| 89 | RxGOOSE DPS 89 |
| 90 | RxGOOSE DPS 90 |
| 91 | RxGOOSE DPS 91 |
| 92 | RxGOOSE DPS 92 |
| 93 | RxGOOSE DPS 93 |
| 94 | RxGOOSE DPS 94 |
| 95 | RxGOOSE DPS 95 |
| 96 | RxGOOSE DPS 96 |
| 97 | RxGOOSE DPS 97 |
| 98 | RxGOOSE DPS 98 |
| 99 | RxGOOSE DPS 99 |
| 100 | RxGOOSE DPS 100 |
| 101 | RxGOOSE DPS 101 |
| 102 | RxGOOSE DPS 102 |
| 103 | RxGOOSE DPS 103 |
| 104 | RxGOOSE DPS 104 |
| 105 | RxGOOSE DPS 105 |
| 106 | RxGOOSE DPS 106 |
| 107 | RxGOOSE DPS 107 |
| 108 | RxGOOSE DPS 108 |
| 109 | RxGOOSE DPS 109 |
| 110 | RxGOOSE DPS 110 |
| 111 | RxGOOSE DPS 111 |
| 112 | RxGOOSE DPS 112 |
| 113 | RxGOOSE DPS 113 |
| 114 | RxGOOSE DPS 114 |
| 115 | RxGOOSE DPS 115 |
| 116 | RxGOOSE DPS 116 |
| 117 | RxGOOSE DPS 117 |
| 118 | RxGOOSE DPS 118 |
| 119 | RxGOOSE DPS 119 |
| 120 | RxGOOSE DPS 120 |
| 121 | RxGOOSE DPS 121 |
| 122 | RxGOOSE DPS 122 |
| 123 | RxGOOSE DPS 123 |
| 124 | RxGOOSE DPS 124 |
| 125 | RxGOOSE DPS 125 |
| 126 | RxGOOSE DPS 126 |
| 127 | RxGOOSE DPS 127 |
| 128 | RxGOOSE DPS 128 |

### G60 FormatIndex 9805 (3 entries)

| Code | Name |
|------|------|
| 0 | millisecond |
| 1 | second |
| 2 | minute |

### G60 FormatIndex 9986 (2 entries)

| Code | Name |
|------|------|
| 0 | SIGNED |
| 1 | ABSOLUTE |

### G60 FormatIndex 9987 (2 entries)

| Code | Name |
|------|------|
| 0 | LEVEL |
| 1 | DELTA |

### G60 FormatIndex 9988 (2 entries)

| Code | Name |
|------|------|
| 0 | OVER |
| 1 | UNDER |

### G60 FormatIndex 9989 (3 entries)

| Code | Name |
|------|------|
| 0 | Milliseconds |
| 1 | Seconds |
| 2 | Minutes |

### G60 FormatIndex 9786 (3 entries)

| Code | Name |
|------|------|
| 0 | Self-reset |
| 1 | Latched |
| 2 | Disabled |

### G60 FormatIndex 9990 (2 entries)

| Code | Name |
|------|------|
| 0 | Reset Dominant |
| 1 | Set Dominant |

### G60 FormatIndex 9829 (3 entries)

| Code | Name |
|------|------|
| 0 | Forward |
| 1 | Reverse |
| 2 | Non-directional |

### G60 FormatIndex 9797 (2 entries)

| Code | Name |
|------|------|
| 0 | Mho |
| 1 | Quad |

### G60 FormatIndex 9828 (13 entries)

| Code | Name |
|------|------|
| 0 | None |
| 1 | Dy1 |
| 2 | Dy3 |
| 3 | Dy5 |
| 4 | Dy7 |
| 5 | Dy9 |
| 6 | Dy11 |
| 7 | Yd1 |
| 8 | Yd3 |
| 9 | Yd5 |
| 10 | Yd7 |
| 11 | Yd9 |
| 12 | Yd11 |

### G60 FormatIndex 9762 (2 entries)

| Code | Name |
|------|------|
| 0 | Mho Shape |
| 1 | Quad Shape |

### G60 FormatIndex 9984 (2 entries)

| Code | Name |
|------|------|
| 0 | Two Step |
| 1 | Three Step |

### G60 FormatIndex 9985 (2 entries)

| Code | Name |
|------|------|
| 0 | Delayed |
| 1 | Early |

### G60 FormatIndex 9798 (2 entries)

| Code | Name |
|------|------|
| 0 | Phasor |
| 1 | RMS |

### G60 FormatIndex 9780 (17 entries)

| Code | Name |
|------|------|
| 0 | IEEE Mod Inv |
| 1 | IEEE Very Inv |
| 2 | IEEE Ext Inv |
| 3 | IEC Curve A |
| 4 | IEC Curve B |
| 5 | IEC Curve C |
| 6 | IEC Short Inv |
| 7 | IAC Ext Inv |
| 8 | IAC Very Inv |
| 9 | IAC Inverse |
| 10 | IAC Short Inv |
| 11 | I2t |
| 12 | Definite Time |
| 13 | Flexcurve A |
| 14 | Flexcurve B |
| 15 | Flexcurve C |
| 16 | Flexcurve D |

### G60 FormatIndex 9781 (2 entries)

| Code | Name |
|------|------|
| 0 | Instantaneous |
| 1 | Timed |

### G60 FormatIndex 9886 (5 entries)

| Code | Name |
|------|------|
| 0 | Voltage |
| 1 | Current |
| 2 | Dual |
| 3 | Dual-V |
| 4 | Dual-I |

### G60 FormatIndex 9887 (2 entries)

| Code | Name |
|------|------|
| 0 | Calculated V0 |
| 1 | Measured VX |

### G60 FormatIndex 9871 (2 entries)

| Code | Name |
|------|------|
| 0 | Calculated 3I0 |
| 1 | Measured IG |

### G60 FormatIndex 9881 (2 entries)

| Code | Name |
|------|------|
| 0 | Over |
| 1 | Over-Under |

### G60 FormatIndex 9854 (2 entries)

| Code | Name |
|------|------|
| 0 | Neg Sequence |
| 1 | Zero Sequence |

### G60 FormatIndex 9861 (2 entries)

| Code | Name |
|------|------|
| 0 | Phase to Ground |
| 1 | Phase to Phase |

### G60 FormatIndex 9788 (6 entries)

| Code | Name |
|------|------|
| 0 | Definite Time |
| 1 | Inverse Time |
| 2 | FlexCurve A |
| 3 | FlexCurve B |
| 4 | FlexCurve C |
| 5 | FlexCurve D |

### G60 FormatIndex 9793 (4 entries)

| Code | Name |
|------|------|
| 0 | Definite Time |
| 1 | Flexcurve A |
| 2 | Flexcurve B |
| 3 | Flexcurve C |

### G60 FormatIndex 9896 (8 entries)

| Code | Name |
|------|------|
| 0 | Definite Time |
| 1 | Inverse A |
| 2 | Inverse B |
| 3 | Inverse C |
| 4 | Flexcurve A |
| 5 | Flexcurve B |
| 6 | Flexcurve C |
| 7 | Flexcurve D |

### G60 FormatIndex 9868 (2 entries)

| Code | Name |
|------|------|
| 0 | UV AND OFFLINE |
| 1 | UV OR OFFLINE |

### G60 FormatIndex 9826 (49 entries)

| Code | Name |
|------|------|
| 0 | NONE |
| 1 | RTD 1 |
| 2 | RTD 2 |
| 3 | RTD 3 |
| 4 | RTD 4 |
| 5 | RTD 5 |
| 6 | RTD 6 |
| 7 | RTD 7 |
| 8 | RTD 8 |
| 9 | RTD 9 |
| 10 | RTD 10 |
| 11 | RTD 11 |
| 12 | RTD 12 |
| 13 | RTD 13 |
| 14 | RTD 14 |
| 15 | RTD 15 |
| 16 | RTD 16 |
| 17 | RTD 17 |
| 18 | RTD 18 |
| 19 | RTD 19 |
| 20 | RTD 20 |
| 21 | RTD 21 |
| 22 | RTD 22 |
| 23 | RTD 23 |
| 24 | RTD 24 |
| 25 | RTD 25 |
| 26 | RTD 26 |
| 27 | RTD 27 |
| 28 | RTD 28 |
| 29 | RTD 29 |
| 30 | RTD 30 |
| 31 | RTD 31 |
| 32 | RTD 32 |
| 33 | RTD 33 |
| 34 | RTD 34 |
| 35 | RTD 35 |
| 36 | RTD 36 |
| 37 | RTD 37 |
| 38 | RTD 38 |
| 39 | RTD 39 |
| 40 | RTD 40 |
| 41 | RTD 41 |
| 42 | RTD 42 |
| 43 | RTD 43 |
| 44 | RTD 44 |
| 45 | RTD 45 |
| 46 | RTD 46 |
| 47 | RTD 47 |
| 48 | RTD 48 |

### G60 FormatIndex 9760 (2 entries)

| Code | Name |
|------|------|
| 0 | Time-out |
| 1 | Acknowledge |

### G60 FormatIndex 9761 (3 entries)

| Code | Name |
|------|------|
| 0 | Restore |
| 1 | Synchronize |
| 2 | Sync/Restore |

### G60 FormatIndex 10117 (7 entries)

| Code | Name |
|------|------|
| 0 | Auto |
| 1 | Vag |
| 2 | Vbg |
| 3 | Vcg |
| 4 | Vab |
| 5 | Vbc |
| 6 | Vca |

### G60 FormatIndex 9851 (6 entries)

| Code | Name |
|------|------|
| 0 | None |
| 1 | LV1 and DV2 |
| 2 | DV1 and LV2 |
| 3 | DV1 or DV2 |
| 4 | DV1 Xor DV2 |
| 5 | DV1 and DV2 |

### G60 FormatIndex 10112 (2 entries)

| Code | Name |
|------|------|
| 0 | 3-PHASE |
| 1 | 1-PHASE |

### G60 FormatIndex 10096 (6 entries)

| Code | Name |
|------|------|
| 0 | DC |
| 1 | 2nd |
| 2 | 3rd |
| 3 | 4th |
| 4 | 5th |
| 5 | THD |

### G60 FormatIndex 10103 (4 entries)

| Code | Name |
|------|------|
| 0 | ANY ONE |
| 1 | ANY TWO |
| 2 | ALL THREE |
| 3 | AVERAGE |

### G60 FormatIndex 9880 (3 entries)

| Code | Name |
|------|------|
| 0 | Increasing |
| 1 | Decreasing |
| 2 | Bidirectional |

### G60 FormatIndex 9804 (4 entries)

| Code | Name |
|------|------|
| 0 | 17 Vdc |
| 1 | 33 Vdc |
| 2 | 84 Vdc |
| 3 | 166 Vdc |

### G60 FormatIndex 9848 (7 entries)

| Code | Name |
|------|------|
| 0 | 0 to -1 mA |
| 1 | 0 to 1 mA |
| 2 | -1 to 1 mA |
| 3 | 0 to 5 mA |
| 4 | 0 to 10 mA |
| 5 | 0 to 20 mA |
| 6 | 4 to 20 mA |

### G60 FormatIndex 9993 (3 entries)

| Code | Name |
|------|------|
| 0 | -1 to 1 mA |
| 1 | 0 to 1 mA |
| 2 | 4 to 20 mA |

### G60 FormatIndex 10092 (3 entries)

| Code | Name |
|------|------|
| 1 | On |
| 3 | Test |
| 4 | Test Blocked |

---

## Source file metadata

| | G30 Publix 1367 | G60 Base |
|---|-----------------|----------|
| version | 760 | 860 |
| orderCode | G30-U00-HCL-F8L-H6P-M8L-P5A-UXX-WXX | G60-V00-HKL-F8L-H6P-M8L-P5A |
| URSetupVersion | 8.71 | 8.71 |
