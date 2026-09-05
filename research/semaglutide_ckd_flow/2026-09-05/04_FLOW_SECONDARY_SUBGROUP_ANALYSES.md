# 04. FLOW Secondary and Subgroup Analyses

Unless a subsection says otherwise, the subgroup analyses below were **prespecified but not adjusted for multiplicity**; a nonsignificant interaction P-value is evidence of *failure to detect* effect modification, never proof of *equivalent, additive, or preserved* effect (CLAUDE.md rules 5, 7). One important exception is `FLOW-CKDSEVERITY-2026-CJASN`: its primary-outcome/eGFR/UACR subgroup analyses were prespecified, but its all-cause-death analyses by CKD severity were post hoc.

## 4.1 By CKD severity — CV death/MI/stroke and all-cause death (`FLOW-CKDSEVERITY-2025`, Mahaffey, Eur Heart J 2025)

**Note on source quality:** an earlier version of local `fulltext/glp1_cardiorenal_Mahaffey_2025.md` misassigned HR/CI values across the eGFR≥60 and KDIGO panels and failed numeric QA. The local file was corrected on 2026-09-05 after visual comparison with the published source image. The table below uses that **source-image-verified Figure 2 matrix** (PMCID PMC11931213; Eur Heart J 2025;46:1096–1108, Figure 2, journal p.1103); historical/cached copies remain unsafe.

| Stratum | HR (95% CI) | P-interaction |
|---|---|---|
| Overall CV death/MI/stroke | 0.82 (0.68–0.98) | — |
| eGFR <60 | 0.87 (0.71–1.06) | .13 |
| eGFR ≥60 | 0.59 (0.37–0.94) | |
| UACR <300 | 1.04 (0.72–1.51) | .13 |
| UACR ≥300 | 0.75 (0.61–0.93) | |
| KDIGO low/moderate | 0.67 (0.27–1.67) | .79 |
| KDIGO high | 0.75 (0.50–1.12) | |
| KDIGO very high | 0.84 (0.68–1.04) | |
| All-cause death, overall | 0.80 (0.67–0.95) | — |

**Two nominally significant interactions — must be labeled exploratory/chance, not effect modifiers:**
- All-cause death by UACR: <300 mg/g HR **1.17 (0.83–1.65)** (numerically *higher* mortality, CI crosses 1) vs ≥300 mg/g HR **0.70 (0.57–0.85)**; **P-interaction = .01**.
- Nonfatal MI by eGFR: <60 HR 0.94 (0.63–1.39) vs ≥60 HR 0.28 (0.09–0.87); **P-interaction = .04**.

The trial's own authors, testing 15 subgroup interactions without multiplicity correction and finding these two in opposite directions with no biologically plausible mechanism, judge both "likely due to chance." This project adopts that judgment while flagging both signals explicitly in `12_EVIDENCE_GAPS_AND_CONTROVERSIES.md` — a single significant subgroup interaction is not proof of a UACR-dependent mortality effect, and higher UACR must not be described as conferring a larger absolute semaglutide benefit without published stratum-specific absolute-risk data (none exists; see NNT note below).

**NNT (week 156, Aalen–Johansen pseudo-observation method):** CV death/MI/stroke 45 (23–623); all-cause death 39 (21–238) — trial-level, not stratum-specific. Locator: `FLOW-CKDSEVERITY-2025`, Methods/Statistical Analysis and Results paragraph immediately after Table 2, journal pp.1103–1106 (PMCID PMC11931213). No stratum-specific (KDIGO/eGFR/UACR) NNT has been published anywhere in this evidence base; do not back-calculate one.

## 4.2 By CKD severity — FLOW five-component composite (including CV death) and mortality (`FLOW-CKDSEVERITY-2026-CJASN`, Tuttle/Mann, CJASN 2026; official CC BY 4.0 full text, PMCID PMC13143484)

