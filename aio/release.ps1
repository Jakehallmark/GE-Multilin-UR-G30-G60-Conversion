# Bump version, commit, tag, push to GitHub, and build the release exe.
#
#   .\aio\release.ps1                     # bump patch (e.g. 1.0.4 -> 1.0.5), push tag, build
#   .\aio\release.ps1 -Version 1.1.0      # explicit semver
#   .\aio\release.ps1 -Bump minor         # bump minor instead of patch
#   .\aio\release.ps1 -SkipPush           # update version + build locally only
#   .\aio\release.ps1 -SkipBuild          # tag/push only (CI builds the exe on GitHub)
#   .\aio\release.ps1 -Sign               # Authenticode-sign after local build
#
# Requires: git, network access for push, pip deps for build.ps1

param(
    [string]$Version,
    [ValidateSet("major", "minor", "patch")]
    [string]$Bump = "patch",
    [string]$Message,
    [switch]$SkipPush,
    [switch]$SkipBuild,
    [switch]$Sign
)

$ErrorActionPreference = "Stop"
$AioDir = $PSScriptRoot
$RepoRoot = Split-Path $AioDir -Parent
$VersionFile = Join-Path $AioDir "version.json"
$BuildScript = Join-Path $AioDir "build.ps1"

function Get-LatestSemverTag {
    param([string]$RepoPath)
    Push-Location $RepoPath
    try {
        $tags = git tag -l "v*.*.*" | ForEach-Object { $_ -replace "^v", "" }
        $valid = $tags | Where-Object { $_ -match "^\d+\.\d+\.\d+$" } | Sort-Object {
            $parts = $_.Split(".")
            [version]"$($parts[0]).$($parts[1]).$($parts[2])"
        }
        return $valid | Select-Object -Last 1
    } finally {
        Pop-Location
    }
}

function Bump-Semver {
    param(
        [string]$Current,
        [string]$Kind
    )
    $parts = $Current.Split(".")
    if ($parts.Count -lt 3) {
        throw "Invalid semver: $Current"
    }
    [int]$major = $parts[0]
    [int]$minor = $parts[1]
    [int]$patch = $parts[2]
    switch ($Kind) {
        "major" { return "{0}.0.0" -f ($major + 1) }
        "minor" { return "{0}.{1}.0" -f $major, ($minor + 1) }
        default { return "{0}.{1}.{2}" -f $major, $minor, ($patch + 1) }
    }
}

if (-not (Test-Path -LiteralPath $VersionFile)) {
    throw "Missing $VersionFile"
}

$current = Get-Content -LiteralPath $VersionFile -Raw | ConvertFrom-Json
$previousVersion = [string]$current.version
$previousBuild = [int]$current.build

if ($Version) {
    if ($Version -notmatch "^\d+\.\d+\.\d+$") {
        throw "Version must be semver like 1.0.4, got: $Version"
    }
    $newVersion = $Version
} else {
    $tagBase = Get-LatestSemverTag $RepoRoot
    if (-not $tagBase) { $tagBase = "0.0.0" }
    $fromTag = Bump-Semver -Current $tagBase -Kind $Bump
    if ([version]$previousVersion -gt [version]$fromTag) {
        $newVersion = $previousVersion
    } else {
        $newVersion = $fromTag
    }
}

$newBuild = if ($newVersion -ne $previousVersion) {
    1
} else {
    $tagExists = git -C $RepoRoot tag -l "v$newVersion"
    if ($tagExists) { $previousBuild + 1 } else { [Math]::Max($previousBuild, 1) }
}

$versionPayload = [ordered]@{
    version = $newVersion
    build   = $newBuild
}
($versionPayload | ConvertTo-Json) + "`n" | Set-Content -LiteralPath $VersionFile -Encoding utf8 -NoNewline

. (Join-Path $AioDir "read-version.ps1")

Write-Host "Release version: $AppDisplayVersion"
Write-Host "Git tag:         $AppTag"

$status = git -C $RepoRoot status --porcelain
if ($status) {
    $other = $status | Where-Object { $_ -notmatch "version\.json" }
    if ($other) {
        Write-Warning @"
Other uncommitted changes will NOT be included in the release commit:
$other
Commit them separately before running release.ps1, or stash them.
"@
    }
    Write-Host ""
    Write-Host "Working tree:"
    Write-Host $status
}

$commitMessage = if ($Message) { $Message } else { "Release $AppTag (build $AppBuild)" }
git -C $RepoRoot add $VersionFile
git -C $RepoRoot commit -m $commitMessage

git -C $RepoRoot tag -a $AppTag -m "Release $AppDisplayVersion"

if (-not $SkipBuild) {
    if ($Sign) {
        & $BuildScript -Sign
    } else {
        & $BuildScript
    }
} else {
    Write-Host "Skipped local build (-SkipBuild). GitHub Actions will build on tag push."
}

if ($SkipPush) {
    Write-Host ""
    Write-Host "Skipped push (-SkipPush)."
    Write-Host "When ready: git push origin main && git push origin $AppTag"
    exit 0
}

Write-Host ""
Write-Host "Pushing commit and tag..."
git -C $RepoRoot push origin HEAD
git -C $RepoRoot push origin $AppTag

Write-Host ""
Write-Host "Done."
Write-Host "  Tag:       $AppTag"
Write-Host "  Exe:       $(Join-Path $RepoRoot 'release\G30-to-G60-Converter.exe')"
Write-Host "  GitHub CI will also attach the exe to the Release for $AppTag."
