#!/usr/bin/env bash
set -euo pipefail

project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
output_dir="$project_root/research/semaglutide_ckd_flow/2026-09-05"

required=(
  01_SOURCE_INVENTORY.md
  02_FLOW_TRIAL_ANATOMY.md
  03_FLOW_PRIMARY_OUTCOMES.md
  04_FLOW_SECONDARY_SUBGROUP_ANALYSES.md
  05_PRE_FLOW_SEMAGLUTIDE_KIDNEY_EVIDENCE.md
  06_POST_FLOW_SELECT_SOUL_POOLED_EVIDENCE.md
  07_SGLT2_COMBINATION_EVIDENCE.md
  08_MRA_FINERENONE_COMBINATION_EVIDENCE.md
  09_MECHANISMS_OF_KIDNEY_PROTECTION.md
  10_SAFETY_ADVANCED_CKD_DIALYSIS.md
  11_GUIDELINE_REGULATORY_EVOLUTION.md
  12_EVIDENCE_GAPS_AND_CONTROVERSIES.md
  13_CLINICAL_DECISION_FRAMEWORK.md
  14_MASTER_EVIDENCE_TABLE.md
  15_CLAIM_EVIDENCE_MAP.md
  16_FINAL_SYNTHESIS_ZH_TW.md
  SOURCE_LEDGER.csv
)

failed=0
for file in "${required[@]}"; do
  path="$output_dir/$file"
  if [[ ! -s "$path" ]]; then
    echo "MISSING_OR_EMPTY $file"
    failed=1
  fi
done

if [[ -s "$output_dir/15_CLAIM_EVIDENCE_MAP.md" ]] && ! grep -q 'SYNTHESIS GATE: PASS' "$output_dir/15_CLAIM_EVIDENCE_MAP.md"; then
  echo "GATE_NOT_PASSED 15_CLAIM_EVIDENCE_MAP.md"
  failed=1
fi

expected_header='source_id,title,authors,journal,year,doi,pmid,trial,study_type,prespecified_or_posthoc,population,intervention,comparator,primary_endpoint,key_result,limitations,evidence_level,used_for_claims'
if [[ -s "$output_dir/SOURCE_LEDGER.csv" ]]; then
  actual_header="$(head -n 1 "$output_dir/SOURCE_LEDGER.csv" | tr -d '\r')"
  if [[ "$actual_header" != "$expected_header" ]]; then
    echo "BAD_CSV_HEADER SOURCE_LEDGER.csv"
    failed=1
  fi
fi

if grep -RniE 'proves? (an )?additive|proven additive|semaglutide[^.]{0,80}replace(s|d)? SGLT2|FLOW proves[^.]{0,80}finerenone' "$output_dir" --include='*.md'; then
  echo "REVIEW_POSSIBLE_OVERCLAIMS"
  failed=1
fi

if grep -RniE '\b(TODO|TBD|PLACEHOLDER|INSERT CITATION|citation needed)\b' "$output_dir" --include='*.md' --include='*.csv'; then
  echo "UNRESOLVED_PLACEHOLDER"
  failed=1
fi

if [[ "$failed" -ne 0 ]]; then
  exit 1
fi

echo "DELIVERABLE_QA_PASS"