Restates FLOW's own overall counts (primary five-component composite, including CV death: 331/1,767 vs 410/1,766, HR 0.76 [0.66–0.88]; all-cause death 227/1,767 vs 279/1,766, HR 0.80 [0.67–0.95]) stratified by baseline eGFR (<30 to ≥60) and UACR (<100 to ≥2,000 mg/g) — this is the same trial and the same headline events, not an independent cohort. The **prespecified** primary-outcome subgroup analysis found no detected heterogeneity across eGFR (P-interaction .83; Results/Fig.1) or UACR (P-interaction .42; Results/Fig.2). The baseline UACR<100 subgroup contained 350 participants and 13/177 versus 17/173 primary events, HR **0.70 (0.34–1.44)** (Fig.2). This imprecise, baseline-reclassified subgroup arose despite screening eligibility thresholds >100/>300 mg/g and is not a prospectively eligible cohort with persistently low UACR; it therefore cannot close the normoalbuminuric-CKD evidence gap. By contrast, the paper states in its limitations that the **all-cause-death analyses by CKD severity were post hoc**. The UACR ≥2,000 mg/g mortality estimate, HR **0.47 (0.31–0.70)** with P-interaction **.02** (Results/Fig.5), is therefore exploratory and unadjusted for multiplicity—not proof of a UACR-dependent mortality effect or of a larger absolute benefit. Locator: [official PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC13143484/), Methods/Statistical Analysis, Results/Figs.1–5, and Discussion/limitations; DOI 10.2215/CJN.0000000974, PMID 41706532. Distinct DOI/PMID from the JACC 2026 CV-phenotype paper below; the two must not be merged.

## 4.3 By cardiovascular phenotype (`FLOW-CVPHENOTYPE-2026`, Tuttle/Bakris, JACC 2026; abstract-level only)

| Baseline phenotype (n) | Semaglutide-vs-placebo HR for FLOW five-component composite (includes CV death), within phenotype | Semaglutide-vs-placebo all-cause-death HR within phenotype vs its complement | Published descriptive 3-year NNT for the five-component composite |
|---|---|---|---|
| Established ASCVD (1,198) | 0.80 (0.63–1.02) | 0.82 (0.63–1.07) vs 0.78 (0.62–0.99) | 22 |
| Heart failure (678) | 0.67 (0.49–0.93) | 0.75 (0.54–1.05) vs 0.81 (0.66–0.99) | 13 |
| High total-CVD-risk, no established CVD (PREVENT≥20%; 1,329 of 2,000 without ASCVD/HF) | 0.73 (0.58–0.91) | 0.71 (0.52–0.95) vs 0.82 (0.47–1.43) | 17 |

No interaction test was below 0.40: primary-outcome P-interaction values were **.62/.40/.99** for ASCVD/HF/high-risk status, respectively, and mortality values were **.79/.74/.63**. These are the only published **CV-phenotype** NNTs in this evidence base: HF 13, high-risk without established CVD 17, and ASCVD 22. They describe these three **CV phenotypes only** and do not license extrapolation to eGFR, UACR, or KDIGO strata; the separate MRA-subgroup publication reports exploratory NNTs 9/23 and is discussed in §4.5/`08`, not treated as a CV phenotype. Do not read the CV-phenotype NNTs as proof that FLOW's relative efficacy differs by CV phenotype or as establishing a globally “greatest-benefit” CKD phenotype. Locator: `FLOW-CVPHENOTYPE-2026`, structured abstract/results; DOI 10.1016/j.jacc.2026.02.5125, PMID 42233552.

## 4.4 By baseline SGLT2i use (`FLOW-SGLT2-2024`, Mann, Nat Med 2024) — see `07_SGLT2_COMBINATION_EVIDENCE.md` for the full combination-therapy discussion

Baseline SGLT2i users n=550 (277/273, 15.6% of trial) vs non-users n=2,983 (1,490/1,493).

| Outcome | Users HR (95% CI) | Non-users HR (95% CI) | P-interaction |
|---|---|---|---|
| Primary 5-component composite (including CV death) | 1.07 (0.69–1.67) | 0.73 (0.63–0.85) | 0.109 |
| Kidney-specific 4-component composite | 1.18 (0.71–1.98) | 0.75 (0.61–0.90) | 0.100 |
| Total eGFR slope difference | 0.75 (−0.01, 1.50) | 1.25 (0.91, 1.58) | 0.237 |
| MACE | — | — | 0.741 |
| All-cause death | — | — | 0.901 |
| UACR reduction, week 104 | 24% (4–39%) | 34% (26–40%) | 0.279 |

