# Full-text acquisition and parsing policy

## Allowed routes

Use, in order:

1. publisher or journal open-access full text;
2. PubMed Central / Europe PMC JATS XML or another official repository;
3. author-accepted manuscript in a legitimate institutional repository;
4. Crossref/OpenAlex/Unpaywall links that resolve to an authorized copy;
5. access through the user's existing institutional or personal subscription.

For each acquired item, record DOI/PMID, landing page, resolved file URL, access route, license when stated, retrieval date, SHA-256, and parser status in `SOURCE_ACQUISITION_LOG.csv`.

`SOURCE_ACQUISITION_LOG.csv` is an artifact-level log for files that were locally acquired, downloaded, or parsed. Abstract-only, registry, regulatory, guideline, comparator, and other citation-only sources that produced no local artifact are tracked in `01_SOURCE_INVENTORY.md` and `SOURCE_LEDGER.csv`; they are not duplicated here as synthetic acquisition rows.

Do not use access-control circumvention. A lawfully accessible paper can be read and summarized, but its PDF or full-text extraction must not be committed to the public repository unless redistribution rights are explicit.

## Storage

- PDFs and full-text Markdown: `sources/retrieved/cache/` (Git-ignored).
- Short provenance/extraction notes: `sources/retrieved/` (tracked).
- Existing user-provided corpus: top-level `fulltext/` (Git-ignored and immutable).

## LlamaParse

The `llamaparse` MCP is configured at user scope and reads the API credential from a local mode-600 key file. Sessions must call the MCP without echoing or copying the credential.

- Prefer repository JATS XML when available; it preserves article structure without uploading a PDF to a third-party parser.
- Before uploading a subscription or otherwise restricted PDF, verify that the access terms permit third-party cloud processing. If uncertain, parse locally or mark `manual_review_required`.
- Record parser/server version, job ID when available, parameters, hashes, and per-page QA status.
- Verify each parse for title/authors, tables, endpoint definitions, minus signs, superscripts, confidence intervals, and two-column reading order before using numerical data.

## Copyright-safe outputs

Research artifacts should paraphrase and cite. Avoid lengthy verbatim passages, reproduced publisher figures/tables, or redistributing PDFs. Numerical facts and compact, newly structured evidence tables are acceptable when independently checked and properly cited.
