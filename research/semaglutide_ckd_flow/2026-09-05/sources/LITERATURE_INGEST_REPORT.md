# Literature acquisition and parse audit

**Session role:** flow-literature-ingest
**Scope:** metadata, provenance, licensing, and content-QA only. The canonical artifacts are SOURCE_ACQUISITION_LOG.csv and this report.

## Current status

- The CSV contains **17 source records** and parses as 31 columns per row. `FLOW-CKDSEVERITY-2025` now points to a fresh official Europe PMC acquisition with reproducible hashes and a deterministic local JATS-to-Markdown conversion; the earlier Mahaffey local-derivative immutability incident remains explicit in the same row and below.
- The private cache contains **nine LlamaParse Markdown outputs with corresponding PDFs**, including one quarantined identity misfetch. This is an artifact count, not a reconstructable count of upload jobs.
- A separate 2026-09-07 post-FLOW response-literature cache now represents **27 unique full-text sources as canonical Markdown derivatives/events and 24 valid PDFs**: 23 canonical Markdown files came from official JATS/XML and four from official PMC printable HTML. One of the 27 sources also has a LlamaParse comparator, so the physical count is **28 Markdown artifacts**, not 28 independent publications. The private JATS manifest records PMID/PMCID/DOI, source URL, captured rights notice, SHA-256, and parser identity; the separate HTML manifest records artifact hashes and parser route, while the four HTML rights determinations are summarized below. Neither machine-local paths nor source artifacts are published.
- For the nine legacy LlamaParse rows, parser version, model version, job ID, parameter hash, and true per-file retrieval time were not captured. The CSV now records **not_recorded** rather than inventing values. Historical session-log times were 2026-09-04T18:25:03Z and 2026-09-04T18:33:50Z, but they are not valid per-file retrieval timestamps.
- The original literature-ingest correction pass used local files and an independent source audit only. It made no network or cloud-parser calls. A later 2026-09-05 QA event directly read the official PMC HTML and source images for the CJASN CKD-severity paper (Figures 1, 2, and 5); that event created no local full-text artifact and used no parser. Separately, the Mahaffey local derivative had already been modified in violation of the repository's fulltext-immutability rule; that incident is documented below rather than being described as compliant source maintenance.

**Gate:** the cache is useful for identity discovery and spot checks, but no legacy LlamaParse row has reproducible provenance; the new comparator likewise lacks parser version, engine metadata, and job ID. Independent revalidation supports a scientific claim only; it does not retroactively authorize an earlier parse. Rights-restricted or uncleared derivatives remain quarantined and must not be redistributed, indexed, or reprocessed unless separately cleared.

## Post-FLOW citation/response acquisition — 2026-09-07

### Scope and result

The post-FLOW search started from PMID 38785209, its PubMed cited-in graph and formal `CommentsCorrectionsList`, then added date-limited FLOW+semaglutide and semaglutide+kidney/renal/CKD title/abstract searches. At execution time the dynamic inventory contained 673 cited-in records, four formal `CommentIn` records, a 1,047-record union, and 77 automatically prioritized records. Manual triage selected publications that materially address endpoint interpretation, background therapy, measurement artifact, MRA/SGLT2i combinations, dialysis, generalizability, safety, or citation echo. Search counts are dated observations, not permanent quality metrics.

Official PMC/Europe PMC JATS was requested before PDF because it provides identity, structure, captured license text, and stable table/figure labels without requiring a third-party parser. Twenty-three records passed title/PMID/PMCID/DOI identity checks and produced private Markdown conversion events with `local-jats-etree-v1`; 20 also yielded valid PDFs. Three records—PMC13493325, PMC13493327, and PMC13518088—had valid official JATS/HTML but their attempted PDF endpoints did not return a valid PDF. Those responses were isolated as failed downloads and were never relabeled `.pdf`. Artifact creation is an event inventory, not a representation that automated processing was permitted for every source.