The two hard-composite HRs in SGLT2i users (**1.07 and 1.18**) sit on the null side of 1 with wide, asymmetric CIs, reflecting only 79 primary-outcome events in a subgroup that is 15.6% of the trial. This is underpowered, not null: the data are compatible with benefit, no effect, or harm and do not directionally establish retained hard-outcome benefit, additivity, or safety of the interaction. Only the eGFR-slope and UACR-reduction point estimates run in a supportive direction (see `07` for the full “supported vs. not established” table). Post-randomization SGLT2i initiation was asymmetric (more common in the placebo arm, ~20% vs ~10% by 36 months), which further complicates interpretation of the “no-SGLT2i” contrast over time; the direction/magnitude of any resulting bias is not identifiable from the initiation proportions alone. Locator: `FLOW-SGLT2-2024`, Fig. 1/Table 1 and Extended Data Fig. 4; local source lines 34–42, 100–128, 237–305, and 984 onward.

## 4.5 By baseline MRA use (`FLOW-MRA-2025`, Rossing, Diabetes Care 2025) — see `08_MRA_FINERENONE_COMBINATION_EVIDENCE.md` for the full combination-therapy discussion

Baseline MRA users n=257 (7.3%; spironolactone 218, eplerenone 38, esaxerenone 1, finerenone 0) vs non-users n=3,276.

FLOW primary five-component composite including CV death: users HR **0.51 (0.30–0.86)**, 59 events; non-users HR **0.79 (0.68–0.92)**, 682 events; P-interaction = **0.12**. Because baseline MRA use was overwhelmingly steroidal (spironolactone/eplerenone) with zero finerenone users, this subgroup provides no direct randomized evidence about a semaglutide+finerenone combination specifically, regardless of the numerically larger point estimate in MRA users. Locator: `FLOW-MRA-2025`, Fig. 1/Supplementary Table 2; local source lines 205–213.

## 4.6 Heart failure outcomes (`FLOW-HF-2024`, Pratley, JACC 2024; abstract-level only)

Baseline HF present n=678 (342/336) vs absent. HF event or CV death composite HR **0.73 (0.62–0.87)**, P=0.0005; HF events alone HR **0.73 (0.58–0.92)**, P=0.0068; CV death alone HR **0.71 (0.56–0.89)**, P=0.0036; similar effect with and without baseline HF. This is a prespecified secondary analysis of an existing trial, not a dedicated HF-outcomes trial — FLOW should not be described as a direct HFrEF/HFpEF therapy trial. Whether the apparent HF benefit is a direct cardiac effect, secondary to CKD/CV improvement, or partly mediated by weight/volume/metabolic change is not distinguishable from the data available (see `09_MECHANISMS_OF_KIDNEY_PROTECTION.md`).

Locator: `FLOW-HF-2024`, PubMed structured abstract/Results (DOI 10.1016/j.jacc.2024.08.004; PMID 39217553); full text was not obtained, so NYHA/HFrEF/HFpEF details are not inferred.

## 4.7 By baseline HbA1c

`FLOW-PRIMARY-2024`'s prespecified subgroup analysis shows a directionally consistent primary-outcome HR regardless of baseline glycemic control (HbA1c ≤7.0%: HR 0.69 [0.54–0.89]; >7.0%: HR 0.80 [0.67–0.96]; ≤8.0%: HR 0.75 [0.62–0.90]; >8.0%: HR 0.79 [0.63–1.00]), with all CIs overlapping the overall estimate and no formal interaction P reported in the primary paper's forest plot as extracted. This supports only the narrower claim that FLOW's benefit "is not confined to poorly controlled patients" — it does not establish glycemia-independence of the mechanism (see `09`).

Locator: `FLOW-PRIMARY-2024`, Figure 2/Results, journal pp.116–117 (DOI 10.1056/NEJMoa2403347; PMID 38785209).
