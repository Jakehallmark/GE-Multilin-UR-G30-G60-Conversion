function Read-UrXml($path) {
    $raw = [System.IO.File]::ReadAllBytes($path)
    if ($raw.Length -ge 2 -and $raw[0] -eq 0xFF -and $raw[1] -eq 0xFE) {
        return [System.Text.Encoding]::Unicode.GetString($raw)
    }
    if ($raw.Length -ge 2 -and $raw[0] -eq 0x3C -and $raw[1] -eq 0x00) {
        return [System.Text.Encoding]::Unicode.GetString($raw)
    }
    return [System.Text.Encoding]::UTF8.GetString($raw)
}

function Parse-EnumItems($items) {
    $entries = [ordered]@{}
    if (-not $items) { return $entries }
    foreach ($entry in ($items -split ';')) {
        $entry = $entry.Trim()
        if (-not $entry) { continue }
        $spaceIdx = $entry.IndexOf(' ')
        if ($spaceIdx -lt 1) { continue }
        $code = $entry.Substring(0, $spaceIdx)
        $name = $entry.Substring($spaceIdx + 1).Trim()
        if (-not ($code -match '^\d+$')) { continue }
        if (-not $entries.Contains($code)) { $entries[$code] = $name }
    }
    return $entries
}

function Get-AllTables($path) {
    [xml]$xml = Read-UrXml $path
    $tables = [ordered]@{}
    foreach ($el in $xml.SelectNodes('//EnumType')) {
        $idx = $el.GetAttribute('FormatIndex')
        if (-not $idx) { $idx = '(none)' }
        $key = $idx
        $n = 1
        while ($tables.Contains($key)) { $key = "$idx#$n"; $n++ }
        $items = $el.GetAttribute('Items')
        $tables[$key] = [PSCustomObject]@{
            FormatIndex = $idx
            Items       = $items
            Entries     = Parse-EnumItems $items
            Parent      = $el.ParentNode.GetAttribute('screenName')
        }
    }
    return $tables
}

function Escape-Md($s) {
    if ($null -eq $s) { return '' }
    return ($s -replace '\|', '\|')
}

function Get-TableRole($idx, $entryCount) {
    switch ($idx) {
        '10012' { return 'Logic / Flex operand dictionary (contacts, VOs, protection outputs, FlexLogic tokens)' }
        '10013' { return 'Signal / measurement operand dictionary (SRC1 Ia RMS, SRC1 P, etc.)' }
        '10010' { return 'Small flex-related enum' }
        '10014' { return 'Auxiliary enum' }
        '10015' { return 'Auxiliary enum' }
        '10016' { return 'Auxiliary enum' }
        '10118' { return 'Large G60-specific enum (130 entries)' }
        default {
            if ($entryCount -gt 100) { return 'Large firmware enum table' }
            return 'Setting-specific enum (dropdown choices for registers)'
        }
    }
}

