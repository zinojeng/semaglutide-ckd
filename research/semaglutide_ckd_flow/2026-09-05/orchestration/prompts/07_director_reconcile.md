# Session brief — Research director and reconciler

Read `CLAUDE.md`, the complete master prompt, every Wave 1 lane memo, all six
Wave 2 cross-reviews, `orchestration/WAVE2_DIALOGUE_LOG.md`, both CODEX audits,
`sources/ACQUISITION_POLICY.md`, `sources/SOURCE_ACQUISITION_LOG.csv`,
`sources/LITERATURE_INGEST_REPORT.md`, and the primary/official sources needed
to adjudicate conflicts. Source precedence is: primary paper/supplement/SAP or
official guideline/label > current-evidence audit > deliverable-gap audit >
closed cross-review resolution > lane memo > secondary summary. Do not trust a
lane summary when a primary locator is available.

Before drafting, require all six cross-reviews and explicit
`CHALLENGE -> RESPONSE -> CLOSED` dispositions. If the gate is incomplete, stop
and report the missing items rather than creating partial numbered files.

Create the exact required files `01_SOURCE_INVENTORY.md` through `15_CLAIM_EVIDENCE_MAP.md` and `SOURCE_LEDGER.csv`. Requirements:

- reconcile numerical discrepancies explicitly;
- make every major claim source-traceable;
- distinguish direct evidence, indirect evidence, expert extrapolation and unknowns;
- answer all 22 clinical questions from the master prompt across the appropriate files;
- include the five patient scenarios and an evidence-graded layering algorithm;
- include a complete “What we know / What we think / What we still do not know” table before authorizing final synthesis;
- ensure all 2026 guidance/publication/regulatory statuses are dated and verified as of 2026-09-05;
- attach a stable source ID and exact page/table/figure/section/line locator to
  every quantitative claim; mark unavailable values `NR`/`not estimable`;
- rebuild the inventory/ledger from current evidence rather than copying the
  stale draft embedded in lane 01;
- do not create `16_FINAL_SYNTHESIS_ZH_TW.md` in this wave.

Non-negotiable adjudications:

1. FLOW component rows overlap; reject 37.2%, 41.2%, 39.4% and 35–40% as exact
   CV-death shares. Use only the publication's approximate “about 35% of primary
   endpoint components,” state that exact first-event share is not derivable,
   and never call it 35% of treatment effect.
2. Separate AE-driven permanent discontinuation (233/211), GI-specific
   permanent discontinuation (79/20), and the unresolved overall any-reason
   discontinuation discrepancy (primary pooled 26% vs SGLT2 paper 28.8%).
3. Baseline MRA N=257: spironolactone 218, eplerenone 38, esaxerenone 1,
   finerenone 0. Published NNT 9/23 is exploratory.
4. In baseline SGLT2i users, hard-composite HRs 1.07 and 1.18 do not show a
   directionally retained hard benefit; only slope/UACR directions are
   supportive. Additive hard-outcome efficacy and incremental ARR/NNT are not
   established.
5. EMA SmPC 4.1 remains a T2D glycaemic indication; FLOW appears in 5.1. Do
   not describe this as a US-style independent CKD-risk indication or say all
   three jurisdictions are aligned.
6. Keep Mahaffey EHJ 2025, Tuttle CJASN 2026 (PMID 41706532), and Tuttle JACC
   2026 (PMID 42233552) distinct. Treat the local Mahaffey Markdown as failed
   numerical QA and use the corrected Figure 2 values/locator in the ingest
   report. The SELECT/FLOW/SOUL pooled paper was online 2026-08-07.
7. The >=50% eGFR decline and kidney-specific composite are supportive, not
   hierarchy-confirmed. FLOW did not prove kidney failure alone.
8. Subgroup consistency is not additivity, mediation, equivalence, or evidence
   of greater absolute benefit without published stratum-specific risks.
9. HbA1c-at-goal positioning requires organ-outcome RCT evidence plus verified
   guidance; the FLOW HbA1c enrollment ceiling is not supporting evidence.
10. Restricted PDFs/derived Markdown stay private and cannot be the sole
    evidentiary basis. No further cloud parsing without demonstrated authority.
11. Preserve the design paper's N=3,534 and the primary publication's N=3,533
    as source-specific counts. The checked sources do not establish why they
    differ; do not invent an enrolled, randomized, dosed, or analysis-population
    explanation.
12. For SOUL kidney outcomes, use the primary-analysis figures: five-point
    composite 403/4,825 versus 435/4,825, HR 0.91 (0.80–1.05), P=.19;
    four-point composite 112/4,825 versus 129/4,825, HR 0.86 (0.66–1.10),
    P=.22; total-slope difference +0.40 (0.27–0.53) mL/min/1.73m²/year. Do not
    substitute the incompatible 502/539, HR 0.82 secondary-review figure.
13. Keep FLOW safety denominators and labels distinct: severe-hypoglycemia
    participants were 37 per arm whereas supportive endpoint episodes were
    47/46; systematic diabetic-retinopathy rates were 22.8%/22.5%, while the
    broader serious-eye-disorder SOC was 53/30 and must not be relabeled as
    adjudicated retinopathy complications.
14. Date current sources precisely: KDIGO 2026 diabetes/CKD is a public-review
    draft at cutoff; ADA 2026 and the AHA/ACC/ADA/ASN CKM guideline are final;
    TFDA 2026-01-26 is a label-revision date, not a verified first-approval
    date; FDA S-025 anchors the 2025-01-28 initial CKD approval and S-038 /
    DailyMed 2026-05 anchors current wording.
15. Higher UACR identifies higher baseline risk, but no larger absolute
    semaglutide benefit may be claimed without published stratum-specific risk
    differences/NNT. Direct human kidney-cell GLP-1 receptor signaling remains
    uncertain. SMART is short-term surrogate evidence in non-diabetic CKD;
    dialysis evidence is descriptive continuation safety; REMODEL had no
    peer-reviewed primary-results paper by the cutoff.

`SOURCE_LEDGER.csv` must use exactly this header:

```csv
source_id,title,authors,journal,year,doi,pmid,trial,study_type,prespecified_or_posthoc,population,intervention,comparator,primary_endpoint,key_result,limitations,evidence_level,used_for_claims
```

End `15_CLAIM_EVIDENCE_MAP.md` with a clear `SYNTHESIS GATE: PASS` only if the source ledger, trial reconstruction, evidence tables and claim map are adequate. Otherwise write `SYNTHESIS GATE: HOLD` and list blockers.
