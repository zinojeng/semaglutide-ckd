# Lane 02 — Nephrology Trialist / Statistician: FLOW Trial Anatomy, Endpoints, Statistics

**Session role:** `flow-trialist` (Wave 1). **Scope:** reconstruct FLOW (`FLOW-PRIMARY-2024` + `FLOW-SUPPLEMENT-2024`) with exact locators; quantify how much of the primary result is CV-death-dependent; eGFR slope (creatinine vs cystatin C); UACR; early stopping/alpha-spending/estimand/multiplicity/competing risks; SGLT2i/MRA/eGFR/UACR/KDIGO/CV-phenotype subgroup power cautions; contextual (non-ranking) comparison to CREDENCE/DAPA-CKD/EMPA-KIDNEY/FIDELIO-DKD/FIDELITY; explicit discrepancy log.

**Sources actually opened this session:** `fulltext/FLOW.pdf` (read directly as page images, pages 8–9, to resolve a text-extraction fault — see §0), `fulltext/FLOW_primary_NEJM_2024_fulltext.md` (full, 1141 lines), `fulltext/FLOW_supplement_fulltext.md` (full, 995 lines — eligibility criteria, trial outcomes list, interim-analysis/alpha-spending methodology, Table S1–S3), `fulltext/glp1_cardiorenal_Mann_2024.md` (FLOW+SGLT2i, full), `fulltext/glp1_cardiorenal_Mahaffey_2025.md` (FLOW CV-by-CKD-severity, full), `fulltext/glp1_cardiorenal_Rossing_2025.md` (FLOW+MRA, abstract as embedded in file). Web-verified (WebSearch, results pointing to NEJM/PMC/Oxford Academic primary pages) for the four non-FLOW comparator trials: CREDENCE (NEJM 2019, doi 10.1056/NEJMoa1811744), DAPA-CKD (NEJM 2020, doi 10.1056/NEJMoa2024816), EMPA-KIDNEY (NEJM 2023, doi 10.1056/NEJMoa2204233), FIDELIO-DKD (NEJM 2020, doi 10.1056/NEJMoa2025845 per PubMed 33264825), FIDELITY pooled (Eur Heart J 2022). No Sci-Hub or circumvention route used; no PDFs downloaded (only primary-source snippets read via search results). Did not fetch NEJM full text directly (403 on WebFetch); relied on PubMed-indexed/other-outlet quotations of the NEJM-published numbers, cross-checked for internal consistency (event counts, CI, P values match across independent snippets).

---

## 0. Data-quality note on the local fulltext (read this before trusting `FLOW_primary_NEJM_2024_fulltext.md` Table 2)

`fulltext/FLOW_primary_NEJM_2024_fulltext.md` lines ~480–535 render **Table 2 (Efficacy and Safety Outcomes)** as mirrored/character-reversed text (a PDF→Markdown extraction fault specific to that shaded table), and the source-librarian lane (`01_source_librarian.md` §0) already flagged this and worked around it using body-text prose only. I went further and opened `fulltext/FLOW.pdf` directly with the PDF-page-image reader (pages 8–9 = journal pp. 116–117) and transcribed Table 2 in full, including the **component-level event counts that never appear in the body prose** (e.g., persistent ≥50% eGFR reduction, persistent eGFR<15, initiation of kidney-replacement therapy, death from kidney-related causes, each individually). All numbers in §3–§5 below are transcribed directly from that page image and are the highest-confidence local source for Table 2. Any other lane citing Table 2 component counts from the `.md` file's garbled block should re-verify against the PDF image rather than the `.md` extraction.

---

## 1. Design, inclusion pathways, baseline phenotype, background therapy

**Trial:** FLOW (Evaluate Renal Function with Semaglutide Once Weekly), NCT03819153. International, double-blind, randomized, placebo-controlled, event-driven, 1:1 allocation, 387 sites/28 countries, recruitment June 2019–May 2021, 5581 screened → 3533 randomized (1767 semaglutide / 1766 placebo). [`FLOW-PRIMARY-2024`, lines 41–48, 179–184]

**Inclusion — two eGFR/UACR pathways** (verbatim from protocol eligibility criteria, `FLOW-SUPPLEMENT-2024` lines 377–397; consistent with Methods prose lines 80–104):
- **Pathway A:** eGFR ≥50 and ≤75 mL/min/1.73 m² (CKD-EPI 2009) **and** UACR >300 and <5000 mg/g.
- **Pathway B:** eGFR ≥25 and <50 mL/min/1.73 m² **and** UACR >100 and <5000 mg/g.
- Plus: T2D, HbA1c ≤10%, on maximum labeled/tolerated dose of an ACEi or ARB (stable ≥4 weeks) unless not tolerated/contraindicated.
- **Design cap not mentioned in the main NEJM text but present in the protocol:** *"The number of subjects with inclusion eGFR ≥60 mL/min/1.73 m² was capped at 20% of randomized subjects."* [`FLOW-SUPPLEMENT-2024`, line 407–408] — this is a meaningful enrollment constraint for interpreting the eGFR-≥60 subgroup (see §7).

**Key exclusions:** congenital/hereditary kidney disease incl. polycystic kidney disease, autoimmune kidney disease incl. glomerulonephritis; current/recent (≤90 d) dialysis; NYHA IV heart failure; MI/stroke/unstable angina/TIA ≤60 d before screening; planned revascularization; any GLP-1RA use ≤30 d before screening; combined ACEi+ARB use; prior/awaiting solid-organ transplant; personal/family MEN2/MTC history; unstable diabetic retinopathy. [`FLOW-SUPPLEMENT-2024`, lines 411–438]