function Write-OperandComparison($sb, [string]$title, $g30Entries, $g60Entries, [string[]]$notes) {
    [void]$sb.AppendLine('')
    [void]$sb.AppendLine("## $title")
    [void]$sb.AppendLine('')
    foreach ($note in $notes) {
        [void]$sb.AppendLine($note)
    }
    if ($notes.Count -gt 0) { [void]$sb.AppendLine('') }

    $g30Names = @{}
    foreach ($kv in $g30Entries.GetEnumerator()) { $g30Names[$kv.Value] = $kv.Key }
    $g60Names = @{}
    foreach ($kv in $g60Entries.GetEnumerator()) { $g60Names[$kv.Value] = $kv.Key }

    $allNames = [System.Collections.Generic.SortedSet[string]]::new()
    foreach ($n in $g30Names.Keys) { [void]$allNames.Add($n) }
    foreach ($n in $g60Names.Keys) { [void]$allNames.Add($n) }

    $same = 0; $renamed = 0; $g30only = 0; $g60only = 0
    foreach ($name in $allNames) {
        $inG30 = $g30Names.ContainsKey($name)
        $inG60 = $g60Names.ContainsKey($name)
        if ($inG30 -and $inG60) {
            if ($g30Names[$name] -eq $g60Names[$name]) { $same++ } else { $renamed++ }
        }
        elseif ($inG30) { $g30only++ }
        else { $g60only++ }
    }

    [void]$sb.AppendLine('### Summary')
    [void]$sb.AppendLine('')
    [void]$sb.AppendLine('| Metric | Count |')
    [void]$sb.AppendLine('|--------|------:|')
    [void]$sb.AppendLine("| G30 entries | $($g30Entries.Count) |")
    [void]$sb.AppendLine("| G60 entries | $($g60Entries.Count) |")
    [void]$sb.AppendLine("| Same name **and** same code | $same |")
    [void]$sb.AppendLine("| Same name, **different code** | $renamed |")
    [void]$sb.AppendLine("| G30 only (name absent on G60) | $g30only |")
    [void]$sb.AppendLine("| G60 only (name absent on G30) | $g60only |")
    [void]$sb.AppendLine('')
    [void]$sb.AppendLine('### Full entry comparison')
    [void]$sb.AppendLine('')
    [void]$sb.AppendLine('| Name | G30 Code | G60 Code | Status |')
    [void]$sb.AppendLine('|------|----------|----------|--------|')
    foreach ($name in $allNames) {
        $c30 = if ($g30Names.ContainsKey($name)) { $g30Names[$name] } else { '-' }
        $c60 = if ($g60Names.ContainsKey($name)) { $g60Names[$name] } else { '-' }
        $status = if ($c30 -eq '-') { 'G60 only' }
        elseif ($c60 -eq '-') { 'G30 only' }
        elseif ($c30 -eq $c60) { 'Identical' }
        else { 'Code changed' }
        [void]$sb.AppendLine("| $(Escape-Md $name) | $c30 | $c60 | $status |")
    }
}

function Write-FullTable($sb, [string]$heading, $table) {
    [void]$sb.AppendLine("### $heading")
    [void]$sb.AppendLine('')
    [void]$sb.AppendLine('| Code | Name |')
    [void]$sb.AppendLine('|------|------|')
    foreach ($kv in ($table.Entries.GetEnumerator() | Sort-Object { [int64]$_.Key })) {
        [void]$sb.AppendLine("| $($kv.Key) | $(Escape-Md $kv.Value) |")
    }
    [void]$sb.AppendLine('')
}

$repoRoot = if ($PSScriptRoot) { Split-Path $PSScriptRoot -Parent } else { Get-Location }
$g30Path  = Join-Path $repoRoot 'Publix Store 1367 Firmware7-6_208V4000A (from EXPORT 9-9-15) 3-20-18.xml'
$g60Path  = Join-Path $repoRoot 'G60 Base.xml'
$outPath  = Join-Path $repoRoot 'FIRMWARE_TABLES.md'

if (-not (Test-Path $g30Path)) { throw "G30 file not found: $g30Path" }
if (-not (Test-Path $g60Path)) { throw "G60 Base not found: $g60Path" }

$g30Tables = Get-AllTables $g30Path
$g60Tables = Get-AllTables $g60Path
[xml]$g30x = Read-UrXml $g30Path
[xml]$g60x = Read-UrXml $g60Path

