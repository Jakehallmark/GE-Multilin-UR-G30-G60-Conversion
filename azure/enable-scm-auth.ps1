# Enable SCM basic auth and verify (required for zip/OneDeploy to SCM endpoint).
param(
    [Parameter(Mandatory = $true)]
    [string]$FunctionAppName,
    [string]$ResourceGroup = "rg-g30-g60-converter"
)

$ErrorActionPreference = "Stop"

if (-not (Get-Command az -ErrorAction SilentlyContinue)) {
    throw "Azure CLI (az) not found."
}

$null = az account show --query id -o tsv 2>$null
if ($LASTEXITCODE -ne 0) {
    throw "Not logged in. Run: az login"
}

Write-Host "Enabling SCM Basic Auth Publishing for $FunctionAppName ..."

az resource update `
    --resource-group $ResourceGroup `
    --name scm `
    --namespace Microsoft.Web `
    --resource-type basicPublishingCredentialsPolicies `
    --parent "sites/$FunctionAppName" `
    --set properties.allow=true `
    --output none

if ($LASTEXITCODE -ne 0) {
    throw "Failed to enable SCM basic auth. Use portal: Configuration -> General settings -> SCM Basic Auth -> Apply"
}

Start-Sleep -Seconds 5

$allowed = az resource show `
    --resource-group $ResourceGroup `
    --name scm `
    --namespace Microsoft.Web `
    --resource-type basicPublishingCredentialsPolicies `
    --parent "sites/$FunctionAppName" `
    --query "properties.allow" -o tsv

Write-Host "SCM basic auth allow = $allowed"

if ($allowed -ne "true") {
    Write-Host ""
    Write-Host "SCM auth is still disabled." -ForegroundColor Yellow
    Write-Host "Enable manually in portal:"
    Write-Host "  $FunctionAppName -> Configuration -> General settings"
    Write-Host "  Check 'SCM Basic Auth Publishing Credentials' -> Apply"
    Write-Host "  Overview -> Restart"
    exit 1
}

Write-Host "Restarting function app so SCM setting takes effect ..."
az functionapp restart --resource-group $ResourceGroup --name $FunctionAppName --output none
Start-Sleep -Seconds 15

Write-Host "SCM basic auth is ON (restarted app)."