Four additional high-value commentaries—PMC11387018, PMC11795657, PMC12499624, and PMC13143466—were available from official PMC printable HTML even though their JATS endpoints were not consistently synchronized. Their HTML produced private GFM conversion events with Pandoc 3.9, and valid PDFs were retrieved through the official Europe PMC PDF API. A separate private manifest records the HTML, PDF, and Markdown SHA-256 values and parser route; it does not contain license fields, so the rights status is reported source by source below. The combined post-FLOW corpus is therefore 27 canonical source-linked Markdown artifacts and 24 valid PDFs. A second parse of PMC12640882 made solely as a parser comparator raises the physical Markdown-artifact count to 28 without adding a source, participant, or evidence unit.

### Private parsed corpus

| PMCID | PMID | Evidence role | Private artifact status | Public-use boundary |
|---|---:|---|---|---|
| PMC11384876 | 39258261 | Semaglutide-associated AIN/podocytopathy cases and FAERS signal | JATS→MD + PDF | CC BY; case signal cannot establish incidence/causality |
| PMC11387018 | 39078703 | “Renal reinforcements” editorial | PMC HTML→MD + PDF | PMC-readable; captured page has a copyright notice but no affirmative reuse/TDM license (`NOASSERTION`); opinion, not combination-efficacy evidence |
| PMC11485243 | 38914124 | FLOW baseline-SGLT2i analysis | JATS→MD + PDF | CC BY; official Figures 1–3 reusable with attribution after third-party-credit check |
| PMC11595976 | 39598276 | DKD narrative review | JATS→MD + PDF | CC BY; secondary source only |
| PMC11795657 | 39907537 | Combination-nephroprotection editorial | PMC HTML→MD + PDF | CC BY-NC; additive-mechanism framing, no randomized combination proof |
| PMC11843104 | 39990872 | FLOW interpretive editorial | JATS→MD + PDF | CC BY-NC-ND; no adapted publisher artwork |
| PMC11931213 | 39211948 | FLOW CV outcomes by CKD severity | JATS→MD + PDF | CC BY; Figure 2 already independently checked |
| PMC11981399 | 40212218 | Semaglutide CKD meta-analytic review | JATS→MD + PDF | CC BY-NC-ND; full SUSTAIN-6/PIONEER-6 populations are not CKD-only and endpoints were not harmonized; not primary confirmation |
| PMC12487346 | 41029853 | GLP-1RA+SGLT2i combination meta-analysis | JATS→MD + PDF | CC BY; post hoc RCT subgroups plus observational evidence do not prove additivity |
| PMC12499624 | 40327845 | Rapid/simultaneous four-therapy review | PMC HTML→MD + PDF | PMC-readable; captured page has a copyright notice but no affirmative reuse/TDM license (`NOASSERTION`); explicitly notes the trial gap |
| PMC12548029 | 40359159 | ERA individualized renoprotection commentary | JATS→MD + PDF | CC BY; commentary/gap map, not trial evidence |
| PMC12559791 | 40608494 | REMODEL design/baseline | JATS→MD + PDF | CC BY; mechanism-study design, not outcomes |
| PMC12578383 | 41178712 | GLP-1RA CKD/obesity review | JATS→MD + PDF | CC BY; secondary source only |
| PMC12583412 | 40730031 | FLOW baseline-MRA analysis | JATS→MD + PDF | `ADA_OLDER_NOTICE_PROCESSING_UNCLEARED`: captured ADA educational/not-for-profit, properly cited and unaltered-use notice; the recorded notice does not expressly mention TDM/ML. Automated-processing authorization was not established; manual rights review is required |
| PMC12584374 | 41188987 | Overlapping-report cardiovascular meta-analysis | JATS→MD + PDF | CC BY-NC-ND; publication-level double counting of SUSTAIN-6/FLOW reports, mixed designs/routes, and internally inconsistent statistics make it suitable only as a negative methods audit |
| PMC12640882 | 41276951 | Semaglutide-specific CKD systematic review/meta-analysis | JATS→MD + PDF | CC BY; denominator mismatch and duplicate use of the FLOW cohort make its pooled estimate unsuitable as primary confirmation |
| PMC12754405 | 41479840 | CKM spectrum review | JATS→MD + PDF | CC BY-NC; secondary source only |
| PMC12824789 | 41380027 | SOUL kidney outcomes | JATS→MD + PDF | `ADA_EXPLICIT_NO_TDM_ML`: captured ADA notice expressly requires prior written permission for reproduction, TDM, ML, or similar technologies; conversion retained as a restricted-processing incident and excluded from AI/RAG/reprocessing |
| PMC13037467 | 40982219 | GLP-1RA kidney systematic review/meta-analysis | JATS→MD + PDF | CC BY; reported N conflicts with table/arm totals, composite definitions vary, and kidney-failure estimate is imprecise/highly heterogeneous |
| PMC13143484 | 41706532 | FLOW kidney/survival by CKD severity | JATS→MD + PDF | CC BY; subgroup/multiplicity boundaries retained |
| PMC13143466 | 41960971 | CJASN editorial on CKD-severity evidence | PMC HTML→MD + PDF | PMC-readable; captured page has a copyright notice but no affirmative reuse/TDM license (`NOASSERTION`); commentary only |
| PMC13191384 | 41771053 | Comment on FLOW MRA analysis | JATS→MD + PDF | `ADA_EXPLICIT_NO_TDM_ML`: captured ADA notice expressly requires prior written permission for reproduction, TDM, ML, or similar technologies; conversion retained as a restricted-processing incident and excluded from AI/RAG/reprocessing |
| PMC13191398 | 41893299 | Post-dialysis continuation-safety analysis | JATS→MD + PDF | `ADA_EXPLICIT_NO_TDM_ML`: captured ADA notice expressly requires prior written permission for reproduction, TDM, ML, or similar technologies; conversion retained as a restricted-processing incident and excluded from AI/RAG/reprocessing |
| PMC13191419 | 42160608 | Author reply to MRA comment | JATS→MD + PDF | `ADA_EXPLICIT_NO_TDM_ML`: captured ADA notice expressly requires prior written permission for reproduction, TDM, ML, or similar technologies; conversion retained as a restricted-processing incident and excluded from AI/RAG/reprocessing |
| PMC13493325 | 42623535 | Comment on dialysis analysis | JATS→MD; PDF response invalid/quarantined | `ADA_EXPLICIT_NO_TDM_ML`: captured ADA notice expressly requires prior written permission for reproduction, TDM, ML, or similar technologies; conversion retained as a restricted-processing incident and excluded from AI/RAG/reprocessing |
| PMC13493327 | 42623532 | Author reply to dialysis comment | JATS→MD; PDF response invalid/quarantined | `ADA_EXPLICIT_NO_TDM_ML`: captured ADA notice expressly requires prior written permission for reproduction, TDM, ML, or similar technologies; conversion retained as a restricted-processing incident and excluded from AI/RAG/reprocessing |
| PMC13518088 | 41728915 | FLOW infection/COVID-19 analysis | JATS→MD; PDF response invalid/quarantined | CC BY; not central to the present nephrology debate |

