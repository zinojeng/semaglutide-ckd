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
  VISUAL_ASSET_CATALOG_ZH_TW.md
  VISUAL_RIGHTS_GUIDE.md
  PRIVATE_ASSET_MANIFEST.md
  public_assets/ATTRIBUTION.md
  public_assets/FLOW_CKDSEVERITY_Mahaffey_Figure2.jpg
  public_assets/source_figures/ATTRIBUTION.md
  public_assets/source_figures/SELECT_KIDNEY_Colhoun_2024_Figure1_KM.png
  public_assets/redrawn/MANIFEST.json
  public_assets/redrawn/01_flow_endpoints_forest_zh_tw.svg
  public_assets/redrawn/01_flow_endpoints_forest_zh_tw@2x.png
  public_assets/redrawn/02_flow_egfr_phases_zh_tw.svg
  public_assets/redrawn/02_flow_egfr_phases_zh_tw@2x.png
  public_assets/redrawn/03_flow_sglt2_subgroup_forest_zh_tw.svg
  public_assets/redrawn/03_flow_sglt2_subgroup_forest_zh_tw@2x.png
  public_assets/redrawn/04_flow_mra_subgroup_forest_zh_tw.svg
  public_assets/redrawn/04_flow_mra_subgroup_forest_zh_tw@2x.png
  public_assets/redrawn/05_select_soul_pooled_context_zh_tw.svg
  public_assets/redrawn/05_select_soul_pooled_context_zh_tw@2x.png
  public_assets/redrawn/06_flow_safety_dotplot_zh_tw.svg
  public_assets/redrawn/06_flow_safety_dotplot_zh_tw@2x.png
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

if [[ ! -s "$project_root/scripts/generate_presentation_visuals.py" ]]; then
  echo "PRESENTATION_MISSING_OR_EMPTY scripts/generate_presentation_visuals.py" >&2
  failed=1
fi

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

expected_select_hash="3c59c3ea870f76e2898cb5a9d76c1b9faf3da5c718d713a2186dd11055e11bfa"
select_image="$pack/public_assets/source_figures/SELECT_KIDNEY_Colhoun_2024_Figure1_KM.png"
if [[ -s "$select_image" ]]; then
  actual_select_hash="$(/usr/bin/shasum -a 256 "$select_image" | awk '{print $1}')"
  if [[ "$actual_select_hash" != "$expected_select_hash" ]]; then
    echo "PRESENTATION_SELECT_ASSET_HASH_MISMATCH" >&2
    failed=1
  fi
  if ! python3 - "$select_image" <<'PY'
import struct
import sys
from pathlib import Path

path = Path(sys.argv[1])
with path.open("rb") as handle:
    if handle.read(8) != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("not PNG")
    length = struct.unpack(">I", handle.read(4))[0]
    if handle.read(4) != b"IHDR" or length != 13:
        raise SystemExit("bad PNG header")
    width, height = struct.unpack(">II", handle.read(8))
if (width, height) != (2280, 3330):
    raise SystemExit(f"unexpected dimensions {width}x{height}")
PY
  then
    echo "PRESENTATION_SELECT_ASSET_DIMENSIONS_INVALID" >&2
    failed=1
  fi
  select_attribution="$pack/public_assets/source_figures/ATTRIBUTION.md"
  for required_text in \
    '10.1038/s41591-024-03015-5' \
    'Figure 1' \
    'https://creativecommons.org/licenses/by/4.0/' \
    'crop only'; do
    if ! grep -Fqi "$required_text" "$select_attribution"; then
      echo "PRESENTATION_SELECT_ATTRIBUTION_INCOMPLETE missing=$required_text" >&2
      failed=1
    fi
  done
fi

if [[ -s "$pack/public_assets/redrawn/MANIFEST.json" ]]; then
  if ! python3 - "$project_root" "$pack/public_assets/redrawn/MANIFEST.json" <<'PY'
import hashlib
import json
import struct
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

root = Path(sys.argv[1]).resolve()
manifest_path = Path(sys.argv[2]).resolve()
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
outputs = manifest.get("outputs", [])
if len(outputs) != 6:
    raise SystemExit(f"expected 6 redrawn outputs, found {len(outputs)}")

for item in outputs:
    for kind in ("svg", "png"):
        rel = item.get(kind, "")
        path = (root / rel).resolve()
        if root not in path.parents or not path.is_file():
            raise SystemExit(f"invalid or missing {kind}: {rel}")
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != item.get(f"{kind}_sha256"):
            raise SystemExit(f"hash mismatch: {rel}")

    png = (root / item["png"]).resolve()
    with png.open("rb") as handle:
        if handle.read(8) != b"\x89PNG\r\n\x1a\n":
            raise SystemExit(f"not PNG: {item['png']}")
        length = struct.unpack(">I", handle.read(4))[0]
        if handle.read(4) != b"IHDR" or length != 13:
            raise SystemExit(f"bad PNG header: {item['png']}")
        width, height = struct.unpack(">II", handle.read(8))
    if [width, height] != item.get("png_pixels") or (width, height) != (3840, 2160):
        raise SystemExit(f"bad PNG dimensions: {item['png']} {width}x{height}")

    svg = (root / item["svg"]).resolve()
    tree = ET.parse(svg)
    for element in tree.iter():
        local_tag = element.tag.rsplit("}", 1)[-1]
        if local_tag in {"script", "foreignObject", "image"}:
            raise SystemExit(f"unsafe SVG element {local_tag}: {item['svg']}")
        for name, value in element.attrib.items():
            if "javascript:" in value.lower():
                raise SystemExit(f"unsafe SVG javascript URI: {item['svg']}")
            if name.rsplit("}", 1)[-1] == "href" and not value.startswith("#"):
                raise SystemExit(f"external or embedded SVG href: {item['svg']}")
