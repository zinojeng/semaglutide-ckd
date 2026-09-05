# 14. Master Evidence Table

All values map to `SOURCE_LEDGER.csv`; each quantitative block below carries a source locator. `NE` = not estimable from this evidence base (not calculated here per CLAUDE.md rule 8); `NR` = not reported or not independently re-verified in the cited source. Cross-trial rows are **contextual only** — never ranked by hazard ratio (CLAUDE.md rule 9).

## FLOW (`FLOW-PRIMARY-2024`) — N=1,767 semaglutide / 1,766 placebo, median follow-up 3.4 years

Locator for the block: N and median follow-up are from `FLOW-PRIMARY-2024`, Table 1 and Results—“Trial Participants,” journal pp.112–113; efficacy values are from Table 2, journal p.116 (local PDF page 8), with endpoint definitions and sensitivity analyses in `FLOW-SUPPLEMENT-2024` Tables S2–S3 (local Markdown lines 737–830). Safety/discontinuation rows 23–26 are from `FLOW-PRIMARY-2024`, Table 3, journal p.120 (local PDF p.12), and `FLOW-SUPPLEMENT-2024`, Tables S4–S5, supplement pp.28–32. The week-156 MACE/all-cause-death risk differences and NNTs in rows 21–22 are from `FLOW-CKDSEVERITY-2025`, Methods/Statistical Analysis and the Results paragraph immediately after Table 2 (PMCID PMC11931213; DOI 10.1093/eurheartj/ehae613), not from FLOW primary Table 2.

| Outcome | Sema events/value | Placebo events/value | Effect estimate | 95% CI | P | Reported event rate | Risk difference (sema−placebo) | NNT (3y) |
|---|---:|---:|---:|---:|---:|---|---|---:|
| **Primary composite (5-component, incl. CV death)** | 331 (18.7%) | 410 (23.2%) | 0.76 | 0.66–0.88 | 0.0003 | 5.8 vs 7.5/100 patient-yr | — | **20 (14–40)** |
| — Persistent ≥50% eGFR decline (outside hierarchy; nominal/supportive only; no percentage-reduction headline) | 165 (9.3%) | 213 (12.1%) | 0.73 | 0.59–0.89 | — | — | — | NE (not independently confirmatory; supportive) |
| — Persistent eGFR<15 | 92 (5.2%) | 110 (6.2%) | 0.80 | 0.61–1.06 | — | — | — | NE |
| — Chronic KRT initiation | 87 (4.9%) | 100 (5.7%) | 0.84 | 0.63–1.12 | — | — | — | NE |
| — Kidney death | 5 (0.3%) | 5 (0.3%) | 0.97 | 0.27–3.49 | — | — | — | NE |
| — CV death | 123 (7.0%) | 169 (9.6%) | 0.71 | 0.56–0.89 | — | — | — | NE |
| **Kidney-specific composite (4-component, excl. CV death)** | 218 (12.3%) | 260 (14.7%) | 0.79 | 0.66–0.94 | — | — | — | **NE — no NNT published anywhere in this evidence base for this outcome; not back-calculated** |
| Total eGFR slope (mL/min/1.73m²/yr) | −2.19 | −3.36 | diff +1.16 | 0.86–1.47 | <0.001 | — | — | n/a (continuous) |
| Baseline→week 12 absolute eGFR change (mL/min/1.73m²) | −1.07 | −1.05 | diff −0.03 | −0.56 to 0.51 | — | no semaglutide-specific differential dip through week 12; earlier resolved transient not excluded | — | n/a (continuous) |
| Chronic eGFR slope, week 12→end (mL/min/1.73m²/yr) | −2.36 | −3.30 | diff +0.94 | 0.62–1.26 | — | — | — | n/a (continuous) |
| MACE | 212 (12.0%) | 254 (14.4%) | 0.82 | 0.68–0.98 | 0.029 | — | −0.02 (−0.04, −0.002) | **45 (23–623)** |
| All-cause death | 227 (12.8%) | 279 (15.8%) | 0.80 | 0.67–0.95 | 0.01 | — | −0.03 (−0.05, −0.004) | **39 (21–238)** |
| Severe hypoglycemia (participants with ≥1 episode) | 37 (2.1%) | 37 (2.1%) | — | — | — | — | — | n/a |
| Severe hypoglycemia (episodes; episode-count ratio) | 47 | 46 | 1.02 | 0.62–1.67 | — | — | — | n/a |
| AE-driven permanent discontinuation | 233 (13.2%) | 211 (11.9%) | — | — | — | — | — | n/a |
| — GI-specific (subset) | 79 (4.5%) | 20 (1.1%) | — | — | — | — | — | n/a |