The private manifest, source XML/JATS, Markdown, PDFs, failed responses, and parser code remain under the gitignored retrieval cache. The public `SOURCE_ACQUISITION_LOG.csv` is not padded with synthetic rows that omit actual private artifact paths or hashes; this section is the sanitized public audit, while the artifact-complete record remains private. Any future import into the canonical 31-column log must preserve the actual hashes and acquisition routes rather than reconstructing them from this summary.

### Content QA performed

- Title, PMID, PMCID and DOI identity were checked before parsing.
- The MRA and dialysis main/comment/reply chains were analyzed as scientific dialogues. Public claims were subsequently rechecked against official human-readable pages, tables, or public abstracts; rights-restricted derivatives are quarantined and excluded from further AI/RAG use or reprocessing.
- Speaker locators were catalogued for SGLT2i Figures 1–3, MRA Table 1/Figures 1–3, dialysis Figure 1/Table 1/Table 2/Figure 2, CKD-severity Figures 1/2/5, meta-analysis forest captions, and rare-injury cases/tables. Locator QA does not authorize reuse of source artwork.
- Numeric claims in the public review were independently checked against official source prose/tables or PubMed abstracts. Scientific revalidation does not cure an earlier processing-rights incident.
- No paywall, CAPTCHA, access control, or publisher anti-bot challenge was bypassed. NEJM and Kidney International correspondence not reached through an authorized human-reading route remains metadata/official-preview level and is labeled accordingly.

