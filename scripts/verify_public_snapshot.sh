#!/usr/bin/env bash
set -euo pipefail

project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$project_root"

if [[ "${1:-}" != "--strict-curated" ]]; then
  echo "usage: $0 --strict-curated" >&2
  exit 2
fi

failed=0
required=(
  README.md
  PUBLICATION_NOTES.md
  CLAUDE.md
  "Semaglutide ckd and flow evidence prompt.md"
  research/semaglutide_ckd_flow/2026-09-05/16_FINAL_SYNTHESIS_ZH_TW.md
  research/semaglutide_ckd_flow/2026-09-05/19_WAVE4_PEER_REVIEW_ADDENDUM_ZH_TW.md
  research/semaglutide_ckd_flow/2026-09-05/SOURCE_LEDGER.csv
  research/semaglutide_ckd_flow/2026-09-05/articles_zh_tw/README.md
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/README.md
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/VISUAL_ASSET_CATALOG_ZH_TW.md
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn/MANIFEST.json
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/source_figures/ATTRIBUTION.md
  scripts/source_corpus_guard.sh
  scripts/generate_presentation_visuals.py
  scripts/verify_presentation_pack.sh
)

for path in "${required[@]}"; do
  if [[ ! -s "$path" ]]; then
    echo "PUBLIC_SNAPSHOT_MISSING_OR_EMPTY $path" >&2
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

if git grep -nI -E '/Users/|llx-[A-Za-z0-9_-]{10,}|sk-[A-Za-z0-9_-]{12,}|gh[pousr]_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----' -- . ':(exclude)scripts/verify_public_snapshot.sh'; then
  echo "PUBLIC_SNAPSHOT_PRIVATE_PATH_OR_SECRET_PATTERN" >&2
  failed=1
fi

allowed_visuals=(
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/FLOW_CKDSEVERITY_Mahaffey_Figure2.jpg
  research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/source_figures/SELECT_KIDNEY_Colhoun_2024_Figure1_KM.png
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

if [[ -x scripts/verify_presentation_pack.sh ]]; then
  scripts/verify_presentation_pack.sh
fi

if ! git diff --check; then
  failed=1
fi

if [[ "$failed" -ne 0 ]]; then
  exit 1
fi

echo "PUBLIC_SNAPSHOT_QA_PASS"
