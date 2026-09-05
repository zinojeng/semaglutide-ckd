# Project instructions: Semaglutide, CKD, and FLOW

## Mission

Build the evidence review defined in `Semaglutide ckd and flow evidence prompt.md`. The evidence cutoff is 2026-09-05. Final prose is primarily Traditional Chinese (zh-TW), retaining standard English clinical terms.

## Non-negotiable evidence rules

1. Start with the local prompt and local fulltexts. Use primary publications, supplements, protocols, trial registries, official guidelines, and official regulatory labels before reviews or commentary.
2. For a current or missing source, search the web and verify the bibliographic record and result against a primary or official source. Do not invent inaccessible results.
   - Prefer the configured `research_hub`, `paper-search`, and `google-scholar` MCPs for discovery and lawful full-text routes. `openevidence` may orient a clinical question but never substitutes for the primary source.
   - Use `llamaparse` only on a PDF already obtained through an open-access, publisher-authorized, institutional/user-authorized, or otherwise lawful route. Record the route and license/access status.
   - Do not use Sci-Hub or another circumvention source. Do not claim that access implies permission to republish.
3. Every quantitative claim must carry a locator: source ID plus table, figure, supplement section, page, or exact local line range when available.
4. Keep endpoint wording exact. Never call FLOW's CV-death-inclusive primary composite a purely kidney endpoint. Separate the five-component primary outcome from kidney-specific outcomes.
5. Distinguish prespecified, post hoc, exploratory, subgroup, observational, and mechanistic evidence. A nonsignificant interaction is not proof of equivalence or additive efficacy.
6. Do not claim that semaglutide + SGLT2i or semaglutide + finerenone has proven additive hard-kidney benefit unless direct randomized evidence actually establishes it.
7. Do not infer causally independent glucose-, weight-, or BP-mediated effects from subgroup consistency alone.
8. Calculate ARR/NNT only from compatible time-specific absolute risks. State the horizon and method; otherwise label the value not estimable.
9. Cross-trial comparisons are contextual only. Do not rank therapies from HRs across dissimilar trials.
10. Treat direct renal GLP-1 receptor signaling as uncertain unless supported by defensible human evidence.

## File and collaboration contract

- Never modify `fulltext/` or the master prompt.
- Keep downloaded PDFs and full-text parses under the ignored `sources/retrieved/cache/`; the public repository receives only metadata, provenance, short evidence notes, and links unless redistribution rights are explicit.
- During Wave 1, write only to your assigned file in `research/semaglutide_ckd_flow/2026-09-05/lanes/` and, if needed, add retrieved-source notes under `sources/retrieved/` using a role-prefixed filename.
- During Wave 2, read the named peer memo and write only to your assigned file in `cross_reviews/`. Address the peer's strongest and weakest claim, unresolved numerical conflicts, and exact correction wording.
- Only the director/reconciler may write required numbered deliverables `01_...` through `15_...` and `SOURCE_LEDGER.csv`.
- `16_FINAL_SYNTHESIS_ZH_TW.md` may be written only after `15_CLAIM_EVIDENCE_MAP.md` and the explicit “What we know / What we think / What we still do not know” gate exist.
- `17_RED_TEAM_QA.md` belongs only to the independent Wave 5 red-team reviewer. After the owning director acknowledges that report, the root coordinator may write `18_RED_TEAM_CLOSURE.md` solely to record verified dispositions and the separate clinical, process, and publication gates; it must not introduce or re-adjudicate clinical claims.
- Do not commit, push, delete, rename, or rewrite other sessions' files.
- Never print, message, log, or commit API keys. The configured LlamaParse MCP reads its credential from a local mode-600 key file; use the MCP without reproducing the credential.
- At the end of each turn, summarize: files written, sources actually checked, unresolved conflicts, and the next session that needs your evidence.

## Citation and uncertainty style

- Use stable IDs such as `FLOW-PRIMARY-2024`, `FLOW-SGLT2-2024`, `SELECT-KIDNEY-2024`, `SOUL-KIDNEY-2026`.
- Link DOI, PubMed, journal, registry, or official regulatory/guideline page wherever available.
- Prefer calibrated language: established; strongly supported; suggestive; hypothesis-generating; unknown.
- If the full source cannot be verified, say so explicitly and do not promote the claim above provisional status.

## Safety

This is clinician-facing academic material, not patient-specific advice. Preserve nuance for advanced CKD, frailty, sarcopenia, dehydration/prerenal AKI, hypoglycemia with insulin or sulfonylurea, retinopathy, gastroparesis, and dialysis evidence gaps.