### Rights and internal academic use

The user's internal academic-speech scope may include non-CC full texts that an authorized reader can lawfully access. Access, copying, automated processing, and redistribution are separate determinations: lawful human reading does not by itself authorize format conversion, TDM/ML, third-party cloud upload, figure/table reuse, recording, or public distribution. Accordingly:

- source PDFs, JATS/XML, full-text Markdown and source-page screenshots are private and gitignored; private storage is a publication-control measure, not evidence that copying or processing was authorized;
- CC BY source figures may be reused publicly only with complete attribution and after checking third-party credit lines;
- educational/noncommercial or all-rights-reserved figures may be used only within the applicable source and venue terms, preferably unaltered in English for a live internal talk;
- a recorded talk, downloadable deck, public GitHub release, social post, or translated/adapted figure requires a separate rights check and normally uses an original project redraw;
- credentials are read from local secure configuration, never written into prompts, reports, logs, or Git history;
- before any new local conversion or cloud parse, the workflow must separately record the access basis, automated-processing basis, and redistribution basis. If processing authority is unresolved, use only authorized human reading, public metadata/abstracts, and ordinary short scholarly notes.

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
| SOUL-KIDNEY-2026 | PDF + private MD | NOASSERTION; explicit ADA TDM/ML restriction | Rights incident; derivative quarantined and excluded from further AI/RAG/reprocessing; public claims require authorized human reading or public abstract verification |
| FLOW-DIALYSIS-SAFETY-2026 | official PMC JATS/HTML + PDF + private MD | NOASSERTION; explicit ADA TDM/ML restriction | Public values were independently rechecked against the official reading source; derivative quarantined and excluded from further AI/RAG/reprocessing; publisher artwork is not republished |
| CKM-GUIDELINE-2026 | author-manuscript PDF + private MD | NOASSERTION; express AHA reuse restriction | Rights incident; derivative excluded from evidence discovery/support, AI/RAG, and reprocessing; independently verify recommendations through an official reading source; tables not QA-passed |
| MISFETCH-GRADE-CGM-2026 | quarantined PDF + MD | NOASSERTION; ADA restriction | Wrong document; never cite or index |
| FDA-LABEL-OZEMPIC-PI-2025 | historical label PDF + private MD | NOASSERTION; proprietary sponsor labeling | Rights incident; derivative excluded from evidence discovery/support, AI/RAG, and reprocessing; independently use the current official label for regulatory wording |
| FLOW-HF-2024 | abstract/metadata | CC BY-NC-ND 4.0 VOR | Abstract-only QA; full text not acquired |
| FLOW-CVPHENOTYPE-2026 | abstract/metadata | CC BY-NC-ND 4.0 VOR | Abstract-only QA; full text not acquired |
| SUSTAIN6-2016 | abstract/metadata | NOASSERTION | Abstract-only; full-text rights not assessed |
| SOUL-CV-2025 | abstract/metadata | NOASSERTION | Amsterdam UMC reading route identified; full text not acquired |
| SELECT-FLOW-SOUL-POOLED-2026 | abstract/metadata | NOASSERTION | Abstract-only; repository record checked had no full-text file |
| GLP1-CLASSMETA-BADVE-2025 | abstract/metadata | CC BY-NC-ND 4.0 accepted manuscript | Glasgow reading route identified; no modified derivative distribution |
| FLOW-CKDSEVERITY-2026-CJASN | official PMC HTML/source images checked 2026-09-05; official JATS→private MD + PDF added 2026-09-07 | CC BY 4.0 VOR via PMC13143484 | Focused content QA passed for Methods/Results and Figs. 1, 2, and 5; the later local conversion used `local-jats-etree-v1`, not LlamaParse; complete PDF/table/layout QA was not performed |
| FLOW-CKDSEVERITY-2025 | fresh official Europe PMC JATS/PDF plus deterministic private Markdown; historical local derivative retained only as incident evidence | CC BY 4.0 VOR via PMC11931213 | Fresh artifact identity/license and Figure 2 numeric/visual QA passed; new cache artifacts are read-only. The original mutation remains a disclosed process incident. |

