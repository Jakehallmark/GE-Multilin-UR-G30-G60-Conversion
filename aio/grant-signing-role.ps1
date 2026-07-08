# Assign the Artifact Signing Certificate Profile Signer role to the current user.
#
# Required before signing works — a 403 Forbidden from sign.exe almost always
# means this role is missing on the certificate profile (not just the account).
#
# Usage:
#   az login --scope "https://codesigning.azure.net/.default"
#   .\grant-signing-role.ps1
#
# Optional overrides (defaults match this repo's Azure resources):
#   $env:SIGNING_RESOURCE_GROUP = "rg-g30-g60-converter"
#   $env:ARTIFACT_SIGNING_ACCOUNT = "jhallmarksigning"
#   $env:ARTIFACT_SIGNING_PROFILE = "private"

$ErrorActionPreference = "Stop"

function Find-AzureCli {
    $cmd = Get-Command az -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }
    $path = "${env:ProgramFiles}\Microsoft SDKs\Azure\CLI2\wbin\az.cmd"
    if (Test-Path -LiteralPath $path) { return $path }
    throw "Azure CLI not found. Install: winget install Microsoft.AzureCLI"
}

$az = Find-AzureCli
$rg = if ($env:SIGNING_RESOURCE_GROUP) { $env:SIGNING_RESOURCE_GROUP } else { "rg-g30-g60-converter" }
$account = if ($env:ARTIFACT_SIGNING_ACCOUNT) { $env:ARTIFACT_SIGNING_ACCOUNT } else { "jhallmarksigning" }
$profile = if ($env:ARTIFACT_SIGNING_PROFILE) { $env:ARTIFACT_SIGNING_PROFILE } else { "public" }

Write-Host "Checking Azure login..."
$subId = & $az account show --query id -o tsv
if ($LASTEXITCODE -ne 0) {
    throw "Not logged in. Run: az login --scope `"https://codesigning.azure.net/.default`""
}

$userId = & $az ad signed-in-user show --query id -o tsv
$userUpn = & $az ad signed-in-user show --query userPrincipalName -o tsv
if ($LASTEXITCODE -ne 0) {
    throw "Could not read signed-in user. Run: az login --scope `"https://codesigning.azure.net/.default`""
}

$scope = "/subscriptions/$subId/resourceGroups/$rg/providers/Microsoft.CodeSigning/codeSigningAccounts/$account/certificateProfiles/$profile"

Write-Host "Subscription : $subId"
Write-Host "User         : $userUpn"
Write-Host "Scope        : $scope"
Write-Host ""

$existing = & $az role assignment list --assignee $userId --scope $scope --role "Artifact Signing Certificate Profile Signer" -o json | ConvertFrom-Json
if ($existing.Count -gt 0) {
    Write-Host "Role already assigned. You can run .\aio\build.ps1 -Sign"
    exit 0
}

Write-Host "Assigning 'Artifact Signing Certificate Profile Signer'..."
& $az role assignment create `
    --assignee $userId `
    --role "Artifact Signing Certificate Profile Signer" `
    --scope $scope

if ($LASTEXITCODE -ne 0) {
    throw "Role assignment failed. Assign manually in Azure Portal → certificate profile → Access control (IAM)."
}

Write-Host ""
Write-Host "Done. Wait ~1 minute for RBAC to propagate, then run:"
Write-Host "  .\aio\build.ps1 -Sign"
