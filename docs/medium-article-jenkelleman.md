# What a Broken PDF Export Revealed About Product Trust

*A polished version in a jenkelleman voice: systems-minded, practical, and human.*

I was exporting a polished PDF from HTML when I noticed something I did not put there.

Then a few more things.

- timestamp in the header
- page title at the top
- local `file:///...` path in the footer

That moment always bothers me more than it should: not because the output looks messy, but because the system quietly crossed a boundary I did not ask it to cross.

I said export this document.

The system also exported machine-local context.

That is not polish debt. That is trust debt.

![Before vs After](https://raw.githubusercontent.com/jkelleman/html-to-pdf-clean-export/main/docs/assets/before-after.png)

For me, this kind of issue sits in the most interesting part of technical work: the seam between implementation detail and human confidence.

The user-facing task sounds simple. The underlying behavior is anything but.

## The real problem was the abstraction layer

The initial workflow used Chrome's CLI print path.

That is a common pattern, and it looked reasonable. But "looked reasonable" is not the same as "behaviorally reliable."

I tried the expected fixes: header/footer flags, margin tweaks, print settings that suggested control. None produced the output contract I needed.

That was the signal.

When I keep adding flags and still cannot guarantee behavior, I stop asking for a better workaround and start asking for a better surface.

So I moved the export path from Chrome CLI print mode to Playwright's PDF API.

Not a dramatic code rewrite. A meaningful systems rewrite.

That gave me explicit control where it mattered and removed visible browser-generated print chrome from output.

## Why I care about this category of bug

People talk about trust in big terms. Safety. Reliability. Transparency.

But trust usually breaks in small places first.

- a hidden default
- a leaky edge case
- an output artifact that carries context the user never intended to publish

This one happened to be a PDF export.

The pattern is much bigger than PDF export.

The pattern is: systems that appear stable until they meet real-world use, then offload complexity and risk onto the user.

That pattern shows up in developer tools, internal platforms, AI workflows, and content systems alike.

## What I shipped

I packaged the fix into a small open-source tool:

Repo: [html-to-pdf-clean-export](https://github.com/jkelleman/html-to-pdf-clean-export)

It includes:

- a Playwright-based exporter
- safe sample assets
- a visual before/after
- docs on why Chrome CLI print mode was not enough

I intentionally used non-personal sample content and screenshot flow. If the problem is about leakage, the public artifact should model the standard it argues for.

## What this taught me (again)

The most valuable engineering work is often not adding more logic.

It is choosing an abstraction that can keep the promises your product is already making.

In this case:

- the visible bug was a leaky footer
- the actual issue was contract reliability
- the fix was to move to a surface designed for dependable control

That is the kind of systems work I love: precise implementation choices in service of human trust.

> The interesting work was not suppressing a bad footer. It was choosing a surface that could actually honor the output standard I cared about.

If you have seen similar moments where a "small" tooling bug exposed a much larger trust boundary, I would genuinely love to hear about it.

## Suggested Medium Setup

- **Title:** What a Broken PDF Export Revealed About Product Trust
- **Subtitle:** A small tooling failure, a better abstraction, and what reliable systems owe their users.
- **Tags:** software-engineering, developer-tools, product-design, playwright, python
