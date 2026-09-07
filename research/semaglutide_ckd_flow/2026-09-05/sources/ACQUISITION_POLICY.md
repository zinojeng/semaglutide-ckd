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

Do not use access-control circumvention. A lawfully accessible paper can be read and summarized within the applicable access terms, but its PDF or full-text extraction must not be committed to the public repository unless redistribution rights are explicit.

Access, copying, automated processing, and redistribution are separate determinations. A lawful access route may permit an authorized human reader to read and make ordinary scholarly notes; it does not by itself authorize format conversion, TDM/ML, third-party cloud upload, figure/table reuse, recording, or public distribution.

## Storage

- PDFs and full-text Markdown: `sources/retrieved/cache/` (Git-ignored).
- Short provenance/extraction notes: `sources/retrieved/` (tracked).
- Existing user-provided corpus: top-level `fulltext/` (Git-ignored and immutable).

Private or Git-ignored storage is a publication-control measure, not evidence that copying or processing was authorized. Rights-restricted or uncleared automated derivatives are processing incidents: preserve only the minimum audit record, exclude them from AI/RAG/reprocessing, and use authorized human reading plus official-page verification until a processing basis is established.

## LlamaParse

The `llamaparse` MCP is configured at user scope and reads the API credential from a local mode-600 key file. Sessions must call the MCP without echoing or copying the credential.

- Prefer repository JATS XML when available; it preserves article structure without uploading a PDF to a third-party parser.
- Before any local automated conversion or third-party cloud parsing, separately document a processing basis under the article license, applicable contract, express permission, or a documented applicable legal exception. PMC availability, subscription access, institutional login, or an internal academic purpose does not by itself satisfy this gate. If unresolved, limit use to authorized human reading, metadata/abstracts, and ordinary short scholarly notes; mark `manual_rights_review_required`.
- Record parser/server version, job ID when available, parameters, hashes, and per-page QA status.
- Verify each parse for title/authors, tables, endpoint definitions, minus signs, superscripts, confidence intervals, and two-column reading order before using numerical data.

## Copyright-safe outputs

Research artifacts should paraphrase and cite. Avoid lengthy verbatim passages, reproduced publisher figures/tables, or redistributing PDFs. Numerical facts and compact, newly structured evidence tables are acceptable when independently checked and properly cited.
