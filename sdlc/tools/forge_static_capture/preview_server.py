"""Short-lived loopback HTTP server for static directories (site previews, doc captures)."""

from __future__ import annotations

import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def _make_handler_class(directory: Path) -> type[SimpleHTTPRequestHandler]:
    root = str(directory.resolve())

    class _SilentHandler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=root, **kwargs)

        def log_message(self, format: str, *args) -> None:  # noqa: A003
            pass

    return _SilentHandler


def start_preview_server(
    root_dir: Path,
    *,
    host: str = "127.0.0.1",
    port_min: int,
    port_max: int,
) -> tuple[ThreadingHTTPServer, int] | None:
    """Bind the first free port in ``port_min``..``port_max``; serve ``root_dir``; return server and port."""
    Handler = _make_handler_class(root_dir)
    for port in range(port_min, port_max + 1):
        try:
            httpd = ThreadingHTTPServer((host, port), Handler)
        except OSError:
            continue
        thread = threading.Thread(target=httpd.serve_forever, daemon=True)
        thread.start()
        return httpd, port
    return None