The episode-count/value ratio and the participant count use different counting units (episodes versus participants) and are therefore shown on separate rows; the ratio is not a time-to-event HR. See `10`.

## FLOW — SGLT2i subgroup (`FLOW-SGLT2-2024`) — baseline users N=550 vs non-users N=2,983

Locator for the block: Mann et al. Figs. 1–2/Table 1 and Extended Data Figs. 4–7; local source lines 34–42, 65–128, 237–305, 411–450, and 984 onward.

| Outcome | Users HR (95% CI) | Non-users HR (95% CI) | P-interaction |
|---|---|---|---|
| FLOW primary five-component composite (including CV death) | 1.07 (0.69–1.67) | 0.73 (0.63–0.85) | 0.109 |
| Kidney-specific composite | 1.18 (0.71–1.98) | 0.75 (0.61–0.90) | 0.100 |
| Sustained ≥50% eGFR-decline component | 1.30 (0.76–2.26), 30/277 vs 23/273 | 0.66 (0.53–0.83), 135/1,489 vs 190/1,493 | 0.023 (nominal; unadjusted for multiplicity) |
| Total eGFR-slope difference | 0.75 (−0.01, 1.50) | 1.25 (0.91, 1.58) | 0.237 |
| Post hoc eGFRcystatin-C five-component outcome | 0.74 (0.47–1.16) | 0.70 (0.60–0.82) | 0.844 |
| Post hoc total eGFRcystatin-C slope difference | +0.92 (0.16–1.68) | +1.55 (1.21–1.88) | 0.142 |
| Post hoc week-104 eGFRcystatin-C change difference | +3.5 (1.6–5.4) | +3.4 (2.5–4.2) | 0.901 |
| MACE | — | — | 0.741 |
| All-cause death | — | — | 0.901 |

ARR/NNT not estimable for either stratum (`07`, `12`).

Among baseline SGLT2i users, the prespecified creatinine-based five-component estimate was HR **1.07 (0.69–1.67)**, whereas the post hoc modified cystatin-C endpoint gave HR **0.74 (0.47–1.16)**. Because the marker and endpoint definitions differ, neither is “the” subgroup estimate; do not average them, join them into a range, or let the post hoc analysis overturn the prespecified analysis. Incremental hard-kidney benefit is not identified from these analyses.

## FLOW — MRA subgroup (`FLOW-MRA-2025`) — baseline users N=257 vs non-users N=3,276

Locator for the block: Rossing et al. Figs. 1–2/Supplementary Tables 1–2; local source lines 75–219 and 239. Baseline finerenone use was zero.

| Outcome | Users HR (95% CI), events | Non-users HR (95% CI), events | P-interaction | Exploratory 3y NNT |
|---|---|---|---|---:|
| FLOW primary five-component composite (including CV death) | 0.51 (0.30–0.86), 59 | 0.79 (0.68–0.92), 682 | 0.12 | Users: 9; Non-users: 23 (**MRA-user subgroup only; exploratory nonrandomized stratum; never attach these NNTs to a finerenone statement**) |
| Kidney-specific composite | 0.38 (0.15–0.84) | 0.82 (0.68–0.99) | 0.068 | NE |
| RRT-initiation component | 0.18 (0.03–0.71), only 11 total events in MRA-user subgroup | 0.91 (0.68–1.23) | 0.027 (nominal; unadjusted for multiplicity) | NE |

## FLOW — by CKD-severity strata (`FLOW-CKDSEVERITY-2025`, ingest-report-corrected Figure 2 values)

Locator for the block: Mahaffey et al., Eur Heart J 2025;46:1096–1108, Figure 2, journal p.1103 (PMCID PMC11931213). An earlier local transcription failed numeric QA; it was corrected after visual source-image verification on 2026-09-05. The published figure remains the authoritative numeric source.

| Stratum | CV death/MI/stroke HR (95% CI) | P-interaction |
|---|---|---|
| Overall | 0.82 (0.68–0.98) | — |
| eGFR<60 | 0.87 (0.71–1.06) | .13 |
| eGFR≥60 | 0.59 (0.37–0.94) | |
| UACR<300 | 1.04 (0.72–1.51) | .13 |
| UACR≥300 | 0.75 (0.61–0.93) | |
| KDIGO low/moderate | 0.67 (0.27–1.67) | .79 |
| KDIGO high | 0.75 (0.50–1.12) | |
| KDIGO very high | 0.84 (0.68–1.04) | |

