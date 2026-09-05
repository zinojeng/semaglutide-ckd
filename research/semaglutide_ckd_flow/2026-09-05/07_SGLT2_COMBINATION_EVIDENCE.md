# 07. Semaglutide + SGLT2 Inhibitor Combination Evidence

**Clinical question:** In a patient already receiving an ACEi/ARB and an SGLT2 inhibitor, what is the evidence that adding semaglutide further prevents kidney failure?

## The data (`FLOW-SGLT2-2024`, Mann, Nat Med 2024 — prespecified, non-randomized baseline-use subgroup; Figs. 1–2/Table 1 and Extended Data Figs. 4–7; local source lines 34–42, 65–128, 237–305, 984 onward)

Baseline SGLT2i users n=550 (15.6% of the trial; 277 semaglutide/273 placebo) vs non-users n=2,983 (1,490/1,493).

| Outcome | Users HR (95% CI), events | Non-users HR (95% CI), events | P-interaction |
|---|---|---|---|
| FLOW primary 5-component composite (including CV death) | 1.07 (0.69–1.67); 41/277 vs 38/273 | 0.73 (0.63–0.85); 290/1,490 vs 372/1,493 | 0.109 |
| Kidney-specific 4-component composite | 1.18 (0.71–1.98); 32/277 vs 27/273 | 0.75 (0.61–0.90); 186/1,490 vs 233/1,493 | 0.100 |
| Sustained ≥50% eGFR-decline component | 1.30 (0.76–2.26); 30/277 vs 23/273 | 0.66 (0.53–0.83); 135/1,489 vs 190/1,493 | 0.023 (nominal; unadjusted for multiplicity) |
| Total eGFR-slope difference | 0.75 (−0.01, 1.50) | 1.25 (0.91, 1.58) | 0.237 |
| UACR reduction, week 104 | 24% (4–39%) | 34% (26–40%) | 0.279 |
| MACE | — | — | 0.741 |
| All-cause death | — | — | 0.901 |

The prespecified creatinine-based analyses above are complemented by **post hoc cystatin-C analyses** (`FLOW-SGLT2-2024`, Results and Table 1; local source lines 411–450):

| Cystatin-C analysis | Baseline SGLT2i users | Baseline non-users | P-interaction |
|---|---|---|---|
| Five-component outcome, using eGFRcystatin-C change and no confirmatory-measurement requirement | HR 0.74 (0.47–1.16) | HR 0.70 (0.60–0.82) | 0.844 |
| Total eGFRcystatin-C slope difference, mL/min/1.73m²/yr | +0.92 (0.16–1.68) | +1.55 (1.21–1.88) | 0.142 |
| Week-104 eGFRcystatin-C change, semaglutide−placebo | +3.5 (1.6–5.4) | +3.4 (2.5–4.2) | 0.901 |

Across the other cystatin-C renal outcomes, interaction P values ranged from 0.799 to 0.983. These post hoc concordant estimates reduce concern that the subgroup's slope signal is solely a creatinine/muscle-mass artifact; they do not cure the small subgroup, nonfactorial design, or hard-composite uncertainty.

