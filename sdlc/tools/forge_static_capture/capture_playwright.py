"""Headless PNG screenshots via Playwright (viewport or full-page scroll height)."""

from __future__ import annotations

import os
import shlex
from pathlib import Path


def _launch_args_from_env() -> list[str]:
    """Base Chromium flags plus optional ``FORGE_SCREENSHOT_CHROME_FLAGS`` (shell-split)."""
    out = ["--force-device-scale-factor=1"]
    raw = os.environ.get("FORGE_SCREENSHOT_CHROME_FLAGS", "").strip()
    if raw:
        out.extend(shlex.split(raw))
    return out


class PlaywrightCaptureSession:
    """Single ``chromium.launch``; reuse one browser context and page for multiple URLs."""

    def __init__(self, *, launch_args: list[str] | None = None) -> None:
        self._launch_args = launch_args if launch_args is not None else _launch_args_from_env()
        self._pw = None
        self._browser = None
        self._context = None
        self._page = None

    def __enter__(self) -> PlaywrightCaptureSession:
        from playwright.sync_api import sync_playwright

        self._pw = sync_playwright().start()
        self._browser = self._pw.chromium.launch(
            headless=True,
            args=self._launch_args,
        )
        return self

    def __exit__(self, *args: object) -> None:
        if self._page:
            try:
                self._page.close()
            except Exception:
                pass
            self._page = None
        if self._context:
            try:
                self._context.close()
            except Exception:
                pass
            self._context = None
        if self._browser:
            try:
                self._browser.close()
            except Exception:
                pass
            self._browser = None
        if self._pw:
            try:
                self._pw.stop()
            except Exception:
                pass
            self._pw = None

    def _ensure_page(self, viewport_width: int, viewport_height: int) -> None:
        if self._context is None:
            self._context = self._browser.new_context(
                viewport={"width": viewport_width, "height": viewport_height},
                device_scale_factor=1,
            )
            self._page = self._context.new_page()
        else:
            self._page.set_viewport_size({"width": viewport_width, "height": viewport_height})

    def capture(
        self,
        url: str,
        output_path: Path,
        *,
        viewport_size: tuple[int, int],
        full_page: bool = False,
        goto_timeout_ms: int = 90_000,
        settle_ms: int = 400,
    ) -> bool:
        """Navigate to ``url`` and write a PNG. ``viewport_size`` is (width, height) for viewport mode."""
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        vw, vh = int(viewport_size[0]), int(viewport_size[1])
        inner_h = 800 if full_page else vh
        try:
            self._ensure_page(vw, inner_h)
            assert self._page is not None
            self._page.goto(url, wait_until="load", timeout=goto_timeout_ms)
            if settle_ms > 0:
                self._page.wait_for_timeout(settle_ms)
            self._page.screenshot(
                path=str(output_path),
                full_page=full_page,
                scale="css",
            )
            return output_path.is_file()
        except Exception:
            return False


def capture_url_to_png(
    url: str,
    output_path: Path,
    *,
    viewport_size: tuple[int, int] = (1280, 900),
    full_page: bool = False,
    goto_timeout_ms: int = 90_000,
    settle_ms: int = 400,
    launch_args: list[str] | None = None,
) -> bool:
    """Launch Chromium, capture one URL, exit. Prefer :class:`PlaywrightCaptureSession` for batches."""
    try:
        session = (
            PlaywrightCaptureSession(launch_args=launch_args)
            if launch_args is not None
            else PlaywrightCaptureSession()
        )
        with session:
            return session.capture(
                url,
                output_path,
                viewport_size=viewport_size,
                full_page=full_page,
                goto_timeout_ms=goto_timeout_ms,
                settle_ms=settle_ms,
            )
    except ImportError:
        return False
    except Exception:
        return False
