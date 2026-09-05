# Audit of the reference `academic-research-agents` repository

**Repository inspected:** `https://github.com/zinojeng/academic-research-agents.git`

**Inspected commit:** `c2b28fc1b082aca1b1e151a2fca9fe456218b16d`

## Decision

Use the repository only as a conceptual reference for role separation, workflow stages, message correlation, parallel database discovery, and PRISMA-style query logging. Do **not** run its setup script or use it as the evidence retrieval/parsing implementation.

The inspected commit is largely a scaffold:

- PubMed, arXiv, and Semantic Scholar search functions return empty placeholders.
- The PDF parser returns empty text and metadata.
- Screening and several synthesis functions are placeholders; one eligibility function accepts every record.
- The advertised MCP server is a FastAPI/uvicorn REST service rather than an MCP JSON-RPC stdio/SSE implementation.
- It contains no implemented LlamaParse, Unpaywall, OpenAlex, PMC, or Europe PMC pipeline.
- Its setup/config files contain a tracked plaintext third-party credential and can overwrite Claude configuration. They must not be executed or imported.

The repository's MIT license applies to its code only, not to any papers discovered or downloaded through it.

## Safe replacement used here

This project uses the already configured and health-checked user-scope MCPs:

- `research_hub` for literature retrieval workflows;
- `paper-search` for Crossref, PubMed, Europe PMC, and related metadata/search routes;
- `google-scholar` as supplemental discovery;
- `openevidence` only for orientation, never as the primary evidence source;
- `llamaparse` for authorized PDF-to-Markdown conversion.

Primary identifiers and outcomes are independently checked against publisher, PubMed/PMC, trial registry, guideline society, or regulator sources. No Sci-Hub or access-control circumvention is permitted.

## Reusable design concepts

The following ideas are retained in rewritten form:

1. persistent specialist roles with non-overlapping outputs;
2. stage gates with required inputs and expected outputs;
3. correlation/session IDs for traceable cross-session messages;
4. parallel discovery with the originating database recorded per result;
5. reproducible queries, timestamps, deduplication, and screening counts;
6. a separate source ledger and claim-evidence map.

## Credential rule

Credentials belong in a local Keychain, secret manager, or permission-restricted key file and must be inherited by the MCP process. They must never be committed, embedded in MCP JSON, copied into a Claude prompt, or sent between sessions. Any credential pasted into a chat or found tracked in a repository should be rotated.
