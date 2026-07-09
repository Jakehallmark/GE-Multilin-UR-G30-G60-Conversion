# Read aio/version.json and expose version metadata as PowerShell variables.
# Dot-source from build.ps1 / release.ps1:
#   . (Join-Path $PSScriptRoot "read-version.ps1")

$ErrorActionPreference = "Stop"
$VersionFile = Join-Path $PSScriptRoot "version.json"
if (-not (Test-Path -LiteralPath $VersionFile)) {
    throw "Missing version file: $VersionFile"
}

$script:AppVersionData = Get-Content -LiteralPath $VersionFile -Raw | ConvertFrom-Json
$script:AppVersion = [string]$AppVersionData.version
$script:AppBuild = [int]$AppVersionData.build
$script:AppTag = "v$AppVersion"
$script:AppFileVersion = "$AppVersion.$AppBuild"
$script:AppDisplayVersion = "$AppVersion (build $AppBuild)"
