"""
pdf_export.py — PDF Export via Playwright

Generates A4 PDF from rendered HTML using a headless Chromium browser.
Ensures the HTML/CSS is identical to what's shown on screen.

Usage:
    from pdf_export import export_pdf
    export_pdf("output/lecture.html", "output/lecture_v1.pdf")
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional


def export_pdf(
    html_path: str | Path,
    output_path: str | Path,
    format: str = "A4",
    margin_top: str = "20mm",
    margin_bottom: str = "20mm",
    margin_left: str = "18mm",
    margin_right: str = "18mm",
    print_background: bool = True,
    landscape: bool = False,
    timeout: int = 30000,
) -> Path:
    """Convert an HTML file to PDF using Playwright.

    Args:
        html_path: Path to the input HTML file (absolute or relative).
        output_path: Path for the generated PDF.
        format: Paper format (default: 'A4').
        margin_top: Top margin (default: '20mm').
        margin_bottom: Bottom margin (default: '20mm').
        margin_left: Left margin (default: '18mm').
        margin_right: Right margin (default: '18mm').
        print_background: Include background colors/graphics (default: True).
        landscape: Landscape orientation (default: False).
        timeout: Navigation timeout in ms (default: 30000).

    Returns:
        Path to the generated PDF file.
    """
    html_path = Path(html_path).resolve()
    output_path = Path(output_path).resolve()

    if not html_path.exists():
        raise FileNotFoundError(f"HTML file not found: {html_path}")

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Use file:// URL to load local HTML
    html_url = html_path.as_uri()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        raise ImportError(
            "Playwright is required for PDF export.\n"
            "Install it with: pip install playwright\n"
            "Then: python -m playwright install chromium"
        )

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1200, "height": 900},
            device_scale_factor=2,
        )
        page = context.new_page()

        try:
            page.goto(html_url, wait_until="networkidle", timeout=timeout)

            # Wait for KaTeX to render if present
            try:
                page.wait_for_function(
                    "typeof renderMathInElement !== 'undefined' || "
                    "document.querySelector('.katex') !== null",
                    timeout=5000,
                )
            except Exception:
                pass  # KaTeX not loaded — continue

            # Wait a bit more for iframes (graphs) to load
            page.wait_for_timeout(2000)

            # Generate PDF
            page.pdf(
                path=str(output_path),
                format=format,
                print_background=print_background,
                landscape=landscape,
                margin={
                    "top": margin_top,
                    "bottom": margin_bottom,
                    "left": margin_left,
                    "right": margin_right,
                },
            )

        finally:
            browser.close()

    return output_path


def export_pdf_thumbnail(
    html_path: str | Path,
    output_path: str | Path,
    width: int = 1200,
    height: int = 900,
    timeout: int = 30000,
) -> Path:
    """Generate a PNG screenshot/thumbnail of an HTML page.

    Useful for preview before PDF generation.

    Args:
        html_path: Path to the input HTML file.
        output_path: Path for the output PNG.
        width: Screenshot width (default: 1200).
        height: Screenshot height (default: 900).
        timeout: Navigation timeout in ms (default: 30000).

    Returns:
        Path to the generated PNG file.
    """
    html_path = Path(html_path).resolve()
    output_path = Path(output_path).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    html_url = html_path.as_uri()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        raise ImportError("Playwright is required for screenshots.")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": width, "height": height},
            device_scale_factor=2,
        )
        page = context.new_page()

        try:
            page.goto(html_url, wait_until="networkidle", timeout=timeout)
            page.wait_for_timeout(2000)

            # Full page screenshot
            page.screenshot(path=str(output_path), full_page=True)
        finally:
            browser.close()

    return output_path


# ──────────────── CLI Test ────────────────

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: python pdf_export.py <input.html> <output.pdf>")
        sys.exit(1)

    output = export_pdf(sys.argv[1], sys.argv[2])
    print(f"✅ PDF generated: {output}")
    print(f"   Size: {output.stat().st_size / 1024:.1f} KB")
