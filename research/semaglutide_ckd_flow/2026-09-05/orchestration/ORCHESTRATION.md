# Cross-session research orchestration

## Objective

Run independent Claude Code sessions as a structured clinical evidence team. The sessions communicate through durable lane memos, adversarial cross-reviews, explicit resumed-session handoffs, and receipt-verified live messages. This preserves provenance and makes disagreements visible before synthesis.

The core `01`–`16` synthesis remains frozen at the 2026-09-05 evidence cutoff. A later extension inventories dynamic PubMed citations, comments, replies, and post-FLOW evidence through 2026-09-07; a second extension maps review-publication opportunities through 2026-09-09. Neither later search date silently changes the cutoff of the core synthesis.

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
| Root coordinator | integration/provenance recorder | `18_RED_TEAM_CLOSURE.md` | integrate verified corrections, complete the owning-director handoff, and record—not re-adjudicate—the final gates |

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
6. **Wave 5 – red team:** a separate session checks every headline number and high-stakes inference. The root coordinator integrates only independently verified corrections; the owning director then receives the report and repair set through a resumed-session prompt and records the final adjudication without retroactively claiming the coordinator's edits.
7. **Wave 6 – closure and deterministic QA:** after the owning director acknowledges Wave 5, the root coordinator records the finding dispositions and split clinical/process/publication gates in `18_RED_TEAM_CLOSURE.md`; then check required files, links/DOIs, CSV schema, forbidden overclaims, empty placeholders, and Git diff, followed by an independent Claude worktree review.
8. **Wave 4 Run 2 – remedial live peer dialogue and reopened synthesis:** after the first Wave 4 contact attempt was proven not delivered, this project launched permission-compatible nephrology, endocrinology, methodology, and director sessions on the same frozen evidence base. Two-way delivery was first proven with named preflight messages and replies. Each disputed claim then completed a question → challenge → response/counterpoint → method check → rejoinder → closed chain. The coordinator integrated the corrections, reran all gates, and published the clinically relevant, public-safe adjudications in `19_WAVE4_PEER_REVIEW_ADDENDUM_ZH_TW.md`; the failed first attempt remains in provenance rather than being rewritten. Future runs should perform this receipt-verified dialogue before the red-team gate.
9. **Post-FLOW citation/response extension:** source-librarian, nephrology, methodology, CKM, and director roles independently examine formal comments, author replies, later analyses, measured-GFR studies, citation overlap, and clinical translation. Six disputes are routed through the same challenge/response/method-check/rejoinder protocol. Public conclusions are synthesized in `21_POST_FLOW_CITATION_COMMENT_REPLY_REVIEW_ZH_TW.md`; an eight-slide, nephrologist-facing application layer is provided in `presentation_zh_tw/POST_FLOW_NEPHROLOGIST_SPEAKER_ADDENDUM_ZH_TW.md`. A role chain is reported as closed only after the director verifies the complete receipt-linked sequence against the source record.

### Post-FLOW cross-session 實際結果（2026-09-07）

四個專家角色均完成 PREFLIGHT／ACK，六個正式 CHALLENGE 也都有送達紀錄；但只有 MRA／finerenone 爭點完成全部 `RESPONSE → METHOD_CHECK → CLINICAL_TRANSLATION → REJOINDER` 並由 director 關閉。最終裁決為 **1 CLOSED、4 PARTIALLY RESOLVED、1 OPEN**：

| Issue | Disposition | Closure boundary |
|---|---|---|
| 1. NEJM criticism/reply | OPEN | 正文未取得；只確認書目關係，不重建具體主張。 |
| 2. Kidney protection vs measurement artifact | PARTIALLY RESOLVED | FLOW marker data 與 mGFR studies 可核實；KI correspondence 原文仍不可讀。 |
| 3. MRA/finerenone additivity | CLOSED | 三角色完成全文核對與完整往返；不宣稱 synergy，baseline finerenone 為 0/257。 |
| 4. Baseline SGLT2i/modern combinations | PARTIALLY RESOLVED | subgroup 與一項 citation overclaim 已重核；完整對話鏈未完成。 |
| 5. Advanced CKD/dialysis/safety | PARTIALLY RESOLVED | 收案外族群的結構性限制已確認；部分評論正文不可讀。 |
| 6. Citation echo/meta-analysis/fourth-pillar claims | PARTIALLY RESOLVED | 一項 overclaim 已由兩角色確認；另兩項候選因角色端工具存取限制未裁決。 |

這些狀態只描述 AI 角色對話的完成度，不改變來源本身的證據階級。Raw session identifiers、逐字訊息與 private logs 留在非公開稽核層；公開版不得用角色共識取代 primary-source verification。

### FLOW-centered review publication extension（2026-09-09）

