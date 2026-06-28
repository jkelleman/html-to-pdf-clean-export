from __future__ import annotations

import argparse
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright


def format_size(path: Path) -> str:
    size = path.stat().st_size
    units = ["B", "K", "M", "G"]
    value = float(size)
    for unit in units:
        if value < 1024 or unit == units[-1]:
            if unit == "B":
                return f"{int(value)}{unit}"
            return f"{value:.0f}{unit}"
        value /= 1024
    return f"{size}B"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export one or more HTML files to PDFs without Chrome print headers or footers.",
    )
    parser.add_argument("--chrome", required=True, help="Path to the Chrome or Chromium executable.")
    parser.add_argument(
        "--mapping",
        action="append",
        default=[],
        metavar="HTML=PDF",
        help="Map an input HTML file to an output PDF file. Can be repeated.",
    )
    parser.add_argument("--margin-top", default="0.4in")
    parser.add_argument("--margin-bottom", default="0.4in")
    parser.add_argument("--margin-left", default="0.5in")
    parser.add_argument("--margin-right", default="0.5in")
    return parser.parse_args()


def parse_mapping(raw_mapping: str) -> tuple[Path, Path]:
    try:
        html_path, pdf_path = raw_mapping.split("=", 1)
    except ValueError as exc:
        raise ValueError(f"Invalid mapping '{raw_mapping}'. Expected HTML=PDF.") from exc

    input_file = Path(html_path).expanduser().resolve()
    output_file = Path(pdf_path).expanduser().resolve()
    return input_file, output_file


def export_all(args: argparse.Namespace) -> int:
    mappings = [parse_mapping(raw_mapping) for raw_mapping in args.mapping]
    if not mappings:
        print("No mappings were provided.", file=sys.stderr)
        return 1

    chrome_path = Path(args.chrome).expanduser().resolve()
    if not chrome_path.is_file():
        print(f"Chrome executable not found: {chrome_path}", file=sys.stderr)
        return 1

    exit_code = 0
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True, executable_path=str(chrome_path))
        page = browser.new_page()

        for input_file, output_file in mappings:
            if not input_file.is_file():
                print(f"  ✗ File not found: {input_file}")
                exit_code = 1
                continue

            output_file.parent.mkdir(parents=True, exist_ok=True)
            print(f"Converting: {input_file.name} → {output_file.name}")
            page.goto(input_file.as_uri(), wait_until="load")
            page.emulate_media(media="print")
            page.pdf(
                path=str(output_file),
                print_background=True,
                display_header_footer=False,
                prefer_css_page_size=True,
                margin={
                    "top": args.margin_top,
                    "bottom": args.margin_bottom,
                    "left": args.margin_left,
                    "right": args.margin_right,
                },
            )
            print(f"  ✓ Created: {output_file} ({format_size(output_file)})")

        browser.close()

    return exit_code


def main() -> int:
    return export_all(parse_args())


if __name__ == "__main__":
    raise SystemExit(main())