## Provenance limitations

All nine legacy parse rows in the 17-record `SOURCE_ACQUISITION_LOG.csv` identify the parser as LlamaParse, but parser version, model version, job ID, parameter hash, and per-file retrieval time are unavailable. This limitation does not describe the separately manifested 2026-09-07 JATS/Pandoc corpus. Therefore, for those nine legacy rows:

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

`FLOW-CKDSEVERITY-2026-CJASN` was initially logged at metadata level under the alias `FLOW-CKD-SEVERITY-2026`. A 2026-09-05 QA event directly inspected the official PMC full-text HTML and source images for Figures 1, 2, and 5 (PMCID PMC13143484). It confirmed that the primary-outcome analyses across eGFR and UACR severity strata were prespecified, while all-cause-death analyses by CKD severity were post hoc; it also checked the cited UACR<100 and UACR≥2,000 estimates. That first event created no derivative. The separate 2026-09-07 post-FLOW acquisition later added official JATS, a deterministic `local-jats-etree-v1` private Markdown conversion, and a valid PDF to the gitignored cache. Neither event used LlamaParse for this paper, and neither is represented as complete PDF/table/layout QA.

### Parsed-file artifacts

- **SELECT-KIDNEY-2024:** approximately lines 677–1044 are a generic Nature Reporting Summary, not article findings. Exclude that tail from indexing.
- **SOUL-KIDNEY-2026:** valid table values at approximately lines 16/20/21 are rendered as Markdown strikethrough; the ADA notice is interleaved into Methods near line 116.
- **CKM-GUIDELINE-2026:** SGLT2i is corrupted near line 1796; the 208-page tables and figures have not been numerically QA-passed.
- **FLOW primary, supplement, and Mann SGLT2 analysis:** raw two-column/table reading-order artifacts remain. Prefer prose-stated values and verify table cells against the PDF image.
- **GRADE-CGM misfetch:** permanently exclude from all semaglutide/CKD evidence and RAG.

## Abstract-level evidence captured

These remain abstract-level unless an authorized human-reading route has also been content-QA'd; reading access alone is not a processing license:

- **SELECT/FLOW/SOUL pooled 2026:** N=30,787; primary composite 973 vs 1,134, HR 0.84 (0.77–0.91); kidney-specific composite 347 vs 416, HR 0.80 (0.69–0.92).
- **Badve class meta-analysis:** the T2D-only set included 10 trials and N=67,769, with a kidney composite excluding CV death HR 0.82 (0.73–0.93); the exploratory set after adding SELECT included 11 trials and N=85,373, with HR 0.81 (0.72–0.92). Per-molecule effects are not available in the abstract.
- **FLOW-HF-2024:** HF event or CV death HR 0.73 (0.62–0.87); HF events HR 0.73 (0.58–0.92); CV death HR 0.71 (0.56–0.89).
- **FLOW-CVPHENOTYPE-2026:** PMID 42233552; first author Tuttle; do not conflate with PMID 41706532.
- **SUSTAIN6-2016:** MACE HR 0.74 (0.58–0.95); retinopathy complications HR 1.76 (1.11–2.78).
- **SOUL-CV-2025:** MACE 579/4,825 vs 668/4,825, HR 0.86 (0.77–0.96); confirmatory kidney composite nonsignificant in the abstract.
- **SOUL-KIDNEY-2026:** five-point HR 0.91 (0.80–1.05), P=.19; four-point HR 0.86 (0.66–1.10), P=.22; eGFR-slope difference 0.40 (0.27–0.53) mL/min/1.73m²/year.
- **FLOW dialysis pooled analysis:** 307 initiated dialysis and 165 remained on treatment. This is descriptive continuation safety, not evidence for initiating semaglutide in maintenance dialysis.