**Baseline phenotype (full analysis set, N=3533):** mean age 66.6±9.0 y; 30.3% female; mean eGFR 47.0±15.2 mL/min/1.73 m² (eGFR distribution: ≥60 = 20.4%, 45–<60 = 29.9%, 30–<45 = 38.4%, <30 = 11.3%); median UACR 567.6 mg/g (macroalbuminuria [A3, ≥300] 68.5%, microalbuminuria [A2] 28.4%, normoalbuminuria [A1] 3.1%); mean HbA1c 7.8±1.3%; mean BMI 32.0±6.3; diabetes duration ≥15 y in 56.8%; prior MI/stroke 22.9%; chronic heart failure 19.2%. By KDIGO risk calculator, **68% (2412/3532) were "very high risk"; 24.9% (878) "high risk"; 6.8% (242) "low/moderate risk"** [`FLOW-PRIMARY-2024` line 299 states "68%"; `FLOW-CKDSEVERITY-2025` gives the exact denominators 2412/878/242 out of 3532 with known baseline CKD status — internally consistent, see §11 for the one associated discrepancy]. [`FLOW-PRIMARY-2024`, Table 1, lines 193–261]

**Background therapy at baseline:** ACEi 35.1%, ARB 60.2% (i.e., ~95% on RASi as required by design), SGLT2i 15.6% (550/3533; 277 semaglutide/273 placebo), insulin 61.4%, lipid-lowering drug 80.2%, diuretic 50.4%. **MRA use was present in only 257/3533 (7.3%) participants, predominantly spironolactone; finerenone was essentially unrepresented because FLOW began enrolling in 2019, before the finerenone (FIDELIO-DKD/FIGARO-DKD) trials completed** [`FLOW-MRA-2025` abstract: "n=257 (136 semaglutide/121 placebo)... Baseline MRA was predominantly spironolactone; finerenone was only available after recruitment ended"; `FLOW-CKDSEVERITY-2025` line 149: "none were receiving finerenone"]. [`FLOW-PRIMARY-2024`, Table 1, lines 255–261]

---

## 2. Primary outcome and hierarchical confirmatory secondary outcomes — exact wording

**Primary outcome** (time to first event of a 5-component composite), verbatim from the protocol outcome list [`FLOW-SUPPLEMENT-2024`, lines 447–452] and consistent with the NEJM Methods [`FLOW-PRIMARY-2024`, lines 141–148]:
1. Onset of persistent (≥28 days) ≥50% reduction in eGFR (CKD-EPI 2009) from baseline
2. Onset of persistent (≥28 days) eGFR (CKD-EPI) <15 mL/min/1.73 m²
3. Initiation of chronic renal-replacement therapy (dialysis or kidney transplantation)
4. Renal death (death from kidney-related causes)
5. **CV death**

**This is not a purely kidney endpoint** — per CLAUDE.md rule 4, it must always be reported as the 5-component composite (kidney failure/≥50% eGFR decline/kidney death/CV death), separate from the kidney-specific 4-component composite (identical minus CV death; see §4).

**Confirmatory secondary outcomes**, tested hierarchically only if the primary outcome met superiority, in this pre-specified order [`FLOW-SUPPLEMENT-2024`, lines 528–536]:
1. Total eGFR slope (annual rate of change in eGFR, randomization → end of trial)
2. Time to first major adverse cardiovascular event (MACE: nonfatal MI, nonfatal stroke, or CV death)
3. Time to all-cause death

Testing stopped the first time an analysis failed to confirm superiority at the nominal level; **no adjustment for the group sequential design (GSD) was applied to the confirmatory secondary outcomes** — only the primary outcome's HR/CI/P were GSD-adjusted (likelihood-ratio ordering). [`FLOW-SUPPLEMENT-2024`, lines 537–541]

Supportive secondary/exploratory outcomes (body weight, HbA1c, SBP/DBP, UACR, cystatin-C eGFR, severe hypoglycemia, major adverse limb events, EQ-5D) were **not adjusted for multiplicity; their CIs "should not be used in place of hypothesis testing."** [`FLOW-PRIMARY-2024`, lines 165–170]

---

## 3. Table 2 reconstructed in full (transcribed from `FLOW.pdf` pages 8–9 / journal pp. 116–117)

N=1767 semaglutide, N=1766 placebo. All time-to-first-event analyses use a stratified (by baseline SGLT2i use) Cox proportional-hazards model; primary-outcome HR/CI/P are GSD-adjusted via likelihood-ratio ordering; cumulative incidence used the Aalen–Johansen estimator with non-CV/non-renal death as the competing risk for the primary outcome (and all-cause death excl. renal death as competing risk for the kidney-specific composite, per `FLOW-SGLT2-2024` Fig. 1 legend).

