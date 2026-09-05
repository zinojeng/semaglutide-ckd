# Literature acquisition and parse audit

**Session role:** flow-literature-ingest
**Scope:** metadata, provenance, licensing, and content-QA only. The canonical artifacts are SOURCE_ACQUISITION_LOG.csv and this report.

## Current status

- The CSV contains **17 source records** and parses as 31 columns per row. `FLOW-CKDSEVERITY-2025` now points to a fresh official Europe PMC acquisition with reproducible hashes and a deterministic local JATS-to-Markdown conversion; the earlier Mahaffey local-derivative immutability incident remains explicit in the same row and below.
- The private cache contains **nine LlamaParse Markdown outputs with corresponding PDFs**, including one quarantined identity misfetch. This is an artifact count, not a reconstructable count of upload jobs.
- Parser version, model version, job ID, parameter hash, and true per-file retrieval time were not captured. The CSV now records **not_recorded** rather than inventing values. Historical session-log times were 2026-09-04T18:25:03Z and 2026-09-04T18:33:50Z, but they are not valid per-file retrieval timestamps.
- The original literature-ingest correction pass used local files and an independent source audit only. It made no network or cloud-parser calls. A later 2026-09-05 QA event directly read the official PMC HTML and source images for the CJASN CKD-severity paper (Figures 1, 2, and 5); that event created no local full-text artifact and used no parser. Separately, the Mahaffey local derivative had already been modified in violation of the repository's fulltext-immutability rule; that incident is documented below rather than being described as compliant source maintenance.

**Gate:** the cache is useful for identity discovery and spot checks, but no LlamaParse row has reproducible provenance. Restricted parses cannot be a sole evidentiary basis. Every claim drawn from such a source requires revalidation against an official reading source or independently verified public abstract/metadata.

## Corrections now canonical

1. **FDA label rights and version.** The earlier government-work reuse classification is retracted. The cached 10/2025 Ozempic label is sponsor-authored proprietary material, carries Novo Nordisk notices, and is recorded as **NOASSERTION**. Its cloud parse was not rights-authorized. It is also historical: current wording must be checked against FDA supplement S-038 / DailyMed revised 5/2026.
2. **PMID 41706532 is a distinct paper, now directly content-checked.** Tuttle et al., “Kidney and Survival Outcomes with Semaglutide by CKD Severity in the FLOW Trial,” CJASN 2026;21(5):841–851, DOI 10.2215/CJN.0000000974, PMID 41706532, PMCID PMC13143484, Version of Record, **CC BY 4.0**. It is separate from the JACC cardiovascular-phenotype analysis, PMID 42233552. After the metadata audit, a later QA event directly read official PMC Methods/Results and source images for Figures 1, 2, and 5 without downloading or parsing a file.
3. **AHA CKM manuscript restriction.** The cached author manuscript expressly limits copies, modification, alteration, enhancement, and distribution without permission. Its license is **NOASSERTION**; the private parse is a rights incident and all extracted recommendations/numbers require official-source revalidation.
4. **JACC FLOW papers are open-access Versions of Record.** FLOW-HF-2024 and FLOW-CVPHENOTYPE-2026 are recorded by Crossref under **CC BY-NC-ND 4.0**. An HTTP 403 from one automated request is a route failure, not an access-status finding.
5. **Correction and misfetch metadata.** The FLOW design erratum is PMID 38033315 / PMCID PMC10966322. The quarantined GRADE-CGM misfetch is PMID 41925680 / PMCID PMC13186179, 10 pages, Markdown SHA-256 43e9d241d3008da8314926422e076c8b3c1b5fe0615df082a13bb534aaa4ce81.
6. **Repository routes.** SOUL-CV-2025 has an Amsterdam UMC Taverne reading route. The Badve class meta-analysis has a Glasgow accepted-manuscript route under CC BY-NC-ND. Repository access does not by itself authorize redistribution or cloud TDM.

## Acquisition and reuse matrix