NNT (week 156, whole trial, not stratum-specific): CV death/MI/stroke 45 (23–623); all-cause death 39 (21–238). Locator: `FLOW-CKDSEVERITY-2025`, Methods/Statistical Analysis and Results paragraph immediately after Table 2, journal pp.1103–1106 (PMCID PMC11931213).

The distinct CJASN severity analysis (`FLOW-CKDSEVERITY-2026-CJASN`, Figs. 1–2) reported an eGFR<30 subgroup of n=400: 73/218 versus 67/182 primary events, HR **0.81 (0.58–1.13)**; overall eGFR-category P-interaction **.83** (Fig. 1). It also reported a baseline UACR<100 subgroup of n=350: 13/177 versus 17/173 primary events, HR **0.70 (0.34–1.44)**; overall UACR-category P-interaction **.42** (Fig. 2). Because protocol screening required UACR >100 or >300 mg/g, this baseline-reclassified, imprecise UACR subgroup is not evidence from a prospectively eligible persistent-low-UACR cohort.

## FLOW — by CV phenotype (`FLOW-CVPHENOTYPE-2026`, abstract-level)

Locator for the block: structured abstract/results, DOI 10.1016/j.jacc.2026.02.5125, PMID 42233552. These are descriptive NNTs for the CV phenotypes shown, not CKD-severity-stratum NNTs.

| Phenotype (n) | FLOW five-component composite HR (95% CI), within phenotype | HR (95% CI), complement | P-interaction | Published descriptive 3y NNT |
|---|---|---|---:|---:|
| Established ASCVD (1,198) | 0.80 (0.63–1.02) | 0.74 (0.62–0.89) | .62 | 22 |
| Heart failure (678) | 0.67 (0.49–0.93) | 0.79 (0.67–0.93) | .40 | 13 |
| High-risk, no established CVD (1,329/2,000) | 0.73 (0.58–0.91) | 0.73 (0.49–1.08) | .99 | 17 |

All three are descriptive 3-year NNTs for the **CV-death-inclusive five-component endpoint**. Their differences are mathematically fully explicable by the strata's differing baseline risks and contain no evidence of differential relative drug efficacy; the magnitude of that explanation cannot be empirically decomposed because phenotype-specific baseline event rates were not reported. No kidney-only NNT exists in this evidence base.

## FLOW — heart failure analysis (`FLOW-HF-2024`, abstract-level)

Locator for the block: structured abstract/results, DOI 10.1016/j.jacc.2024.08.004, PMID 39217553.

| Outcome | HR (95% CI) | P |
|---|---|---|
| HF event or CV death | 0.73 (0.62–0.87) | 0.0005 |
| HF events alone | 0.73 (0.58–0.92) | 0.0068 |
| CV death alone | 0.71 (0.56–0.89) | 0.0036 |

## SUSTAIN-6, PIONEER-6, SELECT, SOUL, and pooled analyses

Row locators: `SUSTAIN6-2016` and `PIONEER6-2019`, primary-publication abstracts/results (DOIs 10.1056/NEJMoa1607141 and 10.1056/NEJMoa1901118); the retinopathy row is additionally verified in `SUSTAIN6-RETINOPATHY-2018`, Methods §2.1.4/Results (PMCID PMC5888154); `SELECT-KIDNEY-2024`, primary analysis abstract/results (DOI 10.1038/s41591-024-03015-5, PMID 38796653); `SOUL-PRIMARY-2025` and `SOUL-KIDNEY-2026`, structured abstracts/results (DOIs 10.1056/NEJMoa2501006 and 10.2337/dc25-1080); `SELECT-FLOW-SOUL-POOLED-2026` and `GLP1-CLASSMETA-BADVE-2025`, structured abstracts/findings (PMIDs 42567173 and 39608381). For PMID 42567173, PubMed records electronic publication on 2026-08-07 and ahead-of-print status at the cutoff; raw Crossref metadata supplies only month-level 2026-08, not an exact 2026-08-01 date.

