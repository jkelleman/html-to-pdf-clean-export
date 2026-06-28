# Screenshot Guide

Use the included `examples/2026-football-preview.html` file for screenshots if you want something timely without exposing personal documents.

## Why this example works

- it feels current
- it is fully original
- it does not expose personal names or local work artifacts
- it avoids official tournament logos, marks, or copyrighted media

## Important note

Avoid using official FIFA branding, logos, mascots, or copied marketing assets in the repo screenshot unless you have a clear right to do so.

For a public open-source utility, a generic football-themed sample is the safer choice.

## Recommended comparison layout

Create a side-by-side image with:

- `Before` on the left
- `After` on the right

Left side:

- label: `Chrome --print-to-pdf`
- show leaked timestamp or page title at the top
- show leaked `file:///...` path at the bottom

Right side:

- label: `html-to-pdf-clean-export`
- same content area
- no visible browser-generated header or footer text

## Suggested command for the clean version

```bash
python export_html_to_pdf.py \
  --chrome "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --mapping "examples/2026-football-preview.html=output/2026-football-preview.pdf"
```

## Suggested visual annotation

- red outline around the broken header and footer on the left
- green outline or check mark on the clean right side
- tight crop so the problem is visible immediately on GitHub and social