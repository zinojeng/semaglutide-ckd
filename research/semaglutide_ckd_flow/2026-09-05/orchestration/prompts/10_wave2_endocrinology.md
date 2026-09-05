# Wave 2 brief — Endocrinology reviews CKM

Work only in the existing `flow-endocrinologist` linked worktree. Do not modify
`.claude/**`, `lanes/**`, orchestration logs, numbered deliverables, or canonical
`main`. If a write is blocked, report the block; do not disable isolation.

Read the canonical-main versions with `git show main:<path>`:

- `research/semaglutide_ckd_flow/2026-09-05/lanes/05_ckm_combinations.md`
- `research/semaglutide_ckd_flow/2026-09-05/cross_reviews/05_ckm_reviews_endocrinology.md`
- `research/semaglutide_ckd_flow/2026-09-05/sources/retrieved/00_CODEX_CURRENT_EVIDENCE_AUDIT.md`
- `CLAUDE.md`

Use Claude Code `ListAgents` and `SendMessage` for an actual exchange with
`flow-ckm`. First answer CKM's citation/regulatory challenges, including the
Neuen citation-adjacency issue. Then send CKM one structured `CHALLENGE` that
asks it to reconcile:

1. organ protection at HbA1c goal versus glycemic escalation;
2. obesity/ASCVD/weight priorities versus kidney-specific outcomes;
3. FLOW 1 mg SC versus SELECT 2.4 mg SC versus SOUL oral 14 mg;
4. frailty, GI intolerance, dehydration, retinopathy, insulin/SU
   de-intensification, and advanced-CKD/dialysis limits;
5. whether phenotype-based sequencing is better supported than a rigid drug
   ladder.

Require a `RESPONSE` from `flow-ckm`. Record each challenge, response,
disposition, exact replacement wording, evidence grade, and source locator.
State correctly that EMA includes FLOW in SmPC section 5.1 but section 4.1
remains a T2D glycemic indication, not an independent CKD risk-reduction
indication. End with `DIALOGUE_CLOSED` only after CKM responds; otherwise mark
the item open for Wave 3.

Write only:

`research/semaglutide_ckd_flow/2026-09-05/cross_reviews/04_endocrinology_reviews_ckm.md`

Commit to the worktree branch and report the hash. Do not push.
