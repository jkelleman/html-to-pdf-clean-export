# What a Broken PDF Export Revealed About Product Trust

*A short version for Medium attention span.*

I exported a polished PDF from HTML and found three things that should never have been there:

- a timestamp in the header
- the page title at the top
- a local `file:///...` path in the footer

That was not a styling issue. It was a trust issue.

If I ask a system to export a document, it should preserve intent, not append machine-local noise.

![Before vs After](https://raw.githubusercontent.com/jkelleman/html-to-pdf-clean-export/main/docs/assets/before-after.png)

The original flow used Chrome CLI print flags. On paper, it looked fine. In practice, it still leaked browser print chrome.

The fix was simple and architectural: move from Chrome's CLI print path to Playwright's PDF API.

That shift gave me a cleaner contract:

- render HTML
- preserve styling
- generate PDF with explicit control
- disable visible browser-generated header/footer output

I turned the fix into a small open-source utility:

Repo: [html-to-pdf-clean-export](https://github.com/jkelleman/html-to-pdf-clean-export)

## Why this matters beyond PDFs

Small bugs like this reveal bigger systems truths.

The visible failure was a bad footer.

The deeper failure was an abstraction that looked controllable but was not dependable where it mattered.

I care about this category of work: finding where system behavior drifts from user intent, then choosing a better surface that can actually keep the promises the product is already making.

> The interesting work was not suppressing a bad footer. It was choosing a surface that could actually honor the output standard I cared about.

If you've hit similar edge cases where a small tooling glitch turned into a trust problem, I would love to compare notes.

## Suggested Medium Setup

- **Title:** What a Broken PDF Export Revealed About Product Trust
- **Subtitle:** A small tooling failure, a better abstraction, and what reliable systems owe their users.
- **Tags:** software-engineering, developer-tools, product-design, playwright, python
