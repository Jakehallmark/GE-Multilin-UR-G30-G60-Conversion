# Build the standalone GUI exe and copy it to release/ for GitHub tagging.
# Requires: pip install pyinstaller
#
#   C:\path\to\repo\aio\build.ps1

$ErrorActionPreference = "Stop"
$AioDir = $PSScriptRoot
$RepoRoot = Split-Path $AioDir -Parent
$BasesDir = Join-Path $RepoRoot "bases"
$ReleaseDir = Join-Path $RepoRoot "release"
$ReleaseExe = Join-Path $ReleaseDir "G30-to-G60-Converter.exe"

if (-not (Get-ChildItem -LiteralPath $BasesDir -Filter "G60 Base*.xml" -ErrorAction SilentlyContinue)) {
    throw "No G60 Base*.xml files in $BasesDir"
}

New-Item -ItemType Directory -Force -Path $ReleaseDir | Out-Null

Push-Location $AioDir
try {
    python -m PyInstaller `
        --noconfirm `
        --onefile `
        --windowed `
        --name "G30-to-G60-Converter" `
        --distpath $ReleaseDir `
        --workpath (Join-Path $AioDir "build") `
        --specpath $AioDir `
        --add-data "$BasesDir;bases" `
        --paths $RepoRoot `
        app.py
    Write-Host "Built: $ReleaseExe"
}
finally {
    Pop-Location
}
