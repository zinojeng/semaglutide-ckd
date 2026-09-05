#!/usr/bin/env bash
set -euo pipefail

project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
pack="$project_root/research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw"

required=(
  README.md
  SLIDE_STORYBOARD_ZH_TW.md
  SPEAKER_NOTES_ZH_TW.md
  FIGURE_TABLE_SOURCE_MAP.md
  ARTICLE_REFERENCE_GUIDE.md
  VISUAL_RIGHTS_GUIDE.md
  PRIVATE_ASSET_MANIFEST.md
  public_assets/ATTRIBUTION.md
  public_assets/FLOW_CKDSEVERITY_Mahaffey_Figure2.jpg
  chart_data/01_flow_primary_outcomes.csv
  chart_data/02_flow_egfr_uacr.csv
  chart_data/03_flow_background_subgroups.csv
  chart_data/04_select_soul_pooled.csv
  chart_data/05_flow_safety.csv
)

failed=0
for file in "${required[@]}"; do
  if [[ ! -s "$pack/$file" ]]; then
    echo "PRESENTATION_MISSING_OR_EMPTY $file" >&2
    failed=1
  fi
done

if [[ -s "$pack/SPEAKER_NOTES_ZH_TW.md" ]]; then
  slide_count="$(grep -Ec '^## Slide ([1-9]|1[0-9]|2[0-5])｜' "$pack/SPEAKER_NOTES_ZH_TW.md")"
  if [[ "$slide_count" -ne 25 ]]; then
    echo "PRESENTATION_BAD_SPEAKER_SLIDE_COUNT expected=25 actual=$slide_count" >&2
    failed=1
  fi
fi

if [[ -s "$pack/SLIDE_STORYBOARD_ZH_TW.md" ]]; then
  storyboard_count="$(grep -Ec '^\| ([1-9]|1[0-9]|2[0-5]) \|' "$pack/SLIDE_STORYBOARD_ZH_TW.md")"
  if [[ "$storyboard_count" -ne 25 ]]; then
    echo "PRESENTATION_BAD_STORYBOARD_COUNT expected=25 actual=$storyboard_count" >&2
    failed=1
  fi
fi

for article in "$project_root"/research/semaglutide_ckd_flow/2026-09-05/articles_zh_tw/0[1-5]_*.md; do
  if ! grep -q '^## 投影片用 reference 快速索引$' "$article"; then
    echo "PRESENTATION_ARTICLE_INDEX_MISSING ${article#"$project_root/"}" >&2
    failed=1
  fi
done

master="$project_root/research/semaglutide_ckd_flow/2026-09-05/16_FINAL_SYNTHESIS_ZH_TW.md"
series_readme="$project_root/research/semaglutide_ckd_flow/2026-09-05/articles_zh_tw/README.md"
if [[ -s "$master" ]]; then
  master_hash="$(/usr/bin/shasum -a 256 "$master" | awk '{print $1}')"
  master_short="${master_hash:0:8}…${master_hash: -6}"
  if ! grep -q "$master_hash" "$series_readme"; then
    echo "PRESENTATION_STALE_MASTER_HASH articles_zh_tw/README.md" >&2
    failed=1
  fi
  for article in "$project_root"/research/semaglutide_ckd_flow/2026-09-05/articles_zh_tw/0[1-5]_*.md; do
    if ! grep -q "$master_short" "$article"; then
      echo "PRESENTATION_STALE_MASTER_HASH ${article#"$project_root/"}" >&2
      failed=1
    fi
  done
fi

expected_image_hash="6ae529d670dee31eb7ca67d6893b9d613a70c295da9124023d30e3d59b79c9a6"
if [[ -s "$pack/public_assets/FLOW_CKDSEVERITY_Mahaffey_Figure2.jpg" ]]; then
  actual_image_hash="$(/usr/bin/shasum -a 256 "$pack/public_assets/FLOW_CKDSEVERITY_Mahaffey_Figure2.jpg" | awk '{print $1}')"
  if [[ "$actual_image_hash" != "$expected_image_hash" ]]; then
    echo "PRESENTATION_PUBLIC_ASSET_HASH_MISMATCH" >&2
    failed=1
  fi
fi

if grep -HnE 'Table 3[^[:cntrl:]]*(journal |NEJM )?p\.117' \
  "$pack/SPEAKER_NOTES_ZH_TW.md" \
  "$pack/SLIDE_STORYBOARD_ZH_TW.md" \
  "$pack/ARTICLE_REFERENCE_GUIDE.md"; then
  echo "PRESENTATION_STALE_TABLE3_LOCATOR" >&2
  failed=1
fi

if grep -HnE 'FLOW-SUPPLEMENT-2024[^[:cntrl:]]*pp?\. ?15[–-]16' \
  "$pack/SPEAKER_NOTES_ZH_TW.md" \
  "$pack/SLIDE_STORYBOARD_ZH_TW.md" \
  "$pack/ARTICLE_REFERENCE_GUIDE.md"; then
  echo "PRESENTATION_STALE_INTERIM_LOCATOR expected=PDF_pp.16-17" >&2
  failed=1
fi

if grep -Hn 'EMA-OZEMPIC-SMPC-2025' "$pack/SLIDE_STORYBOARD_ZH_TW.md"; then
  echo "PRESENTATION_STALE_EMA_SOURCE_ID" >&2
  failed=1
fi

if ! grep -Fq 'total eGFR slope' "$pack/FIGURE_TABLE_SOURCE_MAP.md" || \
   ! grep -F 'total eGFR slope' "$pack/FIGURE_TABLE_SOURCE_MAP.md" | grep -Fq 'Fig.1D' || \
   ! grep -F '**MACE**' "$pack/FIGURE_TABLE_SOURCE_MAP.md" | grep -Fq 'Fig.1E' || \
   ! grep -F '**全因死亡**' "$pack/FIGURE_TABLE_SOURCE_MAP.md" | grep -Fq 'Fig.1F'; then
  echo "PRESENTATION_BAD_FLOW_FIGURE1_PANEL_MAP" >&2
  failed=1
fi

safety_csv="$pack/chart_data/05_flow_safety.csv"
if ! grep -Fq '"serious-AE preferred-term dehydration",10,0.6,10,0.6' "$safety_csv" || \
   ! grep -F '"serious-AE preferred-term acute kidney injury"' "$safety_csv" | grep -Fq 'PDF p.29' || \
   ! grep -F '"serious-AE preferred-term dehydration"' "$safety_csv" | grep -Fq 'PDF p.30' || \
   ! grep -F '"severe hypoglycemia participants"' "$safety_csv" | grep -Fq 'Table 3; NEJM p.120; local PDF p.12'; then
  echo "PRESENTATION_BAD_FLOW_SAFETY_DATA_OR_LOCATOR" >&2
  failed=1
fi

if [[ "$failed" -ne 0 ]]; then
  exit 1
fi

echo "PRESENTATION_PACK_QA_PASS"