## Rights incidents and citation rule

The SOUL kidney paper, FLOW dialysis paper, AHA/ACC/ADA/ASN CKM manuscript, and historical FDA label were sent to a third-party parser without a documented processing basis. The 2026-09-07 deterministic conversion run also created local derivatives for sources whose processing basis was unresolved or whose captured notice expressly required permission. Six artifacts—PMC12824789, PMC13191384, PMC13191398, PMC13191419, PMC13493325, and PMC13493327—contain an explicit captured ADA notice requiring prior written permission for reproduction, TDM, ML, or similar technologies. PMC12583412 is different: its captured older ADA notice permits educational, not-for-profit, properly cited and unaltered use but does not expressly mention TDM/ML; automated-processing authorization was nevertheless not established. These derivatives are retained only as quarantined processing-incident records, not represented as authorized artifacts, and are excluded from further AI/RAG use or reprocessing.

This does **not** make the underlying publications categorically uncitable. An authorized reader may use an official webpage, public abstract/metadata, or lawful human-reading route to verify a claim, make ordinary short scholarly notes, and provide a normal citation within applicable terms. That evidence QA does not retroactively cure a processing-rights incident. Restricted PDFs, source artwork, and Markdown must not be redistributed; future automated processing requires a separately documented basis.

The GRADE-CGM misfetch is different: it is unrelated to this review and is never an evidence source, regardless of citation rights.

## Retrieval integrity incidents

The PMC fallback downloader silently returned the wrong document twice:

1. A request for FLOW-DESIGN-2023 returned its one-page correction. Both artifacts are now separately identified.
2. A request for SOUL-KIDNEY-2026 returned an unrelated GRADE-CGM substudy. It is quarantined and fully identified in the CSV.

Every future automated download must pass a title + DOI + PMID/PMCID identity gate before parsing.

## Regulatory version control

The cached FDA label is revised 10/2025 and is superseded by the 2026 S-038 / DailyMed 5/2026 revision. Any statement about current indication wording or warnings must cite the newer official label after direct verification. The historical cached label may support historical comparison only.

## Remaining targeted acquisition or QA priorities

Already completed checks—FLOW protocol/SAP/registry, current official labels/guidelines, comparator primary sources, SMART/REMODEL records, and the 2026-09-07 post-FLOW PMC corpus—are not relisted as future work. The remaining targeted gaps are:

1. Obtain and content-QA the JACC FLOW-HF and cardiovascular-phenotype full texts/supplements through an authorized publisher or institutional reading route; separately document any processing basis and honor CC BY-NC-ND.
2. Obtain the Kidney International and NEJM correspondence through an authorized human-reading route if exact argument-level verification becomes necessary; access alone will not authorize automated processing, reproduction, or redistribution.
3. Obtain and table-QA the Badve class meta-analysis and SELECT/FLOW/SOUL pooled full texts if a future talk needs results beyond their structured abstracts.
4. Extend `FLOW-CKDSEVERITY-2026-CJASN` beyond the current Methods/Results/Figures 1, 2, and 5 QA only when a new claim requires it; keep the dated direct-reading event separate from the 2026-09-07 JATS/PDF/private-Markdown provenance.

## Handoff requirements

- Source librarian: maintain the 17-record legacy acquisition log plus the separate artifact-complete post-FLOW private manifests; use `FLOW-CKDSEVERITY-2026-CJASN` as the canonical ID (with `FLOW-CKD-SEVERITY-2026` retained only as a historical alias), and preserve the direct-PMC partial-QA boundary.
- Director/editor: quarantine rights-restricted or uncleared parse text and exclude it from further AI/RAG or reprocessing; revalidate public claims through authorized human reading or public abstracts and keep abstract-only claims labeled.
- CKM/regulatory lane: use the current FDA revision and independently verify guideline recommendations.
- Nephrology/trialist lane: apply the Mahaffey Figure 2 matrix above and preserve source-specific FLOW counts.
- RAG builder: exclude all restricted parses, the quarantined misfetch, SELECT’s Reporting Summary tail, and any table region that has not passed numeric/layout QA.
