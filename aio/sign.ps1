# Sign a Windows executable with Authenticode.
#
# Supports two backends (first match wins):
#
#   1. Azure Artifact Signing (recommended for Microsoft 365 / SharePoint orgs)
#      Requires:
#        winget install Microsoft.AzureCLI
#        dotnet tool install -g --prerelease sign
#        az login --scope "https://codesigning.azure.net/.default"
#      Environment variables (or aio/signing.local.ps1):
#        ARTIFACT_SIGNING_ENDPOINT   e.g. https://eus.codesigning.azure.net/
#        ARTIFACT_SIGNING_ACCOUNT    your signing account name
#        ARTIFACT_SIGNING_PROFILE    certificate profile name
#        AZURE_CREDENTIAL_TYPE       azure-cli (default) or azure-powershell
#
#   2. Traditional certificate (PFX file or Windows cert store)
#      Environment variables:
#        CODE_SIGN_PFX_PATH          path to .pfx
#        CODE_SIGN_PFX_PASSWORD      PFX password (optional if empty)
#      OR
#        CODE_SIGN_CERT_THUMBPRINT   cert in CurrentUser\My or LocalMachine\My
#
# Optional:
#   CODE_SIGN_TIMESTAMP_URL         default http://timestamp.acs.microsoft.com
#
# Usage:
#   .\sign.ps1 -FilePath ..\release\G30-to-G60-Converter.exe

param(
    [Parameter(Mandatory = $true)]
    [string]$FilePath
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $FilePath)) {
    throw "File not found: $FilePath"
}

$timestampUrl = $env:CODE_SIGN_TIMESTAMP_URL
if (-not $timestampUrl) {
    $timestampUrl = "http://timestamp.acs.microsoft.com"
}

function Find-SignCli {
    $cmd = Get-Command sign -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }

    $toolPath = Join-Path $env:USERPROFILE ".dotnet\tools\sign.exe"
    if (Test-Path -LiteralPath $toolPath) { return $toolPath }

    return $null
}

function Find-AzureCli {
    $cmd = Get-Command az -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }

    $candidates = @(
        "${env:ProgramFiles}\Microsoft SDKs\Azure\CLI2\wbin\az.cmd",
        "${env:ProgramFiles(x86)}\Microsoft SDKs\Azure\CLI2\wbin\az.cmd"
    )
    foreach ($path in $candidates) {
        if (Test-Path -LiteralPath $path) { return $path }
    }
    return $null
}

function Test-SignatureValid {
    param([string]$Path)
    $sig = Get-AuthenticodeSignature -LiteralPath $Path
    if ($sig.Status -eq "Valid") {
        return $true
    }
    # Azure PrivateTrust: file is signed and timestamped, but the org root CA
    # is not in this machine's trusted store yet — that is expected.
    if ($sig.SignerCertificate -and $sig.Status -eq "UnknownError") {
        $msg = if ($sig.StatusMessage) { $sig.StatusMessage } else { "" }
        if ($msg -match "not trusted by the trust provider") {
            return $true
        }
    }
    return $false
}

function Invoke-AzureArtifactSigning {
    param([string]$Path)

    $endpoint = $env:ARTIFACT_SIGNING_ENDPOINT
    $account = $env:ARTIFACT_SIGNING_ACCOUNT
    $profile = $env:ARTIFACT_SIGNING_PROFILE

    if (-not ($endpoint -and $account -and $profile)) {
        return $false
    }

    $signExe = Find-SignCli
    if (-not $signExe) {
        throw @"
Azure Artifact Signing is configured but the 'sign' CLI is not installed.

  dotnet tool install -g --prerelease sign
"@
    }

    $credType = $env:AZURE_CREDENTIAL_TYPE
    if (-not $credType) { $credType = "azure-cli" }

    if ($credType -eq "azure-cli") {
        $az = Find-AzureCli
        if (-not $az) {
            throw @"
Azure CLI is required for signing but was not found.

Install it:
  winget install Microsoft.AzureCLI

Restart PowerShell, then log in with the codesigning scope:
  az login --scope "https://codesigning.azure.net/.default"
"@
        }

        Write-Host "Checking Azure CLI login..."
        $azOut = & $az account show --query "{name:name, user:user.name}" -o tsv 2>&1
        if ($LASTEXITCODE -ne 0) {
            throw @"
Azure CLI is not logged in. Run:

  az login --scope "https://codesigning.azure.net/.default"

Then verify your account has the 'Trusted Signing Certificate Profile Signer'
role on the Artifact Signing account in Azure Portal.
"@
        }
        Write-Host "Azure account: $azOut"
    }

    if (-not $endpoint.EndsWith("/")) {
        $endpoint = "$endpoint/"
    }

    Write-Host "Signing with Azure Artifact Signing..."
    Write-Host "  endpoint : $endpoint"
    Write-Host "  account  : $account"
    Write-Host "  profile  : $profile"
    Write-Host "  auth     : $credType"

    if ($profile -match "private") {
        Write-Warning @"
Profile '$profile' is PrivateTrust — SmartScreen will show 'Unknown publisher'
on machines without your org root CA. For SharePoint/public downloads, create a
PublicTrust profile in Azure Portal and set ARTIFACT_SIGNING_PROFILE to its name.
"@
    }

    $signArgs = @(
        "code", "artifact-signing",
        "--verbosity", "Information",
        "--azure-credential-type", $credType,
        "--timestamp-url", $timestampUrl,
        "--artifact-signing-endpoint", $endpoint,
        "--artifact-signing-account", $account,
        "--artifact-signing-certificate-profile", $profile,
        $Path
    )

    $output = & $signExe @signArgs 2>&1
    $exitCode = $LASTEXITCODE

    if ($output) {
        $output | ForEach-Object { Write-Host $_ }
    }

    if ($exitCode -ne 0) {
        $hint = @"

Common fixes for exit code $exitCode :
  1. 403 Forbidden → run:  .\aio\grant-signing-role.ps1
     (Signer role must be on the certificate PROFILE, not just the account)
  2. Re-login:             az login --scope "https://codesigning.azure.net/.default"
  3. Verify endpoint region matches your account (yours: eastus → eus.codesigning.azure.net)
  4. Verify account/profile names in signing.local.ps1 (case-sensitive)
  5. Ensure identity validation is Complete and profile status is Active
"@
        throw "Azure Artifact Signing failed with exit code $exitCode.$hint"
    }
    return $true
}

