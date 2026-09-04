# CKM lane — retrieved source notes (regulatory labels + 2026 guideline status)

**Role prefix:** `ckm-`
**Written by:** flow-ckm (Wave 1)
**Purpose:** Preserve exact retrieval provenance for web-verified items cited in `lanes/05_ckm_combinations.md` §5 and §0 source table, so other lanes/director don't have to re-derive access routes. This note contains no full-text PDF caching — only short excerpts, dates, and access routes actually retrieved this session via WebSearch/WebFetch.

---

## 1. FDA — OZEMPIC label (semaglutide), Indications and Usage

- **Route:** DailyMed (NLM official repository of FDA-approved labeling) via WebFetch.
- **URL:** https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=adec4fd2-6858-4c99-91d4-531f5f2a2d79
- **Label revision date shown on page:** Revised 5/2026.
- **Verbatim indications retrieved:**
  1. "as an adjunct to diet and exercise to improve glycemic control in adults with type 2 diabetes mellitus"
  2. "to reduce the risk of major adverse cardiovascular events (cardiovascular death, non-fatal myocardial infarction or non-fatal stroke) in adults with type 2 diabetes mellitus and established cardiovascular disease"
  3. "to reduce the risk of sustained eGFR decline, end-stage kidney disease, and cardiovascular death in adults with type 2 diabetes mellitus and chronic kidney disease"
- **Cross-check:** Original CKD-indication sNDA approval reported 2025-01-28 by multiple independent press sources (National Kidney Foundation, PR Newswire/Novo Nordisk press release, AJMC, Pharmacy Times) — consistent with the DailyMed label content.
- **Not retrieved this session:** the accessdata.fda.gov PDF fetch returned only binary/undecoded content; DailyMed HTML was used instead as the working official source. A "Limitations of Use" statement was searched for but not found in the section returned.

## 2. EMA — Ozempic SmPC kidney indication

- **Route:** WebSearch only (multiple independent secondary sources); direct WebFetch of ema.europa.eu and worldpharmaceuticals.net returned HTTP 402/403.
- **Fact confirmed (multi-source):** CHMP positive opinion / label update adding kidney-disease-related risk reduction to the Ozempic SmPC, dated **mid-December 2024**.
- **Not retrieved:** exact SmPC section 4.1 indication wording. Flagged as unverified-quote in the lane file; director/red-team should fetch the official EMA EPAR/SmPC PDF directly (not via WebFetch, which was blocked) before quoting.

## 3. Taiwan TFDA — 胰妥讚 (Ozempic) label, CKD indication

- **Route:** WebFetch of official 食藥署 label-lookup platform (mcp.fda.gov.tw), page for license 衛部菌疫輸字第001107號.
- **URL:** https://mcp.fda.gov.tw/im_detail_1/衛部菌疫輸字第001107號
- **Label revision date shown:** 2026年1月26日 (2026-01-26).
- **Verbatim CKD indication (3rd indication) retrieved, Traditional Chinese:**
  > 「用於已有慢性腎臟病的第二型糖尿病病人時，可降低eGFR持續下降、進展至腎臟病末期或心血管疾病死亡之風險。」
- **Cross-check:** semantically matches FDA/EMA kidney-indication scope (eGFR decline / ESKD / CV death), consistent with FLOW primary composite framing.

## 4. KDIGO 2026 Diabetes and CKD Guideline — status

