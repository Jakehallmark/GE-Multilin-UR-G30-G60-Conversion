# Smoke-test that the packaged exe starts without python.exe on PATH.
# Usage: .\aio\verify-standalone.ps1 [path\to\G30-to-G60-Converter.exe]

param(
    [string]$ExePath = (Join-Path (Split-Path $PSScriptRoot -Parent) "release\G30-to-G60-Converter.exe")
)

$ErrorActionPreference = "Stop"
$ExeName = [System.IO.Path]::GetFileNameWithoutExtension($ExePath)

if (-not (Test-Path -LiteralPath $ExePath)) {
    throw "Exe not found: $ExePath"
}

$pythonPattern = '(?i)\\python|\\pyenv|\\conda|\\miniconda|\\anaconda'
$cleanPath = ($env:PATH -split ';' | Where-Object { $_ -and ($_ -notmatch $pythonPattern) }) -join ';'

$psi = New-Object System.Diagnostics.ProcessStartInfo
$psi.FileName = $ExePath
$psi.UseShellExecute = $false
$psi.WorkingDirectory = Split-Path $ExePath -Parent
$psi.Environment["PATH"] = $cleanPath
[void]$psi.Environment.Remove("PYTHONPATH")
[void]$psi.Environment.Remove("PYTHONHOME")

$proc = [System.Diagnostics.Process]::Start($psi)
if (-not $proc) {
    throw "Failed to start $ExePath"
}

Start-Sleep -Seconds 10

$stillRunning = Get-Process -Id $proc.Id -ErrorAction SilentlyContinue
$related = Get-Process -Name $ExeName, "flet" -ErrorAction SilentlyContinue

if (-not $stillRunning -and -not $related) {
  throw "Exe exited within 10 seconds when started without Python on PATH."
}

Write-Host "OK: $ExeName started without python.exe on PATH."

$toStop = @()
if ($stillRunning) { $toStop += $stillRunning }
if ($related) { $toStop += $related }
foreach ($p in ($toStop | Sort-Object Id -Unique)) {
    Stop-Process -Id $p.Id -Force -ErrorAction SilentlyContinue
}
