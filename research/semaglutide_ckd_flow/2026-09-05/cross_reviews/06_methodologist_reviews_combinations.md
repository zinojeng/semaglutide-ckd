# Cross-review — flow-methodologist reviews flow-ckm (lane 05, combinations)

**Reviewer:** `flow-methodologist` (lane 06)
**Reviewed file:** `lanes/05_ckm_combinations.md` (as of the version fetched from `origin/worktree-ckm-combinations-lane`, 286 lines, Chinese-language)
**Wave:** 2 (cross-examination), per `ORCHESTRATION.md`: "methodologist reviews combination/causal claims"
**Scope:** This review does not re-derive lane 05's numbers from primary sources except where flagged; it audits causal-inference discipline, evidence-grading calibration, and cross-checks overlapping quantitative claims against this lane's own Wave-1 findings (`lanes/06_methods_mechanisms.md`). No lane file or numbered deliverable is edited by this review.

---

## 1. Strongest claim in lane 05

**§1.2 (points 1–4), the SGLT2i-subgroup power/confounding analysis**, is the strongest methodological work in the memo and independently converges with this lane's own Wave-1 analysis (`06_methods_mechanisms.md` §4.4), which was written before either lane had read the other's file — the agreement is a genuine independent replication, not shared drafting.

Specifically, lane 05 correctly:
- Distinguishes "failure to reject the null of no heterogeneity" from "proof of no heterogeneity" (§1.2 point 2), citing `FLOW-SGLT2-2024`'s own author admission of limited power (l.462–464, l.480–482) — this is exactly CLAUDE.md rule 5's requirement and matches this lane's §4.4 verbatim conclusion.
- Correctly reasons that asymmetric post-randomization SGLT2i initiation (more in placebo) biases the "SGLT2i-naive" contrast **toward the null**, i.e., toward *under*-stating semaglutide's relative benefit, not overstating it (§1.2 point 4) — this is the correct direction of contamination bias for an add-on that itself lowers event rates in the comparator arm, and lane 05 correctly downgrades the resulting time-dependent Cox estimate (HR 0.75, 95% CI 0.65–0.86) to hypothesis-generating rather than randomized-comparison status.
- Section 2.2 point 2 deserves separate commendation: lane 05 identifies an internal tension within `FLOW-MRA-2025` itself — its own Conclusions line ("add to the body of evidence regarding the additive treatment effect," l.245) sits uneasily against its own Discussion/Limitations language ("numerically greater," "numbers were small," l.247) — and lane 05 explicitly declines to adopt the stronger Conclusions-section phrasing as its own claim, flagging the tension for red-team/director attention instead of silently picking the more citable sentence. This is precisely the kind of close, adversarial reading CLAUDE.md rule 6 requires, and it independently reinforces the prohibited-phrasing entry this lane wrote for the analogous SGLT2i case (`06_methods_mechanisms.md` §7, row "No significant interaction by SGLT2i use proves...").

**No correction needed here; this lane's Wave-1 findings corroborate rather than dispute this section.**

---

## 2. Weakest claim in lane 05, with exact correction wording

**§6.1 point 3** grades the claim that semaglutide's benefit is "**strongly supported**" ("strongly supported") to "疊加使用而不互相抵銷" (can be layered on top of RASi±SGLT2i without cancelling out), i.e.:

> Original (lane 05, §6.1 point 3): "...此效益在已有 RASi±SGLT2i 背景下方向一致地保留（**strongly supported** 其"可疊加使用而不互相抵銷"，但相加之硬終點量化幅度為 unknown／suggestive...）"