本輪不是規劃新 RCT，而是替一篇以 FLOW 為主軸、面向腎臟科讀者的 review article 找出仍可投稿的問題。Coordinator 重新啟動原有 nephrology、endocrinology 與 methodology 三個持久角色，而非建立同名假會話。流程依序完成：各角色獨立選題、將臨床角色的主張逐字送給另一角色挑戰、methodology session 對實際新全文區段作 article-boundary 與 claim-level adjudication，再把兩個必答問題送回原臨床角色取得明確同意／不同意與理由。

三方最後收斂為 **two-gate critical review**：

1. **Gate 1 — 單藥證據鏈的內部效度：** filtration-marker validity（creatinine、cystatin C、mGFR、BSA）→ eGFR slope／UACR surrogate → hard outcomes／statistical hierarchy。
2. **Gate 2 — 合併療法的加成效度：** 單藥 trial、背景治療 subgroup、短期 biomarker combination 與 factorial／direct randomized evidence 必須分級；Gate 1 已通過不能自動讓 Gate 2 通過。

實際對話造成三項具體修正：

- 把 FLOW 未公開的 cystatin-C 結果標成 `data on file`／未閉環缺口；BSA 校正前後的 1.16 與 1.04 只回答 BSA 分母敏感度，不能替代 lean-mass／creatinine-generation 問題。
- 把「null interaction」「方向一致」「機轉互補」「add-on biomarker effect」與「additive／synergistic hard-outcome effect」拆成不同層級。
- 將 finerenone versus semaglutide 保留為臨床 application section；主稿的新穎性改由 endpoint／measurement validity 與 combination-inference validity 的正交矩陣承擔。

2026-09-07 表格中的 `OPEN`／`PARTIALLY RESOLVED` 是當時對話與取文完成度的歷史快照。使用者後續提供的 NEJM correspondence、Kidney International letter–reply 與一篇 review 已於本輪作邊界稽核；其中一檔實為完全無關的錯誤文章。受限制原文仍只留在本機，公開版只發布短摘要、數值、stable identifiers、方法學判定與 rights boundary。完整投稿藍圖見 `23_FLOW_CENTERED_REVIEW_PUBLICATION_AGENDA_ZH_TW.md`，逐檔 QA 見 `sources/NEW_FULLTEXT_BOUNDARY_AUDIT_2026-09-09.md`。

## Post-FLOW acquisition and publication boundary

The 2026-09-07 extension maintains a Git-ignored private cache of 27 unique full-text sources, 27 canonical Markdown conversions plus one alternate LlamaParse comparator (28 Markdown artifacts total), and 24 valid PDFs. Source access did not bypass access controls, but access, automated processing, cloud transfer, and republication are separate rights determinations. Rights-restricted or uncleared conversions remain disclosed processing incidents and are excluded from AI/RAG use; private storage does not cure missing authorization. PDFs, source JATS/XML or HTML, full-text derivatives, private manifests, failed retrieval responses, rights-restricted table/figure captures, credentials, and raw session logs are never added to the public snapshot.

The public extension therefore contains source identities, short paraphrases, verified numerical facts, Table/Figure locators, rights boundaries, and independently designed redraw instructions. Cross-session agreement is an audit mechanism, not a new unit of medical evidence; claims remain limited to the strongest source actually checked.

## Cross-session message protocol

Every handoff must name exact files and ask for one of these message types:

- `CHALLENGE`: identify an unsupported or overstated claim and propose replacement wording.
- `CONFLICT`: list two inconsistent numbers/definitions with exact source locators.
- `CONFIRM`: independently reproduce a number or classification.
- `GAP`: identify a population, endpoint, guideline, or safety issue still unsupported.

For live dialogue, transport success alone is insufficient. Each message must carry a unique logical ID and `in_reply_to`; the receiving session must return a reply or receipt that names that ID. The methodology auditor receives each original chain message—not a coordinator paraphrase—as it arrives. A dispute may be marked `CLOSED` only after the final rejoinder and a receipt-linked closure; routing omissions and later repairs remain visible in the durable internal log.

Reviews must separate factual corrections from interpretive disagreements. The director records each material dispute and resolution in `12_EVIDENCE_GAPS_AND_CONTROVERSIES.md` or `15_CLAIM_EVIDENCE_MAP.md`.

## Completion gate

The project is complete only when all required files exist, all headline quantitative claims are traceable to a primary source, uncertain 2026 items are correctly labeled, combination-therapy limitations are explicit, and the red-team blockers are resolved or transparently retained as uncertainty.

Internal deliverable QA and permission to publish are separate gates. `scripts/verify_deliverables.sh`
fails while `18_RED_TEAM_CLOSURE.md` records a publication hold; `--allow-hold` may be used only to
verify the internal artifact set while preserving an explicit nonpublication status.