| source_id | Acquired content | Rights / license | QA and permitted use |
|---|---|---|---|
| FLOW-DESIGN-2023 | PDF + private MD | CC BY-NC 4.0 | Identity and selected values spot-checked; tables/layout not fully QA-passed |
| FLOW-DESIGN-2023-CORRECTION | PDF + private MD | CC BY-NC 4.0 | One-page erratum identity passed; cite only as correction |
| SELECT-KIDNEY-2024 | PDF + private MD | CC BY 4.0 | Partial QA; remove Reporting Summary tail before any index/RAG use |
| SUSTAIN6-PIONEER6-EGFR-NDT-2025 | PDF + private MD | CC BY-NC 4.0 | Identity and selected slope result spot-checked only |
| SOUL-KIDNEY-2026 | PDF + private MD | NOASSERTION; ADA TDM/ML restriction | Rights incident; parse private, not sole evidence; official-source revalidation required |
| FLOW-DIALYSIS-SAFETY-2026 | PDF + private MD | NOASSERTION; ADA TDM/ML restriction | Rights incident; abstract-level facts only after independent verification |
| CKM-GUIDELINE-2026 | author-manuscript PDF + private MD | NOASSERTION; express AHA reuse restriction | Rights incident; tables not QA-passed; official-source revalidation required |
| MISFETCH-GRADE-CGM-2026 | quarantined PDF + MD | NOASSERTION; ADA restriction | Wrong document; never cite or index |
| FDA-LABEL-OZEMPIC-PI-2025 | historical label PDF + private MD | NOASSERTION; proprietary sponsor labeling | Rights incident; use current official label for regulatory wording |
| FLOW-HF-2024 | abstract/metadata | CC BY-NC-ND 4.0 VOR | Abstract-only QA; full text not acquired |
| FLOW-CVPHENOTYPE-2026 | abstract/metadata | CC BY-NC-ND 4.0 VOR | Abstract-only QA; full text not acquired |
| SUSTAIN6-2016 | abstract/metadata | NOASSERTION | Abstract-only; full-text rights not assessed |
| SOUL-CV-2025 | abstract/metadata | NOASSERTION | Amsterdam UMC reading route identified; full text not acquired |
| SELECT-FLOW-SOUL-POOLED-2026 | abstract/metadata | NOASSERTION | Abstract-only; repository record checked had no full-text file |
| GLP1-CLASSMETA-BADVE-2025 | abstract/metadata | CC BY-NC-ND 4.0 accepted manuscript | Glasgow reading route identified; no modified derivative distribution |
| FLOW-CKDSEVERITY-2026-CJASN | official PMC HTML/source images; no local file | CC BY 4.0 VOR via PMC13143484 | Partial content QA passed for Methods/Results and Figs. 1, 2, and 5; no parser was used and complete PDF/table/layout QA was not performed |
| FLOW-CKDSEVERITY-2025 | fresh official Europe PMC JATS/PDF plus deterministic private Markdown; historical local derivative retained only as incident evidence | CC BY 4.0 VOR via PMC11931213 | Fresh artifact identity/license and Figure 2 numeric/visual QA passed; new cache artifacts are read-only. The original mutation remains a disclosed process incident. |

## Provenance limitations

All cached parse rows identify the parser as LlamaParse, but parser version, model version, job ID, parameter hash, and per-file retrieval time are unavailable. Therefore:

- no cached parse is **provenance-complete** or exactly reproducible;
- the same historical session timestamp is no longer represented as a file-specific retrieval time;
- QA labels distinguish identity/spot-check success from full numeric and layout validation;
- retraction status is **not_checked** unless a source is itself a correction notice;
- license_evidence_url is now a URL or **not_recorded**, while local text locators remain in notes;
- proprietary/restricted sources use SPDX-compatible **NOASSERTION**, not free-text pseudo-SPDX values.

## Content-QA findings

### FLOW design count

The design paper reports N=3534; the primary FLOW analysis reports N=3533. Both source-specific counts must be retained. The checked sources do not establish why they differ, so no enrolled-versus-dosed explanation should be asserted.

### Mahaffey Figure 2 — verified numeric correction and immutability incident

The pre-existing ignored derivative `fulltext/glp1_cardiorenal_Mahaffey_2025.md` contained a transcription error and was directly edited on 2026-09-05, despite `CLAUDE.md`'s rule never to modify `fulltext/`. The numerical repair was correct, but the mutation was a provenance-process failure: neither the edited file nor its later-added front matter is an immutable acquisition record.

The available lineage is:

