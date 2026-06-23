# Copy converter script and G60 base template from repo root into azure/function_app.
$Root = Split-Path $PSScriptRoot -Parent
$Dest = Join-Path $PSScriptRoot "function_app"

if (-not (Test-Path $Dest)) {
    New-Item -ItemType Directory -Force -Path $Dest | Out-Null
}

Copy-Item (Join-Path $Root "convert_g30_to_g60.py") $Dest -Force
Write-Host "Copied convert_g30_to_g60.py"

Copy-Item (Join-Path $Root "G60 Base.xml") $Dest -Force
Write-Host "Copied G60 Base.xml"