| Trial / analysis | Population | Dose/route | Outcome | Semaglutide events/value | Comparator events/value | Effect estimate (95% CI) | P / heterogeneity note |
|---|---|---|---|---:|---:|---:|---:|
| SUSTAIN-6 | T2D, high CV risk, N=3,297 | 0.5/1.0mg SC | MACE | — | — | 0.74 (0.58–0.95) | Prespecified noninferiority met; nominal post hoc/non-prespecified superiority P=.02 |
| SUSTAIN-6 | same | same | Nephropathy composite (excl. hard-endpoint breakdown) | 62/1,648 (3.8%) | 100/1,649 (6.1%) | 0.64 (0.46–0.88) | 0.005 |
| SUSTAIN-6 | same | same | Retinopathy complications | 50/1,648 (3.0%) | 29/1,649 (1.8%) | 1.76 (1.11–2.78) | 0.02 |
| PIONEER-6 | T2D, high CV risk, N=3,183 | 14mg oral | MACE (noninferiority) | 61/1,591 (3.8%) | 76/1,592 (4.8%) | 0.79 (0.57–1.11) | NI met, superiority not shown |
| SELECT (kidney) | Obesity+ASCVD, no diabetes, N=17,604 | 2.4mg SC | Kidney composite (incl. macroalbuminuria onset) | 1.8% | 2.2% | 0.78 (0.63–0.96) | 0.02 |
| SOUL (primary) | T2D+ASCVD/CKD, N=9,650 | 14mg oral | MACE | 579/4,825 (12.0%) | 668/4,825 (13.8%) | 0.86 (0.77–0.96) | 0.006 |
| SOUL (kidney) | same | same | Five-point kidney/CV-death composite (incl. CV death) | 403/4,825 (8.4%) | 435/4,825 (9.0%) | 0.91 (0.80–1.05) | 0.19 (NS) |
| SOUL (kidney) | same | same | 4-point composite (excl. CV death) | 112/4,825 (2.3%) | 129/4,825 (2.7%) | 0.86 (0.66–1.10) | 0.22 (NS) |
| SOUL (kidney) | same | same | Total eGFR slope (formally exploratory after hierarchy gate failed) | −1.67 mL/min/1.73m²/yr | −2.06 mL/min/1.73m²/yr | difference +0.40 (0.27–0.53) mL/min/1.73m²/yr | nominal <0.0001 |
| Pooled SELECT+FLOW+SOUL | N=30,787, mixed | mixed doses/routes | Primary pooled kidney/CV-death composite: persistent ≥50% eGFR decline, kidney failure (persistent eGFR<15 or KRT), kidney death, or CV death | 973 | 1,134 | 0.84 (0.77–0.91) | Prespecified integrated estimate; statistically dependent on parent trials, so do not present beside FLOW/SOUL as three independent estimates or rank them |
| Pooled SELECT+FLOW+SOUL | same | same | Narrower secondary kidney-specific composite: same structure, excluding CV death | 347 | 416 | 0.80 (0.69–0.92) | Integrated estimate; not evidence of dose/route equivalence or cross-trial homogeneity |
| GLP-1RA class meta-analysis (Badve, T2D-only) | **10 T2D RCTs, N=67,769** | mixed molecules | Kidney composite excluding CV death (kidney failure, sustained ≥50% eGFR decline/nearest equivalent, or kidney-failure death) | — | — | 0.82 (0.73–0.93) | — |
| GLP-1RA class meta-analysis (Badve, T2D-only) | same | same | Kidney failure | — | — | 0.84 (0.72–0.99) | — |
| GLP-1RA class meta-analysis (with SELECT post hoc) | **11 RCTs, N=85,373** | mixed molecules | Serious adverse events / AE discontinuation | — | — | RR 0.95 (0.90–1.01) / 1.51 (1.18–1.94) | I² 88.5% / 96.3% |

### SELECT prespecified continuous kidney outcomes (`SELECT-KIDNEY-2024`)

Locator: primary PMC article, Results and Table 1/Figs. 4–5 (DOI 10.1038/s41591-024-03015-5; PMID 38796653; PMCID PMC11271413). All P values below are unadjusted for multiplicity.

