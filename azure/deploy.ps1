# Build a deployment zip and publish to Azure Function App.
# Requires: Azure CLI (az) logged in.
param(
    [Parameter(Mandatory = $true)]
    [string]$FunctionAppName,
    [string]$ResourceGroup = "rg-g30-g60-converter"
)

$ErrorActionPreference = "Stop"
$AppDir = Join-Path $PSScriptRoot "function_app"
$ZipPath = Join-Path $PSScriptRoot "deploy.zip"

if (-not (Get-Command az -ErrorAction SilentlyContinue)) {
    throw "Azure CLI (az) not found. Install: winget install Microsoft.AzureCLI"
}

Write-Host "Syncing files from repo root..."
& (Join-Path $PSScriptRoot "sync-from-root.ps1")

$required = @(
    "function_app.py",
    "convert_g30_to_g60.py",
    "G60 Base.xml",
    "host.json",
    "requirements.txt"
)
foreach ($name in $required) {
    $path = Join-Path $AppDir $name
    if (-not (Test-Path $path)) {
        throw "Missing required file: $path"
    }
}

if (Test-Path $ZipPath) { Remove-Item $ZipPath -Force }

Write-Host "Creating deployment zip..."
$archiveItems = @(Get-ChildItem -Path $AppDir -File | ForEach-Object { $_.FullName })
if ($archiveItems.Count -eq 0) {
    throw "No files found in $AppDir"
}
Compress-Archive -LiteralPath $archiveItems -DestinationPath $ZipPath -Force

$zipSize = (Get-Item $ZipPath).Length
Write-Host "Zip size: $([math]::Round($zipSize / 1MB, 2)) MB (XML compresses heavily; ~0.2 MB is normal)"

Write-Host ""
Write-Host "Preparing deploy access (SCM auth + optional IP allow) ..."
& (Join-Path $PSScriptRoot "enable-scm-auth.ps1") `
    -FunctionAppName $FunctionAppName `
    -ResourceGroup $ResourceGroup
if ($LASTEXITCODE -ne 0) {
    exit 1
}

& (Join-Path $PSScriptRoot "allow-scm-ip.ps1") `
    -FunctionAppName $FunctionAppName `
    -ResourceGroup $ResourceGroup
# allow-scm-ip.ps1 always exits 0; duplicate IP rule is OK

& (Join-Path $PSScriptRoot "fix-flex-deploy.ps1") `
    -FunctionAppName $FunctionAppName `
    -ResourceGroup $ResourceGroup

Write-Host ""
Write-Host "Deploying zip to $FunctionAppName (OneDeploy - required for Flex Consumption) ..."
az functionapp deploy `
    --resource-group $ResourceGroup `
    --name $FunctionAppName `
    --src-path $ZipPath `
    --type zip `
    --timeout 600

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "DEPLOY FAILED (403)." -ForegroundColor Red
    Write-Host ""
    Write-Host "Try these in order:"
    Write-Host "  1. Portal: Configuration -> General settings -> SCM Basic Auth = ON -> Apply"
    Write-Host "  2. az login   (refresh Entra token)"
    Write-Host "  3. winget upgrade Microsoft.AzureCLI"
    Write-Host "  4. .\azure\enable-scm-auth.ps1 -FunctionAppName $FunctionAppName"
    Write-Host "  5. .\azure\allow-scm-ip.ps1 -FunctionAppName $FunctionAppName"
    Write-Host "  6. .\azure\deploy.ps1 -FunctionAppName $FunctionAppName -ResourceGroup $ResourceGroup"
    Write-Host ""
    Write-Host 'Portal: Diagnose and solve problems -> Flex Consumption Deployment'
    exit 1
}

Write-Host ""
Write-Host "Deploy succeeded." -ForegroundColor Green
Write-Host "Test URL: https://$FunctionAppName.azurewebsites.net/api/convert?code=YOUR_KEY"
Write-Host 'Function key: Portal - Functions - convert - Function keys'
Write-Host "See azure/README.md for curl examples."
