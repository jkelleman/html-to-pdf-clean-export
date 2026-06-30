# What a Broken PDF Export Revealed About Product Trust

*A small tooling failure, a better abstraction, and what reliable systems owe their users.*

When I exported the PDF, the document looked polished enough at first glance.

Then I noticed what the system had quietly added.

- A timestamp in the header.
- The page title at the top.
- A local `file:///...` path in the footer.

I hadn't asked for any of that. But it was there, embedded in an artifact meant to be shared.

At one level, this was a small bug in an HTML-to-PDF workflow.

At another, it exposed something more important: product trust often breaks in exactly this way. Not through catastrophic failure, but through seemingly minor moments when a system adds behavior the user did not intend, did not authorize, and may not even notice until it is too late.

That kind of failure interests me because it sits at the boundary between implementation detail and human confidence. The problem was not only that the PDF looked wrong. The deeper problem was that the system had violated the user's mental model of what "export" should mean.

So I fixed it, packaged the fix into a small open-source utility, and published it.

But the real lesson was not about PDFs.

It was about what reliable systems owe their users.

![Before vs After](https://raw.githubusercontent.com/jkelleman/html-to-pdf-clean-export/main/docs/assets/before-after.png)

*Chrome CLI leaked visible print chrome into the exported PDF. The Playwright-based export did not.*

## A Small Failure With Bigger Implications

It is easy to dismiss a leaked footer or header as formatting noise.

But that framing misses the real issue.

If a user exports a document, the system should not quietly append machine-local metadata. It should not decide to include a timestamp, a page title, or a local file path unless the user explicitly wants that output.

Once a tool starts adding visible information outside the user's intent, the failure is no longer cosmetic. It becomes structural.

This matters in at least three ways.

First, it is a reliability problem. The output is no longer a faithful representation of the source.

Second, it is a privacy problem. Local file paths and machine-generated context can leak information that was never meant to travel with the document.

Third, it is a product problem. The system is no longer behaving in a way that feels stable, predictable, or legible.

That last point matters a lot to me.

A surprising amount of product quality comes down to whether the system behaves in a way that preserves user intent without forcing the user to reason about irrelevant internal machinery. People should not need to understand browser print internals in order to trust a PDF export.

And yet that is exactly what this bug was asking of me.

### Why the leak matters

- The output is no longer a faithful representation of the source.
- Local file paths can expose implementation details the user never meant to share.
- The product feels less stable, predictable, and trustworthy.

### What users actually expect

- Export should preserve intent, not add machine-local noise.
- Polished artifacts should be safe to share by default.
- The system should hide incidental complexity, not export it.

## The Wrong Abstraction Usually Reveals Itself Indirectly

The original export flow used a common pattern: render HTML, call Chrome in headless mode, and print to PDF through CLI flags.

On paper, that seemed reasonable. The workflow was simple, scriptable, and widely used.

It was also the wrong abstraction for what I actually needed.

I tried the obvious fixes first. Header and footer template flags. Margin adjustments. Blink settings that implied more control than they delivered. Each attempt suggested the surface should be capable of clean output. None actually gave me the guarantee I needed.

That was the real signal.

When a tool appears expressive enough to solve the problem, but continues to behave inconsistently where precision matters, I stop asking how to force it harder and start asking whether I am solving the problem at the wrong layer.

That shift is often where the actual design problem becomes visible.

The issue was not that I had missed the right shell incantation. The issue was that I was using a print-oriented CLI surface for a task that required a more dependable programmatic contract.

```text
HTML source -> Chrome CLI print path -> PDF with leaked print chrome
HTML source -> Playwright page.pdf() -> Clean PDF output
```

## The Better Fix Was to Move to a Better Surface

I replaced Chrome's CLI print flow with Playwright's PDF API.

The code change was relatively small. The systems difference was substantial.

Instead of relying on a shell-level print path that kept leaking unwanted behavior into the output, I moved to an interface designed for programmatic control over PDF generation.

That gave me a more truthful export model:

- render the HTML
- preserve backgrounds and styling
- generate the PDF through the browser's PDF API
- explicitly disable visible browser-generated header and footer content

The result was not just a cleaner PDF.

It was a cleaner contract.

That distinction matters.

A workaround can hide a symptom. A better abstraction changes what the system can reliably promise.

And in my experience, that is where a lot of good systems work lives: not in layering more logic over unstable surfaces, but in recognizing when the current surface is the problem.

## What Product Trust Actually Looks Like

People often talk about trust in product terms that are large and abstract: safety, quality, transparency, reliability.

But trust is often built or broken in much smaller moments.

It lives in whether a system does what it appears to do.

It lives in whether hidden behavior leaks into visible output.

It lives in whether users have to compensate for unstable abstractions.

That is why I do not think of this as a minor formatting fix.

It is a small case study in a broader principle: trustworthy systems do not merely complete tasks. They preserve meaning.

> The interesting work was not suppressing a bad footer. It was choosing a surface that could actually honor the output standard I cared about.

## Why I Turned the Fix Into an Open-Source Tool

I only publish small utilities when the underlying lesson seems broader than the original workflow.

This one clearly was.

A lot of people generate PDFs from HTML for resumes, reports, portfolios, invoices, internal documentation, and application materials. Many of those workflows depend on an implicit assumption: if the document looks correct in the browser, the export path will probably behave.

That assumption is weaker than it should be.

So I wanted to publish something more reusable than a local fix. I wanted a small tool, a visible before-and-after example, and a clear articulation of the actual failure mode.

The resulting utility is called **html-to-pdf-clean-export**.

It uses Playwright's PDF API instead of Chrome's `--print-to-pdf` CLI path, and I built the public repo to reflect the same principles as the fix itself: clear behavior, minimal leakage, safe examples, and explicit explanation.

I even used a non-personal, sports-themed sample asset for the public screenshots so the demonstration would feel current without exposing private documents or relying on branded media.

That detail mattered to me too.

If you are publishing a fix about leakage and trust, the artifact should embody that same standard.

## The Broader Lesson

The older I get, the less interested I am in systems that merely work under favorable assumptions.

I care more about systems that behave honestly.

Systems that do not smuggle implementation details into user-facing outputs.

Systems that let people build accurate mental models.

Systems that reduce the amount of hidden behavior users have to absorb.

The visible bug here was a broken PDF export.

The deeper problem was a system making promises at the interface layer that it could not reliably keep.

That is usually the kind of systems work I want to do.

If you've run into similar cases where a seemingly minor tooling issue turned out to reveal a deeper abstraction or trust problem, I'd love to hear about it.

Repo: [html-to-pdf-clean-export](https://github.com/jkelleman/html-to-pdf-clean-export)

## Suggested Medium Setup

- **Title:** What a Broken PDF Export Revealed About Product Trust
- **Subtitle:** A small tooling failure, a better abstraction, and what reliable systems owe their users.
- **Tags:** software-engineering, developer-tools, product-design, playwright, python

## Paste Notes

- Paste this directly into Medium if you want the cleanest structure retention.
- Upload the screenshot manually if Medium does not preserve the embedded image.
- If Medium flattens the monospace code block, convert the two-line flow into a quote or simple bullet comparison.
