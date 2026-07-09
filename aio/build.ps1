# Build the standalone GUI exe and copy it to release/ for GitHub tagging.
# Requires: pip install -r aio/requirements.txt pyinstaller
#
#   C:\path\to\repo\aio\build.ps1
#   C:\path\to\repo\aio\build.ps1 -Sign          # also Authenticode-sign (see CODE_SIGNING.md)
#
# Close G30-to-G60-Converter.exe before rebuilding — Windows locks the file
# while it is running and PyInstaller cannot overwrite it.

param(
    [switch]$Sign
)

$ErrorActionPreference = "Stop"
$AioDir = $PSScriptRoot
$RepoRoot = Split-Path $AioDir -Parent
$BasesDir = Join-Path $RepoRoot "bases"
$FirmwareDir = Join-Path $RepoRoot "firmware"
$FirmwareBundleDir = Join-Path $AioDir "pack-staging\firmware-bundle"
$ReleaseDir = Join-Path $RepoRoot "release"
$ReleaseExe = Join-Path $ReleaseDir "G30-to-G60-Converter.exe"
$StageDir = Join-Path $AioDir "dist"
$StageExe = Join-Path $StageDir "G30-to-G60-Converter.exe"
$SignScript = Join-Path $AioDir "sign.ps1"
$SignConfig = Join-Path $AioDir "signing.local.ps1"
$ExeName = "G30-to-G60-Converter"

if (Test-Path -LiteralPath $SignConfig) {
    Write-Host "Loading signing config from signing.local.ps1"
    . $SignConfig
}

function Test-SigningConfigured {
    return (
        ($env:ARTIFACT_SIGNING_ENDPOINT -and $env:ARTIFACT_SIGNING_ACCOUNT -and $env:ARTIFACT_SIGNING_PROFILE) -or
        $env:CODE_SIGN_PFX_PATH -or
        $env:CODE_SIGN_CERT_THUMBPRINT
    )
}

if (-not (Get-ChildItem -LiteralPath $BasesDir -Filter "G60 Base*.xml" -ErrorAction SilentlyContinue)) {
    throw "No G60 Base*.xml files in $BasesDir"
}

$ursCount = (Get-ChildItem -LiteralPath $BasesDir -Filter "G60 Base*.urs" -ErrorAction SilentlyContinue).Count
if ($ursCount -eq 0) {
    Write-Warning "No G60 Base*.urs files in $BasesDir - URS conversion will be disabled until paired .urs bases are added."
} else {
    Write-Host "Bundling $ursCount URS base template(s) for URS conversion."
}

$running = Get-Process -Name $ExeName -ErrorAction SilentlyContinue
if ($running) {
    throw @"
$ExeName is still running (PID $($running.Id -join ', ')).
Close the converter window, then run build.ps1 again.
"@
}

if (Test-Path -LiteralPath $ReleaseExe) {
    try {
        [System.IO.File]::OpenWrite($ReleaseExe).Close()
    } catch {
        throw @"
Cannot overwrite locked file:
  $ReleaseExe

Close $ExeName if it is open, check Task Manager for a stray process,
or reboot if antivirus is holding the file. Then run build.ps1 again.
"@
    }
}

New-Item -ItemType Directory -Force -Path $ReleaseDir | Out-Null
if (Test-Path -LiteralPath $StageDir) {
    Remove-Item -LiteralPath $StageDir -Recurse -Force
}

function New-FirmwareBundle {
    param([string]$SourceRoot, [string]$DestRoot)
    if (Test-Path -LiteralPath $DestRoot) {
        Remove-Item -LiteralPath $DestRoot -Recurse -Force
    }
    $csvCount = 0
    foreach ($side in @("g30", "g60")) {
        $srcSide = Join-Path $SourceRoot $side
        if (-not (Test-Path -LiteralPath $srcSide)) { continue }
        $destSide = Join-Path $DestRoot $side
        New-Item -ItemType Directory -Force -Path $destSide | Out-Null
        $csvs = Get-ChildItem -LiteralPath $srcSide -Filter "AnalogoperandTo61850_*.csv" -File -ErrorAction SilentlyContinue
        foreach ($csv in $csvs) {
            Copy-Item -LiteralPath $csv.FullName -Destination $destSide -Force
            $csvCount++
        }
    }
    if ($csvCount -eq 0) {
        throw "No AnalogoperandTo61850_*.csv files under $SourceRoot/g30 or g60"
    }
    return $csvCount
}

