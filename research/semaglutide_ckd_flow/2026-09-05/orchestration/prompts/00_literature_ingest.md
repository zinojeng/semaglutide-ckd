# Session brief — Literature MCP and lawful full-text ingestion

Read `CLAUDE.md`, the master prompt, `sources/ACQUISITION_POLICY.md`, and the other lane briefs. Use the configured `research_hub`, `paper-search`, and `google-scholar` MCPs to resolve the missing primary-source list. Use official publisher, registry, guideline, regulatory, PMC/Europe PMC, institutional-repository, Crossref/OpenAlex/Unpaywall-style lawful routes. Do not use Sci-Hub or access-control circumvention. `openevidence` is supplementary orientation only.

For each high-priority missing source:

1. verify title, DOI/PMID, journal/year, study type, and prespecified/post hoc status;
2. locate the lawful full text or best official landing page;
3. if a PDF is lawfully downloadable, save it under ignored `sources/retrieved/cache/pdfs/` and record its SHA-256;
4. parse the PDF through the configured `llamaparse` MCP into ignored `sources/retrieved/cache/markdown/` without printing or copying any credential;
5. visually/textually QA the parse, especially tables, signs, CI values and two-column order;
6. update `sources/SOURCE_ACQUISITION_LOG.csv` and write a concise tracked provenance/evidence memo at `lanes/00_literature_ingest.md`.

Prioritize: FLOW design/protocol/SAP/registry, FLOW HF, JACC 2026 CV phenotypes, SUSTAIN-6/PIONEER kidney evidence, SELECT kidney, SOUL primary and kidney analysis, 2026 SELECT/FLOW/SOUL pooled analysis, Badve class meta-analysis, official FDA/EMA/Taiwan labels, KDIGO/ADA/CKM guidance, and comparator kidney RCTs.

Use `SendMessage` to notify `flow-source-librarian` and `flow-director` of the acquisition log path, newly available parses, failed retrievals, and any citation inconsistency. Never write numbered final deliverables.
