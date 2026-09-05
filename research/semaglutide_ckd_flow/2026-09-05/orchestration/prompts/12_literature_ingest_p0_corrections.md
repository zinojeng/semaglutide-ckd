# Literature ingest P0 correction brief

Scope: correct only these two tracked files, then commit; do not push and do not make any network/cloud-parser call.

- `sources/SOURCE_ACQUISITION_LOG.csv`
- `sources/LITERATURE_INGEST_REPORT.md`

Required corrections:

1. FDA PI rights: retract “US Government work/public domain.” The cached label carries Novo Nordisk copyright notices. Record `NOASSERTION` / proprietary manufacturer labeling; local reading and short quotation only. Do not infer permission to publish the full PDF/Markdown or to upload it to a cloud parser.
2. PMID 41706532 is a real, distinct FLOW paper, not unresolved and not a duplicate: Tuttle et al., “Kidney and Survival Outcomes with Semaglutide by CKD Severity in the FLOW Trial,” CJASN 2026, DOI `10.2215/CJN.0000000974`, PMID `41706532`, PMCID `PMC13143484`. Add/correct `FLOW-CKD-SEVERITY-2026`; keep it distinct from JACC CV-phenotype DOI `10.1016/j.jacc.2026.02.5125`, PMID `42233552`.
3. CKM guideline rights: state that its notice expressly prohibits multiple copies, modification, alteration, enhancement, and distribution without AHA permission. Reading access is not a reuse/TDM grant; retain the parser incident.
4. FLOW-HF and FLOW-CVPHENOTYPE: retract “not open access/no lawful route.” Crossref reports the version of record under CC BY-NC-ND 4.0 and publisher TDM endpoints (PIIs `S0735109724081166` and `S0735109726057311`). Direct automated retrieval returned 403, so record the route as unresolved/browser, subscription, or publisher API required—not “not OA.”
5. Acquisition-log completeness: fill known PMID/PMCID/page count/hash fields where already present locally; do not invent parser job IDs, model/version, parameters, or per-file timestamps. Explicitly mark unavailable fields `NA`/`not recorded`, and label the shared timestamp as session-log time rather than per-file retrieval time. Keep `license_evidence_url` as a URL field; move prose/local-line evidence to notes.
6. Content QA warnings (do not edit `fulltext/` or cached parses):
   - `fulltext/glp1_cardiorenal_Mahaffey_2025.md` must be treated as `content_verified: false`. Correct Figure 2 values for downstream use: eGFR <60 HR 0.87 (0.71–1.06); eGFR >=60 HR 0.59 (0.37–0.94), interaction P=.13; KDIGO low/moderate 0.67 (0.27–1.67), high 0.75 (0.50–1.12), very high 0.84 (0.68–1.04), interaction P=.79. Its local lines 56/58/60 are wrong.
   - quarantined PMID 41925680 / DOI dc25-3055 is unrelated GRADE/liraglutide CGM and must stay excluded.
   - SOUL kidney parse has erroneous strike-through markup and a license notice interleaved into methods.
   - CKM parse corrupts `SGLT2i` around line 1796 and its tables need PDF QA.
   - SELECT parse has unrelated generic Nature form/noise from about line 677 to EOF; exclude that tail from RAG/index.
   - FLOW primary/supplement and Mann 2024 parses have two-column/table-order artifacts and are not numerically QA-passed.
7. Do not claim that all restricted parses are quarantined “from citation.” Restricted PDFs/derived MD must remain private and cannot be the sole evidentiary basis; public abstracts/metadata and independently verified lawful sources may still be cited.

Validation before commit:

- Parse the CSV with a real CSV parser.
- Search both files for the retracted phrases and wrong PMID mapping.
- Confirm no PDFs, cache files, `fulltext/`, secrets, or `.claude/**` are tracked.
- Commit only the two corrected files (and do not stage this prompt file).