function Find-SignTool {
    $kits = @(
        "${env:ProgramFiles(x86)}\Windows Kits\10\bin\*\x64\signtool.exe",
        "${env:ProgramFiles}\Windows Kits\10\bin\*\x64\signtool.exe"
    )
    foreach ($pattern in $kits) {
        $found = Get-Item $pattern -ErrorAction SilentlyContinue | Sort-Object {
            [version]($_.Directory.Parent.Name)
        } -Descending | Select-Object -First 1
        if ($found) { return $found.FullName }
    }
    return $null
}

function Invoke-PfxSigning {
    param([string]$Path)

    $pfxPath = $env:CODE_SIGN_PFX_PATH
    if (-not $pfxPath) { return $false }
    if (-not (Test-Path -LiteralPath $pfxPath)) {
        throw "CODE_SIGN_PFX_PATH not found: $pfxPath"
    }

    $signtool = Find-SignTool
    if (-not $signtool) {
        throw "signtool.exe not found. Install the Windows 10/11 SDK."
    }

    Write-Host "Signing with PFX certificate..."
    $signArgs = @(
        "sign", "/v", "/fd", "SHA256",
        "/tr", $timestampUrl, "/td", "SHA256",
        "/f", $pfxPath
    )
    if ($env:CODE_SIGN_PFX_PASSWORD) {
        $signArgs += @("/p", $env:CODE_SIGN_PFX_PASSWORD)
    }
    $signArgs += $Path

    & $signtool @signArgs
    if ($LASTEXITCODE -ne 0) {
        throw "signtool failed with exit code $LASTEXITCODE"
    }
    return $true
}

function Invoke-StoreSigning {
    param([string]$Path)

    $thumb = $env:CODE_SIGN_CERT_THUMBPRINT
    if (-not $thumb) { return $false }

    $signtool = Find-SignTool
    if (-not $signtool) {
        throw "signtool.exe not found. Install the Windows 10/11 SDK."
    }

    Write-Host "Signing with certificate thumbprint $thumb..."
    & $signtool sign /v /fd SHA256 /tr $timestampUrl /td SHA256 /sha1 $thumb $Path
    if ($LASTEXITCODE -ne 0) {
        throw "signtool failed with exit code $LASTEXITCODE"
    }
    return $true
}

$signed = $false
if (Invoke-AzureArtifactSigning -Path $FilePath) { $signed = $true }
elseif (Invoke-PfxSigning -Path $FilePath) { $signed = $true }
elseif (Invoke-StoreSigning -Path $FilePath) { $signed = $true }

if (-not $signed) {
    throw @"
No signing backend configured. Set one of:

  Azure Artifact Signing (copy aio/signing.local.ps1.example to signing.local.ps1):
    ARTIFACT_SIGNING_ENDPOINT, ARTIFACT_SIGNING_ACCOUNT, ARTIFACT_SIGNING_PROFILE

  PFX file:
    CODE_SIGN_PFX_PATH  (+ optional CODE_SIGN_PFX_PASSWORD)

  Certificate store:
    CODE_SIGN_CERT_THUMBPRINT
"@
}

if (-not (Test-SignatureValid -Path $FilePath)) {
    $sig = Get-AuthenticodeSignature -LiteralPath $FilePath
    throw "Signature verification failed: $($sig.Status) - $($sig.StatusMessage)"
}

$sig = Get-AuthenticodeSignature -LiteralPath $FilePath
Write-Host "Signed successfully - $($sig.SignerCertificate.Subject)"
if ($sig.Status -ne "Valid") {
    Write-Host ""
    Write-Host "Note: Windows reports '$($sig.Status)' because this is a PrivateTrust signature."
    Write-Host "      The file IS signed and timestamped. Deploy your Artifact Signing root"
    Write-Host "      certificate via GPO/Intune so company machines trust it automatically."
    Write-Host "      (Azure Portal → certificate profile → download root certificate)"
}
