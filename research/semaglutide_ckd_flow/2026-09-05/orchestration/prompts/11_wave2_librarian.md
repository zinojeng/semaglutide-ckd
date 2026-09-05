# Wave 2 brief — Source librarian audit

Run only after the literature-ingest metadata and rights report have landed on
canonical `main`. Work in an isolated linked worktree. Never disable background
isolation or modify `.claude/**`, `lanes/**`, numbered deliverables, or cache
contents.

Read `CLAUDE.md`, all six canonical-main lane files, all other Wave 2 reviews,
`SOURCE_ACQUISITION_LOG.csv`, `LITERATURE_INGEST_REPORT.md`, the current-evidence
audit, and the master prompt. Audit every source identity, DOI/PMID/PMCID,
article type, prespecification, access route, license/reuse decision, correction
relationship, and evidence locator. Explicitly cover:

- the three distinct FLOW severity/CV papers (EHJ 2025, CJASN 2026, JACC 2026);
- the Mahaffey local-markdown Figure 2 misassignment and required corrected
  values/locator;
- FLOW primary/supplement table-extraction artifacts;
- the two automated-download mis-resolutions and quarantine;
- restricted or unclear TDM/ML items whose LlamaParse outputs must remain
  private and must not be treated as authorized evidence;
- the FDA PI copyright notice (manufacturer labeling is not automatically a
  US-government/public-domain work), the explicit AHA/CKM reuse restriction,
  and the CC BY-NC-ND metadata versus still-blocked retrieval route for the two
  JACC FLOW analyses;
- SOUL strike-through/license-text corruption, CKM `SGLT2i` token corruption,
  SELECT's generic-form tail, and raw two-column/table-order artifacts in the
  FLOW/Mann parses;
- missing protocol/SAP/registry, primary comparator RCTs, guidelines, labels,
  and full texts;
- online-versus-print dates and label revision dates.

Use `SendMessage` to issue any `LA-*` citation or rights challenges to the
relevant role or director, and record responses if received. Do not silently
upgrade abstract-only evidence.

Write only:

`research/semaglutide_ckd_flow/2026-09-05/cross_reviews/01_librarian_audit.md`

Commit to the worktree branch and report the hash. Do not push.
