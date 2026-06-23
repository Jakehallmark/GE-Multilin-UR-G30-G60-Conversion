# Allow this machine's public IP on the SCM site (fixes 403 when access restrictions block deploy).
param(
    [Parameter(Mandatory = $true)]
    [string]$FunctionAppName,
    [string]$ResourceGroup = "rg-g30-g60-converter"
)

$prevEap = $ErrorActionPreference
$ErrorActionPreference = "Continue"

Write-Host "Detecting public IP..."
$ip = (Invoke-RestMethod -Uri "https://api.ipify.org" -TimeoutSec 15).Trim()
$cidr = "$ip/32"
Write-Host "Your IP: $cidr"

$existing = az functionapp config access-restriction list `
    --resource-group $ResourceGroup `
    --name $FunctionAppName `
    --scm-site true `
    --query "[?ipAddress=='$cidr']" -o tsv 2>$null

if ($existing) {
    Write-Host "SCM IP allow rule already present (OK)."
    $ErrorActionPreference = $prevEap
    exit 0
}

Write-Host "Allowing SCM access for this IP (rule: LocalDeployMachine) ..."
$null = az functionapp config access-restriction add `
    --resource-group $ResourceGroup `
    --name $FunctionAppName `
    --scm-site true `
    --rule-name LocalDeployMachine `
    --action Allow `
    --ip-address $cidr `
    --priority 100 `
    --output none 2>&1

if ($LASTEXITCODE -eq 0) {
    Write-Host "SCM IP allow rule added."
} else {
    Write-Host "Note: could not add SCM IP rule (deploy may still work)."
}

$ErrorActionPreference = $prevEap
exit 0
