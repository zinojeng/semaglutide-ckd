# Semaglutide in CKD: FLOW evidence project

This repository contains a source-grounded, multi-session clinical evidence review of semaglutide in chronic kidney disease, centered on FLOW and updated through 2026-09-05.

The research brief is [`Semaglutide ckd and flow evidence prompt.md`](./Semaglutide%20ckd%20and%20flow%20evidence%20prompt.md). Read either the single merged Traditional Chinese article, [`16_FINAL_SYNTHESIS_ZH_TW.md`](./research/semaglutide_ckd_flow/2026-09-05/16_FINAL_SYNTHESIS_ZH_TW.md), or the [five-part Traditional Chinese clinical series](./research/semaglutide_ckd_flow/2026-09-05/articles_zh_tw/README.md). The public-safe [`19_WAVE4_PEER_REVIEW_ADDENDUM_ZH_TW.md`](./research/semaglutide_ckd_flow/2026-09-05/19_WAVE4_PEER_REVIEW_ADDENDUM_ZH_TW.md) records the five issues resolved through genuine nephrology, endocrinology, and methodology cross-session dialogue. A separate [Traditional Chinese presentation evidence pack](./research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/README.md) provides a 25-slide storyboard, dual-specialty speaker notes, exact Table/Figure/page locators, editable chart-data CSVs, image-rights rules, and a small set of explicitly licensed public visuals.

Local primary papers, supplements, and authorized PDF-to-Markdown parses are deliberately Git-ignored and are not included in this public repository. Public availability of this synthesis does not grant reuse rights to any cited third-party article, guideline, label, protocol, or supplement.

The private `fulltext/` source corpus is guarded read-only by [`scripts/source_corpus_guard.sh`](./scripts/source_corpus_guard.sh); public clones intentionally lack those files, which the guard treats as expected. The tracked presentation deliverables can be checked separately with [`scripts/verify_presentation_pack.sh`](./scripts/verify_presentation_pack.sh).

The public `main` branch is released as a curated, single-root snapshot so superseded local history, internal session logs, private source files, and rights-restricted screenshots are not exposed. The exact inclusion and exclusion boundary is documented in [`PUBLICATION_NOTES.md`](./PUBLICATION_NOTES.md).

On the curated public branch, run `./scripts/verify_public_snapshot.sh --strict-curated` to enforce that boundary and re-run the presentation checks.

The workflow uses persistent Claude Code sessions with distinct clinical and methodological roles. Each lane first produces an independent evidence memo, then reviews another lane, and only then may the director reconcile the evidence and commission the Traditional Chinese synthesis. A first Wave 4 contact attempt failed transparently; a second permission-compatible run completed five genuine challenge/response/rejoinder chains and corrected the public synthesis. See [`ORCHESTRATION.md`](./research/semaglutide_ckd_flow/2026-09-05/orchestration/ORCHESTRATION.md) and the public peer-review addendum above.

Missing literature is resolved through connected research MCPs and a copyright-aware acquisition log. Authorized PDFs may be converted to private, Git-ignored Markdown with LlamaParse; full-text files are not republished merely because they are readable. See [`ACQUISITION_POLICY.md`](./research/semaglutide_ckd_flow/2026-09-05/sources/ACQUISITION_POLICY.md).

This material is an academic evidence synthesis, not individualized medical advice.
