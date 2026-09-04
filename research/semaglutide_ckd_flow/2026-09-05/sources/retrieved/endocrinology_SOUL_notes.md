# SOUL primary + SOUL kidney outcomes — retrieved source notes (endocrinology lane)

Retrieved 2026-09-05 via WebSearch/WebFetch + Crossref/Europe PMC/ClinicalTrials.gov APIs. Raw material only, no interpretation. See message to team-lead for full structured extraction with locators.

## Sources verified
- **SOUL-PRIMARY-2025**: McGuire DK et al. N Engl J Med. 2025;392(20):2001-2012. DOI 10.1056/NEJMoa2501006. PMID 40162642. NCT03914326. Abstract confirmed via Europe PMC (raw JSON, exact text pulled).
- **SOUL-KIDNEY-2026**: Mann JFE et al. Diabetes Care. 2026;49(2):257-265. DOI 10.2337/dc25-1080. PMID 41380027. PMCID PMC12824789 (open access, full text fetched via pmc.ncbi.nlm.nih.gov).
- ClinicalTrials.gov NCT03914326 record pulled via API v2 (clinicaltrials.gov/api/v2/studies/NCT03914326) — exact eligibility criteria text captured.

## Verification caveats
- NEJM.org full text is paywalled (403 to WebFetch); primary-paper abstract came from Europe PMC's indexed abstract (should match PubMed/NEJM verbatim — standard MEDLINE abstract). Individual secondary-outcome HRs (HF hosp, all-cause mortality, kidney composite HR as reported in the *2025* primary paper) were NOT independently recovered — only the abstract's summary sentence ("confirmatory secondary outcomes ... did not differ significantly") was accessible. The kidney-specific HR from the *2026* Diabetes Care paper (HR 0.91) is confirmed directly.
- Kidney paper (PMC12824789) full text was accessed and is open access; discussion-section quotes on the FLOW-vs-SOUL comparison were extracted via WebFetch (small-model summarization of full text) and cross-checked across two independent fetches with consistent numbers (35%/71% CV-death share; 65%/29% kidney-specific share; 7.5 vs 2.3 events/100 patient-years). Treat exact wording as close-paraphrase/verbatim-quoted by the fetch tool, not hand-verified character-by-character against the PDF.
- Albuminuria/UACR was NOT collected in SOUL (explicit limitation stated by authors) — this is a key population-comparability fact versus FLOW.
