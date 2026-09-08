#!/usr/bin/env bash
set -euo pipefail

project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$project_root"

if [[ "${1:-}" != "--strict-curated" ]]; then
  echo "usage: $0 --strict-curated" >&2
  exit 2
fi

failed=0
# Curated-snapshot contract. These values are intentionally centralized and
# exact: a corpus expansion must update the source report and both public-facing
# summaries in the same reviewed release. Claim-level locator tokens below serve
# the same purpose; a legitimate wording/data change requires a conscious audit
# update rather than weakening the gate.
post_flow_source_count=27
post_flow_pdf_count=24
post_flow_markdown_count=28
required=(
  README.md
  PUBLICATION_NOTES.md
  CLAUDE.md
  "Semaglutide ckd and flow evidence prompt.md"
  research/semaglutide_ckd_flow/2026-09-05/01_SOURCE_INVENTORY.md
  research/semaglutide_ckd_flow/2026-09-05/16_FINAL_SYNTHESIS_ZH_TW.md
  research/semaglutide_ckd_flow/2026-09-05/19_WAVE4_PEER_REVIEW_ADDENDUM_ZH_TW.md
  research/semaglutide_ckd_flow/2026-09-05/20_NEPHROLOGIST_TALK_DEBATE_SYNTHESIS_ZH_TW.md
  research/semaglutide_ckd_flow/2026-09-05/21_POST_FLOW_CITATION_COMMENT_REPLY_REVIEW_ZH_TW.md
  research/semaglutide_ckd_flow/2026-09-05/22_FINERENONE_VS_SEMAGLUTIDE_AFTER_RASI_SGLT2I_ZH_TW.md
  research/semaglutide_ckd_flow/2026-09-05/23_FLOW_CENTERED_REVIEW_PUBLICATION_AGENDA_ZH_TW.md
  research/semaglutide_ckd_flow/2026-09-05/SOURCE_LEDGER.csv
  research/semaglutide_ckd_flow/2026-09-05/sources/ACADEMIC_RESEARCH_AGENTS_AUDIT.md
  research/semaglutide_ckd_flow/2026-09-05/sources/ACQUISITION_POLICY.md
  research/semaglutide_ckd_flow/2026-09-05/sources/LITERATURE_INGEST_REPORT.md
  research/semaglutide_ckd_flow/2026-09-05/sources/NEW_FULLTEXT_BOUNDARY_AUDIT_2026-09-09.md
  research/semaglutide_ckd_flow/2026-09-05/sources/SOURCE_ACQUISITION_LOG.csv
  research/semaglutide_ckd_flow/2026-09-05/articles_zh_tw/README.md
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/README.md
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/POST_FLOW_NEPHROLOGIST_SPEAKER_ADDENDUM_ZH_TW.md
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/VISUAL_ASSET_CATALOG_ZH_TW.md
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/ENGLISH_ORIGINAL_VISUAL_GUIDE.md
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn/MANIFEST.json
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn_en/MANIFEST.json
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/source_figures/ATTRIBUTION.md
  research/semaglutide_ckd_flow/2026-09-05/orchestration/ORCHESTRATION.md
  research/semaglutide_ckd_flow/2026-09-05/orchestration/CLAUDE_CROSS_SESSION_RUNBOOK.md
  scripts/source_corpus_guard.sh
  scripts/generate_presentation_visuals.py
  scripts/generate_presentation_visuals_en.py
  scripts/verify_presentation_pack.sh
  scripts/verify_english_visual_pack.sh
)

for path in "${required[@]}"; do
  if [[ ! -s "$path" ]]; then
    echo "PUBLIC_SNAPSHOT_MISSING_OR_EMPTY $path" >&2
    failed=1
  elif ! git ls-files --error-unmatch -- "$path" >/dev/null 2>&1; then
    echo "PUBLIC_SNAPSHOT_REQUIRED_PATH_NOT_TRACKED $path" >&2
    failed=1
  fi
done

