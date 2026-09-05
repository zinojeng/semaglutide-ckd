# Semaglutide in CKD: FLOW evidence project

This repository contains a source-grounded, multi-session clinical evidence review of semaglutide in chronic kidney disease, centered on FLOW and updated through 2026-09-05.

## 主要產出（繁體中文）

- **[公開繁中同儕校讀增補](./research/semaglutide_ckd_flow/2026-09-05/19_WAVE4_PEER_REVIEW_ADDENDUM_ZH_TW.md)**：腎臟科、內分泌科與方法學角色完成的五項真實跨會話裁決。
- **[更新後完整繁中總論](./research/semaglutide_ckd_flow/2026-09-05/16_FINAL_SYNTHESIS_ZH_TW.md)**：FLOW、SELECT、SOUL、組合治療、安全性、機轉與雙專科觀點的整合文章。
- **[五篇繁中系列文章](./research/semaglutide_ckd_flow/2026-09-05/articles_zh_tw/README.md)**：可分篇閱讀或用於教學與演講準備。
- **[繁中演講投影片證據包](./research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/README.md)**：25 張投影片 storyboard、雙專科講稿、Table／Figure／page 定位、可編輯圖表資料與圖像授權指引。
- **[繁中投影片視覺素材總目錄](./research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/VISUAL_ASSET_CATALOG_ZH_TW.md)**：6 組可直接投影的原創重繪圖、2 張 CC BY 4.0 出版圖，以及逐圖 caption、講稿、source locator 與不可越過的解讀邊界。
- **[結構化來源帳本](./research/semaglutide_ckd_flow/2026-09-05/SOURCE_LEDGER.csv)**：來源識別碼、研究設計、終點、結果、限制與證據分級。

### 投影片視覺預覽

![FLOW 五項主要終點、四項腎臟專屬終點與個別組成](./research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn/01_flow_endpoints_forest_zh_tw@2x.png)

公開簡報素材現含 6 組繁中原創重繪圖（SVG＋3840×2160 PNG）與 2 張逐圖核實為 CC BY 4.0 的出版圖。所有圖的建議投影片、繁中圖說、30 秒講稿、source locator、授權及「不可怎麼說」均收在[視覺素材總目錄](./research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/VISUAL_ASSET_CATALOG_ZH_TW.md)。

研究任務原始規格見 [`Semaglutide ckd and flow evidence prompt.md`](./Semaglutide%20ckd%20and%20flow%20evidence%20prompt.md)。

Local primary papers, supplements, and authorized PDF-to-Markdown parses are deliberately Git-ignored and are not included in this public repository. Public availability of this synthesis does not grant reuse rights to any cited third-party article, guideline, label, protocol, or supplement.

The private `fulltext/` source corpus is guarded read-only by [`scripts/source_corpus_guard.sh`](./scripts/source_corpus_guard.sh); public clones intentionally lack those files, which the guard treats as expected. The tracked presentation deliverables can be checked separately with [`scripts/verify_presentation_pack.sh`](./scripts/verify_presentation_pack.sh).

The public `main` branch is released as a curated, single-root snapshot so superseded local history, internal session logs, private source files, and rights-restricted screenshots are not exposed. The exact inclusion and exclusion boundary is documented in [`PUBLICATION_NOTES.md`](./PUBLICATION_NOTES.md).

On the curated public branch, run `./scripts/verify_public_snapshot.sh --strict-curated` to enforce that boundary and re-run the presentation checks.

The workflow uses persistent Claude Code sessions with distinct clinical and methodological roles. Each lane first produces an independent evidence memo, then reviews another lane, and only then may the director reconcile the evidence and commission the Traditional Chinese synthesis. A first Wave 4 contact attempt failed transparently; a second permission-compatible run completed five genuine challenge/response/rejoinder chains and corrected the public synthesis. See [`ORCHESTRATION.md`](./research/semaglutide_ckd_flow/2026-09-05/orchestration/ORCHESTRATION.md) and the public peer-review addendum above.

Missing literature is resolved through connected research MCPs and a copyright-aware acquisition log. Authorized PDFs may be converted to private, Git-ignored Markdown with LlamaParse; full-text files are not republished merely because they are readable. See [`ACQUISITION_POLICY.md`](./research/semaglutide_ckd_flow/2026-09-05/sources/ACQUISITION_POLICY.md).

This material is an academic evidence synthesis, not individualized medical advice.
