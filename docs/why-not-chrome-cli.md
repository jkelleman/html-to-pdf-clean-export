# Why Not Chrome CLI?

Chrome's headless `--print-to-pdf` flow looks convenient, but it can still produce visible browser-generated print artifacts in exported PDFs.

Common symptoms include:

- a timestamp in the header
- the page title in the header
- a local `file:///...` path in the footer

This is a problem for professional documents and public-facing assets because it can leak machine-local information or simply make the PDF look broken.

## Why Flags Are Not Always Enough

You can try combinations like:

- `--print-to-pdf-header-template=""`
- `--print-to-pdf-footer-template=""`
- `--blink-settings=displayHeaderFooter=false`

Depending on the environment and browser behavior, those may still fail to suppress the visible print header or footer.

## What This Project Does Instead

This project uses Playwright's `page.pdf()` API with:

- `display_header_footer=False`
- `print_background=True`
- `prefer_css_page_size=True`

That gives you direct control over PDF generation without relying on the flaky CLI print path.

## Practical Rule

If your output needs to be clean, shareable, or privacy-safe, do not rely on Chrome `--print-to-pdf` CLI as your production export path.