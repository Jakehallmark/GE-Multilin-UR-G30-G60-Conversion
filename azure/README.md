# Azure Function — G30 to G60 Converter

HTTP API wrapper around the desktop `convert_g30_to_g60.py` converter. Accepts a G30 settings XML file and returns a ZIP containing the converted G60 XML and `_OR.html` report.

Used with **SharePoint → Power App → Power Automate** for browser-based conversion. The desktop `.bat` workflow in the repo root is unchanged.

## Layout

```
azure/
  deploy.ps1                 # Sync, zip, and deploy (recommended)
  sync-from-root.ps1         # Copy converter + G60 Base.xml from repo root
  diagnose-deploy.ps1        # SCM auth, storage roles, publish profile checks
  enable-scm-auth.ps1        # Turn on SCM Basic Auth for zip deploy
  allow-scm-ip.ps1           # Add current public IP to SCM allow list
  fix-flex-deploy.ps1        # Flex Consumption: UAMI blob write on deployment storage
  function_app/
    function_app.py          # POST /api/convert
    convert_g30_to_g60.py    # Synced copy from repo root
    G60 Base.xml             # Synced copy from repo root
    host.json
    requirements.txt
```

## Prerequisites

| Tool | Purpose |
|------|---------|
| [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli-windows) | `az login`, `.\azure\deploy.ps1` |
| Azure Functions extension (VS Code) | Optional deploy from IDE |
| [Functions Core Tools](https://learn.microsoft.com/azure/azure-functions/functions-run-local) | Optional local `func start` |

## First-time setup

From the repo root:

```powershell
.\azure\sync-from-root.ps1
```

Copy local settings for optional local run:

```powershell
Copy-Item azure\function_app\local.settings.json.example azure\function_app\local.settings.json
cd azure\function_app
pip install -r requirements.txt
func start
```

Local endpoint: `POST http://localhost:7071/api/convert`

## Deploy

**Recommended:** Linux **Consumption** plan (not Flex Consumption) unless your tenant requires Flex. Flex needs extra storage identity setup; see `fix-flex-deploy.ps1`.

```powershell
az login
.\azure\deploy.ps1 -FunctionAppName <your-function-app-name> -ResourceGroup <your-rg>
```

If deploy returns **403** from `*.scm.*.azurewebsites.net`:

1. Portal → Function App → Configuration → General settings → **SCM Basic Auth** ON → **Apply** → **Restart**
2. `.\azure\enable-scm-auth.ps1`
3. `.\azure\allow-scm-ip.ps1`
4. On Flex: `.\azure\fix-flex-deploy.ps1`
5. `.\azure\diagnose-deploy.ps1` to verify

For a full IT provisioning brief, see [docs/IT-Ticket-Azure-Function-G30-G60-Converter.pdf](../docs/IT-Ticket-Azure-Function-G30-G60-Converter.pdf).

## Test deployed function

```powershell
curl -X POST "https://<app>.azurewebsites.net/api/convert?code=<FUNCTION_KEY>" `
  -F "file=@path\to\your-g30-file.xml" `
  -o converted.zip
```

Success: HTTP 200, `application/zip` with `.xml` and `_OR.html`.

## Keep in sync with desktop converter

When `convert_g30_to_g60.py` or `G60 Base.xml` changes at the repo root:

```powershell
.\azure\sync-from-root.ps1
.\azure\deploy.ps1 -FunctionAppName <app> -ResourceGroup <rg>
```

Do not commit `local.settings.json` (gitignored).
