# Copy converter script and G60 base templates from repo root into azure/function_app.
$Root = Split-Path $PSScriptRoot -Parent
$Dest = Join-Path $PSScriptRoot "function_app"
$BasesSrc = Join-Path $Root "bases"
$BasesDest = Join-Path $Dest "bases"

if (-not (Test-Path $Dest)) {
    New-Item -ItemType Directory -Force -Path $Dest | Out-Null
}

Copy-Item (Join-Path $Root "convert_g30_to_g60.py") $Dest -Force
Write-Host "Copied convert_g30_to_g60.py"

New-Item -ItemType Directory -Force -Path $BasesDest | Out-Null
Get-ChildItem -LiteralPath $BasesSrc -Filter "G60 Base*.xml" | ForEach-Object {
    Copy-Item -LiteralPath $_.FullName -Destination (Join-Path $BasesDest $_.Name) -Force
    Write-Host "Copied bases/$($_.Name)"
}

# Default template at function_app root for deploy checks / legacy layout
Copy-Item -LiteralPath (Join-Path $BasesSrc "G60 Base.xml") -Destination (Join-Path $Dest "G60 Base.xml") -Force