| Outcome | Semaglutide, n (%) | Placebo, n (%) | Hazard Ratio (95% CI) | Estimated Difference (95% CI) | P |
|---|---:|---:|---:|---:|---:|
| **Primary outcome: major kidney disease events** | 331 (18.7) | 410 (23.2) | 0.76 (0.66–0.88) | — | **0.0003** |
| *Components of primary outcome* | | | | | |
| Persistent ≥50% reduction in eGFR | 165 (9.3) | 213 (12.1) | 0.73 (0.59–0.89) | — | — |
| Persistent eGFR <15 mL/min/1.73 m² | 92 (5.2) | 110 (6.2) | 0.80 (0.61–1.06) | — | — |
| Initiation of kidney-replacement therapy | 87 (4.9) | 100 (5.7) | 0.84 (0.63–1.12) | — | — |
| Death from kidney-related causes | 5 (0.3) | 5 (0.3) | 0.97 (0.27–3.49) | — | — |
| Death from cardiovascular causes | 123 (7.0) | 169 (9.6) | 0.71 (0.56–0.89) | — | — |
| **Composite of kidney-specific components (excl. CV death)** | **218 (12.3)** | **260 (14.7)** | **0.79 (0.66–0.94)** | — | — |
| *Confirmatory secondary outcomes* | | | | | |
| Mean annual rate of change in eGFR (total slope), mL/min/1.73 m²/yr | −2.19 | −3.36 | — | **1.16 (0.86–1.47)** | **<0.001** |
| Major cardiovascular events (MACE) | 212 (12.0) | 254 (14.4) | 0.82 (0.68–0.98) | — | **0.029** |
| — Death from cardiovascular causes (component) | 123 (7.0) | 169 (9.6) | 0.71 (0.56–0.89) | — | — |
| — Nonfatal myocardial infarction | 52 (2.9) | 64 (3.6) | 0.80 (0.55–1.15) | — | — |
| — Nonfatal stroke | 63 (3.6) | 51 (2.9) | 1.22 (0.84–1.77) | — | — |
| Death from any cause | 227 (12.8) | 279 (15.8) | 0.80 (0.67–0.95) | — | **0.01** |
| *Supportive secondary outcomes (not multiplicity-adjusted)* | | | | | |
| Ratio of UACR at wk104 to baseline | 0.60 | 0.88 | 0.68 (0.62–0.75)‡ | — | — |
| Mean Δ body weight, wk104, kg | −5.55 | −1.45 | — | −4.10 (−4.56 to −3.65) | — |
| Mean Δ HbA1c, wk104, pct pts | −0.87 | −0.06 | — | −0.81 (−0.90 to −0.72) | — |
| Mean Δ SBP, wk104, mmHg | −3.79 | −1.55 | — | −2.23 (−3.33 to −1.13) | — |
| Mean Δ DBP, wk104, mmHg | −0.23 | −1.01 | — | 0.78 (0.16–1.41) | — |
| Mean Δ eGFR, baseline→wk12, mL/min/1.73 m² | −1.07 | −1.05 | — | −0.03 (−0.56 to 0.51) | — |
| Mean annual rate of Δ eGFR, wk12→end of trial | −2.36 | −3.30 | — | 0.94 (0.62–1.26) | — |
| Mean Δ eGFR by cystatin-C equation, baseline→wk104 | −2.01 | −5.41 | — | **3.39 (2.63–4.15)** | — |
| Major adverse limb event (time-to-first-event) | 16 | 28 | 0.56 (0.30–1.02) | — | — |
| No. of severe hypoglycemic episodes | 47 | 46 | 1.02 (0.62–1.67) | — | — |
| Death, noncardiovascular/non-kidney-related (supplementary, time-to-first-event) | 99 | 105 | 0.93 (0.70–1.22) | — | — |

‡ Value is the ratio of the value in the semaglutide group to the value in the placebo group (not a HR). [Table 2 footnote, `FLOW.pdf` p.9]

**Cross-check:** the "on-treatment"/retrieved-dropout sensitivity analyses in Table S3 reproduce essentially the same primary-outcome HR (range 0.75–0.77 across 6 variants: ITT 0.76; multiple imputation of missing eGFR 0.75; eGFR-persistence-at-scheduled-visits-only 0.76; eGFR-persistence-with-local-labs 0.76; retrieved-dropouts-permanent-discontinuation 0.77; retrieved-dropouts-first-discontinuation 0.77), MACE HR stable at 0.82, and all-cause death HR stable at 0.79–0.80. [`FLOW-SUPPLEMENT-2024`, lines 782–813]

---

## 4. How much of the primary result depends on CV death (the "24% reduction" question)

Per master-prompt Section VIII and CLAUDE.md rule 4, the 5-component primary composite (incl. CV death) and the kidney-specific 4-component composite (excl. CV death) must be reported separately, never conflated:

- **5-component primary composite:** 331/1767 vs 410/1766; HR 0.76 (0.66–0.88), P=0.0003; NNT over 3 years = 20 (95% CI 14–40).
- **Kidney-specific composite (excl. CV death):** 218/1767 vs 260/1766; HR 0.79 (0.66–0.94). *No NNT for this outcome is reported anywhere in the primary paper, supplement, or the two subgroup papers reviewed — see §6 for why it is not estimable from public data.*
- **CV death alone:** 123/1767 vs 169/1766; HR 0.71 (0.56–0.89).

**CV death's share of primary-composite events:** summing the Table 2 component counts, CV death accounts for **123+169 = 292 of the 331+410 = 741 total primary-outcome events (39.4%)**. The Supplementary Appendix's representativeness table states this share as **"approximately 35%"** [`FLOW-SUPPLEMENT-2024`, line 755]. These two figures do not match exactly — flagged as Discrepancy #1 (§11); the true first-event-adjudicated share used for the "≈35%" claim may reflect a different counting rule (e.g., component assigned only when it is the temporally *first* qualifying event on a given day under a pre-specified hierarchy, vs. Table 2's independent per-component counts) that I could not resolve from locally available text.

**Interpretation implication:** the kidney-specific HR (0.79, 0.66–0.94) is directionally consistent with but numerically *smaller* than the 5-component HR (0.76), and its CI is wider and closer to the null. The correct headline is therefore something like *"24% relative reduction in the composite of major kidney events and cardiovascular death, with a 21% relative reduction in the kidney-specific composite excluding CV death"* — matching the master prompt's suggested preferred phrasing (Section VIII) and confirmed by these primary data. Do not report "24% reduction in kidney disease progression" without the CV-death caveat.

---

## 5. eGFR slope: total vs chronic, creatinine vs cystatin C