$fletExe = Get-Command flet -ErrorAction SilentlyContinue
if (-not $fletExe) {
    $fallbackFlet = Join-Path $env:LOCALAPPDATA "Python\pythoncore-3.14-64\Scripts\flet.exe"
    if (Test-Path -LiteralPath $fallbackFlet) {
        $fletExe = Get-Command $fallbackFlet
    } else {
        throw "flet CLI not found. Run: pip install -r aio/requirements.txt"
    }
}

. (Join-Path $AioDir "read-version.ps1")

Write-Host "Building version $AppDisplayVersion (file version $AppFileVersion)"

Push-Location $AioDir
try {
    # flet pack deletes aio/build/ before PyInstaller runs — stage CSVs outside it.
    $bundledCsvCount = New-FirmwareBundle -SourceRoot $FirmwareDir -DestRoot $FirmwareBundleDir
    Write-Host "Bundling $bundledCsvCount Analogoperand CSV(s) (firmware binaries are excluded from the exe)"

    # Repo-root modules (convert_g30_to_g60, urs_io, etc.) live outside aio/.
    # PyInstaller only searches aio/ by default; PYTHONPATH makes them discoverable.
    $prevPythonPath = $env:PYTHONPATH
    $env:PYTHONPATH = if ($prevPythonPath) { "$RepoRoot;$prevPythonPath" } else { $RepoRoot }

    & $fletExe.Source pack app.py `
        -y `
        -n $ExeName `
        --distpath $StageDir `
        --add-data "$BasesDir;bases" `
        --add-data "$FirmwareBundleDir;firmware" `
        --add-data "$AioDir\version.json;." `
        --file-description "GE Multilin UR G30 to G60 settings converter" `
        --product-name "G30 to G60 Converter" `
        --product-version $AppVersion `
        --file-version $AppFileVersion `
        --company-name "GE Multilin UR Tools" `
        --copyright "Copyright (C) 2026" `
        --hidden-import convert_g30_to_g60 `
        --hidden-import convert_g30_to_g60_urs `
        --hidden-import urs_io `
        --hidden-import base_templates `
        --hidden-import aio.base_templates `
        --hidden-import app_version

    if ($null -ne $prevPythonPath) {
        $env:PYTHONPATH = $prevPythonPath
    } else {
        Remove-Item Env:PYTHONPATH -ErrorAction SilentlyContinue
    }

    if ($LASTEXITCODE -ne 0) {
        throw "flet pack failed with exit code $LASTEXITCODE"
    }

    if (-not (Test-Path -LiteralPath $StageExe)) {
        throw "flet pack finished but staged exe was not created: $StageExe"
    }

    Copy-Item -LiteralPath $StageExe -Destination $ReleaseExe -Force
    Write-Host "Built: $ReleaseExe"

    $verifyScript = Join-Path $AioDir "verify-standalone.ps1"
    if (Test-Path -LiteralPath $verifyScript) {
        Write-Host "Verifying exe starts without python.exe on PATH..."
        & $verifyScript -ExePath $ReleaseExe
    }

    $shouldSign = $Sign -or (Test-SigningConfigured)
    if ($shouldSign) {
        if (-not (Test-SigningConfigured)) {
            throw "Build -Sign was passed but no signing credentials are configured. See aio/CODE_SIGNING.md"
        }
        & $SignScript -FilePath $ReleaseExe
    } else {
        Write-Host ""
        Write-Host "Note: exe is unsigned. Edge/SmartScreen will warn on SharePoint downloads."
        Write-Host "      See aio/CODE_SIGNING.md to set up Authenticode signing."
    }
}
finally {
    Pop-Location
}
