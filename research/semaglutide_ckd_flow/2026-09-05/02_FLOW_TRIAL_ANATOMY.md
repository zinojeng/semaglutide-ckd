# 02. FLOW Trial Anatomy

Source: `FLOW-PRIMARY-2024`, `FLOW-SUPPLEMENT-2024`, `FLOW-DESIGN-2023`, `FLOW-PROTOCOL-2021`, and `FLOW-SAP-2023` unless noted. All FLOW-primary locators refer to `fulltext/FLOW_primary_NEJM_2024_fulltext.md` / `fulltext/FLOW_supplement_fulltext.md` line ranges as independently triple-cross-verified in Wave 1/2 (see `01_SOURCE_INVENTORY.md` §1); FLOW-primary Table 2 values are from the PDF-page/`pdftotext -layout` re-transcription, not the garbled `.md` block. The official standalone protocol and SAP were opened/read locally on 2026-09-05; exact versions, hashes, and rights handling are logged in `01` §8 and `SOURCE_LEDGER.csv`.

## Identity

FLOW ("Evaluate Renal Function with Semaglutide Once Weekly"), NCT03819153. International, double-blind, randomized, placebo-controlled, event-driven trial. 387 sites, 28 countries. Enrollment window June 2019–May 2021; 5,581 screened. **Randomized N = 3,533 (1,767 semaglutide / 1,766 placebo)** — `FLOW-PRIMARY-2024`, lines 41–48, 179–184. The official registry record is tracked separately as `FLOW-REGISTRY-2025`; its source-specific status/time-frame reconciliation and remaining version-history limitation are documented in `01` and the ledger.

**N discrepancy (preserved, not resolved):** `FLOW-DESIGN-2023` (design/baseline paper) reports N=3,534 at baseline; the primary publication reports 3,533 randomized. No source checked by any lane establishes the reason. Do not infer an enrolled-vs-randomized, dosed, or analysis-population explanation. Locators: `FLOW-DESIGN-2023`, structured abstract Results and Table 3; `FLOW-PRIMARY-2024`, structured abstract Results and Results—“Trial Participants,” journal p.113.

## Population (Full Analysis Set, N=3,533)

| Characteristic | Value | Locator |
|---|---|---|
| Mean age | 66.6 ± 9.0 y | `FLOW-PRIMARY-2024`, Table 1, journal p.112 |
| Female | 30.3% | `FLOW-PRIMARY-2024`, Table 1, journal p.112 |
| Diabetes duration ≥15 y | 56.8% | `FLOW-PRIMARY-2024`, Table 1, journal p.112 |
| Mean HbA1c | 7.8 ± 1.3% | `FLOW-PRIMARY-2024`, Table 1, journal p.112 |
| Mean BMI | 32.0 ± 6.3 kg/m² | `FLOW-PRIMARY-2024`, Table 1, journal p.112 |
| Mean eGFR | 47.0 ± 15.2 mL/min/1.73m² | `FLOW-PRIMARY-2024`, Table 1, journal p.112 |
| eGFR distribution | ≥60: 20.4%; 45–<60: 29.9%; 30–<45: 38.4%; <30: 11.3% | `FLOW-PRIMARY-2024`, Table 1, journal p.112 |
| Median UACR | 567.6 mg/g | `FLOW-PRIMARY-2024`, Table 1, journal p.112 |
| Albuminuria category | Macroalbuminuria (A3, ≥300): 68.5%; microalbuminuria (A2): 28.4%; normoalbuminuria (A1): 3.1% | `FLOW-PRIMARY-2024`, Table 1, journal p.112 |
| KDIGO risk category | Very high: 68.3% (2,412/3,532); high: 24.9% (878); low/moderate: 6.8% (242) | `FLOW-CKDSEVERITY-2025`, structured abstract Results |
| Prior MI or stroke | 22.9% | `FLOW-PRIMARY-2024`, Table 1, journal p.112 |
| Chronic heart failure | 19.2% (342 [19.4%] semaglutide / 336 [19.0%] placebo) | `FLOW-PRIMARY-2024`, Table 1, journal p.112 |
| ASCVD (established) | 33.9% (1,198/3,533) | `FLOW-CVPHENOTYPE-2026`, structured abstract Results |

## Inclusion — two enrollment pathways (exactly transcribed from the verified supplement)

1. **Pathway A:** eGFR **≥50 and ≤75** mL/min/1.73m² (CKD-EPI 2009) **and** UACR **>300 and <5,000** mg/g.
2. **Pathway B:** eGFR **≥25 and <50** mL/min/1.73m² **and** UACR **>100 and <5,000** mg/g.