- **Total eGFR slope** (randomization → end of trial, the formal confirmatory secondary outcome): −2.19 (semaglutide) vs −3.36 (placebo) mL/min/1.73 m²/yr; between-group difference **1.16 (95% CI 0.86–1.47), P<0.001**. [Table 2]
- **Early/acute component, baseline→week 12:** difference only **−0.03 (95% CI −0.56 to 0.51)** — essentially no between-group difference in the initial ~12 weeks, meaning the trial's early period does **not** show a large acute hemodynamic dip attributable to semaglutide (contrast with SGLT2i trials, which typically show an early dip followed by slope divergence).
- **Chronic slope, week 12→end of trial:** difference **0.94 (95% CI 0.62–1.26)** — this is the "chronic" component isolated from any early/acute effect, and it is slightly smaller than the total-slope difference (1.16), consistent with almost all of the treatment effect accruing after week 12 rather than in an early creatinine shift.
- **Creatinine-based vs cystatin-C-based eGFR at week 104 (post hoc concordance check):** creatinine-based difference 3.30 (95% CI 2.43–4.17) vs cystatin-C-based difference **3.39 (95% CI 2.63–4.15)** — near-identical, which the authors use to argue that the observed slope benefit is **not an artifact of semaglutide-induced muscle-mass/weight loss lowering serum creatinine independent of true GFR change** [`FLOW-PRIMARY-2024`, Discussion, lines 1019–1022, 1076–1080]. This is a biologically important but still single-trial, industry-sponsored concordance check, not independent confirmation.
- **SGLT2i-subgroup slopes** (from `FLOW-SGLT2-2024`, for context — see §7): with baseline SGLT2i, total slope difference 0.75 (95% CI −0.01 to 1.50); without baseline SGLT2i, 1.25 (95% CI 0.91–1.58); P-interaction 0.237 (no significant heterogeneity, but the SGLT2i-subgroup CI crosses zero).

---

## 6. Absolute risk / ARR / NNT — methods, values, and what is NOT estimable

Two independently reported NNT methods exist for FLOW, and they agree:

1. **Primary paper** (method not explicitly named beyond "over 3 years"; almost certainly the same pseudo-observation/Aalen–Johansen-based approach used in the CV-severity paper): primary outcome NNT = **20 (95% CI 14–40)** over 3 years; MACE NNT = **45 (95% CI 23–623)**; all-cause-death NNT = **39 (95% CI 21–238)**. [`FLOW-PRIMARY-2024`, lines 411–413, 470–472]
2. **`FLOW-CKDSEVERITY-2025`** states its explicit method: *"Absolute risk difference estimated using a generalized linear regression model with identity link on pseudo-observations from the Aalen–Johansen estimate at Week 156 [≈3 years]. NNT = 1/(cumulative incidence for placebo − cumulative incidence for semaglutide 1.0 mg)."* Using this method it reports **CV death/MI/stroke (MACE): ARR −0.02 (−0.04 to −0.002), NNT 45 (23–623)**; **all-cause death: ARR −0.03 (−0.05 to −0.004), NNT 39 (21–238)** — identical to the primary paper's numbers, confirming both use the same week-156/3-year horizon and the same pseudo-observation method.

**Not estimable from the material reviewed this session:**
- **Kidney-specific composite (excl. CV death) ARR/NNT** — neither the primary paper, the supplement, nor `FLOW-CKDSEVERITY-2025`/`FLOW-SGLT2-2024`/`FLOW-MRA-2025` report a week-156/3-year absolute risk or NNT specifically for the 218/260-event kidney-specific composite. Per CLAUDE.md rule 8, I am **not** computing one from the raw crude proportions (18.7%/23.2%-style event percentages are cumulative over a variable, competing-risk-affected observation period averaging 3.4 years — not a clean time-specific absolute risk — and naively subtracting crude percentages would not use the same Aalen–Johansen/pseudo-observation adjustment the trialists used elsewhere). **Label: not estimable without applying the sponsor's own week-156 pseudo-observation method to this specific composite, which has not been published as far as this review found.**
- Any subgroup-specific (SGLT2i, MRA, KDIGO-stratum) ARR/NNT beyond the two exceptions given directly in the source text (`FLOW-MRA-2025` reports the MRA-subgroup HRs but not ARR/NNT; `FLOW-CKDSEVERITY-2025` reports overall, not stratum-specific, ARR/NNT) — flag as an evidence gap for the director/CKM lane rather than compute post hoc.

---

## 7. Early stopping, planned/observed events, alpha spending, estimand, multiplicity, competing risks