| Outcome | Semaglutide | Placebo | Estimated treatment difference (95% CI) | P |
|---|---:|---:|---:|---:|
| Week-104 eGFR change, overall (mL/min/1.73m²) | −0.86 | −1.61 | +0.75 (0.43–1.06) | <.001 |
| Week-104 eGFR change, baseline eGFR<60 subgroup | +5.28 | +3.09 | +2.19 (1.00–3.38) | <.001 |
| Total eGFR slope (mL/min/1.73m²/yr) | −0.78 | −1.17 | +0.39 (0.30–0.48) | <.001 |
| Chronic eGFR slope, week 20→end (mL/min/1.73m²/yr) | −0.98 | −1.28 | +0.29 (0.18–0.40) | <.001 |
| Acute eGFR slope, baseline→week 16, European subset (mL/min/1.73m²/yr) | −2.41 | −1.08 | −1.33 (−2.68 to 0.02) | .0535 (Table display rounds to .05; not statistically significant) |
| Week-104 UACR relative change, overall | +0.3% | +12.3% | −10.7% (−13.2 to −8.2) | <.001 |

Baseline-UACR subgroup treatment differences were −8.1% (−10.6 to −5.6) for <30, −27.2% (−35.3 to −18.1) for 30–<300, and −31.4% (−54.9 to 4.3; P=.08) for ≥300 mg/g. The eGFR<60 rise in both arms may partly reflect regression to the mean; the acute-slope estimate is from a European subset; these continuous outcomes do not establish hard-outcome benefit in dedicated non-diabetic CKD.

## Contextual comparator trials (non-ranking)

### Eligibility and background therapy

| Trial | N / diabetes requirement | eGFR and UACR eligibility | Background RAAS | Background SGLT2i / GLP-1RA |
|---|---|---|---|---|
| FLOW | 3,533; T2D required | eGFR ≥50–≤75 with UACR >300–<5,000, or eGFR ≥25–<50 with UACR >100–<5,000 | Stable maximal labeled/tolerated ACEi/ARB; baseline ACEi 35.1% + ARB 60.2% | SGLT2i 15.6%; GLP-1RA within 30 days excluded |
| CREDENCE | 4,401; T2D required | eGFR 30–<90; UACR >300–5,000 | Stable maximal labeled/tolerated ACEi/ARB required | Other SGLT2i not background therapy; GLP-1RA NR in primary report |
| DAPA-CKD | 4,304; T2D not required (67.5% T2D) | eGFR 25–75; UACR 200–5,000 | ACEi/ARB 97% | Other SGLT2i not background therapy; GLP-1RA 2.8% overall |
| EMPA-KIDNEY | 6,609; T2D not required (46% diabetes) | eGFR ≥20–<45 regardless of UACR, or ≥45–<90 with UACR ≥200; median UACR 329 | RAS inhibitor 86%/85% by arm | Other SGLT2i not background therapy; GLP-1RA not separately reported in primary Table 1 |
| FIDELIO-DKD | 5,734 randomized; T2D required | eGFR 25–<60 + UACR 30–<300 with retinopathy, or eGFR 25–<75 + UACR 300–5,000 | Max tolerated ACEi/ARB required | SGLT2i 4.5%; GLP-1RA 7.0% |
| FIDELITY (FIDELIO+FIGARO) | 13,026 analyzed; T2D required | Combined complementary pathways: eGFR ≥25 with pathway-specific upper bounds; FIGARO's UACR 300–5,000/eGFR≥60 pathway had no stated eGFR upper bound. Median UACR 515. | RAS inhibitor 99.8% | SGLT2i 6.7%; GLP-1RA 7.2% |

### Endpoints and renal-function context

