# Cross-session research orchestration

## Objective

Run independent Claude Code sessions as a structured clinical evidence team. The sessions communicate through durable lane memos, adversarial cross-reviews, and explicit resumed-session handoffs. This preserves provenance and makes disagreements visible before synthesis.

## Roles

| Session | Role | Wave 1 artifact | Main responsibility |
|---|---|---|---|
| `flow-source-librarian` | source librarian | `lanes/01_source_librarian.md` | source inventory, identifiers, evidence classification, ledger rows |
| `flow-trialist` | nephrology trialist/statistician | `lanes/02_trialist_statistics.md` | FLOW anatomy, endpoints, event counts, slope, early stop, ARR/NNT |
| `flow-nephrologist` | senior nephrologist | `lanes/03_nephrology.md` | kidney interpretation, advanced CKD/dialysis, safety, evidence gaps |
| `flow-endocrinologist` | senior endocrinologist | `lanes/04_endocrinology.md` | pre-/post-FLOW evolution, glycemia/weight, patient phenotypes |
| `flow-ckm` | cardio-kidney-metabolic specialist | `lanes/05_ckm_combinations.md` | SGLT2i, RASi, MRA/finerenone, CV/HF, guidelines/regulation |
| `flow-methodologist` | evidence methodologist/mechanist | `lanes/06_methods_mechanisms.md` | causal claims, mediation, mechanisms, multiplicity, class effect |
| `flow-director` | research director/reconciler | numbered deliverables | resolve conflicts and integrate files 01-15 |
| `flow-editor` | clinician-editor | `16_FINAL_SYNTHESIS_ZH_TW.md` | readable Traditional Chinese synthesis after evidence gate |
| `flow-red-team` | adversarial reviewer | `17_RED_TEAM_QA.md` | numerical, citation, inference, and clinical-safety audit |

## Wave sequence

1. **Wave 0 – setup:** fingerprint local sources; initialize Git; record Claude Code version and session IDs.
2. **Wave 1 – independent research:** six specialist sessions work in parallel, each in a non-overlapping lane file.
3. **Wave 2 – cross-examination:** resume the same sessions and assign peer reviews:
   - trialist reviews nephrology claims;
   - nephrologist reviews trial statistics and applicability;
   - endocrinologist reviews CKM sequencing;
   - CKM specialist reviews endocrinology positioning;
   - methodologist reviews combination/causal claims;
   - librarian audits citation completeness across all lanes.
4. **Wave 3 – reconciliation:** director reads all lane and review files, resolves conflicts against primary sources, and creates `01`–`15` plus `SOURCE_LEDGER.csv`.
5. **Wave 4 – synthesis:** editor reads only reconciled deliverables and writes `16_FINAL_SYNTHESIS_ZH_TW.md`.
6. **Wave 5 – red team:** a separate session checks every headline number and high-stakes inference. The director receives the red-team report through a resumed-session prompt and applies only verified corrections.
7. **Wave 6 – deterministic QA:** check required files, links/DOIs, CSV schema, forbidden overclaims, empty placeholders, and Git diff; then run an independent Claude worktree review.

## Cross-session message protocol

Every handoff must name exact files and ask for one of these message types:

- `CHALLENGE`: identify an unsupported or overstated claim and propose replacement wording.
- `CONFLICT`: list two inconsistent numbers/definitions with exact source locators.
- `CONFIRM`: independently reproduce a number or classification.
- `GAP`: identify a population, endpoint, guideline, or safety issue still unsupported.

Reviews must separate factual corrections from interpretive disagreements. The director records each material dispute and resolution in `12_EVIDENCE_GAPS_AND_CONTROVERSIES.md` or `15_CLAIM_EVIDENCE_MAP.md`.

## Completion gate

The project is complete only when all required files exist, all headline quantitative claims are traceable to a primary source, uncertain 2026 items are correctly labeled, combination-therapy limitations are explicit, and the red-team blockers are resolved or transparently retained as uncertainty.