- **Sample-size/power:** designed to detect a 20% relative risk reduction with 90% power at overall one-sided α=2.5%, requiring a minimum of **854 primary-outcome events**. [`FLOW-PRIMARY-2024`, lines 172–176]
- **Interim analysis:** pre-specified single interim analysis planned after **~2/3 of 854 ≈ 569–570** events; triggered when **~570 events** had accrued; DMC unblinded assessment occurred **October 10, 2023**, recommending early stopping for efficacy because the O'Brien-Fleming-approximating **Lan–DeMets alpha-spending** boundary was crossed; no futility stopping rule was included. [`FLOW-PRIMARY-2024`, lines 178–180, 285–289; `FLOW-SUPPLEMENT-2024`, lines 493–513]
- **Final database lock:** February 6, 2024, with **741 primary-outcome events accrued** (well short of the 854 originally planned had the trial run to completion) — median follow-up 3.4 years (range 0–4.5). [`FLOW-SUPPLEMENT-2024`, lines 514–515; `FLOW-PRIMARY-2024`, lines 292–296]
- **Alpha-spending consequence:** the nominal two-sided significance threshold for the primary outcome and all confirmatory secondary outcomes was recalculated (based on the *information fraction* = 741/854 observed/planned events) to **0.0322** — i.e., the reported P values (primary 0.0003, MACE 0.029, all-cause death 0.01) were tested against this stricter-than-0.05 boundary, not against a naive 0.05. The same information fraction (not a separately re-derived one) was applied to the confirmatory secondary outcomes because their own event/information totals were not separately knowable at the time of the interim look. [`FLOW-SUPPLEMENT-2024`, lines 516–525]
- **Early-stopping caveat the master prompt asks to investigate explicitly:** stopping early at an interim analysis that crosses an efficacy boundary carries a well-known statistical property — the observed effect size at the stopping point is expected to be, on average, an overestimate of the true effect size ("regression to the truth" / stopping-time bias), especially when the boundary is crossed close to the trigger point rather than by a wide margin. FLOW crossed its efficacy boundary and stopped with 741/854 (87%) of planned information — a substantial but not overwhelming excess over the ~570-event interim trigger. **I did not find any published re-estimation of a bias-corrected HR** (e.g., a median-unbiased estimator) in the primary paper, supplement, or either subgroup paper reviewed; the reported HR of 0.76 should therefore be treated as the trial's as-reported estimate, with the standard caveat that early-stopped trials can somewhat overstate long-run effect size. This is a genuine, currently-unresolved gap in the local evidence, not resolved by anything I read.
- **Estimand:** the primary/confirmatory analyses use the **in-trial-period, intention-to-treat "treatment policy"-like estimand** (from randomization to end of trial participation, regardless of adherence or background-medication changes; missing data not imputed for the primary HR analysis). [`FLOW-PRIMARY-2024`, lines 181–186] Sensitivity analyses (Table S3) additionally probe an on-treatment/retrieved-dropout framing and a multiple-imputation-of-missing-eGFR framing; all point in the same direction (§3).
- **Model:** stratified (by baseline SGLT2i use) Cox proportional-hazards model, treatment as a categorical fixed factor, P values from a score test; eGFR slope from a linear mixed-effects/random-effects model (participant random intercept, time random slope, treatment×time interaction fixed).
- **Competing risks:** cumulative incidence curves (Fig. 1) use the **Aalen–Johansen estimator**, treating non-CV/non-renal death as a competing risk for the primary outcome (and all-cause death excl. renal death as the competing risk for the kidney-specific composite, per the `FLOW-SGLT2-2024` figure legend) — this is the methodologically correct choice for a composite that includes a death component, avoiding the overestimation of cumulative incidence that a naive Kaplan–Meier (1−KM) approach would produce in the presence of competing mortality.
- **Multiplicity:** controlled via the pre-specified hierarchical (fixed-sequence) testing of the 3 confirmatory secondary outcomes, gated on primary-outcome superiority; all other outcomes (supportive/exploratory) are explicitly unadjusted and their CIs are not to be used as hypothesis tests. [`FLOW-PRIMARY-2024`, lines 158–170]

---

## 8. Subgroup power/interaction cautions (SGLT2i, MRA, eGFR/UACR/KDIGO, CV phenotype)

### 8.1 SGLT2i (`FLOW-SGLT2-2024`, Mann et al., Nat Med 2024 — prespecified)

550/3533 (15.6%) participants on SGLT2i at baseline (277 semaglutide/273 placebo); 2983 not on SGLT2i at baseline.

| Subgroup | Semaglutide events/N | Placebo events/N | HR (95% CI) | P | P-interaction |
|---|---:|---:|---:|---:|---:|
| **Primary composite (5-component), overall** | 331/1767 | 410/1766 | 0.76 (0.66–0.88) | — | — |
| — with baseline SGLT2i | 41/277 (14.8%) | 38/273 (13.9%) | **1.07 (0.69–1.67)** | 0.755 | **0.109** |
| — without baseline SGLT2i | 290/1490 (19.5%) | 372/1493 (24.9%) | 0.73 (0.63–0.85) | <0.001 | |
| **Kidney-specific composite (4-component, excl. CV death)** | | | | | |
| — with baseline SGLT2i | 32/277 (11.6%) | 27/273 (9.9%) | 1.18 (0.71–1.98) | 0.532 | **0.100** |
| — without baseline SGLT2i | 186/1490 (12.5%) | 233/1493 (15.6%) | 0.75 (0.61–0.90) | 0.003 | |
| MACE | — | — | — | — | 0.741 (no heterogeneity) |
| All-cause death | — | — | — | — | 0.901 (no heterogeneity) |
| Total eGFR slope (mL/min/1.73 m²/yr, between-group diff) | with SGLT2i: 0.75 (−0.01 to 1.50) | without: 1.25 (0.91–1.58) | — | — | 0.237 |
| UACR reduction at wk104 | with SGLT2i: 24% (4–39%) | without: 34% (26–40%) | — | — | 0.279 |

**Why the baseline-SGLT2i point estimate crosses the null (HR 1.07) and is directionally reversed for the primary composite:** the authors themselves attribute this explicitly to **low statistical power**, not to a true harmful interaction — verbatim: *"the power for testing interactions was low because the number of participants using SGLT2i at baseline was small, at just 15.6% of randomized participants... kidney disease events occurred later (~5% at 24 months) versus MACE (~5% at 12 months), which also reflects lower power to detect treatment effects on kidney outcomes within the trial time frame."* [`FLOW-SGLT2-2024`, lines 480–488] **P-interaction = 0.109 (primary) / 0.100 (kidney-specific) is not statistically significant, and a nonsignificant interaction test here must not be read as proof of a true null or harmful interaction in this subgroup** — the point estimate (1.07/1.18) with wide, null-crossing CIs in a subgroup with only 41+38=79 primary events is fully compatible with a modest true benefit obscured by sampling noise (per CLAUDE.md rule 5).