$sb = New-Object System.Text.StringBuilder
[void]$sb.AppendLine('# GE Multilin UR Firmware Enum Tables - G30 vs G60 Comparison')
[void]$sb.AppendLine('')
[void]$sb.AppendLine('> Auto-generated reference comparing every `EnumType` table embedded in:')
[void]$sb.AppendLine('> - **G30 source:** Publix Store 1367 (firmware 7.6x)')
[void]$sb.AppendLine('> - **G60 template:** G60 Base (firmware 8.6x)')
[void]$sb.AppendLine('')
[void]$sb.AppendLine('Regenerate: `powershell -File tools/generate_firmware_tables.ps1`')
[void]$sb.AppendLine('')
[void]$sb.AppendLine('---')
[void]$sb.AppendLine('')
[void]$sb.AppendLine('## How tables work in UR Setup XML')
[void]$sb.AppendLine('')
[void]$sb.AppendLine('Each `<EnumType FormatIndex="..." Items="..."/>` element embeds a firmware enum dictionary.')
[void]$sb.AppendLine('Entries are semicolon-delimited: `code name` (e.g. `7168 SRC1       P`).')
[void]$sb.AppendLine('')
[void]$sb.AppendLine('| Table | Purpose in conversion |')
[void]$sb.AppendLine('|-------|----------------------|')
[void]$sb.AppendLine('| **10012** | Flex operand remapping - logic, contacts, VOs, protection element outputs |')
[void]$sb.AppendLine('| **10013** | Signal operand remapping - measurements; user-display Item code lookup |')
[void]$sb.AppendLine('| **Other FormatIndex values** | Dropdown enums for `SettingType="Enum"` registers |')
[void]$sb.AppendLine('')
[void]$sb.AppendLine('**Key difference:** FormatIndex numbers change between firmware generations for setting-specific enums.')
[void]$sb.AppendLine('Only **10012** and **10013** keep the same FormatIndex across G30 7.x and G60 8.x.')
[void]$sb.AppendLine('')
[void]$sb.AppendLine('---')
[void]$sb.AppendLine('')
[void]$sb.AppendLine('## Table inventory')
[void]$sb.AppendLine('')

$g30Total = ($g30Tables.Values | ForEach-Object { $_.Entries.Count } | Measure-Object -Sum).Sum
$g60Total = ($g60Tables.Values | ForEach-Object { $_.Entries.Count } | Measure-Object -Sum).Sum
[void]$sb.AppendLine('| Source | EnumType count | Total entries |')
[void]$sb.AppendLine('|--------|---------------:|--------------:|')
[void]$sb.AppendLine("| G30 Publix 1367 | $($g30Tables.Count) | $g30Total |")
[void]$sb.AppendLine("| G60 Base | $($g60Tables.Count) | $g60Total |")
[void]$sb.AppendLine('')

[void]$sb.AppendLine('### G30 tables')
[void]$sb.AppendLine('')
[void]$sb.AppendLine('| FormatIndex | Entries | Role |')
[void]$sb.AppendLine('|-------------|--------:|------|')
foreach ($t in $g30Tables.Values) {
    $role = Get-TableRole $t.FormatIndex $t.Entries.Count
    [void]$sb.AppendLine("| $($t.FormatIndex) | $($t.Entries.Count) | $role |")
}
[void]$sb.AppendLine('')
[void]$sb.AppendLine('### G60 Base tables')
[void]$sb.AppendLine('')
[void]$sb.AppendLine('| FormatIndex | Entries | Role |')
[void]$sb.AppendLine('|-------------|--------:|------|')
foreach ($t in $g60Tables.Values) {
    $role = Get-TableRole $t.FormatIndex $t.Entries.Count
    [void]$sb.AppendLine("| $($t.FormatIndex) | $($t.Entries.Count) | $role |")
}

$g30_10012 = ($g30Tables.GetEnumerator() | Where-Object { $_.Value.FormatIndex -eq '10012' } | Select-Object -First 1).Value.Entries
$g60_10012 = ($g60Tables.GetEnumerator() | Where-Object { $_.Value.FormatIndex -eq '10012' } | Select-Object -First 1).Value.Entries
$g30_10013 = ($g30Tables.GetEnumerator() | Where-Object { $_.Value.FormatIndex -eq '10013' } | Select-Object -First 1).Value.Entries
$g60_10013 = ($g60Tables.GetEnumerator() | Where-Object { $_.Value.FormatIndex -eq '10013' } | Select-Object -First 1).Value.Entries

[void]$sb.AppendLine('')
[void]$sb.AppendLine('---')

