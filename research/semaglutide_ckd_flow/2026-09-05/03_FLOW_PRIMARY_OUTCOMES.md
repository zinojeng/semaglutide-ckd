# 03. FLOW Primary Outcomes

Source: `FLOW-PRIMARY-2024` Table 2 (journal p.116; local `fulltext/FLOW.pdf` PDF page 8; independently re-transcribed and cross-verified byte-identical by two Wave-1 lanes via two different extraction methods — treat as high-confidence, do not re-transcribe a third time), and `FLOW-SUPPLEMENT-2024` Tables S2/S3 (local Markdown lines 737–830).

## Table 2 — full reconstruction (N=1,767 semaglutide / N=1,766 placebo)

| Outcome | Semaglutide n (%) | Placebo n (%) | HR (95% CI) | P |
|---|---:|---:|---:|---:|
| **Primary composite (5 components)** | 331 (18.7) | 410 (23.2) | **0.76 (0.66–0.88)** | **0.0003** |
| — Persistent ≥50% eGFR reduction | 165 (9.3) | 213 (12.1) | 0.73 (0.59–0.89) | — |
| — Persistent eGFR <15 | 92 (5.2) | 110 (6.2) | 0.80 (0.61–1.06) | — |
| — Initiation of chronic KRT | 87 (4.9) | 100 (5.7) | 0.84 (0.63–1.12) | — |
| — Death from kidney-related causes | 5 (0.3) | 5 (0.3) | 0.97 (0.27–3.49) | — |
| — Death from cardiovascular causes | 123 (7.0) | 169 (9.6) | 0.71 (0.56–0.89) | — |
| **Kidney-specific composite (4 components, excl. CV death)** | 218 (12.3) | 260 (14.7) | **0.79 (0.66–0.94)** | — |
| Total eGFR slope, mL/min/1.73m²/yr (confirmatory secondary #1) | −2.19 | −3.36 | diff 1.16 (0.86–1.47) | <0.001 |
| Baseline→week 12 eGFR change, mL/min/1.73m² | −1.07 | −1.05 | diff −0.03 (−0.56 to 0.51) | — |
| Chronic eGFR slope, week 12→end, mL/min/1.73m²/yr | −2.36 | −3.30 | diff +0.94 (0.62–1.26) | — |
| MACE (confirmatory secondary #2) | 212 (12.0) | 254 (14.4) | 0.82 (0.68–0.98) | 0.029 |
| All-cause death (confirmatory secondary #3) | 227 (12.8) | 279 (15.8) | 0.80 (0.67–0.95) | 0.01 |

**Event-rate framing (primary Results):** 5.8 vs 7.5 events per 100 patient-years for the primary composite. **NNT (primary composite, 3-year): 20 (95% CI 14–40).** NNT (MACE, week 156): 45 (23–623). NNT (all-cause death, week 156): 39 (21–238), both via a pseudo-observation/Aalen–Johansen method at week 156 (~3 years). Locators: primary-composite rates and 3-year NNT in `FLOW-PRIMARY-2024`, Results—“Primary Outcomes,” journal p.115 (local lines 400–415); week-156 MACE/all-cause-death NNTs and method in `FLOW-CKDSEVERITY-2025`, Methods—“Statistical analysis” and Results paragraph beginning “The absolute risk reduction ... at Week 156.”

## What "24% reduction" is and is not

FLOW's headline HR of 0.76 describes the **five-component composite that includes CV death**, not a purely kidney-progression endpoint. The kidney-specific four-component composite (excluding CV death) was reduced by a numerically smaller, directionally consistent 21% (HR 0.79, 95% CI 0.66–0.94), with a wider CI closer to the null. Per master prompt §VIII, the defensible headline wording is:

> "Semaglutide reduced the risk of the prespecified primary composite of major kidney events and cardiovascular death by 24% (HR 0.76, 95% CI 0.66–0.88); the kidney-specific composite excluding cardiovascular death was reduced by 21% (HR 0.79, 95% CI 0.66–0.94)."

Locator for both relative reductions and HR/CI pairs in this wording: `FLOW-PRIMARY-2024`, Table 2, journal p.116.

**Do not write** "24% reduction in kidney disease progression" without the CV-death caveat, and do not write that the result is "just a CV-death artifact" — both overstate in opposite directions.

## CV death's share of the composite — the non-negotiable correction

`FLOW-SUPPLEMENT-2024` (Table S2 note, line 755) states cardiovascular death accounted for **"approximately 35% of the components of the primary endpoint."** This is the *only* defensible wording. **Reject 37.2%, 41.2%, 39.4%, and any exact "35–40%" range** as precise first-event shares: the five component rows in Table 2 are not a mutually exclusive partition of the 331/410 first-composite-events — summing the semaglutide-arm component counts (165+92+87+5+123 = 472) already exceeds the 331 actual first-event total, proving overlap (a participant can accrue more than one component-level event while contributing only one event to the composite denominator). This was independently confirmed by two Wave-1/Wave-2 lanes using the same arithmetic check.

Two further points follow directly:
- **No exact first-event share is derivable from Table 2** by any arithmetic manipulation of the published component counts.
- **The ~35% figure is never a share of the treatment effect.** Event-share and effect-share are different quantities, and no source in this evidence base decomposes the observed HR into a "CV-death-attributable fraction."
- How much of the primary benefit is attributable to CV death therefore **cannot be validly answered** by subtracting event counts or HRs; report the five-component and kidney-specific composites side by side instead (as above), never as an algebraic decomposition.

## Individual hard-kidney components — not independently confirmatory

Kidney-replacement-therapy initiation (HR 0.84, 0.63–1.12), persistent eGFR<15 (HR 0.80, 0.61–1.06), and kidney death (HR 0.97, 0.27–3.49, only 5 vs 5 events) were each individually nonsignificant and outside the hierarchical confirmatory-testing sequence. `FLOW-PRIMARY-2024`'s own Discussion states the trial "was not powered to separately detect effects on kidney failure." The most frequently reported renal component was sustained ≥50% eGFR decline (HR 0.73, 0.59–0.89); because component rows overlap, it must not be labeled the causal or first-event "driver" of the kidney-specific composite. It is a clinically meaningful, supportive-secondary-level renal endpoint but is **not** the same as demonstrating reduced kidney failure (dialysis/transplant/eGFR<15/kidney death) as a stand-alone, adequately powered result. Do not describe FLOW as having "proven" a reduction in kidney failure per se; describe it as reducing the composite that includes kidney failure among its components, with the individual hard-failure components directionally favorable but not independently statistically confirmed. Locator for every component value in this block: `FLOW-PRIMARY-2024`, Table 2, journal p.116; power limitation: Discussion, journal p.119.

## Statistical caveats that qualify every number above

1. **Early stopping.** FLOW stopped after a single prespecified interim analysis crossing an efficacy boundary (DMC recommendation 2023-10-10; final lock 2024-02-06, 741/854 planned events). The primary-outcome HR/CI is adjusted for the group-sequential design (likelihood-ratio ordering); the three confirmatory secondary point estimates (eGFR slope, MACE, all-cause death) were **not** separately re-adjusted. These mechanics were independently checked in `FLOW-SAP-2023`, §2.1 pp.6–7, §2.3.1 p.12, and §2.4.1 pp.17–18; the dated DMC/final-lock and 741/854-event record is also in `FLOW-SUPPLEMENT-2024`, “Statistical Methods Relating to the Interim Analysis and Hierarchical Testing,” supplement PDF pp.16–17 (local lines 493–525). All should be read with the standard caveat that early-stopped trials can somewhat overstate the true long-run effect size; no bias-corrected (e.g., median-unbiased) re-estimate exists in any source reviewed for this project.
2. **Multiplicity.** Only the three confirmatory secondary outcomes were tested under the prespecified hierarchical gate; every subgroup analysis, the kidney-specific composite, individual components, and safety comparisons are supportive/exploratory and explicitly not multiplicity-adjusted per `FLOW-PRIMARY-2024`, Methods—“Statistical Analysis,” journal p.111, and `FLOW-SUPPLEMENT-2024`, “Statistical Methods Relating to the Interim Analysis and Hierarchical Testing,” supplement p.16.
3. **Competing risks.** The Aalen–Johansen estimator (not naïve Kaplan–Meier) is used throughout, appropriately treating death not captured by the outcome definition as a competing risk (`FLOW-PRIMARY-2024`, Figure 1 legend, journal pp.114–115; `FLOW-SUPPLEMENT-2024`, Table S3 note, supplement pp.26–27).
4. **A time-to-event kidney-specific composite ARR/NNT is not available** from any source in this evidence base — it has not been published for either the overall trial or any subgroup/stratum, and this project does not substitute a crude event-proportion back-calculation (per CLAUDE.md rule 8). Separately, `FLOW-MRA-2025` reports exploratory subgroup NNTs for the **five-component primary composite**, not for the kidney-specific composite (Results—“Outcomes With and Without MRA Use at Baseline”; see `08_MRA_FINERENONE_COMBINATION_EVIDENCE.md`); those values are therefore not an exception to this kidney-specific ARR/NNT gap.

## eGFR slope, safety, weight/HbA1c/BP, and UACR

See `dedicated` treatment in files `09` (mechanisms/eGFR-slope detail), `10` (safety), and the master evidence table (`14`) for full component detail; headline numbers are reproduced here for completeness:

- Total eGFR slope difference **1.16 (0.86–1.47) mL/min/1.73m²/yr**, P<0.001. Baseline→week 12 absolute eGFR change was essentially identical (**−1.07 vs −1.05 mL/min/1.73m²; difference −0.03 [−0.56 to 0.51] mL/min/1.73m²**), so there was no semaglutide-specific differential dip **through week 12**; the corpus contains no earlier FLOW time point, so an earlier resolved transient is not excluded. From week 12 to trial end, chronic slopes were **−2.36 vs −3.30 mL/min/1.73m²/yr; difference +0.94 (0.62–1.26) mL/min/1.73m²/yr**. These estimates are from `FLOW-PRIMARY-2024` Table 2 (journal p.116; local PDF page 8); the chronic-slope definition is also specified in `FLOW-SUPPLEMENT-2024` (local Markdown lines 472–474). Cystatin-C-based absolute eGFR-loss difference at week 104 was **3.39 (2.63–4.15) mL/min/1.73m²**; the post hoc creatinine-based comparator over the identical window was **3.30 (2.43–4.17) mL/min/1.73m²**. Their difference CI was not reported. This near-concordance lowers concern for a pure weight/muscle-mass-loss creatinine-generation artifact, but it neither excludes measurement artifact generally nor establishes weight independence. Locator for the two week-104 absolute-loss contrasts: `FLOW-PRIMARY-2024`, Results—“Other Outcomes,” journal p.116.
- **UACR time course:** observed mean UACR ratios separated by week 12 and the between-arm gap persisted through the main follow-up observations to week 182; week-208 estimates are visibly imprecise because only 216/201 participants contributed. The figure does not label exact ratios at every visit, so none are reverse-engineered here. The prespecified formal week-104 estimate was 0.60 (semaglutide) vs 0.88 (placebo), ratio-of-ratios **0.68 (0.62–0.75)**, i.e., ~32% (95% CI 25–38%) lower. Locator: `FLOW-SUPPLEMENT-2024`, Figure S2A, PDF p.19 (observed means over weeks 0, 12, 52, 104, 156, 182, and 208); `FLOW-PRIMARY-2024`, Results/Table 2, journal p.116 for the week-104 estimate.
- Body weight −4.10 kg (−4.56, −3.65) greater loss; HbA1c −0.81 percentage points (−0.90, −0.72) greater reduction; systolic BP −2.23 mmHg (−3.33, −1.13) greater reduction (all favoring semaglutide, reported as the between-group difference). Locator: `FLOW-PRIMARY-2024`, Results—“Other Outcomes,” journal p.116; `FLOW-SUPPLEMENT-2024`, Figure S2B–D, supplement p.19.
- Serious adverse events: 877 (49.6%) vs 950 (53.8%). Locator: `FLOW-PRIMARY-2024`, Table 3, journal p.120 (local PDF p.12) and structured abstract Results; `FLOW-SUPPLEMENT-2024`, Table S4, supplement pp.28–31.
