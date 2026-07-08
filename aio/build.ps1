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

$fletExe = Get-Command flet -ErrorAction SilentlyContinue
if (-not $fletExe) {
    $fallbackFlet = Join-Path $env:LOCALAPPDATA "Python\pythoncore-3.14-64\Scripts\flet.exe"
    if (Test-Path -LiteralPath $fallbackFlet) {
        $fletExe = Get-Command $fallbackFlet
    } else {
        throw "flet CLI not found. Run: pip install -r aio/requirements.txt"
    }
}

Push-Location $AioDir
try {
    # Repo-root modules (convert_g30_to_g60, urs_io, etc.) live outside aio/.
    # PyInstaller only searches aio/ by default; PYTHONPATH makes them discoverable.
    $prevPythonPath = $env:PYTHONPATH
    $env:PYTHONPATH = if ($prevPythonPath) { "$RepoRoot;$prevPythonPath" } else { $RepoRoot }

    & $fletExe.Source pack app.py `
        -y `
        -n $ExeName `
        --distpath $StageDir `
        --add-data "$BasesDir;bases" `
        --add-data "$FirmwareDir;firmware" `
        --file-description "GE Multilin UR G30 to G60 settings converter" `
        --product-name "G30 to G60 Converter" `
        --hidden-import convert_g30_to_g60 `
        --hidden-import convert_g30_to_g60_urs `
        --hidden-import urs_io `
        --hidden-import base_templates `
        --hidden-import aio.base_templates

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