PY
  then
    echo "PRESENTATION_REDRAW_MANIFEST_OR_ASSET_INVALID" >&2
    failed=1
  fi
fi

if [[ "${PRESENTATION_REGENERATE_QA:-0}" == "1" ]]; then
  regen_dir="$(mktemp -d "${TMPDIR:-/tmp}/semaglutide-ckd-redraw-qa.XXXXXX")"
  cleanup_regen() {
    rm -rf -- "$regen_dir"
  }
  trap cleanup_regen EXIT
  if ! python3 "$project_root/scripts/generate_presentation_visuals.py" \
      --output-dir "$regen_dir" \
      --manifest "$regen_dir/MANIFEST.json" >/dev/null; then
    echo "PRESENTATION_REDRAW_REGENERATION_FAILED" >&2
    failed=1
  else
    for generated in \
      01_flow_endpoints_forest_zh_tw.svg \
      01_flow_endpoints_forest_zh_tw@2x.png \
      02_flow_egfr_phases_zh_tw.svg \
      02_flow_egfr_phases_zh_tw@2x.png \
      03_flow_sglt2_subgroup_forest_zh_tw.svg \
      03_flow_sglt2_subgroup_forest_zh_tw@2x.png \
      04_flow_mra_subgroup_forest_zh_tw.svg \
      04_flow_mra_subgroup_forest_zh_tw@2x.png \
      05_select_soul_pooled_context_zh_tw.svg \
      05_select_soul_pooled_context_zh_tw@2x.png \
      06_flow_safety_dotplot_zh_tw.svg \
      06_flow_safety_dotplot_zh_tw@2x.png; do
      if ! cmp -s "$regen_dir/$generated" "$pack/public_assets/redrawn/$generated"; then
        echo "PRESENTATION_REDRAW_NONDETERMINISTIC_OR_STALE $generated" >&2
        failed=1
      fi
    done
  fi
  cleanup_regen
  trap - EXIT
fi

private_count="$(grep -Ec '^\| `[^`]+\.png` \|' "$pack/PRIVATE_ASSET_MANIFEST.md" || true)"
if [[ "$private_count" -ne 20 ]]; then
  echo "PRESENTATION_PRIVATE_MANIFEST_COUNT expected=20 actual=$private_count" >&2
  failed=1
fi

private_dir="$project_root/research/semaglutide_ckd_flow/2026-09-05/sources/retrieved/cache/presentation_assets/source_pages"
if [[ -d "$private_dir" ]]; then
  if ! python3 - "$project_root" "$pack/PRIVATE_ASSET_MANIFEST.md" "$private_dir" <<'PY'
import hashlib
import re
import subprocess
import sys
from pathlib import Path

root = Path(sys.argv[1]).resolve()
manifest = Path(sys.argv[2]).read_text(encoding="utf-8")
private_dir = Path(sys.argv[3]).resolve()
entries = dict(re.findall(r"^\| `([^`]+\.png)` \| `([0-9a-f]{64})` \|", manifest, re.MULTILINE))
actual_files = {path.name: path for path in private_dir.glob("*.png") if path.is_file()}
if len(entries) != 20 or set(entries) != set(actual_files):
    missing = sorted(set(entries) - set(actual_files))
    extra = sorted(set(actual_files) - set(entries))
    raise SystemExit(f"private asset set mismatch missing={missing} extra={extra}")
for name, expected in entries.items():
    path = actual_files[name]
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        raise SystemExit(f"private asset hash mismatch: {name}")
    rel = path.relative_to(root)
    result = subprocess.run(
        ["git", "-C", str(root), "check-ignore", "-q", "--", str(rel)],
        check=False,
    )
    if result.returncode != 0:
        raise SystemExit(f"private asset is not gitignored: {rel}")
PY
  then
    echo "PRESENTATION_PRIVATE_MANIFEST_OR_ASSET_INVALID" >&2
    failed=1
  fi
fi

if git -C "$project_root" ls-files -- 'research/*/sources/retrieved/cache/presentation_assets/source_pages/*' | grep -q .; then
  echo "PRESENTATION_PRIVATE_SOURCE_IMAGE_TRACKED" >&2
  failed=1
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

subgroup_csv="$pack/chart_data/03_flow_background_subgroups.csv"
for expected_counts in \
  '使用者 41/277 vs 38/273；未使用者 290/1490 vs 372/1493' \
  '使用者 32/277 vs 27/273；未使用者 186/1490 vs 233/1493' \
  '使用者 30/277 vs 23/273；未使用者 135/1489 vs 190/1493'; do
  if ! grep -Fq "$expected_counts" "$subgroup_csv"; then
    echo "PRESENTATION_BAD_SGLT2_EVENT_COUNTS missing=$expected_counts" >&2
    failed=1
  fi
done

context_csv="$pack/chart_data/04_select_soul_pooled.csv"
if ! grep -F 'SELECT,' "$context_csv" | grep -Fq 'P 值未校正多重比較'; then
  echo "PRESENTATION_SELECT_MULTIPLICITY_CAVEAT_MISSING" >&2
  failed=1
fi
if grep -Fi 'component' "$context_csv" | grep -Eqi 'unverified|not verified|未核|未驗|未列'; then
  echo "PRESENTATION_STALE_POOLED_ENDPOINT_UNVERIFIED_CLAIM" >&2
  failed=1
fi

if [[ "$failed" -ne 0 ]]; then
  exit 1
fi

echo "PRESENTATION_PACK_QA_PASS"