**Post-randomization SGLT2i initiation:** more placebo-arm participants without baseline SGLT2i started one during the trial than semaglutide-arm participants (~20% vs ~10% by 36 months) [`FLOW-SGLT2-2024`, lines 109–114] — this differential contamination, if anything, would tend to *narrow* the apparent semaglutide-vs-placebo treatment effect in later follow-up (since more placebo patients gain SGLT2i's independent kidney/CV benefit), making the observed benefit, if biased at all by this imbalance, conservative rather than inflated. Analyzing SGLT2i-use (baseline+initiated) as a time-dependent covariate gave a similar primary-outcome HR (0.75, 95% CI 0.65–0.86) to the ITT/baseline-only stratified analysis.

**Conclusion for this section, matching CLAUDE.md rule 6:** FLOW's SGLT2i subgroup data are consistent with no important treatment-effect heterogeneity by SGLT2i status, and directionally preserve eGFR-slope/UACR/MACE/mortality benefit regardless of SGLT2i use — but the subgroup, especially the baseline-SGLT2i-user primary/kidney-specific composite analyses (79 and 59 events respectively), is **underpowered to establish a definitive additive hard-kidney benefit of semaglutide on top of SGLT2i**, and no randomized evidence in FLOW demonstrates superiority of the combination over either drug alone.

### 8.2 MRA (`FLOW-MRA-2025`, Rossing et al., Diabetes Care 2025 — prespecified)

n=257 with baseline MRA (136 semaglutide/121 placebo; predominantly spironolactone, essentially no finerenone) vs n=3276 without (1631 semaglutide/1645 placebo).

- Primary kidney outcome (composite of ≥50% eGFR reduction, kidney failure, or death from kidney/CV causes): **MRA subgroup — 59 events, HR 0.51 (95% CI 0.30–0.86), 49% relative reduction; non-MRA subgroup — 682 events, HR 0.79 (95% CI 0.68–0.92), 21% relative reduction; P-interaction = 0.12** (not significant).
- MACE and all-cause mortality: no heterogeneity by MRA use (P-interaction > 0.7 for both).
- UACR reduction at week 104: 15% (95% CI −41 to 31) in MRA users vs 33% (26–39) in nonusers, P-interaction 0.22 (wide, imprecise CI in the small MRA-user group).
- eGFR-decline reduction: similar between subgroups (P-interaction 0.71).

**Interpretation:** the *numerically larger* point-estimate benefit in the (much smaller) MRA subgroup (HR 0.51 vs 0.79) is almost certainly a **power/precision artifact** — 59 events with wide, imprecise CIs (0.30–0.86) versus 682 events with a tight CI — and is not compatible evidence of a true synergistic effect given the nonsignificant, generously-wide interaction P of 0.12. **Critically, baseline MRA use was predominantly spironolactone, not finerenone; finerenone had not received regulatory approval when FLOW enrollment was underway, so this subgroup provides essentially no direct randomized evidence about a semaglutide+finerenone combination** — consistent with CLAUDE.md rule 6 and master-prompt Section XIV, this analysis must **not** be cited to support a "semaglutide + finerenone has proven additive hard-kidney benefit" claim.

### 8.3 eGFR / UACR / KDIGO / CV-phenotype (`FLOW-CKDSEVERITY-2025`, Mahaffey et al., Eur Heart J 2025 — prespecified)

Baseline distribution known for 3532/3533 (99.97%): eGFR <60 = 2813 (79.6%), ≥60 = 719 (20.4%); UACR <300 = 1113 (31.5%), ≥300 = 2419 (68.5%); KDIGO low/moderate = 242 (6.8%), high = 878 (24.9%), very high = 2412 (68.3%).

- **CV death/MI/stroke composite (MACE), overall:** HR 0.82 (0.68–0.98). Consistent across eGFR, UACR, and KDIGO strata (all P-interaction >0.13; KDIGO-specific P-interaction 0.79, HRs ranging 0.67–0.84 across risk classes). The eGFR<30/30-<45/45-<60/≥60 finer strata "had small numbers and broad CIs" per the paper's own characterization.
- **Nonfatal MI, by eGFR — the one statistically significant CV-phenotype interaction found:** HR 0.94 (0.63–1.39) if eGFR<60 vs HR 0.28 (0.09–0.87) if eGFR≥60; **P-interaction = 0.04**. The authors' own interpretation: *"not aware of biologically plausible mechanisms and, given the number of interactions tested without correction for multiplicity and opposite directions of effect, believe these are likely due to chance."*
- **All-cause mortality, by UACR — the other statistically significant interaction:** UACR≥300 mg/g HR 0.70 (0.57–0.85, favors semaglutide) vs UACR<300 mg/g HR 1.17 (0.83–1.65, trend toward *higher* mortality with semaglutide); **P-interaction = 0.01**. Per the authors and per CLAUDE.md rule 5, **this single nominally-significant interaction — out of 15 interaction tests reported, uncorrected for multiplicity, with no plausible mechanism and a direction-reversing pattern — should be read as a hypothesis-generating chance finding, not as evidence that semaglutide is ineffective or harmful in normo-/microalbuminuric CKD.** It is nonetheless a real signal worth explicit mention in the "evidence gaps" deliverable, since UACR<300 comprised only 31.5% of the trial and had comparatively few events.
- **Absolute risk / NNT (week 156, pseudo-observation method — see §6):** CV death/MI/stroke NNT 45 (23–623); all-cause death NNT 39 (21–238) — identical to the primary-paper figures.
- **Design-relevant limitation stated by the authors themselves:** *"FLOW was not designed with adequate events/power to definitively evaluate treatment effects in subgroups defined by CKD severity; CIs are wide though no statistically significant interaction was observed for the primary composite. CKD was not analysed as a continuous variable due to small numbers of events at the extremes."*

---

## 9. Contextual comparison to CREDENCE, DAPA-CKD, EMPA-KIDNEY, FIDELIO-DKD/FIDELITY

**Per CLAUDE.md rule 9 and master-prompt Section XXIV, this table is for context only. Populations, endpoint definitions, background therapy era, follow-up duration, and event rates all differ across these trials — do not rank drugs/therapies by HR, and do not infer relative efficacy from cross-trial HR comparison.**

| Trial | Drug (dose) | N | Diabetes required? | Approx. eGFR floor/design | Primary composite (brief) | Primary HR (95% CI) | Median follow-up |
|---|---|---:|---|---|---|---:|---:|
| **FLOW** (`FLOW-PRIMARY-2024`) | Semaglutide 1.0 mg SC weekly | 3533 | Yes (T2D) | eGFR 25–75 (two pathways; ≥60 capped at 20% of N) | Kidney failure / ≥50% eGFR decline / kidney death / **CV death** | 0.76 (0.66–0.88) | 3.4 y (stopped early) |
| **CREDENCE** (canagliflozin, NEJM 2019, doi 10.1056/NEJMoa1811744, PMID 30990260) | Canagliflozin 100 mg | 4401 | Yes (T2D) | eGFR ≥30–<90 (lower floor ~30, higher than FLOW/DAPA-CKD) | ESKD / doubling of serum creatinine / renal or CV death | 0.70 (0.59–0.82) | 2.6 y (stopped early) |
| **DAPA-CKD** (dapagliflozin, NEJM 2020, doi 10.1056/NEJMoa2024816, PMID 32970396) | Dapagliflozin 10 mg | 4304 (2152/2152) | No — CKD with or without T2D | eGFR 25–75, UACR ≥200 mg/g (lower UACR floor than CREDENCE) | Sustained ≥50% eGFR decline / ESKD / renal or CV death | 0.61 (0.51–0.72) | 2.4 y (stopped early) |
| **EMPA-KIDNEY** (empagliflozin, NEJM 2023, doi 10.1056/NEJMoa2204233, PMID 36331190) | Empagliflozin 10 mg | 6609 (3304/3305) | No — >50% without diabetes; broadest eGFR range (down to ~20, and normoalbuminuric patients allowed at higher eGFR) | eGFR ≥20; UACR unrestricted at lower eGFR strata | Kidney disease progression or CV death | 0.72 (0.64–0.82) | ~2 y (stopped early) |
| **FIDELIO-DKD** (finerenone, NEJM 2020, doi per PubMed 33264825) | Finerenone (nonsteroidal MRA) | 5674 (2833/2841) | Yes (T2D) | eGFR 25–<75, albuminuric DKD | Kidney failure / sustained ≥40% eGFR decline / renal death | 0.82 (0.73–0.93) | 2.6 y |
| **FIDELITY pooled** (FIDELIO-DKD + FIGARO-DKD, Eur Heart J 2022) | Finerenone | 13,026 | Yes (T2D) | Broader combined eGFR/UACR range across the two component trials | CV composite; separately, kidney composite | CV: 0.86 (0.78–0.95); kidney composite: 0.77 (0.67–0.88) | 3.0 y |

**Explicit non-ranking caveats:**
- Endpoint definitions differ materially: FLOW/CREDENCE/DAPA-CKD/EMPA-KIDNEY's primary composites **include CV death**, while FIDELIO-DKD's primary composite does **not** (kidney-only: failure/40% eGFR decline/renal death) — a "smaller" HR is not automatically a "bigger" kidney effect if the composite denominators/components differ.
- eGFR floors and UACR thresholds differ (CREDENCE's lower eGFR floor ~30 vs FLOW's ~25; EMPA-KIDNEY's much broader eGFR floor ~20 and inclusion of normoalbuminuric patients at higher eGFR vs FLOW/CREDENCE/DAPA-CKD requiring albuminuria) — the trials are not sampling the same population.
- Diabetes requirement differs: only FLOW, CREDENCE, and FIDELIO-DKD/FIGARO-DKD required T2D; DAPA-CKD and EMPA-KIDNEY enrolled substantial non-diabetic CKD populations — FLOW's semaglutide data cannot be extrapolated to non-diabetic CKD the way DAPA-CKD/EMPA-KIDNEY's SGLT2i data can be discussed for that population.
- Background therapy era differs: none of CREDENCE/DAPA-CKD/EMPA-KIDNEY/FIDELIO-DKD had semaglutide as background; FLOW had only 15.6% baseline SGLT2i and ~7.3% MRA (no finerenone) as background — none of these trials tested the others' drugs as combination background at scale.
- Follow-up duration differs materially (FLOW 3.4 y vs EMPA-KIDNEY ~2 y vs CREDENCE/FIDELIO-DKD 2.6 y vs DAPA-CKD 2.4 y vs FIDELITY 3.0 y), which affects absolute event accrual and any implicit "annualized" comparison.
- All five FLOW-comparator numbers above were obtained via WebSearch snippets quoting the NEJM/Eur Heart J-published figures (NEJM full text itself returned HTTP 403 to direct fetch); cross-checked for internal numeric consistency across independent snippets/outlets, but **not independently re-verified against the primary PDF/HTML the way the FLOW numbers were** — treat CREDENCE/DAPA-CKD/EMPA-KIDNEY/FIDELIO-DKD/FIDELITY figures above as web-verified-secondary-confidence, not local-primary-confidence, and re-check against the primary article if any of these numbers becomes load-bearing for a headline claim in later deliverables.

---

## 10. Discontinuation, adherence, vital-status completeness (context for interpreting event counts)

- Adherence to trial regimen: 89% of planned time. Vital status confirmed for 3482/3533 (98.6%); 34 participants withdrew consent; 2 Russian sites closed early (sponsor-sanctioned, 14 participants affected). [`FLOW-PRIMARY-2024`, lines 292–303]
- AE-driven permanent discontinuation: 233/1767 (13.2%) semaglutide vs 211/1766 (11.9%) placebo, driven mainly by GI disorders (79 [4.5%] vs 20 [1.1%]). [Table 3]
- **Overall (any-reason) permanent discontinuation — a genuine discrepancy, see §11 Discrepancy #2.**

---

## 11. Discrepancy log

| # | Item | Value A | Value B | Locators | Assessment |
|---|---|---|---|---|---|
| 1 | CV death's share of primary-composite events | 39.4% (computed: (123+169)/(331+410) from Table 2 component counts) | "approximately 35%" (stated directly) | `FLOW-PRIMARY-2024` Table 2 (`FLOW.pdf` p.8) vs `FLOW-SUPPLEMENT-2024` line 755 (Table S2) | Unresolved. Possible differing counting rule (independent per-component counts in Table 2 vs. a first-qualifying-event hierarchy used for the narrative "≈35%" claim). Not decision-critical (both support "CV death is a large minority, not the majority, driver"), but the two numbers should not both be quoted as if interchangeable in the final synthesis — flag for director. |
| 2 | Overall (any-reason) permanent treatment discontinuation | **26%** of participants ("Semaglutide or placebo was permanently discontinued by 26% of participants during the trial") | **28.8%** ("permanent discontinuation of randomized treatment was reported in 28.8%") | `FLOW-PRIMARY-2024`, line ~303 vs `FLOW-SGLT2-2024` (Mann et al. 2024), line 106 | Unresolved. Both describe the same trial-wide metric but differ by ~3 points; possibly different denominators/definitions (e.g., "discontinuation of trial product" vs. "discontinuation of randomized treatment," or a reporting-date/analysis-population difference between the May 2024 primary paper and the June 2024 companion paper). Not load-bearing for any headline efficacy claim, but should not be silently harmonized without checking the original source tables. |
| 3 | Randomized N, primary paper vs. design/rationale paper | Primary paper: N=3533 randomized | Design paper (`FLOW-DESIGN-2023`, per source-librarian lane 01 §5): N=3534 stated in that paper's own abstract | `FLOW-PRIMARY-2024` line 41 vs. librarian's report of `FLOW-DESIGN-2023` (not independently re-verified by this lane — design paper not fetched locally) | **Not independently verified by this lane** — inherited from `01_source_librarian.md`; flagging forward rather than duplicating investigation, since the design paper is not in local `fulltext/`. |
| 4 | Table 2 extraction fidelity | `.md` extraction of Table 2 is mirrored/reversed and effectively unusable as a direct source | PDF page-image transcription (this lane, §0/§3) is complete and internally consistent (component counts sum correctly to composite totals; cross-checked against Table S3 sensitivity-analysis primary/MACE/all-cause-death numbers, which match) | `FLOW_primary_NEJM_2024_fulltext.md` lines ~480–535 vs `FLOW.pdf` pages 8–9 | Resolved *for this lane's purposes* — use the PDF-transcribed Table 2 in §3 as authoritative going forward; the `.md` file's Table 2 block should not be quoted directly by any other lane. |
| 5 | Kidney-specific composite NNT | Not reported anywhere located this session | — | See §6 | Not a numeric conflict — a genuine gap. Explicitly label "not estimable" rather than compute; do not let a later deliverable quietly back-calculate one from crude percentages. |

---

## 12. Handoff

**Files written this session:** only this file, `research/semaglutide_ckd_flow/2026-09-05/lanes/02_trialist_statistics.md`. No `sources/retrieved/` note added (no new PDFs were downloaded; all FLOW-specific numbers came from files already in local `fulltext/`, and the comparator-trial numbers came from WebSearch snippets of primary-journal pages, not from downloaded/parsed full texts, so there is no retrieved-source artifact to log beyond what appears above with its own URLs/DOIs/PMIDs).

**Sources actually checked (opened and read, not just cited from memory):** `FLOW.pdf` (page images 8–9), `FLOW_primary_NEJM_2024_fulltext.md` (full), `FLOW_supplement_fulltext.md` (full), `glp1_cardiorenal_Mann_2024.md` (full), `glp1_cardiorenal_Mahaffey_2025.md` (full), `glp1_cardiorenal_Rossing_2025.md` (abstract as embedded), `01_source_librarian.md` (read for cross-lane consistency, not modified), plus WebSearch verification passes for CREDENCE/DAPA-CKD/EMPA-KIDNEY/FIDELIO-DKD/FIDELITY.

**Unresolved conflicts requiring director attention:** the two discrepancies (#1 CV-death share 35% vs 39.4%; #2 discontinuation 26% vs 28.8%) in §11, neither of which changes any qualitative conclusion but both of which should not be silently harmonized in `14_MASTER_EVIDENCE_TABLE.md` without picking one value and stating why.

**Coordination note (director relay, Wave 0/1):** `SELECT-FLOW-SOUL-POOLED-2026` (Lancet Diabetes Endocrinol, DOI 10.1016/S2213-8587(26)00134-8) is **outstanding, owned by `flow-methodologist`** — it is a SELECT/FLOW/SOUL pooled post-FLOW analysis, outside this lane's assigned brief (FLOW trial anatomy/statistics only). Not chased by this session; declined per director's coordination request to avoid duplicate retrieval.

**Next sessions that need this evidence:**
- **`flow-nephrologist` (lane 03)** — for kidney-specific interpretation, needs §3 (full Table 2), §4 (CV-death dependency), §8.3 (KDIGO/eGFR/UACR subgroup power caveats, especially the UACR<300 mortality interaction).
- **`flow-ckm` (lane 05)** — for SGLT2i/MRA/finerenone positioning, needs §8.1 and §8.2 verbatim, plus the explicit "not established" framing for both combinations (CLAUDE.md rule 6).
- **`flow-methodologist` (lane 06)** — needs §5 (creatinine/cystatin-C concordance as an "independent of weight-loss confound" argument, but flagged as single-trial/industry-sponsored, not settled), §7 (early-stopping bias caveat — genuinely unresolved, no bias-corrected HR found), and §9 (non-ranking cross-trial caveats) for the causal-independence and multiplicity sections.
- **Wave 2 peer reviewer of this lane:** please specifically stress-test §4 (my count of 39.4% vs the source's stated ≈35%) and §7's early-stopping bias paragraph, which is the one place in this memo where I flag an *analytic gap in the published literature itself* rather than a resolvable numeric disagreement.