while IFS= read -r -d '' path; do
  case "$path" in
    fulltext/*|research/*/sources/retrieved/*|research/*/lanes/*|research/*/cross_reviews/*|research/*/presentation_zh_tw/workstreams/*|research/*/orchestration/*LOG*.md|research/*/17_RED_TEAM_QA.md|research/*/18_RED_TEAM_CLOSURE.md|*.pdf|*.xml|*.docx|*.pptx|*.key|*.pem|.env|.env.*)
      echo "PUBLIC_SNAPSHOT_FORBIDDEN_PATH $path" >&2
      failed=1
      ;;
  esac
done < <(git ls-files -z)

if git ls-files -s | awk '$1 == 120000 {print $4}' | grep -q .; then
  git ls-files -s | awk '$1 == 120000 {print "PUBLIC_SNAPSHOT_SYMLINK " $4}' >&2
  failed=1
fi

# Top-level source documentation is metadata-only and explicitly allowlisted.
# This prevents a rights-restricted raw article Markdown from being staged next
# to an approved audit memo and bypassing the broader sources/retrieved ban.
source_metadata_dir="research/semaglutide_ckd_flow/2026-09-05/sources"
allowed_source_metadata=(
  "$source_metadata_dir/ACADEMIC_RESEARCH_AGENTS_AUDIT.md"
  "$source_metadata_dir/ACQUISITION_POLICY.md"
  "$source_metadata_dir/LITERATURE_INGEST_REPORT.md"
  "$source_metadata_dir/NEW_FULLTEXT_BOUNDARY_AUDIT_2026-09-09.md"
  "$source_metadata_dir/SOURCE_ACQUISITION_LOG.csv"
)
while IFS= read -r -d '' source_path; do
  if [[ "$(dirname "$source_path")" != "$source_metadata_dir" ]]; then
    continue
  fi
  approved=0
  for allowed_path in "${allowed_source_metadata[@]}"; do
    if [[ "$source_path" == "$allowed_path" ]]; then
      approved=1
      break
    fi
  done
  if [[ "$approved" -ne 1 ]]; then
    echo "PUBLIC_SNAPSHOT_UNAPPROVED_SOURCE_METADATA $source_path" >&2
    failed=1
  fi
done < <(git ls-files -z -- "$source_metadata_dir")

if git grep -nI -E '/Users/|llx-[A-Za-z0-9_-]{10,}|sk-[A-Za-z0-9_-]{12,}|gh[pousr]_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----' -- . ':(exclude)scripts/verify_public_snapshot.sh'; then
  echo "PUBLIC_SNAPSHOT_PRIVATE_PATH_OR_SECRET_PATTERN" >&2
  failed=1
fi

rights_report="research/semaglutide_ckd_flow/2026-09-05/sources/LITERATURE_INGEST_REPORT.md"
rights_docs=(
  README.md
  PUBLICATION_NOTES.md
  research/semaglutide_ckd_flow/2026-09-05/sources/ACQUISITION_POLICY.md
  "$rights_report"
  research/semaglutide_ckd_flow/2026-09-05/21_POST_FLOW_CITATION_COMMENT_REPLY_REVIEW_ZH_TW.md
  research/semaglutide_ckd_flow/2026-09-05/22_FINERENONE_VS_SEMAGLUTIDE_AFTER_RASI_SGLT2I_ZH_TW.md
  research/semaglutide_ckd_flow/2026-09-05/23_FLOW_CENTERED_REVIEW_PUBLICATION_AGENDA_ZH_TW.md
  research/semaglutide_ckd_flow/2026-09-05/sources/NEW_FULLTEXT_BOUNDARY_AUDIT_2026-09-09.md
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/README.md
)
legacy_rights_claims=(
  'Local primary papers, supplements, and authorized PDF-to-Markdown parses'
  '受限制全文與解析檔只供內部學術演講研究'
  '只代表依法取得並供內部研究的本機 artifact'
)

for claim in "${legacy_rights_claims[@]}"; do
  if grep -FHn -- "$claim" "${rights_docs[@]}"; then
    echo "PUBLIC_SNAPSHOT_LEGACY_OVERAUTHORIZATION_CLAIM $claim" >&2
    failed=1
  fi
done

if ! grep -Fq \
  'does not by itself authorize format conversion, TDM/ML, third-party cloud upload' \
  research/semaglutide_ckd_flow/2026-09-05/sources/ACQUISITION_POLICY.md; then
  echo "PUBLIC_SNAPSHOT_ACCESS_PROCESSING_BOUNDARY_MISSING" >&2
  failed=1
fi

if ! grep -Fq '不等於自動解析、TDM／ML 或第三方雲端處理的授權' \
  research/semaglutide_ckd_flow/2026-09-05/21_POST_FLOW_CITATION_COMMENT_REPLY_REVIEW_ZH_TW.md; then
  echo "PUBLIC_SNAPSHOT_ZH_TW_ACCESS_PROCESSING_BOUNDARY_MISSING" >&2
  failed=1
fi

new_fulltext_audit="research/semaglutide_ckd_flow/2026-09-05/sources/NEW_FULLTEXT_BOUNDARY_AUDIT_2026-09-09.md"
for marker in \
  'EXCLUDE_WRONG_ARTICLE' \
  '未納入既有 27-source cache' \
  '不可整檔直接進入 RAG'; do
  if ! grep -Fq "$marker" "$new_fulltext_audit"; then
    echo "PUBLIC_SNAPSHOT_NEW_FULLTEXT_AUDIT_MARKER_MISSING $marker" >&2
    failed=1
  fi
done

if ! python3 - "$rights_report" <<'PY'
import sys
from pathlib import Path

path = Path(sys.argv[1])
text = path.read_text(encoding="utf-8")
lines = text.splitlines()

explicit_ids = {
    "PMC12824789",
    "PMC13191384",
    "PMC13191398",
    "PMC13191419",
    "PMC13493325",
    "PMC13493327",
}
explicit_marker = "ADA_EXPLICIT_NO_TDM_ML"
older_id = "PMC12583412"
older_marker = "ADA_OLDER_NOTICE_PROCESSING_UNCLEARED"
errors = []

def table_row(pmcid):
    matches = [line for line in lines if f"| {pmcid} |" in line]
    if len(matches) != 1:
        errors.append(f"{pmcid}: expected one corpus-table row, found {len(matches)}")
        return ""
    return matches[0]

for pmcid in sorted(explicit_ids):
    row = table_row(pmcid)
    if explicit_marker not in row:
        errors.append(f"{pmcid}: missing {explicit_marker}")

older_row = table_row(older_id)
if older_marker not in older_row:
    errors.append(f"{older_id}: missing {older_marker}")
if explicit_marker in older_row:
    errors.append(f"{older_id}: incorrectly classified as explicit notice")

# This is an intentionally audited snapshot set: a newly marked ADA source must
# trigger a conscious rights review and an update to explicit_ids.
classified_ids = {
    line.split("|")[1].strip()
    for line in lines
    if line.startswith("| PMC") and explicit_marker in line
}
if classified_ids != explicit_ids:
    missing = sorted(explicit_ids - classified_ids)
    unexpected = sorted(classified_ids - explicit_ids)
    errors.append(
        f"explicit ADA classification set mismatch; missing={missing}, "
        f"unexpected={unexpected}"
    )

for error in errors:
    print(f"PUBLIC_SNAPSHOT_RIGHTS_CLASSIFICATION_ERROR {error}", file=sys.stderr)

raise SystemExit(bool(errors))
PY
then
  failed=1
fi

acquisition_log="research/semaglutide_ckd_flow/2026-09-05/sources/SOURCE_ACQUISITION_LOG.csv"
if ! python3 - "$acquisition_log" <<'PY'
import csv
import re
import sys
from pathlib import Path

path = Path(sys.argv[1])
with path.open(encoding="utf-8", newline="") as handle:
    raw_rows = list(csv.reader(handle))
with path.open(encoding="utf-8", newline="") as handle:
    reader = csv.DictReader(handle)
    rows = list(reader)

errors = []
if reader.fieldnames is None or len(reader.fieldnames) != 31:
    errors.append(f"expected 31 columns, found {len(reader.fieldnames or [])}")
for line_number, raw_row in enumerate(raw_rows[1:], start=2):
    if len(raw_row) != 31:
        errors.append(
            f"line {line_number}: expected 31 fields, found {len(raw_row)}"
        )

by_id = {row.get("source_id", ""): row for row in rows}
restricted_ids = {
    "SOUL-KIDNEY-2026",
    "FLOW-DIALYSIS-SAFETY-2026",
    "CKM-GUIDELINE-2026",
    "FDA-LABEL-OZEMPIC-PI-2025",
}
for source_id in sorted(restricted_ids):
    row = by_id.get(source_id)
    if row is None:
        errors.append(f"{source_id}: row missing")
        continue
    qa_status = row.get("qa_status", "")
    for marker in ("FAIL_FOR_AI_RAG_REPROCESSING", "RIGHTS_INCIDENT"):
        if marker not in qa_status:
            errors.append(f"{source_id}: {marker} gate missing")
    combined = " ".join(
        row.get(field, "") for field in ("reuse_decision", "qa_status", "notes")
    ).lower()
    if "excluded from evidence discovery" not in combined:
        errors.append(f"{source_id}: evidence-discovery exclusion missing")
    if "cannot be the sole evidentiary basis" in combined or "fail_for_unfiltered_rag" in combined:
        errors.append(f"{source_id}: obsolete soft-gate wording remains")

cjasn_id = "FLOW-CKDSEVERITY-2026-CJASN"
cjasn = by_id.get(cjasn_id)
if cjasn is None:
    errors.append(f"{cjasn_id}: row missing")
else:
    expected = {
        "license_spdx": "CC-BY-4.0",
        "pdf_page_count": "11",
        "parser": "local-jats-etree-v1",
        "parse_status": "success",
    }
    for field, value in expected.items():
        if cjasn.get(field) != value:
            errors.append(f"{cjasn_id}: {field} must equal {value!r}")
    for field in ("pdf_sha256", "markdown_sha256"):
        if not re.fullmatch(r"[0-9a-f]{64}", cjasn.get(field, "")):
            errors.append(f"{cjasn_id}: {field} must be a lowercase SHA-256")
    if not cjasn.get("local_cache_path", "").endswith("/PMC13143484.pdf"):
        errors.append(f"{cjasn_id}: private PDF cache locator missing")
    combined = " ".join(cjasn.values()).lower()
    if re.search(r"no (?:file download|pdf acquired|local full-text artifact)", combined):
        errors.append(f"{cjasn_id}: stale no-acquisition wording remains")
    if "2026-09-05" not in combined or "2026-09-07" not in combined:
        errors.append(f"{cjasn_id}: two-stage reading/acquisition chronology missing")

for error in errors:
    print(f"PUBLIC_SNAPSHOT_ACQUISITION_RIGHTS_ERROR {error}", file=sys.stderr)

raise SystemExit(bool(errors))
PY
then
  failed=1
fi

source_ledger="research/semaglutide_ckd_flow/2026-09-05/SOURCE_LEDGER.csv"
source_inventory="research/semaglutide_ckd_flow/2026-09-05/01_SOURCE_INVENTORY.md"
if ! python3 - "$source_ledger" "$source_inventory" "$rights_report" "$post_flow_source_count" <<'PY'
import csv
import re
import sys
from collections import Counter
from pathlib import Path

ledger_path, inventory_path, report_path = map(Path, sys.argv[1:4])
with ledger_path.open(encoding="utf-8", newline="") as handle:
    raw_rows = list(csv.reader(handle))
with ledger_path.open(encoding="utf-8", newline="") as handle:
    reader = csv.DictReader(handle)
    rows = list(reader)

errors = []
if reader.fieldnames is None or len(reader.fieldnames) != 18:
    errors.append(f"ledger expected 18 columns, found {len(reader.fieldnames or [])}")
for line_number, raw_row in enumerate(raw_rows[1:], start=2):
    if len(raw_row) != 18:
        errors.append(
            f"ledger line {line_number}: expected 18 fields, found {len(raw_row)}"
        )

source_ids = [row.get("source_id", "") for row in rows]
duplicates = sorted(key for key, count in Counter(source_ids).items() if count > 1)
if duplicates:
    errors.append(f"duplicate source_id values: {', '.join(duplicates)}")

by_id = {row.get("source_id", ""): row for row in rows}
locator_expectations = {
    "FLOW-MRA-2025": ("Figure 2", "RRT HR 0.18 (0.03-0.71)", "0.91 (0.68-1.23)"),
    "FLOW-DIALYSIS-SAFETY-2026": ("Table 2", "161.6 vs 110.8", "105.1 vs 110.8", "43/117"),
    "GLP1-CLASSMETA-BADVE-2025": (
        "T2D-only: kidney composite HR 0.82 (0.73-0.93)",
        "with SELECT added post hoc: kidney composite HR 0.81 (0.72-0.92)",
    ),
}
for source_id, expected in locator_expectations.items():
    row = by_id.get(source_id)
    if row is None:
        errors.append(f"{source_id}: row missing")
        continue
    key_result = row.get("key_result", "")
    missing = [token for token in expected if token not in key_result]
    if missing:
        errors.append(f"{source_id}: key_result missing {missing}")

badve = by_id.get("GLP1-CLASSMETA-BADVE-2025")
if badve is not None:
    badve_population = badve.get("population", "")
    for token in ("T2D-only N=67,769", "N=85,373 when SELECT was added post hoc"):
        if token not in badve_population:
            errors.append(f"GLP1-CLASSMETA-BADVE-2025: population missing {token!r}")

report_text = report_path.read_text(encoding="utf-8")
corpus = []
for line in report_text.splitlines():
    match = re.match(r"\| (PMC\d+) \| (\d+) \|", line)
    if match:
        corpus.append(match.groups())
expected_corpus_count = int(sys.argv[4])
if len(corpus) != expected_corpus_count:
    errors.append(
        f"expected {expected_corpus_count} private-corpus source rows, "
        f"found {len(corpus)}"
    )

reference_text = (
    ledger_path.read_text(encoding="utf-8")
    + "\n"
    + inventory_path.read_text(encoding="utf-8")
)
for pmcid, pmid in corpus:
    if pmcid not in reference_text and pmid not in reference_text:
        errors.append(f"{pmcid}/{pmid}: absent from ledger and inventory")

for error in errors:
    print(f"PUBLIC_SNAPSHOT_SOURCE_TRACEABILITY_ERROR {error}", file=sys.stderr)

raise SystemExit(bool(errors))
PY
then
  failed=1
fi

count_docs=(README.md PUBLICATION_NOTES.md "$rights_report")
count_expectations=(
  "$post_flow_source_count unique full-text sources"
  "$post_flow_pdf_count valid PDFs"
  "$post_flow_markdown_count Markdown artifacts"
)
for expected_count in "${count_expectations[@]}"; do
  for count_doc in "${count_docs[@]}"; do
    if ! grep -Fq "$expected_count" "$count_doc"; then
      echo "PUBLIC_SNAPSHOT_POST_FLOW_COUNT_MISSING $count_doc: $expected_count" >&2
      failed=1
    fi
  done
done

allowed_visuals=(
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/FLOW_CKDSEVERITY_Mahaffey_Figure2.jpg
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/source_figures/SELECT_KIDNEY_Colhoun_2024_Figure1_KM.png
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/source_figures/FLOW_SGLT2_Mann_2024_Figure1.jpg
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/source_figures/FLOW_SGLT2_Mann_2024_Figure2.jpg
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/source_figures/FLOW_SGLT2_Mann_2024_Figure3.jpg
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn/01_flow_endpoints_forest_zh_tw.svg
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn/01_flow_endpoints_forest_zh_tw@2x.png
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn/02_flow_egfr_phases_zh_tw.svg
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn/02_flow_egfr_phases_zh_tw@2x.png
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn/03_flow_sglt2_subgroup_forest_zh_tw.svg
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn/03_flow_sglt2_subgroup_forest_zh_tw@2x.png
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn/04_flow_mra_subgroup_forest_zh_tw.svg
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn/04_flow_mra_subgroup_forest_zh_tw@2x.png
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn/05_select_soul_pooled_context_zh_tw.svg
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn/05_select_soul_pooled_context_zh_tw@2x.png
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn/06_flow_safety_dotplot_zh_tw.svg
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn/06_flow_safety_dotplot_zh_tw@2x.png
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn_en/01_flow_endpoints_forest_en.svg
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn_en/01_flow_endpoints_forest_en@2x.png
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn_en/02_flow_egfr_phases_en.svg
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn_en/02_flow_egfr_phases_en@2x.png
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn_en/03_flow_sglt2_subgroup_forest_en.svg
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn_en/03_flow_sglt2_subgroup_forest_en@2x.png
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn_en/04_flow_mra_subgroup_forest_en.svg
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn_en/04_flow_mra_subgroup_forest_en@2x.png
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn_en/05_select_soul_pooled_context_en.svg
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn_en/05_select_soul_pooled_context_en@2x.png
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn_en/06_flow_safety_dotplot_en.svg
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn_en/06_flow_safety_dotplot_en@2x.png
)
while IFS= read -r visual; do
  approved=0
  for allowed in "${allowed_visuals[@]}"; do
    if [[ "$visual" == "$allowed" ]]; then
      approved=1
      break
    fi
  done
  if [[ "$approved" -ne 1 ]]; then
    echo "PUBLIC_SNAPSHOT_UNAPPROVED_VISUAL $visual" >&2
    failed=1
  fi
done < <(git ls-files '*.jpg' '*.jpeg' '*.png' '*.gif' '*.webp' '*.svg')

if [[ ! -x scripts/verify_presentation_pack.sh ]]; then
  echo "PUBLIC_SNAPSHOT_PRESENTATION_VERIFIER_NOT_EXECUTABLE" >&2
  failed=1
else
  scripts/verify_presentation_pack.sh || failed=1
fi

git diff --check || failed=1
git diff --cached --check || failed=1

if [[ "$failed" -ne 0 ]]; then
  exit 1
fi

echo "PUBLIC_SNAPSHOT_QA_PASS"
