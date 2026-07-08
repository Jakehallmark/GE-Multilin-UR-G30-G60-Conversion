# Build the standalone GUI exe and copy it to release/ for GitHub tagging.
# Requires: pip install pyinstaller
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
    Write-Warning "No G60 Base*.urs files in $BasesDir — URS tab will be disabled until paired .urs bases are added."
} else {
    Write-Host "Bundling $ursCount URS base template(s) for the URS converter tab."
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

Push-Location $AioDir
try {
    python -m PyInstaller `
        --noconfirm `
        --clean `
        --onefile `
        --windowed `
        --noupx `
        --name $ExeName `
        --distpath $StageDir `
        --workpath (Join-Path $AioDir "build") `
        --specpath $AioDir `
        --add-data "$BasesDir;bases" `
        --add-data "$FirmwareDir;firmware" `
        --paths $RepoRoot `
        app.py

    if ($LASTEXITCODE -ne 0) {
        throw "PyInstaller failed with exit code $LASTEXITCODE"
    }

    if (-not (Test-Path -LiteralPath $StageExe)) {
        throw "PyInstaller finished but staged exe was not created: $StageExe"
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