- a complete pre-edit Claude Code `Read` result captured at 2026-09-04T17:53:24Z permits reconstruction of the pre-edit byte stream, SHA-256 `c554902a9e201831908a48a6cc57927e0fdae519ab2131a99a497975881ce7b4`;
- the current modified file has SHA-256 `c80ac4e818e2e889bff81905491587bce573bd559f55ebb722c24bd4d26fb369`;
- the file is gitignored and has no Git object history; a search found no standalone pre-edit backup. The earlier hash is therefore **transcript-reconstructed**, not the hash of a separately preserved original artifact.

No further edit to the ignored file is authorized by this repair. This version-controlled section is the derived correction note and, together with the published Figure 2 source image (PMCID PMC11931213; European Heart Journal 2025;46:1096–1108; DOI 10.1093/eurheartj/ehae613; Figure 2, journal p.1103), is the authority for the corrected matrix:

Publication remediation was completed later on 2026-09-05 without overwriting the historical file. The official Europe PMC JATS XML and PDF were freshly retrieved, hashed, and stored under `sources/retrieved/cache/`; Pandoc 3.9 converted the JATS deterministically with `--from=jats --to=gfm --wrap=none`. The acquisition log records the JATS, PDF, Markdown, and parameter hashes. Figure 2 was rendered from the fresh PDF and visually rechecked. These new files and the entire legacy `fulltext/` corpus were made read-only; `scripts/source_corpus_guard.sh verify` enforces that state locally and tolerates the intentional absence of private full text in a public clone. This closes the prospective publication safeguard while retaining the historical incident and both legacy hashes.

| Stratum | HR (95% CI) |
|---|---|
| Overall | 0.82 (0.68–0.98) |
| eGFR <60 | 0.87 (0.71–1.06) |
| eGFR ≥60 | 0.59 (0.37–0.94); P-interaction .13 |
| UACR <300 | 1.04 (0.72–1.51) |
| UACR ≥300 | 0.75 (0.61–0.93); P-interaction .13 |
| KDIGO low/moderate | 0.67 (0.27–1.67) |
| KDIGO high | 0.75 (0.50–1.12) |
| KDIGO very high | 0.84 (0.68–1.04); P-interaction .79 |

The pre-edit derivative swapped values between the eGFR and KDIGO strata and contained an invalid explanatory line. Historical/cached copies remain unsafe. Future corrections to any source artifact must be additive: preserve the acquired object byte-for-byte, record its hash, and place corrections in a separate tracked erratum/QA note such as this one.

### CJASN CKD-severity paper — later direct PMC content QA

`FLOW-CKDSEVERITY-2026-CJASN` was initially logged at metadata level under the alias `FLOW-CKD-SEVERITY-2026`. A later 2026-09-05 QA event directly inspected the official PMC full-text HTML and source images for Figures 1, 2, and 5 (PMCID PMC13143484). It confirmed that the primary-outcome analyses across eGFR and UACR severity strata were prespecified, while all-cause-death analyses by CKD severity were post hoc; it also checked the cited UACR<100 and UACR≥2,000 estimates. No PDF or Markdown derivative was created, no LlamaParse job occurred, and the exact UTC access time was not captured. Accordingly, the CSV records direct reading and partial content QA, not invented download/parser provenance or complete layout QA.

### Parsed-file artifacts

- **SELECT-KIDNEY-2024:** approximately lines 677–1044 are a generic Nature Reporting Summary, not article findings. Exclude that tail from indexing.
- **SOUL-KIDNEY-2026:** valid table values at approximately lines 16/20/21 are rendered as Markdown strikethrough; the ADA notice is interleaved into Methods near line 116.
- **CKM-GUIDELINE-2026:** SGLT2i is corrupted near line 1796; the 208-page tables and figures have not been numerically QA-passed.
- **FLOW primary, supplement, and Mann SGLT2 analysis:** raw two-column/table reading-order artifacts remain. Prefer prose-stated values and verify table cells against the PDF image.
- **GRADE-CGM misfetch:** permanently exclude from all semaglutide/CKD evidence and RAG.

## Abstract-level evidence captured

These remain abstract-level unless a lawful full text has also been content-QA'd:

- **SELECT/FLOW/SOUL pooled 2026:** N=30,787; primary composite 973 vs 1,134, HR 0.84 (0.77–0.91); kidney-specific composite 347 vs 416, HR 0.80 (0.69–0.92).
- **Badve class meta-analysis:** 11 trials, N=85,373; T2D kidney composite HR 0.82 (0.73–0.93); per-molecule effects are not available in the abstract.
- **FLOW-HF-2024:** HF event or CV death HR 0.73 (0.62–0.87); HF events HR 0.73 (0.58–0.92); CV death HR 0.71 (0.56–0.89).
- **FLOW-CVPHENOTYPE-2026:** PMID 42233552; first author Tuttle; do not conflate with PMID 41706532.
- **SUSTAIN6-2016:** MACE HR 0.74 (0.58–0.95); retinopathy complications HR 1.76 (1.11–2.78).
- **SOUL-CV-2025:** MACE 579/4,825 vs 668/4,825, HR 0.86 (0.77–0.96); confirmatory kidney composite nonsignificant in the abstract.
- **SOUL-KIDNEY-2026:** five-point HR 0.91 (0.80–1.05), P=.19; four-point HR 0.86 (0.66–1.10), P=.22; eGFR-slope difference 0.40 (0.27–0.53) mL/min/1.73m²/year.
- **FLOW dialysis pooled analysis:** 307 initiated dialysis and 165 remained on treatment. This is descriptive continuation safety, not evidence for initiating semaglutide in maintenance dialysis.

## Rights incidents and citation rule

The SOUL kidney paper, FLOW dialysis paper, AHA/ACC/ADA/ASN CKM manuscript, and historical FDA label were sent to a third-party parser without documented authorization. Their generated Markdown remains private and gitignored.

This does **not** make the underlying publications categorically uncitable. It means the cloud-derived parse cannot be relied on as the sole source. Use an official webpage, public abstract/metadata, or lawful manual reading route to revalidate each claim, provide a normal scholarly citation, keep quotations short, and do not redistribute restricted PDFs or Markdown.

The GRADE-CGM misfetch is different: it is unrelated to this review and is never an evidence source, regardless of citation rights.

## Retrieval integrity incidents

The PMC fallback downloader silently returned the wrong document twice:

1. A request for FLOW-DESIGN-2023 returned its one-page correction. Both artifacts are now separately identified.
2. A request for SOUL-KIDNEY-2026 returned an unrelated GRADE-CGM substudy. It is quarantined and fully identified in the CSV.

Every future automated download must pass a title + DOI + PMID/PMCID identity gate before parsing.

## Regulatory version control

The cached FDA label is revised 10/2025 and is superseded by the 2026 S-038 / DailyMed 5/2026 revision. Any statement about current indication wording or warnings must cite the newer official label after direct verification. The historical cached label may support historical comparison only.

## Next lawful acquisition priorities

1. For `FLOW-CKDSEVERITY-2026-CJASN`, extend the existing focused PMC QA only if a future claim requires material outside Methods/Results or Figures 1, 2, and 5; preserve the direct-reading/no-local-artifact route unless an independently justified derivative is needed.
2. FLOW protocol, SAP, and ClinicalTrials.gov NCT03819153 results/history.
3. JACC FLOW-HF and cardiovascular-phenotype full text/supplements through publisher/browser routes; honor CC BY-NC-ND.
4. SUSTAIN-6 KDIGO analysis, SMART non-diabetic CKD, SMART measured-GFR, and REMODEL design/methods.
5. Current FDA S-038, EMA, TFDA, ADA 2026, and KDIGO 2026 status-controlled official documents.
6. SOUL primary, Badve meta-analysis, and the SELECT/FLOW/SOUL pooled analysis through lawful reading routes.
7. CREDENCE, DAPA-CKD, EMPA-KIDNEY, FIDELIO/FIGARO/FIDELITY primary sources for cross-drug comparisons.

## Handoff requirements

- Source librarian: maintain the 17-record acquisition log; use `FLOW-CKDSEVERITY-2026-CJASN` as the canonical ID (with `FLOW-CKD-SEVERITY-2026` retained only as a historical alias), and preserve the direct-PMC partial-QA boundary.
- Director/editor: never use restricted parse text as sole evidence; revalidate official-source wording and keep abstract-only claims labeled.
- CKM/regulatory lane: use the current FDA revision and independently verify guideline recommendations.
- Nephrology/trialist lane: apply the Mahaffey Figure 2 matrix above and preserve source-specific FLOW counts.
- RAG builder: exclude all restricted parses, the quarantined misfetch, SELECT’s Reporting Summary tail, and any table region that has not passed numeric/layout QA.
