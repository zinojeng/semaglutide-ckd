# Retrieved-source notes: SELECT-KIDNEY-2024

Role: flow-endocrinologist (lane `04_endocrinology.md`)
Retrieved: 2026-09-05

## Source identification

- **SELECT-KIDNEY-2024**: Colhoun HM, Lingvay I, Brown PM, et al. "Long-term kidney outcomes of semaglutide in obesity and cardiovascular disease in the SELECT trial." *Nature Medicine* 2024;30:2058–2066. DOI: [10.1038/s41591-024-03015-5](https://doi.org/10.1038/s41591-024-03015-5). PubMed: [38796653](https://pubmed.ncbi.nlm.nih.gov/38796653/). Full text (PMC, open access): [PMC11271413](https://pmc.ncbi.nlm.nih.gov/articles/PMC11271413/).
- Parent CV outcomes trial: **SELECT-PRIMARY-2023** — Lincoff AM et al. "Semaglutide and Cardiovascular Outcomes in Obesity without Diabetes." *N Engl J Med* 2023;389:2221–2232.
- Companion glycemia paper used only for HbA1c/prediabetes baseline detail (separate publication, cite separately if used): **SELECT-GLYCEMIA-2024** — "Effect of Semaglutide on Regression and Progression of Glycemia in People With Overweight or Obesity but Without Diabetes in the SELECT Trial." *Diabetes Care* 2024;47:1350. PMC: [PMC11282386](https://pmc.ncbi.nlm.nih.gov/articles/PMC11282386/).

Verification method: PMC open-access full text fetched and parsed section-by-section (Methods, Results, Discussion, figure/table captions); cross-checked overall composite HR against independent search-engine summary of the same DOI. Both agree. HbA1c/prediabetes proportion drawn from the companion glycemia paper, not the kidney paper itself — flagged separately below.

---

## 1. Trial design basics

- N = 17,604 randomized; 8,803 semaglutide, 8,801 placebo. [SELECT-KIDNEY-2024, Methods]
- Population: age ≥45 y, BMI ≥27 kg/m², established CVD (parent SELECT-PRIMARY-2023 inclusion). [SELECT-KIDNEY-2024, Methods]
- **Explicit exclusion of diabetes**: "history of type 1 or type 2 diabetes; HbA1c ≥6.5% (48 mmol/mol)" was an exclusion criterion — confirms this is a population *without* diagnosed diabetes and with HbA1c <6.5% at entry. [SELECT-KIDNEY-2024, Methods]
- Dose: subcutaneous semaglutide, escalated over 16 weeks to a target dose of 2.4 mg once weekly (i.e., the Wegovy obesity dose). [SELECT-KIDNEY-2024, Methods]
- Median follow-up: 182 weeks (~3.5 years). [SELECT-KIDNEY-2024, Results, "Baseline characteristics" subsection]

## 2. Baseline kidney characteristics

- "Just over one-fifth of the trial population had either an eGFR <60 ml/min/1.73m² or a urinary albumin-to-creatinine ratio (UACR) ≥30 mg/g at baseline." [SELECT-KIDNEY-2024, Results, "Baseline characteristics"] — Note this is a *combined* denominator (low eGFR OR elevated UACR), not two separately reported percentages; exact split not given in main text.
- High-baseline-albuminuria subgroup (UACR ≥300 mg/g, i.e., macroalbuminuria range) at randomization: n=159 semaglutide, n=166 placebo. [SELECT-KIDNEY-2024, Fig. 3 / Results subgroup section]
- Mean/median baseline eGFR for the overall cohort: **not stated in the main text**; the paper refers to Supplementary Table 1 for full baseline demographics, which was not accessible in this fetch (paywalled/not rendered by the fetch tool). Flag as not verified — do not report a specific mean eGFR number without accessing Supplementary Table 1 directly.

## 3. Composite kidney outcome — definition and prespecification status

- Exact definition (verbatim, reconstructed from Abstract/Results): "The pre-specified main kidney endpoint was a 5-component composite: first occurrence of death from kidney disease, initiation of chronic kidney replacement therapy (dialysis or transplantation), onset of persistent eGFR <15 ml/min/1.73m², persistent ≥50% reduction in eGFR from baseline, or onset of persistent macroalbuminuria." [SELECT-KIDNEY-2024, Abstract; Results "Effect of semaglutide on the main kidney endpoint"]
- "Persistent" = confirmed by ≥2 measurements at least 4 weeks apart. [SELECT-KIDNEY-2024, Methods, "Outcomes"]
- Status: explicitly labeled **prespecified** ("pre-specified main kidney endpoint," "pre-specified analysis of SELECT") throughout. However, the Discussion also states: "Although the effect of semaglutide on kidney outcomes was a secondary analysis of SELECT, with the primary endpoint being MACE, the analysis presented here was pre-specified." [SELECT-KIDNEY-2024, Discussion, "Strengths and limitations"] — i.e., prespecified *secondary* analysis, not the trial's primary endpoint (primary endpoint = 3-point MACE, reported in SELECT-PRIMARY-2023).

## 4. Overall composite result

- Event rates: 1.8% semaglutide vs 2.2% placebo (in-trial). [SELECT-KIDNEY-2024, Results] → back-calculated event counts ≈158 semaglutide / ≈194 placebo (percentages × N; paper does not appear to state raw counts in the main-text prose extracted here — treat these as derived, not directly quoted, and confirm against Fig. 2 caption/Table if precise integers are needed downstream).
- In-trial HR 0.78 (95% CI 0.63–0.96; P=0.02). [SELECT-KIDNEY-2024, Results, "Effect of semaglutide on the main kidney endpoint"]
- On-treatment HR 0.75 (95% CI 0.59–0.94; P=0.01). [SELECT-KIDNEY-2024, same subsection]

## 5. Component-level drivers — critical caveat

- Authors' own statement: "The effect on the main endpoint was driven by the treatment effect on onset of macroalbuminuria and persistent ≥50% reduction in eGFR, with the other components being sparse." [SELECT-KIDNEY-2024, Results, "Effect of semaglutide on the main kidney endpoint"]
- Component-level HRs/counts are displayed in **Fig. 2** (not extracted as exact numbers here — the fetch returned the caption/description but not the numeric table itself). Do NOT report per-component HRs or counts as verified until Fig. 2 is inspected directly (e.g., via a PDF or image read of the figure).
- Confirmatory caveat: "Due to a small number of events, treatment effects on the additional endpoints, including two further composite endpoints that excluded macroalbuminuria, were not significant." [SELECT-KIDNEY-2024, Results, "Effect of semaglutide on other pre-specified kidney endpoints"] — this directly supports the concern that the "hard" components (kidney failure, kidney death, sustained ≥50% eGFR loss) were too sparse individually to drive significance on their own, and that macroalbuminuria onset (a softer, reversible marker) is doing much of the work in the composite.

## 6. eGFR trajectory / slope

- Overall eGFR at week 104 (MMRM): semaglutide −0.86 vs placebo −1.61 ml/min/1.73m²; treatment benefit +0.75 (95% CI 0.43–1.06; P<0.001). [SELECT-KIDNEY-2024, Results "Effect of semaglutide on eGFR at 104 weeks"; Table 1; Fig. 4a]
- Subgroup baseline eGFR ≥60: treatment difference +0.57 ml/min/1.73m² (95% CI 0.26–0.89; P<0.001). [Table 1; Fig. 5a]
- Subgroup baseline eGFR <60: semaglutide +5.28 vs placebo +3.09 ml/min/1.73m² at week 104 (i.e., a rise in both arms); treatment difference +2.19 (95% CI 1.00–3.38; P<0.001). [Table 1; Fig. 5a]
  - Authors' own caveat on this subgroup: because eGFR rose in *both* arms in the <60 subgroup, "the rise may partly reflect regression to the mean... Whether the treatment benefit reflects a net increase in eGFR in the semaglutide group or prevention of a fall is uncertain." [Discussion]
- Total eGFR slope: −0.78 ml/min/1.73m²/year semaglutide vs −1.17 placebo; difference 0.39 (95% CI 0.30–0.48; P<0.001). [Results "Effect of semaglutide on total and chronic eGFR slope"; Table 1]
- Chronic slope (from week 20): ~0.29 ml/min/1.73m²/year lower slope with semaglutide (exact CI not extracted from this fetch — verify against Table 1 directly). [Results, same subsection]
- Acute-phase slope (baseline→week 16, European-cohort subset only, 34.1% of patients with additional early timepoints): semaglutide arm showed a MORE pronounced early dip, annualized difference −1.33 ml/min/1.73m²/year, reported as P=0.05 (borderline/not significant). [Results "Effect of semaglutide on acute eGFR to week 20"; Table 1; Fig. 4a] — i.e., an initial acute eGFR dip with semaglutide (consistent with a hemodynamic/functional effect), followed by the between-arm divergence favoring semaglutide over the chronic phase.
- Subgroup interaction testing on the **main composite endpoint** (not the slope): "No statistically significant interactions were observed in any subgroup" across the prespecified subgroups shown in Fig. 3 (score test). [Results]
- Post hoc ACEi/ARB subgroup on the composite endpoint: HR 0.74 (95% CI 0.58–0.94) in n=13,054 on ACEi/ARB vs HR 0.92 (95% CI 0.60–1.42) in n=4,550 not on ACEi/ARB; interaction P=0.39 (not significant — explicitly labeled **post hoc**). [Results]

## 7. Glucose-independence argument and authors' own caveats

- Exploratory mediation/correlation analysis: "little correlation between the within-person change in eGFR and the within-person changes in body weight, systolic blood pressure or glycated hemoglobin (HbA1c)... (Supplementary Table 2)." [Results, "Correlation and mediation..."]
- Mediation estimate: "a mediation analysis suggested that 81% (95% CI 41.30, 120) of the change in eGFR was attributable to change in body weight, with considerable imprecision in the estimate." [Results, same subsection] — note the CI crosses well above 100% and is very wide, signaling a fragile point estimate.
- Authors explicitly caution: "such estimates should be treated as suggestive, not definitive" [Discussion, Limitations], and "the number of events of the main composite endpoint was too low to support a formal mediation analysis of this endpoint" [Discussion, Limitations] — i.e., the mediation analysis was done on eGFR slope/change, NOT on the hard composite outcome, because the composite had too few events.
- Weight-related confounding of creatinine-based eGFR: "a caveat of any reduction in estimated GFR based on creatinine in a trial where treatment is associated with weight (and, thereby, muscle mass) loss must consider contributions from both creatinine production and improved kidney filtration." [Discussion] Authors note they lack cystatin C to clarify this: "We have not measured cystatin C as yet in SELECT." [Discussion]
- Applicability caveat (explicit, own words): "Unlike most kidney endpoint trials, we did not selectively include patients at most risk of kidney disease progression. As a consequence, the number of kidney event endpoints and the power to examine effects on endpoints and detect subgroup interactions are limited." [Discussion]
- Positive framing the authors themselves use (for balance): "These data from individuals with overweight or obesity and high cardiovascular risk are important as they constitute the first evidence to suggest that GLP-1RAs, and, specifically, semaglutide, could have beneficial effects on the kidney in the absence of diabetes." [Discussion]

## 8. Baseline HbA1c / prediabetes proportion (nuance on the "non-diabetic" framing)

- **Not from the kidney paper itself** — the kidney paper's inclusion/exclusion criteria only establish HbA1c <6.5% at entry (no diabetes diagnosis). [SELECT-KIDNEY-2024, Methods]
- From the companion glycemia-outcomes paper (SELECT-GLYCEMIA-2024, same parent trial, same baseline cohort): mean baseline HbA1c 5.78% ± 0.34% (39.7 ± 3.68 mmol/mol); 66.4% of participants had baseline HbA1c in the prediabetes range (5.7–6.4%), 33.5% had HbA1c <5.7% (normoglycemic). [SELECT-GLYCEMIA-2024, Table 1; Results, "Change in Glycemia and Body Weight Over Time"]
- Clinical/evidentiary implication for lane synthesis: SELECT participants were free of *diagnosed* diabetes, but roughly two-thirds were prediabetic by HbA1c criteria at baseline — so "non-diabetic" should not be read as "normoglycemic"; residual dysglycemia is a plausible confounder/mediator pathway that the kidney paper's own correlation/mediation analysis (see §7) only partially addresses (weight, not HbA1c, was the factor identified in the fragile mediation estimate).

---

## Verification status

- **Full text verified** for SELECT-KIDNEY-2024 (Nature Medicine 2024, PMC11271413, open access) — Methods, Results, Discussion sections and figure/table captions were retrieved and quoted/paraphrased above with locators.
- **Not verified / gaps remaining**:
  - Exact overall mean/median baseline eGFR (Supplementary Table 1 not accessed).
  - Precise integer event counts per arm for the composite and for each of the 5 individual components (Fig. 2's underlying numeric table not accessed — only its caption/description and the qualitative driver statement were retrieved). **Do not treat the 158/194 event-count figures above as directly quoted** — they are back-calculated from the reported percentages and should be confirmed against Fig. 2 or Table data before use in any deliverable.
  - Exact CI for the chronic eGFR slope (0.29 ml/min/1.73m²/year figure lacks a quoted CI here; Table 1 should be checked directly).
- **Abstract-only vs full-text**: full text was used, not abstract-only.
- Baseline HbA1c/prediabetes proportion (§8) is verified but sourced from a **different, companion publication** (SELECT-GLYCEMIA-2024), not the kidney paper — flag this distinction if cited in the lane memo or cross-review.

## Handback

Raw material only — no clinical interpretation or evidence-grading applied here per task instructions. This note is intended to feed `lanes/04_endocrinology.md` (SELECT section, "what SELECT can and cannot say about glucose-independent kidney benefit") and is available for any other lane (nephrology, CKM, methodologist) that needs SELECT kidney locators. Two known gaps flagged above (mean baseline eGFR; per-component event counts) should be closed by a follow-up fetch of Supplementary Table 1 and Fig. 2's data table before the director finalizes numbered deliverables that cite them.