Plus: T2D diagnosis; HbA1c ≤10%; on maximally tolerated/labeled ACEi or ARB dose (stable ≥4 weeks) unless intolerant/contraindicated. eGFR ≥60 randomized participants were capped at **20% of N**. These details are independently concordant across `FLOW-SUPPLEMENT-2024`, “Eligibility Criteria—Inclusion,” supplement pp.11–12 (local lines 377–408), and the now-read `FLOW-PROTOCOL-2021` synopsis, printed pp.6–7 (PDF pp.7–8).

## Key exclusions

Congenital/hereditary kidney disease including polycystic kidney disease; autoimmune kidney disease including glomerulonephritis; current or recent (≤90 days) dialysis; NYHA IV heart failure; MI/stroke/unstable angina/TIA ≤60 days pre-screening; planned revascularization; GLP-1RA use ≤30 days pre-screening; combined ACEi+ARB use; prior/awaiting solid-organ transplant; personal/family MEN2/MTC history; unstable diabetic retinopathy/maculopathy. Kidney transplant recipients and dialysis patients are therefore structurally excluded from the enrolled population (see `12_EVIDENCE_GAPS_AND_CONTROVERSIES.md`). Locator for the entire exclusion block: `FLOW-SUPPLEMENT-2024`, “Eligibility Criteria—Exclusion,” supplement pp.12–13 (local lines 411–442).

## Background therapy at baseline

| Class | Use | Locator |
|---|---|---|
| ACEi | 35.1% | `FLOW-PRIMARY-2024`, Table 1 (continued), journal p.113 |
| ARB | 60.2% | `FLOW-PRIMARY-2024`, Table 1 (continued), journal p.113 |
| SGLT2i | 15.6% (550/3,533: 277 semaglutide / 273 placebo) | `FLOW-PRIMARY-2024`, Table 1 (continued), journal p.113; `FLOW-SGLT2-2024`, Results—“Participants and baseline characteristics” |
| Metformin | Not separately reported in Table 1. The primary paper's subgroup forest plot gives 908+924 participants with metformin and 859+842 without it, implying **1,832/3,533 (51.9%)** at baseline; this is a denominator-derived proportion, not a reported Table 1 percentage. | `FLOW-PRIMARY-2024`, Figure 2 (local Markdown lines 943–946) |
| Insulin | 61.4% | `FLOW-PRIMARY-2024`, Table 1 (continued), journal p.113 |
| Statin/lipid-lowering therapy | 80.2% | `FLOW-PRIMARY-2024`, Table 1 (continued), journal p.113 |
| Diuretic | 50.4% | `FLOW-PRIMARY-2024`, Table 1 (continued), journal p.113 |
| MRA | 7.3% (257/3,533: 136/121) — spironolactone 218 (84.8%), eplerenone 38 (14.8%), esaxerenone 1 (0.4%), **finerenone 0** | `FLOW-MRA-2025`, Results—“Trial Participants” and Supplementary Table 1/Figure 1 |

Finerenone was absent at baseline because it was first approved (July 2021) after FLOW's recruitment window had ended. Locator: `FLOW-MRA-2025`, Results—“Trial Participants” (paragraph reporting baseline MRA composition and approval timing).

## Intervention

Semaglutide subcutaneous injection, titrated to a target maintenance dose of **1.0 mg weekly**, vs. matching placebo, both on top of background maximally-tolerated RASi (and whatever other background therapy the patient was already receiving). Locator: `FLOW-PRIMARY-2024`, Methods—“Trial Procedures,” journal pp.110–111; `FLOW-DESIGN-2023`, Methods—“Overall trial design and treatment,” Figure 2.

## Primary outcome — five-component composite (time-to-first-event)

1. Onset of persistent (≥28 days) ≥50% reduction in eGFR from baseline.
2. Onset of persistent (≥28 days) eGFR <15 mL/min/1.73m².
3. Initiation of chronic kidney-replacement therapy (dialysis or transplantation).
4. Kidney death.
5. **Cardiovascular death.**

Locator for all five components and their persistence/time-to-first-event definitions: `FLOW-SUPPLEMENT-2024`, “Trial Outcomes,” supplement pp.13–14 (local lines 445–475); `FLOW-PRIMARY-2024`, Methods—“Trial Outcomes,” journal p.111.

**This is not a purely kidney endpoint.** Per CLAUDE.md rule 4 and the master prompt §VIII, it must always be reported as the five-component composite (kidney failure/≥50% eGFR decline/kidney death/CV death), kept explicitly separate from the kidney-specific four-component composite (identical, minus CV death). See `03_FLOW_PRIMARY_OUTCOMES.md` for full results.

## Confirmatory secondary outcomes — prespecified hierarchical (gatekeeping) order

