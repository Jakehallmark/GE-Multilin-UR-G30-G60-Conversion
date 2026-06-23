# Diagnose why zip / VS Code / az deploy returns 403.
param(
    [Parameter(Mandatory = $true)]
    [string]$FunctionAppName,
    [string]$ResourceGroup = "rg-g30-g60-converter"
)

$ErrorActionPreference = "Continue"

if (-not (Get-Command az -ErrorAction SilentlyContinue)) {
    Write-Host "Azure CLI not found." -ForegroundColor Red
    exit 1
}

$sub = az account show --query "{name:name,id:id,user:user.name}" -o json 2>$null | ConvertFrom-Json
Write-Host "=== Account ===" -ForegroundColor Cyan
Write-Host "Subscription: $($sub.name)"
Write-Host "Signed in as: $($sub.user)"
Write-Host "CLI version: $(az version --query '\"azure-cli\"' -o tsv 2>$null)"
Write-Host ""

Write-Host "=== Function App ===" -ForegroundColor Cyan
az functionapp show --resource-group $ResourceGroup --name $FunctionAppName `
    --query "{state:state, kind:kind, sku:sku, publicNetworkAccess:publicNetworkAccess, httpsOnly:httpsOnly}" -o json
Write-Host ""

Write-Host "=== SCM Basic Auth policy (must be true for VS Code zip deploy) ===" -ForegroundColor Cyan
$scmAllow = az resource show `
    --resource-group $ResourceGroup `
    --name scm `
    --namespace Microsoft.Web `
    --resource-type basicPublishingCredentialsPolicies `
    --parent "sites/$FunctionAppName" `
    --query "properties.allow" -o tsv 2>$null
Write-Host "properties.allow = $scmAllow"
if ($scmAllow -ne "true") {
    Write-Host "FAIL: SCM basic auth is OFF. Portal: Configuration -> General settings -> check SCM Basic Auth -> Apply" -ForegroundColor Red
} else {
    Write-Host "OK: SCM basic auth policy is ON at ARM level." -ForegroundColor Green
    Write-Host "If portal checkbox still looks OFF, refresh the page. If deploy still fails, restart the app."
}
Write-Host ""

Write-Host "=== SCM access restrictions (your IP must be allowed) ===" -ForegroundColor Cyan
az functionapp config access-restriction list `
    --resource-group $ResourceGroup `
    --name $FunctionAppName `
    --scm-site true -o table 2>$null
Write-Host ""

Write-Host "=== Main site access restrictions ===" -ForegroundColor Cyan
az functionapp config access-restriction list `
    --resource-group $ResourceGroup `
    --name $FunctionAppName -o table 2>$null
Write-Host ""

Write-Host "=== Publish profile test (fails when SCM auth blocked) ===" -ForegroundColor Cyan
$profileTest = az webapp deployment list-publishing-profiles `
    --resource-group $ResourceGroup `
    --name $FunctionAppName -o none 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "OK: Publishing profiles retrieved (SCM deploy credentials path works)." -ForegroundColor Green
} else {
    Write-Host "FAIL: Cannot get publishing profiles - SCM auth likely still blocked:" -ForegroundColor Red
    Write-Host $profileTest
}
Write-Host ""

Write-Host "=== Deployment storage (Flex Consumption) ===" -ForegroundColor Cyan
$deployConfig = az functionapp deployment config show --resource-group $ResourceGroup --name $FunctionAppName -o json 2>$null
Write-Host $deployConfig
if ($deployConfig) {
    $dc = $deployConfig | ConvertFrom-Json
    $blobUrl = $dc.storage.value
    if ($blobUrl) {
        $sa = ($blobUrl -replace "^https://", "" -split "\.")[0]
        $subId = az account show --query id -o tsv
        $scope = "/subscriptions/$subId/resourceGroups/$ResourceGroup/providers/Microsoft.Storage/storageAccounts/$sa"
        Write-Host ""
        Write-Host "=== UAMI roles on storage account ($sa) ===" -ForegroundColor Cyan
        $uamiId = $dc.storage.authentication.userAssignedIdentityResourceId
        if ($uamiId) {
            $uamiPrincipalId = az identity show --ids $uamiId --query principalId -o tsv 2>$null
            az role assignment list --assignee-object-id $uamiPrincipalId --scope $scope -o table 2>$null
            if (-not (az role assignment list --assignee-object-id $uamiPrincipalId --scope $scope --role "Storage Blob Data Contributor" --query "[0].id" -o tsv 2>$null)) {
                Write-Host "FAIL: Deployment UAMI needs Storage Blob Data Contributor on $sa" -ForegroundColor Red
                Write-Host "Run: .\azure\fix-flex-deploy.ps1"
            }
        }
    }
}
Write-Host ""

Write-Host "=== Your public IP (add to SCM allow list if restricted) ===" -ForegroundColor Cyan
try {
    $ip = (Invoke-RestMethod -Uri "https://api.ipify.org" -TimeoutSec 10).Trim()
    Write-Host $ip
} catch {
    Write-Host "(could not detect)"
}
Write-Host ""

Write-Host "=== What uses 403 ===" -ForegroundColor Cyan
Write-Host @"
VS Code Azure Functions extension -> zip to *.scm.*.azurewebsites.net (NOT your Entra login alone)
az functionapp deploy (OneDeploy) -> still hits SCM endpoint for Flex Consumption
Both need SCM Basic Auth ON (portal Apply + restart) unless a future CLI uses Entra-only path.

Wrong assumption: signed-in VS Code account replaces SCM publishing credentials - it does not for zip deploy.

Fix order:
  1. Portal: SCM Basic Auth ON -> Apply -> Overview -> Restart
  2. .\azure\enable-scm-auth.ps1  (verify allow = true)
  3. .\azure\allow-scm-ip.ps1
  4. .\azure\deploy.ps1  OR VS Code Deploy

If SCM toggle will not stay ON: subscription policy may block it - recreate app on Linux Consumption (not Flex) instead.
"@
