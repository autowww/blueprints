# SDL/tools — shared generator utilities

## `forge_static_capture`

Python helpers for **loopback static HTTP** + **Playwright** screenshots (used by Forge SDLC site, Forge Lenses docs/previews, Situ8-web marketing previews).

### Setup

```bash
pip install playwright
playwright install chromium
```

### Import from a consumer repo

Ensure the repo has the **blueprints** submodule checked out, then add `blueprints/sdlc/tools` to `sys.path` before importing:

```python
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]  # adjust depth to repo root
BP_TOOLS = REPO_ROOT / "blueprints" / "sdlc" / "tools"
sys.path.insert(0, str(BP_TOOLS))

from forge_static_capture import (
    PlaywrightCaptureSession,
    capture_url_to_png,
    start_preview_server,
)
```

### API

- **`start_preview_server(root_dir, host="127.0.0.1", port_min=…, port_max=…)`** — Serves a directory over HTTP on the first free port in the range. Shut down with `httpd.shutdown()` and `httpd.server_close()` when done.
- **`capture_url_to_png(url, path, viewport_size=(w,h), full_page=False, …)`** — One-shot capture (launches Chromium each call).
- **`PlaywrightCaptureSession`** — Context manager; call `.capture(...)` many times with **one** browser launch (use for batch site screenshots).

Optional Chromium flags: environment variable **`FORGE_SCREENSHOT_CHROME_FLAGS`** (shell-split, appended after `--force-device-scale-factor=1`).