| Trial | Primary endpoint and HR (95% CI) | Kidney failure result | CV-death result/handling | eGFR slope |
|---|---|---|---|---|
| FLOW | Five-component kidney/CV-death composite: 0.76 (0.66–0.88) | KRT 0.84 (0.63–1.12); persistent eGFR<15 0.80 (0.61–1.06), each individually NS | Included; isolated CV death 0.71 (0.56–0.89) | Total +1.16 (0.86–1.47); chronic week 12→end +0.94 (0.62–1.26); no semaglutide-specific differential dip through week 12, but an earlier resolved transient is not excluded |
| CREDENCE | ESKD/doubling creatinine/kidney or CV death: 0.70 (0.59–0.82) | ESKD 0.68 (0.54–0.86) | Included; isolated CV death 0.78 (0.61–1.00) | Baseline→week 3 **between-arm difference in absolute eGFR change** −3.17 (−3.87 to −2.47) mL/min/1.73m²; chronic slope difference +2.74 (2.37–3.11) mL/min/1.73m²/yr |
| DAPA-CKD | ≥50% eGFR decline/ESKD/kidney or CV death: 0.61 (0.51–0.72) | Kidney-specific composite 0.56 (0.45–0.68); ESKD 0.64 (0.50–0.82) | Included; isolated CV death 0.81 (0.58–1.12); CV death/HHF 0.71 (0.55–0.92) | Total +0.93 (0.61–1.25); chronic +1.92 (1.61–2.24) |
| EMPA-KIDNEY | Kidney-disease progression or CV death: 0.72 (0.64–0.82) | Kidney-disease progression 0.71 (0.62–0.81); kidney-failure composite 0.69 (0.56–0.85) | Included; isolated CV death 0.84 (0.60–1.19) | Total +0.75 (0.54–0.96); chronic from month 2 +1.37 (1.16–1.59) |
| FIDELIO-DKD | Kidney failure/≥40% eGFR decline/kidney death: 0.82 (0.73–0.93) | 7.3% vs 8.3%; isolated HR NR in primary abstract | Excluded from kidney endpoint; CV death 4.5% vs 5.3%, NS | Chronic month 4→end −2.66 vs −3.97 (difference ≈+1.31) after an initial finerenone dip |
| FIDELITY | Kidney failure/≥57% eGFR decline/kidney death: 0.77 (0.67–0.88); separate CV composite 0.86 (0.78–0.95) | ESKD 0.80 (0.64–0.99); kidney failure reduction reported as 16% | Kidney endpoint excludes CV death; isolated CV death 0.88 (0.76–1.02) | NR in the primary pooled article; no non-primary slope estimate is inserted here |

Primary-source locators for the comparator block: FLOW eligibility and background-therapy values in row 137 are from `FLOW-PROTOCOL-2021`, synopsis pp.6–7; `FLOW-SUPPLEMENT-2024`, “Eligibility Criteria,” supplement pp.11–13; and `FLOW-PRIMARY-2024`, Table 1, journal pp.112–113. `CREDENCE-2019`, [primary publication](https://doi.org/10.1056/NEJMoa1811744) Methods/Results (PMID 30990260), with its acute/chronic eGFR estimates separately sourced to `CREDENCE-EGFR-SLOPE-2020`, the [prespecified secondary analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC7217416/) Table 1 (DOI 10.1681/ASN.2019111168; PMID 32354987); `DAPA-CKD-2020`, [primary publication](https://doi.org/10.1056/NEJMoa2024816) Methods/Results (PMID 32970396), with diabetes prevalence/background ACEi-or-ARB/GLP-1RA values separately sourced to `DAPA-CKD-BASELINE-2020`, [Results and Table 4](https://pmc.ncbi.nlm.nih.gov/articles/PMC7538235/) (DOI 10.1093/ndt/gfaa234; PMID 32862232); `EMPA-KIDNEY-2023`, [primary PMC article](https://pmc.ncbi.nlm.nih.gov/articles/PMC7614055/) Tables 1–2 and Figures 3/S6 (DOI 10.1056/NEJMoa2204233; PMID 36331190); `FIDELIO-DKD-2020`, [primary publication](https://doi.org/10.1056/NEJMoa2025845) Results plus prespecified slope reporting (PMID 33264825); `FIDELITY-POOLED-2022`, [primary pooled analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC8830527/) Tables 1–2/Figures 1–3 (DOI 10.1093/eurheartj/ehab777; PMID 35023547). Any `NR` cell remains an explicit retrieval limit, not a zero effect.

> **Warning:** Cross-trial comparisons cannot establish relative efficacy because populations, endpoint definitions, follow-up, background therapy, event rates, and acute-slope handling differ. Do not rank drugs solely by HR or by slope magnitude.

## Modeled (non-RCT) combination-therapy estimate — `COMBO-MODEL-NEUEN-2024`, explicitly not trial evidence

Locator for the block: Neuen et al. PubMed structured abstract, DOI 10.1161/CIRCULATIONAHA.123.067584, PMID 37952217. Only the MACE row below is retained because its HR/ARR/NNT is directly supported there. FLOW is not an input; the local adapted summary has unresolved derivative-rights metadata and is not used to supply additional quantitative rows.

| Outcome | Modeled HR (full additivity) | 3y ARR | NNT |
|---|---|---|---:|
| MACE | 0.65 (0.55–0.76) | 4.4% (3.0–5.7) | 23 (18–33) |

FLOW is not an input trial to this model; this is a simulated, not observed, combination-therapy estimate.