Write-OperandComparison $sb 'FormatIndex 10012 - Logic / Flex Operand Table' $g30_10012 $g60_10012 @(
    'Used by `SettingType="Flex"` for LED assignments, oscillography triggers, FlexLogic operands, contact/virtual-output picks, and protection element outputs.'
    'The converter builds a **name-to-G60-code** map from this table (`build_flex_operand_map`).'
    ''
    '**Why codes differ:** G30 7.x and G60 8.x assign different internal numeric IDs to the same logical operand. Matching is by **operand name** (or hardware address suffix for contacts/VOs), not by copying the G30 code.'
)

[void]$sb.AppendLine('')
[void]$sb.AppendLine('---')

Write-OperandComparison $sb 'FormatIndex 10013 - Signal / Measurement Operand Table' $g30_10013 $g60_10013 @(
    'Used for measurement signal picks (SRC1 P, Ia RMS, etc.). Also the lookup source for **user-definable display Item codes**.'
    ''
    '| Platform | User-display Item encoding |'
    '|----------|---------------------------|'
    '| G30 | Raw table-10013 code (e.g. `7168` = SRC1 P) |'
    '| G60 | G60 table-10013 code **+ 262144** (e.g. `6912 + 262144 = 269056`) |'
)

[void]$sb.AppendLine('')
[void]$sb.AppendLine('---')
[void]$sb.AppendLine('')
[void]$sb.AppendLine('## Setting-specific enum tables (FormatIndex != 10012/10013)')
[void]$sb.AppendLine('')
[void]$sb.AppendLine('These tables provide dropdown choices for `SettingType="Enum"` registers.')
[void]$sb.AppendLine('The converter copies G30 `value` + `EnumValue` but **always keeps** the G60 `EnumFormatIndex`.')
[void]$sb.AppendLine('')
[void]$sb.AppendLine('FormatIndex numbers differ between G30 7.x and G60 8.x even when the dropdown choices are logically the same.')
[void]$sb.AppendLine('Tables below are listed in full per file.')
[void]$sb.AppendLine('')

[void]$sb.AppendLine('### G30 - all setting enum tables')
[void]$sb.AppendLine('')
foreach ($kv in $g30Tables.GetEnumerator()) {
    if ($kv.Value.FormatIndex -in @('10012', '10013')) { continue }
    Write-FullTable $sb "G30 FormatIndex $($kv.Value.FormatIndex) ($($kv.Value.Entries.Count) entries)" $kv.Value
}

[void]$sb.AppendLine('### G60 Base - all setting enum tables')
[void]$sb.AppendLine('')
foreach ($kv in $g60Tables.GetEnumerator()) {
    if ($kv.Value.FormatIndex -in @('10012', '10013')) { continue }
    Write-FullTable $sb "G60 FormatIndex $($kv.Value.FormatIndex) ($($kv.Value.Entries.Count) entries)" $kv.Value
}

[void]$sb.AppendLine('---')
[void]$sb.AppendLine('')
[void]$sb.AppendLine('## Source file metadata')
[void]$sb.AppendLine('')
[void]$sb.AppendLine('| | G30 Publix 1367 | G60 Base |')
[void]$sb.AppendLine('|---|-----------------|----------|')
[void]$sb.AppendLine("| version | $($g30x.DocumentElement.GetAttribute('version')) | $($g60x.DocumentElement.GetAttribute('version')) |")
[void]$sb.AppendLine("| orderCode | $($g30x.DocumentElement.GetAttribute('orderCode')) | $($g60x.DocumentElement.GetAttribute('orderCode')) |")
[void]$sb.AppendLine("| URSetupVersion | $($g30x.DocumentElement.GetAttribute('URSetupVersion')) | $($g60x.DocumentElement.GetAttribute('URSetupVersion')) |")

[System.IO.File]::WriteAllText($outPath, $sb.ToString(), [System.Text.UTF8Encoding]::new($false))
Write-Host "Written: $outPath"
Write-Host "Size:    $((Get-Item $outPath).Length) bytes"
Write-Host "Lines:   $((Get-Content $outPath).Count)"