Tested only if the primary outcome achieved superiority, in fixed sequence, stopping at the first non-confirmation: (1) total eGFR slope; (2) MACE (nonfatal MI, nonfatal stroke, or CV death); (3) all-cause death. All three passed in FLOW (see `03_FLOW_PRIMARY_OUTCOMES.md`). Locator: `FLOW-SUPPLEMENT-2024`, “Statistical Methods Relating to the Interim Analysis and Hierarchical Testing,” supplement p.16 (local lines 528–540); `FLOW-PRIMARY-2024`, Methods—“Trial Outcomes” and “Statistical Analysis,” journal p.111.

## Other (supportive/exploratory, not multiplicity-adjusted) outcomes

Kidney-specific composite excluding CV death; UACR; HbA1c; body weight; systolic/diastolic BP; heart failure events; severe hypoglycemia; major adverse limb events; safety. `FLOW-PRIMARY-2024` explicitly classifies these supportive/exploratory analyses as unadjusted for multiplicity and cautions against treating their confidence intervals as substitutes for formal hypothesis tests. Locator: `FLOW-SUPPLEMENT-2024`, “Trial Outcomes,” supplement pp.13–15 (local lines 445–490); `FLOW-PRIMARY-2024`, Methods—“Trial Outcomes”/“Statistical Analysis,” journal p.111.

## Statistical architecture (see `06_POST_FLOW_SELECT_SOUL_POOLED_EVIDENCE.md`/`12`/`14` cross-references and lane-06 methodology memo for full detail)

- Sample size: 90% power, 20% assumed relative risk reduction, minimum **854** planned primary-outcome events (`FLOW-SAP-2023`, §2.1, printed pp.6–7).
- Single prespecified interim analysis at ~two-thirds informational fraction (~570 events), no futility test; Lan–DeMets alpha-spending function approximating an O'Brien-Fleming boundary (`FLOW-SAP-2023`, §2.1, pp.6–7). DMC recommended stopping for efficacy on **2023-10-10**; final database lock **2024-02-06** with **741** accrued primary-outcome events (fewer than the 854 planned). Nominal significance level recalculated to **0.0322** (two-sided) in the final report. Final-lock/event-count locator: `FLOW-SUPPLEMENT-2024`, “Statistical Methods Relating to the Interim Analysis and Hierarchical Testing,” supplement PDF pp.16–17 (local lines 493–525).
- The primary-outcome HR/CI/P is adjusted for the group-sequential design via likelihood-ratio ordering (`FLOW-SAP-2023`, §2.3.1, p.12); **the three confirmatory secondary outcomes were not separately re-adjusted for the group-sequential design** (`FLOW-SAP-2023`, §2.4.1, pp.17–18) — a caveat that should attach to the eGFR-slope, MACE, and mortality point estimates, not just the primary composite.
- Cumulative incidence via the Aalen–Johansen estimator (competing risks: non-CV/non-renal death for the primary composite; all-cause death excluding renal death for the kidney-specific composite), stratified Cox proportional-hazards model (by baseline SGLT2i use) for HR/CI estimation (`FLOW-PRIMARY-2024`, Figure 1 legend and Methods—“Statistical Analysis,” journal pp.111, 114–115; `FLOW-SUPPLEMENT-2024`, Table S3 note, supplement pp.26–27).
- Estimand: in-trial-period, treatment-policy-like ITT (randomization → end of trial, irrespective of adherence/background-medication changes), independently confirmed in `FLOW-PROTOCOL-2021`, synopsis p.6, and `FLOW-SAP-2023`, §§1.1.2/2.2.3.

## Funding and conflicts

Sponsored by Novo Nordisk; sponsor managed trial operations; analyses independently verified by Statogen Consulting. Documented without implying invalidity, per CLAUDE.md safety/neutrality guidance. Locator: `FLOW-PRIMARY-2024`, Methods—“Trial Design and Oversight,” journal p.110 and structured abstract Conclusions; `FLOW-SUPPLEMENT-2024`, “Trial Organization and Oversight,” supplement pp.10–11.

## Author-stated limitations (verbatim substance)

Modest baseline SGLT2i (15.6%) and MRA (7.3%, no finerenone) use limits assessment of combination therapy; trial not powered to detect differences within/between important subgroups nor to independently confirm kidney-failure-specific effects; mostly White population; potential weight-loss-on-creatinine confound addressed via cystatin-C concordance (see `03`). Locators: `FLOW-PRIMARY-2024`, Discussion, journal pp.119–120, and Table 1, journal pp.112–113; `FLOW-MRA-2025`, Results—“Trial Participants” and Discussion—“Limitations.”
