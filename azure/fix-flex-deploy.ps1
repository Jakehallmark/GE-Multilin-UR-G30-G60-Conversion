# Fix Flex Consumption deploy 403: deployment package uploads to blob storage via UAMI.
# SCM auth can be ON while deploy still fails if the deployment identity lacks blob write access.
param(
    [Parameter(Mandatory = $true)]
    [string]$FunctionAppName,
    [string]$ResourceGroup = "rg-g30-g60-converter"
)

$prevEap = $ErrorActionPreference
$ErrorActionPreference = "Continue"

if (-not (Get-Command az -ErrorAction SilentlyContinue)) {
    throw "Azure CLI (az) not found."
}

Write-Host "Reading Flex deployment storage config ..."
$configJson = az functionapp deployment config show `
    --resource-group $ResourceGroup `
    --name $FunctionAppName -o json 2>$null

if (-not $configJson) {
    Write-Host "No Flex deployment config found (not a Flex app?). Skipping."
    $ErrorActionPreference = $prevEap
    exit 0
}

$config = $configJson | ConvertFrom-Json
$blobUrl = $config.storage.value
if (-not $blobUrl) {
    Write-Host "No deployment blob container configured. Skipping."
    $ErrorActionPreference = $prevEap
    exit 0
}

$storageAccount = ($blobUrl -replace "^https://", "" -split "\.")[0]
$containerName = ($blobUrl.TrimEnd("/") -split "/")[-1]
Write-Host "Storage account: $storageAccount"
Write-Host "Container: $containerName"

$subId = az account show --query id -o tsv
$scope = "/subscriptions/$subId/resourceGroups/$ResourceGroup/providers/Microsoft.Storage/storageAccounts/$storageAccount"

$authType = $config.storage.authentication.type
$uamiId = $config.storage.authentication.userAssignedIdentityResourceId
Write-Host "Deployment auth type: $authType"

if ($authType -eq "UserAssignedIdentity" -and $uamiId) {
    $principalId = az identity show --ids $uamiId --query principalId -o tsv
    Write-Host "Deployment UAMI principal: $principalId"

    $hasRole = az role assignment list `
        --assignee-object-id $principalId `
        --scope $scope `
        --role "Storage Blob Data Contributor" `
        --query "[0].id" -o tsv 2>$null

    if ($hasRole) {
        Write-Host "OK: UAMI already has Storage Blob Data Contributor on storage account."
    } else {
        Write-Host "Assigning Storage Blob Data Contributor to deployment UAMI ..."
        az role assignment create `
            --assignee-object-id $principalId `
            --assignee-principal-type ServicePrincipal `
            --role "Storage Blob Data Contributor" `
            --scope $scope `
            --output none
        if ($LASTEXITCODE -ne 0) {
            Write-Host "WARN: Could not assign role. You may need Owner on the subscription." -ForegroundColor Yellow
        } else {
            Write-Host "Role assigned. Waiting 45s for propagation ..."
            Start-Sleep -Seconds 45
        }
    }
}

# Also ensure deployer (you) can write to the container when CLI uploads via your login
$userId = az ad signed-in-user show --query id -o tsv 2>$null
if ($userId) {
    $userHasRole = az role assignment list `
        --assignee-object-id $userId `
        --scope $scope `
        --role "Storage Blob Data Contributor" `
        --query "[0].id" -o tsv 2>$null
    if (-not $userHasRole) {
        Write-Host "Assigning Storage Blob Data Contributor to your user on storage account ..."
        az role assignment create `
            --assignee-object-id $userId `
            --assignee-principal-type User `
            --role "Storage Blob Data Contributor" `
            --scope $scope `
            --output none 2>$null
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Waiting 30s for user role propagation ..."
            Start-Sleep -Seconds 30
        }
    }
}

Write-Host ""
Write-Host "Flex deploy fix complete. Retry: .\azure\deploy.ps1"
$ErrorActionPreference = $prevEap
exit 0