**Problem:** The evidentiary basis cited for this claim is the SGLT2i-subgroup analysis discussed at length and correctly in lane 05's own §1 — a subgroup with a primary-outcome point estimate that **crosses the null** (HR 1.07, 95% CI 0.69–1.67) and a nonsignificant interaction test in an underpowered stratum (P=0.109). "Strongly supported" is a calibration mismatch for that evidentiary base: the master prompt's own graded-language scale (established / strongly supported / suggestive / hypothesis-generating / unknown) reserves "strongly supported" for evidence with meaningfully lower residual uncertainty than a single underpowered, null-crossing subgroup with a wide confidence interval. Directional consistency in eGFR slope and UACR (also correctly noted by lane 05 in the same section) is genuinely reassuring for "no signal of antagonism," but "no signal of harm in an underpowered subgroup" is the textbook definition of **suggestive**, not **strongly supported** — this is the same calibration principle lane 05 itself applies correctly one section earlier (§1.4's own summary language: "支持...沒有明顯有害交互作用訊號...保留" without invoking "strongly supported"). §6.1 point 3 is therefore inconsistent with §1.4's own more careful wording in the same document.

**Exact correction wording proposed:**

> Replace: "...此效益在已有 RASi±SGLT2i 背景下方向一致地保留（strongly supported 其"可疊加使用而不互相抵銷"，但相加之硬終點量化幅度為 unknown／suggestive，見第 1、3 節）。"
>
> With: "...此效益在已有 RASi±SGLT2i 背景下方向一致地保留——現有證據對"未觀察到有害交互作用、方向一致地保留"此一較弱主張達 **suggestive** 等級（受限於 SGLT2i 亞組僅 550 人、主要終點 HR 95% CI 跨越 1.0 且未達統計顯著之交互作用檢定，見第 1.2 節），尚不足以支持"strongly supported"之較高等級；相加之硬終點量化幅度則維持 unknown／suggestive 判定不變（見第 1、3 節）。"

(English gloss of the replacement, for the director's cross-language reconciliation: *"...this benefit is retained in direction when layered on RASi±SGLT2i. The weaker claim — 'no harmful interaction signal observed, direction preserved' — is supported at the **suggestive** level given the SGLT2i subgroup's small size (n=550), a primary-outcome 95% CI crossing 1.0, and a nonsignificant interaction test (§1.2); this does not yet meet 'strongly supported.' The magnitude of any additive hard-outcome benefit remains unknown/suggestive, unchanged from §1 and §3."*)

This correction only touches the evidence-grade word and its justification clause; it does not change any of lane 05's underlying numbers, its ordering-algorithm recommendations, or its monitoring table (§6.2–6.3), all of which are unaffected by this recalibration.

---

## 3. Unresolved numerical conflicts

**None found on the figures both lanes independently cite.** This lane cross-checked every overlapping quantitative claim between the two memos:

| Claim | Lane 05 value (locator) | Lane 06 value (locator) | Status |
|---|---|---|---|
| SGLT2i-users primary-outcome HR | 1.07 (95% CI 0.69–1.67), P=0.755 (`FLOW-SGLT2-2024` l.36-48, l.117-126) | 1.07 (95% CI 0.69–1.67) (`06_methods_mechanisms.md` §4.4, same source) | ✅ Match |
| Non-users primary-outcome HR | 0.73 (95% CI 0.63–0.85), P<0.001 | 0.73 (95% CI 0.63–0.85) | ✅ Match |
| Primary-outcome P-interaction | 0.109 | 0.109 | ✅ Match |
| Kidney-specific (4-component) HR, users/non-users | 1.18 (0.71–1.98) / 0.75 (0.61–0.90) | 1.18 (0.71–1.98) / 0.75 (0.61–0.90) | ✅ Match |
| eGFR-slope P-interaction | 0.237 | 0.237 | ✅ Match |
| MACE / all-cause-death P-interaction | 0.741 / 0.901 | 0.741 / 0.901 | ✅ Match |
| Badve 2025 (`GLP1-CLASS-META-2025`) composite kidney HR, T2D | 0.82 (0.73–0.93), transcribed from `FLOW-MRA-2025` Discussion l.249 (secondhand, not independently retrieved by lane 05) | 0.82 (0.73–0.93), independently retrieved via WebSearch/PMC cross-check (two independent secondary sources, not the primary paper) | ✅ Match, and now **doubly independently corroborated** — neither lane has the primary paper's own tables, but two different retrieval routes (lane 05's transcription from a third paper's Discussion section; lane 06's direct web/PMC search) converge on identical numbers. Recommend the director treat this specific figure as higher-confidence than either lane's individual sourcing alone would justify, while still flagging (per both lanes) that the primary paper itself remains unretrieved for appendix-level detail (per-molecule/safety breakdowns). |
| Badve 2025 kidney-failure / MACE / all-cause-death HRs | Not listed in lane 05 (only composite kidney HR transcribed) | 0.84 (0.72–0.99) / 0.87 (0.81–0.93) / 0.88 (0.83–0.93) | No conflict — lane 05 simply does not carry these three figures; recommend lane 05/director add them from `06_methods_mechanisms.md` §5 rather than re-deriving. |

**No corrections required in this section; this is a CONFIRM-type outcome for every overlapping figure.**

---

## 4. Locator supplied (CONFIRM with new evidence)

**§6.2 point 4** states, without a locator (unlike nearly every other claim in the memo, which cites `source l.XXX`): "因 FLOW 收案不要求 HbA1c 未達標（HbA1c ≤10% 即可收案）" (FLOW's enrollment did not require uncontrolled glycemia — HbA1c ≤10% was sufficient for inclusion).

**This lane independently verified the claim is factually correct and supplies the missing locator:** `FLOW-SUPP-2024`, section "ELIGIBILITY CRITERIA / Inclusion," line 385: **"HbA1c ≤ 10% (≤ 86 mmol/mol)*"** — confirmed as an inclusion-criterion ceiling (not a lower bound requiring uncontrolled glycemia), consistent with lane 05's framing. Recommend lane 05 add this exact locator to §6.2 point 4 before Wave 3.

**However, this lane flags an unresolved interpretive gap lane 05 should address, not a numerical error:** the inclusion criterion being an HbA1c *ceiling* only establishes that the trial *population* included glycemically well-controlled patients — it does not by itself establish that semaglutide's *kidney benefit specifically* is independent of glycemic control, which is a mediation question. `06_methods_mechanisms.md` §1/§3/§3a (this lane's Wave-1 work) documents that the best available quantitative mediation evidence (`SUSTAIN6-MEDIATION-2021`, LEADER/SUSTAIN-6, not FLOW itself) found HbA1c mediated a **25–26% point estimate** (95% CI crossing zero in LEADER, noncalculable in SUSTAIN-6) of the kidney-composite effect — not negligible, and not independently re-tested within FLOW's own population. §6.2 point 4's clinical-sequencing recommendation ("this step doesn't need to wait for glycemic failure") is still reasonable as a *population-applicability* argument (the trial enrolled across the HbA1c range, so results are not restricted to uncontrolled patients), but it should not be read as, or extended into, an *independent-of-glycemia mechanism* argument without citing the mediation-uncertainty caveat above. Recommend lane 05 add one clause to §6.2 point 4 distinguishing "FLOW's population was not restricted to uncontrolled HbA1c" (established, per the locator above) from "the kidney benefit itself is proven independent of glycemic effect" (not established — suggestive at best, per `06_methods_mechanisms.md` §3).

---

## 5. Gap flag — new source not yet in lane 05

`SELECT-FLOW-SOUL-POOLED-2026` (Mann, Badve, Perkovic et al., Lancet Diabetes Endocrinol 2026, DOI 10.1016/S2213-8587(26)00134-8, PMID 42567173) does not appear anywhere in lane 05's source table or text. This lane retrieved its structured abstract mid-Wave-1 (via `mcp__paper-search__search_pubmed`, independently corroborated by `flow-endocrinologist` via Europe PMC per a director relay received during this review) and its evidence-layer critique is in `06_methods_mechanisms.md` §3a. It is directly relevant to lane 05's §3 (triple/quadruple-therapy evidence layering table) and §6.1 (sequencing algorithm), because it is participant-level, prespecified, cross-dose/cross-route (FLOW 1.0 mg SC / SELECT 2.4 mg SC / SOUL 14 mg oral) randomized evidence — a materially stronger evidentiary category than the `COMBO-MODEL-NEUEN-2024` lifetime-simulation model lane 05 currently uses as its most quantitative "combination-adjacent" source. It is **not**, however, evidence about combining semaglutide *with* SGLT2i/finerenone (it pools three semaglutide-vs-placebo trials, not a factorial combination design), so it does not change lane 05's core conclusion that no direct randomized combination-therapy trial exists — but the director should have lane 05 or itself incorporate its pooled HRs (primary composite HR 0.84, 95% CI 0.77–0.91; kidney-specific composite HR 0.80, 95% CI 0.69–0.92; N=30,787) into `07_SGLT2_COMBINATION_EVIDENCE.md` and `13_CLINICAL_DECISION_FRAMEWORK.md` as background evidence of consistency across doses/routes, distinct from the combination-therapy question itself.

---

## 6. Resolved versus unresolved causal claims

### Resolved (this review confirms the claim and grading as stated in lane 05; no correction needed)

| Claim | Verdict | Source locator |
|---|---|---|
| Nonsignificant SGLT2i-subgroup interaction (P=0.109 primary; P=0.100 kidney-specific; P=0.237 slope; P=0.741/0.901 MACE/death) does not prove additive hard-kidney benefit is established | **Resolved — confirmed correct**, independently replicated by this lane's own Wave-1 work | `FLOW-SGLT2-2024` l.36-48, 64-69, 77-84, 86-97, 117-126, 412-450; cross-checked against `06_methods_mechanisms.md` §4.4 |
| Post-randomization SGLT2i initiation asymmetry (more in placebo) biases the no-SGLT2i contrast toward the null, not away from it | **Resolved — confirmed correct causal-inference reasoning** | `FLOW-SGLT2-2024` l.109-114, l.126-129 |
| FLOW's MRA subgroup (predominantly spironolactone/eplerenone, 0 baseline finerenone users) cannot support a semaglutide+finerenone additive-efficacy claim | **Resolved — confirmed correct**, consistent with CLAUDE.md rule 6 | `FLOW-MRA-2025` l.75, l.217 |
| `FLOW-MRA-2025`'s own Conclusions-section "additive treatment effect" phrase should not be adopted verbatim given its own Limitations language | **Resolved — confirmed correct, high-value catch** | `FLOW-MRA-2025` l.245 vs. l.247, l.255 |
| No completed RCT has tested triple (RASi+SGLT2i+semaglutide) or quadruple (+finerenone) therapy against fewer components for hard outcomes | **Resolved — confirmed correct**; `COMBO-MODEL-NEUEN-2024` is a lifetime-simulation model, not trial evidence, and is correctly labeled as such | `COMBO-MODEL-NEUEN-2024` Abstract; lane 05 §3, §3.3 |
| "Four pillars" is not traceable to an official finalized guideline as of 2026-09-05; its clearest sourcing is `FLOW-MRA-2025` (a trial-affiliated-author journal paper), and KDIGO 2026 remains a public-review draft | **Resolved — confirmed correct and appropriately cautious** | `FLOW-MRA-2025` l.37, l.251; lane 05 §3.2 |
| Overlapping SGLT2i-subgroup and Badve-2025 numeric figures cited in both lanes | **Resolved — no conflict**, see §3 table above | See §3 table |
| FLOW enrollment did not require uncontrolled HbA1c (ceiling ≤10%, not a lower-bound requirement) | **Resolved — confirmed correct, locator supplied by this review** | `FLOW-SUPP-2024` l.385, "ELIGIBILITY CRITERIA / Inclusion" |
| Differing NNTs across baseline-risk subgroups (e.g., HF NNT 13 vs. ASCVD NNT 22) reflect expected higher absolute benefit at higher baseline risk under a roughly constant relative risk, not evidence of effect-modification heterogeneity | **Resolved — confirmed correct statistical principle** | Lane 05 §4.4 point 1, citing `FLOW-CVPHENOTYPE-2026` (itself flagged by lane 05 as secondary-source-only, see below) |

### Unresolved (open items this review could not close; flagged for librarian/director/red-team)

| Claim | Why unresolved | Source locator / what is missing |
|---|---|---|
| §6.1 point 3's "strongly supported" grade for "no cancellation when layered on RASi±SGLT2i" | Calibration disagreement — this review recommends downgrading to "suggestive"; exact replacement wording given in §2 above | `FLOW-SGLT2-2024`; lane 05 §1.2 vs. §6.1 (internal inconsistency within lane 05 itself) |
| §6.2 point 4's implicit extension from "population not restricted to uncontrolled HbA1c" to "benefit independent of glycemic effect" | Conflates population-applicability with mechanistic independence; needs one clarifying clause (exact wording proposed in §4 above) | `FLOW-SUPP-2024` l.385 (population fact, now confirmed) vs. `SUSTAIN6-MEDIATION-2021` (mediation uncertainty, not yet cross-referenced in lane 05) |
| `FLOW-HF-2024` (Pratley, JACC 2024) figures in lane 05 §4.3 | Secondary-source-only per lane 05's own §0/§7 flag; this lane did not independently retrieve it either | `FLOW-HF-2024` — no PMID/full-text access confirmed by either lane; remains on lane 05's own §7 to-verify list |
| `FLOW-CVPHENOTYPE-2026` (JACC 2026) figures in lane 05 §4.2, including the NNT-heterogeneity example cited above | Secondary-source-only per lane 05's own §0/§7 flag; CIs and P-interaction values not locator-verified by either lane | `FLOW-CVPHENOTYPE-2026` DOI 10.1016/j.jacc.2026.02.5125 — full text not retrieved by either lane |
| KDIGO 2026 draft's "four pillars"/foundational-therapy framing and finerenone 1A-recommendation conditions (lane 05 §5.1, §3.2) | Draft-status document; PDF extraction failed for lane 05; not attempted by this lane | `GUIDE-KDIGO-2026-DRAFT` — remains draft/unverified per both lanes; do not promote to definite in `11_GUIDELINE_REGULATORY_EVOLUTION.md` |
| ADA 2026 exact recommendation numbers (e.g., 11.7b) and CKM 2026 guideline's exact sequencing/Class-of-Recommendation language (lane 05 §5.2, §5.3) | Publisher access blocked (403) for lane 05; not attempted by this lane | `GUIDE-ADA-2026`, `GUIDE-CKM-2026` — both remain on lane 05's own §7 to-verify list |
| Badve 2025 per-molecule heterogeneity and safety/discontinuation data | Neither lane retrieved the primary paper's full tables/appendix | `GLP1-CLASS-META-2025` — flagged independently by both lanes (lane 05 §7 item 7; lane 06 §8 item 3) as needing librarian retrieval |
| `SELECT-FLOW-SOUL-POOLED-2026` not yet incorporated into lane 05's combination-evidence table or sequencing algorithm | New source, not a factual dispute — an evidence-inventory gap | DOI 10.1016/S2213-8587(26)00134-8, PMID 42567173; see §5 above for what it does and does not add |

---

**Files written this review:** `cross_reviews/06_methodologist_reviews_combinations.md` (this file) only. No lane file, numbered deliverable, or `SOURCE_LEDGER.csv` was edited.

**Next step:** per `ORCHESTRATION.md` Wave 2, `flow-ckm` should read this review and, if it agrees, apply the §2 and §4 corrections directly to its own `lanes/05_ckm_combinations.md` (this reviewer cannot edit that file); any disagreement should be recorded as a `CHALLENGE`/`CONFLICT` response addressed back to this lane. The director should treat §3 and §6's "Resolved" table as cross-validated inputs for `07_SGLT2_COMBINATION_EVIDENCE.md`, `08_MRA_FINERENONE_COMBINATION_EVIDENCE.md`, `11_GUIDELINE_REGULATORY_EVOLUTION.md`, and `13_CLINICAL_DECISION_FRAMEWORK.md`, and the "Unresolved" table as the residual verification backlog before those files are finalized.
