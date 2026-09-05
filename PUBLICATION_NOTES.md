# Public release notes

**Evidence cutoff:** 2026-09-05<br>
**Release purpose:** academic research, teaching, journal-club discussion, and preparation of source-grounded presentations.

## What the public snapshot contains

- The reconciled evidence chapters `01`–`16`, the public-safe Wave 4 cross-session peer-review addendum `19`, source inventory, and structured source ledger.
- A five-part Traditional Chinese clinical series.
- A Traditional Chinese presentation evidence pack: 25-slide storyboard, dual-specialty speaker notes, exact Table/Figure/page map, article reference guide, editable chart-data CSV files, and visual-rights guide.
- One unmodified source figure whose CC BY 4.0 status and attribution were independently checked. Its attribution file records the work, DOI, PMCID, license, checksum, and modification status.
- Acquisition and rights-policy documentation, plus a high-level cross-session workflow description and de-identified clinical adjudication record.

## What is deliberately excluded

- Publisher PDFs, supplements, protocols, full-text derivatives, and the private `fulltext/` corpus.
- Rights-restricted source-page screenshots and all files under retrieval/cache paths.
- API keys, MCP credentials, local absolute paths, and machine-specific configuration.
- Internal agent transcripts, session UUIDs, transport receipts, worktrees, detailed dialogue/session logs, detailed workstream scratch files, and superseded development history from the curated `main` branch.
- Original figures or tables for which public redistribution or adaptation was not verified.

The excluded source-page screenshots remain local research aids only. Public slides should use the supplied editable CSV data or newly redrawn visuals unless the visual-rights guide explicitly authorizes reuse.

## Rights and interpretation

Publication of this synthesis does not transfer or expand rights in cited articles, guidelines, labels, protocols, figures, or tables. Third-party materials remain subject to their own terms. The only bundled source image is governed by the CC BY 4.0 license stated in its adjacent `ATTRIBUTION.md`; any crop, translation, annotation, or recoloring should be labeled as an adaptation.

Every numerical slide should retain its endpoint definition, inferential status, and source locator. In particular, FLOW's confirmatory five-component primary endpoint includes cardiovascular death; the kidney-specific four-component estimate is supportive and outside the confirmatory hierarchy. Subgroup analyses do not establish treatment additivity merely because an interaction test is nonsignificant.

## Release method and validation

The public `main` branch is intentionally created from a curated new root rather than by publishing the local development history. This preserves the final academic artifacts without importing historical privacy and reuse-rights incidents into `main`.

This release assurance applies to `main` only. Five pre-existing `worktree-*` role branches were already present in the public repository before this release; they are retained unchanged, are not part of the curated academic release, and may contain obsolete drafts or internal development history. They should not be cited as release artifacts. Removing or rewriting those branches would be a separate destructive maintenance action.

Before release, the curated snapshot is checked for:

- absence of tracked PDF, XML, full-text, cache, private screenshot, and secret-like files;
- synchronized master-article SHA-256 references;
- presentation file completeness, FLOW Table/Figure/page locators, and public-image checksum;
- CSV row-width consistency and Git whitespace errors.

The release gate is executable with `./scripts/verify_public_snapshot.sh --strict-curated` from the curated public branch.

This repository is an academic evidence synthesis and not individualized medical advice.