- **Route:** WebSearch (kdigo.org own announcement page, Guideline Central preview); direct WebFetch of the KDIGO draft PDF (kdigo.org/wp-content/uploads/2026/03/KDIGO-2026-Diabetes-and-CKD-Guideline-Update-Public-Review-Draft-March-2026.pdf) returned HTTP 403 (not readable this session).
- **Status as of 2026-09-05 (session date):** Public Review Draft, posted March 2026; public comment period closed **2026-04-13**. No confirmed final/published version was located via WebSearch as of the session date. **Treat as DRAFT, not finalized guidance**, until another session confirms a final publication.
- **Scope per KDIGO's own summary:** update limited to a new Chapter 1 (definitions/prevention/risk assessment), Chapter 2 (glycemic monitoring), Chapter 4 (comprehensive pharmacotherapy); evidence review through July 2025; GRADE methodology.
- **Content directionality (UNVERIFIED quote-level — secondary summaries only, e.g. Guideline Central preview and an ERA/European Renal Association social-media summary of a KDIGO/KDCT joint session by Katherine R. Tuttle):** described as moving toward a "foundational therapy" (SGLT2i + statin + RASi) plus "additional risk-based therapy" (nsMRA, GLP-1 RA, antiplatelet) framework; a possible new 1A-strength recommendation for nsMRA (eGFR ≥25, normal potassium, UACR ≥30 mg/g, on maximal RASi); possible allowance for simultaneous SGLT2i + nsMRA initiation; GLP-1 RA described as the preferred second-line glucose-lowering agent for T2D+CKD not at glycemic goal despite SGLT2i+metformin, plus a new practice point favoring GLP-1 RA in patients with obesity. **None of this paragraph should be quoted as guideline text in a numbered deliverable without independent primary-document confirmation.**

## 5. ADA Standards of Care in Diabetes—2026, Chapter 11 (CKD and Risk Management)

- **Route:** WebSearch only; direct WebFetch of diabetesjournals.org article page failed (no readable output / effectively blocked).
- **Bibliographic record confirmed:** Diabetes Care 2026;49(Suppl 1):S246; PubMed ID 41358881.
- **Content directionality (UNVERIFIED quote-level, via Pharmacy Times / DiabetesOnTheNet secondary summaries):** SGLT2i or GLP-1 RA with demonstrated benefit recommended for T2D with eGFR 20–60 and/or albuminuria (glycemic + CKD-progression + CV-event indication, irrespective of A1C); GLP-1 RA preferred for glycemic management in eGFR <30 (advanced CKD) given lower hypoglycemia risk plus CV benefit. Exact recommendation numbering (searched for "11.7b", "9.10–9.11") was **not confirmed** — these specific numbers came from the session's master prompt/brief, not from a verified primary-text match this session.

## 6. 2026 AHA/ACC/ADA/ASN CKM Syndrome Guideline

- **Route:** WebSearch (PubMed, AHA Professional Heart Daily, JACC DOI listing, TCTMD news article); WebFetch of professional.heart.org and tctmd.com full detail pages returned 403/402 respectively for the deepest content, though the TCTMD fetch did return one usable paragraph (below).
- **Bibliographic record confirmed:** published 2026-06-09; JACC DOI 10.1016/j.jacc.2026.03.056 (companion Circulation DOI prefix CIR.0000000000001453).
- **One directly retrieved paragraph (TCTMD, quoting guideline co-chair Ndumele, NOT the guideline's own text):**
  > "For type 2 diabetes and CKD, there are a number of effective therapies that not only improve those conditions, but also reduce CVD risk... mentioning treatments like glucagon-like peptide-1 (GLP-1) receptor agonists, sodium-glucose cotransporter 2 (SGLT2) inhibitors, and the nonsteroidal mineralocorticoid receptor antagonist (MRA) finerenone."
- **Confirmed negative finding:** the TCTMD article explicitly does **not** use the phrase "four pillars" when describing this guideline.
- **Not retrieved:** the guideline's own operative recommendation text (Class of Recommendation / Level of Evidence) on RASi+SGLT2i+finerenone+GLP-1RA sequencing/layering.

---

## Access-route summary (for CLAUDE.md compliance note)

All items above were retrieved via `WebSearch`/`WebFetch` (general web tools), not via the configured `research_hub`/`paper-search`/`google-scholar` MCPs, because the material needed here is regulatory-label and guideline-organization web content (DailyMed, national regulator label-lookup platforms, guideline-society sites, news/society coverage of a 2026 guideline) rather than indexed academic literature — those MCPs are oriented at journal-article discovery/full-text retrieval. No Sci-Hub or other circumvention route was used at any point. No PDFs were cached; the one binary PDF fetch attempt (FDA accessdata.fda.gov) returned undecoded content and was not used or saved as a source — DailyMed HTML was used instead as the working official text.