**Explicit power context (authors' own statement):** power for these interaction tests was low because baseline SGLT2i use was only 15.6% of the trial, and kidney events accrue later in follow-up than MACE events. Post-randomization SGLT2i uptake was also asymmetric: by 36 months, roughly 20% of the placebo arm and 10% of the semaglutide arm had newly initiated an SGLT2i — a non-randomized, time-dependent contamination of the “non-user” contrast whose bias direction/magnitude cannot be identified from the initiation proportions alone (`FLOW-SGLT2-2024`, Extended Data Fig. 4; local lines 110–128, 984 onward).

Two post hoc analyses must not be conflated. First, a Cox model treating **SGLT2i use as a time-varying covariate** estimated the **semaglutide-versus-placebo coefficient** as HR **0.75 (0.65–0.86)**; this is not an ever-versus-never SGLT2i effect. Second, an exposure-defined analysis estimated semaglutide versus placebo as HR **0.88 (0.66–1.17)** among participants using an SGLT2i at baseline or initiating one during follow-up and HR **0.70 (0.59–0.82)** among never-users, P-interaction **0.169** (`FLOW-SGLT2-2024`, Results; local lines 120–128). Both are hypothesis-generating because on-study exposure was not randomized.

## Supported

- No statistically significant treatment-by-baseline-SGLT2i heterogeneity was detected for the primary composite, kidney-specific composite, eGFR slope, UACR, MACE, or all-cause death. The isolated sustained-≥50%-eGFR-decline component interaction was nominally significant (P=0.023), but it was one component among multiple comparisons, unadjusted for multiplicity, and based on few events; it neither proves harm in baseline users nor establishes true effect modification. Because the user-subgroup confidence intervals are wide, the composite analyses do **not** exclude clinically important incremental benefit, no effect, or harm.
- Creatinine-based eGFR-slope and UACR-reduction point estimates run in a directionally consistent, supportive direction across the SGLT2i-user and non-user strata (though the CI for the creatinine slope-difference in users, 0.75 [−0.01, 1.50], crosses the null); post hoc cystatin-C slope/week-104 estimates are concordant, with no detected interaction.
- CV/mortality heterogeneity was not statistically detected by baseline SGLT2i use (P-interaction 0.741/0.901); these interaction tests do not establish additivity or equivalence.

## Not established

- **Definitive randomized additive hard-kidney benefit.** The primary and kidney-specific hard-composite point estimates in SGLT2i users — HR **1.07** and **1.18** respectively — sit on the null side of 1 with wide, asymmetric confidence intervals. This does **not** directionally support a retained, let alone additive, hard-outcome benefit on top of SGLT2i; it reflects a genuinely underpowered subgroup (only 79 primary-outcome events among users), not a null result.
- **Exact incremental absolute risk reduction.** No stratum-specific ARR/NNT for SGLT2i users has been published; none should be back-calculated.
- **Superiority of the combination over either monotherapy.** FLOW did not randomize the combination against either drug alone; the baseline-use subgroup is an observational contrast within a randomized trial, not a factorial design.

## Indirect/contextual supporting evidence — kept secondary to FLOW

- `SMART-NONDIABETIC-2025`: a 24-week, non-diabetic-CKD surrogate-endpoint RCT (UACR **52.1% lower** with semaglutide) — surrogate-only, no hard-outcome inference, and a different population than FLOW's diabetic CKD cohort (primary report, Results; DOI 10.1038/s41591-024-03327-6, PMID 39455729).
- `AMPLITUDEO-SGLT2-2022` (efpeglenatide): the primary structured abstract was directly checked. Renal-composite HR was 0.70 (0.59–0.83) without and 0.52 (0.33–0.83) with baseline SGLT2i; all treatment-by-SGLT2i interaction P values were >0.2. This was an exploratory, nonfactorial baseline-use subgroup (618 SGLT2i users) of a different molecule, so it supports class-adjacent plausibility—not semaglutide-specific additivity. Locator: Lam et al., *Circulation* 2022, structured abstract Results; DOI 10.1161/CIRCULATIONAHA.121.057934, PMID 34775781.
- `SEMA-CANA-EARLYDKD-2026`: a 24-week four-arm RCT (N=120; 30/arm) directly randomized canagliflozin, semaglutide, their combination, or control in early DKD. Its abstract reports greater UACR reduction with combination therapy but no significant between-group eGFR difference; it does not provide an exact UACR effect estimate and has no hard-outcome follow-up. This is direct randomized **surrogate-only, small/short-term** evidence, not kidney-failure evidence. Locator: PubMed abstract Methods/Results; DOI 10.36721/PJPS.2026.39.7.204.1, PMID 42170981.
- `GLP1-SGLT2-BMJ-2024`: a UK target-trial-emulation cohort found that adding a GLP-1RA to SGLT2i yielded only 36 serious renal events and HR 0.67 (0.32–1.41) versus SGLT2i alone; class-level exposure included semaglutide among several agents. Residual confounding, short median follow-up (8.5 months), class mixing, and a very wide CI preclude a causal additivity claim. Locator: [BMJ primary full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11043905/), Abstract and Table 4; DOI 10.1136/bmj-2023-078242, PMID 38663919.
- A 2026 UK target-trial emulation (`GLP1-ADDON-SGLT2-2026`) included 33,659 eligible treatment initiations among 31,650 unique people already receiving an SGLT2i and reported kidney-disease-progression HR 0.73 (0.58–0.92) for adding a GLP-1RA versus active comparator. It remains nonrandomized, class-level, and not semaglutide-specific. Locator: PubMed structured abstract Methods/Findings; *Lancet Primary Care* 2026; DOI 10.1016/j.lanprc.2026.100139, PMID 42109572. The direct FLOW subgroup and the small randomized surrogate study above retain precedence for this review.
- `GLP1-CLASSMETA-BADVE-2025` and `SELECT-FLOW-SOUL-POOLED-2026` (see `06`) provide aggregate pooled kidney-effect estimates across trials/populations, but the retrieved evidence did not establish treatment-effect homogeneity by dose or route. They are not combination-therapy trials and do not speak to the SGLT2i-add-on question specifically.
- `COMBO-MODEL-NEUEN-2024` (see `08` and `13`) offers a *modeled*, non-FLOW-inclusive estimate of combined SGLT2i+GLP-1RA+finerenone benefit under an explicit additivity assumption — useful only to illustrate the concept, never as evidence of demonstrated additive efficacy.

The requested search categories are therefore closed as follows: AMPLITUDE-O primary subgroup **found**; SGLT2-outcome-trial background GLP-1RA evidence and large observational/target-trial-emulation studies **found but indirect/class-level**; one small randomized semaglutide+canagliflozin surrogate trial **found**; no adequately powered randomized semaglutide+SGLT2i hard-kidney-outcome factorial trial **found** as of 2026-09-05.

## Preferred wording (per master prompt §XXVII pattern)

> “Available subgroup evidence did not detect statistically significant heterogeneity of semaglutide's effect by baseline SGLT2i use for the FLOW primary five-component composite (including CV death), kidney-specific composite, eGFR slope, UACR, MACE, or all-cause mortality (P-interaction values **≥0.100**). One individual component—sustained ≥50% eGFR decline—had a nominal P-interaction of 0.023, but this isolated, multiplicity-unadjusted finding does not prove harm or true effect modification. The composite results do not constitute randomized evidence of an additive hard-kidney-outcome benefit, nor can they exclude clinically important incremental benefit or harm: the baseline-SGLT2i subgroup is small (15.6% of the trial; 79 primary events), its point estimates for the primary and kidney-specific composites are on the null side of 1 (HR 1.07 and 1.18) with wide CIs, and on-study SGLT2i uptake was asymmetric and non-randomized. The incremental benefit, harm, and additivity of semaglutide on top of an SGLT2 inhibitor therefore remain unresolved.”
