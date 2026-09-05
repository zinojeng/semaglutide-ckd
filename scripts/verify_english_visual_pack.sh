#!/usr/bin/env bash
set -euo pipefail

project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
pack_rel="research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw"
pack="$project_root/$pack_rel"
english_dir="$pack/public_assets/redrawn_en"
manifest="$english_dir/MANIFEST.json"
generator="$project_root/scripts/generate_presentation_visuals_en.py"
source_dir="$pack/public_assets/source_figures"
attribution="$source_dir/ATTRIBUTION.md"
private_rel="research/semaglutide_ckd_flow/2026-09-05/sources/retrieved/cache/presentation_assets/source_pages"
private_dir="$project_root/$private_rel"

failed=0

for required in "$generator" "$manifest" "$attribution"; do
  if [[ ! -s "$required" ]]; then
    echo "ENGLISH_VISUAL_MISSING_OR_EMPTY ${required#"$project_root/"}" >&2
    failed=1
  fi
done

if [[ "$failed" -eq 0 ]]; then
  if ! python3 - "$project_root" "$english_dir" "$manifest" "$generator" "$source_dir" "$attribution" <<'PY'
from __future__ import annotations

import hashlib
import html
import json
import re
import struct
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


root = Path(sys.argv[1]).resolve()
english_dir = Path(sys.argv[2]).resolve()
manifest_path = Path(sys.argv[3]).resolve()
generator_path = Path(sys.argv[4]).resolve()
source_dir = Path(sys.argv[5]).resolve()
attribution_path = Path(sys.argv[6]).resolve()

expected_stems = (
    "01_flow_endpoints_forest_en",
    "02_flow_egfr_phases_en",
    "03_flow_sglt2_subgroup_forest_en",
    "04_flow_mra_subgroup_forest_en",
    "05_select_soul_pooled_context_en",
    "06_flow_safety_dotplot_en",
)
expected_names = {"MANIFEST.json"}
for stem in expected_stems:
    expected_names.add(f"{stem}.svg")
    expected_names.add(f"{stem}@2x.png")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def assert_no_trailing_whitespace(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    for line_number, line in enumerate(text.splitlines(), 1):
        if line.endswith((" ", "\t")):
            raise ValueError(f"trailing whitespace: {path.name}:{line_number}")
    return text


def png_dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        if handle.read(8) != b"\x89PNG\r\n\x1a\n":
            raise ValueError(f"not a PNG: {path.name}")
        length = struct.unpack(">I", handle.read(4))[0]
        if handle.read(4) != b"IHDR" or length != 13:
            raise ValueError(f"bad PNG header: {path.name}")
        return struct.unpack(">II", handle.read(8))


def jpeg_dimensions(path: Path) -> tuple[int, int]:
    sof_markers = {
        0xC0,
        0xC1,
        0xC2,
        0xC3,
        0xC5,
        0xC6,
        0xC7,
        0xC9,
        0xCA,
        0xCB,
        0xCD,
        0xCE,
        0xCF,
    }
    with path.open("rb") as handle:
        if handle.read(2) != b"\xff\xd8":
            raise ValueError(f"not a JPEG: {path.name}")
        while True:
            marker_start = handle.read(1)
            if not marker_start:
                break
            if marker_start != b"\xff":
                continue
            marker_byte = handle.read(1)
            while marker_byte == b"\xff":
                marker_byte = handle.read(1)
            if not marker_byte:
                break
            marker = marker_byte[0]
            if marker in {0x01, 0xD8, 0xD9} or 0xD0 <= marker <= 0xD7:
                continue
            length_bytes = handle.read(2)
            if len(length_bytes) != 2:
                break
            segment_length = struct.unpack(">H", length_bytes)[0]
            if segment_length < 2:
                raise ValueError(f"bad JPEG segment: {path.name}")
            if marker in sof_markers:
                payload = handle.read(5)
                if len(payload) != 5:
                    break
                height, width = struct.unpack(">HH", payload[1:])
                return width, height
            handle.seek(segment_length - 2, 1)
    raise ValueError(f"JPEG dimensions not found: {path.name}")


cjk_pattern = re.compile(
    "["
    "\u2e80-\u2fff"
    "\u3000-\u303f"
    "\u3040-\u30ff"
    "\u3100-\u312f"
    "\u31a0-\u31bf"
    "\u31c0-\u31ef"
    "\u3400-\u4dbf"
    "\u4e00-\u9fff"
    "\uf900-\ufaff"
    "\uac00-\ud7af"
    "]"
)


actual_entries = {path.name for path in english_dir.iterdir()}
if actual_entries != expected_names:
    missing = sorted(expected_names - actual_entries)
    extra = sorted(actual_entries - expected_names)
    raise ValueError(f"English asset set mismatch: missing={missing}, extra={extra}")
for path in english_dir.iterdir():
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"English asset must be a regular file: {path.name}")

manifest_text = assert_no_trailing_whitespace(manifest_path)
manifest = json.loads(manifest_text)
if manifest.get("language") != "English":
    raise ValueError("manifest language is not English")
if manifest.get("generator") != "scripts/generate_presentation_visuals_en.py":
    raise ValueError("manifest generator path is unexpected")
outputs = manifest.get("outputs")
if not isinstance(outputs, list) or len(outputs) != 6:
    raise ValueError(f"manifest must contain six outputs, found {len(outputs or [])}")
if [item.get("stem") for item in outputs] != list(expected_stems):
    raise ValueError("manifest stems/order do not match the six locked English visuals")

svg_comments: dict[str, str] = {}
for item in outputs:
    stem = item["stem"]
    expected_rel = {
        "svg": f"research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn_en/{stem}.svg",
        "png": f"research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw/public_assets/redrawn_en/{stem}@2x.png",
    }
    for kind, rel in expected_rel.items():
        if item.get(kind) != rel:
            raise ValueError(f"unexpected manifest path for {stem} {kind}: {item.get(kind)!r}")
        path = (root / rel).resolve()
        if english_dir not in path.parents or path.is_symlink() or not path.is_file():
            raise ValueError(f"invalid {kind} asset: {rel}")
        expected_hash = item.get(f"{kind}_sha256")
        if not re.fullmatch(r"[0-9a-f]{64}", str(expected_hash)):
            raise ValueError(f"invalid manifest hash for {rel}")
        if digest(path) != expected_hash:
            raise ValueError(f"manifest hash mismatch: {rel}")

    png_path = root / expected_rel["png"]
    dimensions = png_dimensions(png_path)
    if dimensions != (3840, 2160) or item.get("png_pixels") != [3840, 2160]:
        raise ValueError(f"bad English PNG dimensions: {png_path.name} {dimensions}")

    svg_path = root / expected_rel["svg"]
    svg_text = assert_no_trailing_whitespace(svg_path)
    if cjk_pattern.search(svg_text):
        raise ValueError(f"CJK character found in English SVG: {svg_path.name}")
    if re.search(r"<!ENTITY", svg_text, flags=re.IGNORECASE):
        raise ValueError(f"entity declaration found in SVG: {svg_path.name}")
    doctypes = re.findall(r"<!DOCTYPE.*?>", svg_text, flags=re.IGNORECASE | re.DOTALL)
    allowed_doctype = (
        '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" '
        '"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">'
    )
    if len(doctypes) > 1 or (
        doctypes and re.sub(r"\s+", " ", doctypes[0]).strip() != allowed_doctype
    ):
        raise ValueError(f"unexpected SVG doctype: {svg_path.name}")
    tree = ET.parse(svg_path)
    if tree.getroot().tag.rsplit("}", 1)[-1] != "svg":
        raise ValueError(f"unexpected SVG root: {svg_path.name}")
    for element in tree.iter():
        local_tag = element.tag.rsplit("}", 1)[-1]
        if local_tag in {"script", "foreignObject", "image"}:
            raise ValueError(f"unsafe SVG element {local_tag}: {svg_path.name}")
        for raw_name, value in element.attrib.items():
            name = raw_name.rsplit("}", 1)[-1].lower()
            lowered = value.lower().strip()
            if name.startswith("on"):
                raise ValueError(f"SVG event handler {name}: {svg_path.name}")
            if "javascript:" in lowered or "data:" in lowered:
                raise ValueError(f"unsafe SVG URI: {svg_path.name}")
            if name == "href" and not value.startswith("#"):
                raise ValueError(f"external SVG href: {svg_path.name}")
    comments = " ".join(re.findall(r"<!--(.*?)-->", svg_text, flags=re.DOTALL))
    svg_comments[stem] = re.sub(r"\s+", " ", html.unescape(comments)).strip()

generator_text = assert_no_trailing_whitespace(generator_path)
if cjk_pattern.search(generator_text):
    raise ValueError("CJK character found in English visual generator")
if cjk_pattern.search(manifest_text):
    raise ValueError("CJK character found in English manifest")

required_phrases = {
    "01_flow_endpoints_forest_en": (
        "Primary outcome: major kidney disease events — no. (%)†",
        "Composite of kidney-specific components of the primary outcome",
        "Persistent ≥50% reduction from baseline in eGFR",
        "Hazard Ratio (95% CI)",
        "Semaglutide Better",
        "Placebo Better",
        "Project transcription of †:",
        "endpoint components include kidney failure, persistent ≥50% eGFR reduction, kidney death, or cardiovascular death",
        "Table 2 footnote, p.117.",
    ),
    "02_flow_egfr_phases_en": (
        "Mean change in eGFR from baseline to week 12",
        "Mean annual rate of change in eGFR from week 12 to end of trial",
        "Mean annual rate of change in eGFR",
        "Estimated Difference (95% CI)",
    ),
    "03_flow_sglt2_subgroup_forest_en": (
        "Composite renal event (primary endpoint)",
        "Kidney-specific, four-component outcome",
        "50% reduction in eGFR",
        "SGLT2i: Yes",
        "SGLT2i: No",
        "Favors semaglutide 1.0 mg",
        "Favors placebo",
    ),
    "04_flow_mra_subgroup_forest_en": (
        "Composite kidney event (composite primary end point)",
        "Four-component kidney-specific composite outcome",
        "Renal replacement therapy",
        "MRA use at baseline: Yes",
        "MRA use at baseline: No",
        "Favors semaglutide 1.0 mg",
        "Favors placebo",
    ),
    "05_select_soul_pooled_context_en": (
        "Time to first occurrence of the main 5-component kidney composite endpointᵃ.",
        "Total eGFR slope",
        "First 5-point composite kidney event",
        "First 4-point composite kidney event",
        "Annual rate of change in eGFR",
        "primary kidney composite",
        "a narrower secondary kidney composite (excluding cardiovascular-related death from the primary outcome)",
    ),
    "06_flow_safety_dotplot_en": (
        "Serious adverse event",
        "Adverse events leading to permanent trial product discontinuation",
        "Gastrointestinal disorders",
        "Acute kidney injury",
        "Dehydration",
        "Severe hypoglycemia*",
        "Diabetic retinopathy*",
        "No. of participants (%)",
        "Data were from an additional data-collection form",
        "FLOW-PRIMARY-2024, Table 3, NEJM p.120",
        "Table 3 footnote, p.120.",
    ),
}
for stem, phrases in required_phrases.items():
    rendered_text = svg_comments[stem]
    for phrase in phrases:
        if phrase not in rendered_text:
            raise ValueError(f"required locked phrase absent from {stem}.svg: {phrase!r}")

source_expectations = {
    "FLOW_SGLT2_Mann_2024_Figure1.jpg": (
        "763d5c86292cac8bf8a92b4e544ec743fe3f62156fb2a9bb19af351029f4a1eb",
        (679, 845),
    ),
    "FLOW_SGLT2_Mann_2024_Figure2.jpg": (
        "d7d341281b473522b8ba830ff26779c7b335923ddbb547e944b47ddcf5743110",
        (722, 799),
    ),
    "FLOW_SGLT2_Mann_2024_Figure3.jpg": (
        "33d1b35ca01d69aeade75b8ef565d94b493f9fb33d361753414f770cec89e9c3",
        (722, 656),
    ),
    "SELECT_KIDNEY_Colhoun_2024_Figure1_KM.png": (
        "3c59c3ea870f76e2898cb5a9d76c1b9faf3da5c718d713a2186dd11055e11bfa",
        (2280, 3330),
    ),
}
for name, (expected_hash, expected_dimensions) in source_expectations.items():
    path = source_dir / name
    if path.is_symlink() or not path.is_file() or path.stat().st_size == 0:
        raise ValueError(f"missing official public source figure: {name}")
    if digest(path) != expected_hash:
        raise ValueError(f"official source figure hash mismatch: {name}")
    dimensions = png_dimensions(path) if path.suffix.lower() == ".png" else jpeg_dimensions(path)
    if dimensions != expected_dimensions:
        raise ValueError(f"official source figure dimensions mismatch: {name} {dimensions}")

attribution_text = assert_no_trailing_whitespace(attribution_path)
global_attribution_phrases = (
    "CC BY 4.0",
    "https://creativecommons.org/licenses/by/4.0/",
    "10.1038/s41591-024-03133-0",
    "PMC11485243",
    "10.1038/s41591-024-03015-5",
    "PMC11271413",
    "**Changes:** none",
    "crop only",
    "published image displays 231 placebo events",
    "strata sum to 213",
    "Do not silently edit it",
)
for phrase in global_attribution_phrases:
    if phrase not in attribution_text:
        raise ValueError(f"CC BY attribution is incomplete: missing {phrase!r}")
for name, (expected_hash, expected_dimensions) in source_expectations.items():
    width, height = expected_dimensions
    for phrase in (name, expected_hash, f"{width:,} x {height:,}"):
        if phrase not in attribution_text:
            raise ValueError(f"source-figure attribution missing {phrase!r}")
source_locators = {
    "FLOW_SGLT2_Mann_2024_Figure1.jpg": "Figure 1, journal p.2851",
    "FLOW_SGLT2_Mann_2024_Figure2.jpg": "Figure 2, journal p.2852",
    "FLOW_SGLT2_Mann_2024_Figure3.jpg": "Figure 3, journal p.2853",
    "SELECT_KIDNEY_Colhoun_2024_Figure1_KM.png": "Figure 1, journal p.2059 / publisher PDF p.2",
}
for name, locator in source_locators.items():
    if locator not in attribution_text:
        raise ValueError(f"source-figure attribution missing locator for {name}: {locator!r}")
PY
  then
    echo "ENGLISH_VISUAL_ASSET_OR_MANIFEST_INVALID" >&2
    failed=1
  fi
fi

if git -C "$project_root" ls-files -- "$private_rel" "$private_rel/*" "$private_rel/**" | grep -q .; then
  echo "ENGLISH_VISUAL_PRIVATE_SOURCE_PAGE_TRACKED" >&2
  failed=1
fi

if ! git -C "$project_root" check-ignore -q -- "$private_rel/.english-visual-qa-probe"; then
  echo "ENGLISH_VISUAL_PRIVATE_SOURCE_DIRECTORY_NOT_IGNORED" >&2
  failed=1
fi

if [[ -d "$private_dir" ]]; then
  while IFS= read -r -d '' private_asset; do
    private_asset_rel="${private_asset#"$project_root/"}"
    if ! git -C "$project_root" check-ignore -q -- "$private_asset_rel"; then
      echo "ENGLISH_VISUAL_PRIVATE_SOURCE_PAGE_NOT_IGNORED $private_asset_rel" >&2
      failed=1
    fi
  done < <(find "$private_dir" \( -type f -o -type l \) -print0)
fi

temp_base="${TMPDIR:-/tmp}"
temp_base="${temp_base%/}"
regen_dir="$(mktemp -d "$temp_base/semaglutide-ckd-english-visual-qa.XXXXXX")"
cleanup_regen() {
  case "$regen_dir" in
    "$temp_base"/semaglutide-ckd-english-visual-qa.*)
      rm -rf -- "$regen_dir"
      ;;
    *)
      echo "ENGLISH_VISUAL_REFUSED_UNSAFE_TEMP_CLEANUP $regen_dir" >&2
      ;;
  esac
}
trap cleanup_regen EXIT

if [[ -s "$generator" && -s "$manifest" ]]; then
  if ! python3 "$generator" --output-dir "$regen_dir" --manifest "$regen_dir/MANIFEST.json" >/dev/null; then
    echo "ENGLISH_VISUAL_REGENERATION_FAILED" >&2
    failed=1
  elif ! python3 - "$project_root" "$english_dir" "$manifest" "$regen_dir" <<'PY'
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


root = Path(sys.argv[1]).resolve()
published_dir = Path(sys.argv[2]).resolve()
published_manifest_path = Path(sys.argv[3]).resolve()
regen_dir = Path(sys.argv[4]).resolve()
regen_manifest_path = regen_dir / "MANIFEST.json"

published = json.loads(published_manifest_path.read_text(encoding="utf-8"))
regenerated = json.loads(regen_manifest_path.read_text(encoding="utf-8"))
published_by_stem = {item["stem"]: item for item in published["outputs"]}
regen_by_stem = {item["stem"]: item for item in regenerated["outputs"]}
if set(published_by_stem) != set(regen_by_stem):
    raise SystemExit("regenerated manifest stems differ")
expected_regen_names = {"MANIFEST.json"}
for stem in published_by_stem:
    expected_regen_names.update({f"{stem}.svg", f"{stem}@2x.png"})
actual_regen_names = {path.name for path in regen_dir.iterdir()}
if actual_regen_names != expected_regen_names:
    raise SystemExit(
        "regenerated file set differs: "
        f"missing={sorted(expected_regen_names - actual_regen_names)} "
        f"extra={sorted(actual_regen_names - expected_regen_names)}"
    )

for stem, published_item in published_by_stem.items():
    regenerated_item = regen_by_stem[stem]
    for kind, suffix in (("svg", ".svg"), ("png", "@2x.png")):
        published_path = (root / published_item[kind]).resolve()
        regenerated_path = regen_dir / f"{stem}{suffix}"
        if not regenerated_path.is_file():
            raise SystemExit(f"missing regenerated asset: {regenerated_path.name}")
        published_bytes = published_path.read_bytes()
        regenerated_bytes = regenerated_path.read_bytes()
        if published_bytes != regenerated_bytes:
            raise SystemExit(f"nondeterministic or stale English asset: {regenerated_path.name}")
        actual_hash = hashlib.sha256(regenerated_bytes).hexdigest()
        if regenerated_item.get(f"{kind}_sha256") != actual_hash:
            raise SystemExit(f"regenerated manifest hash mismatch: {regenerated_path.name}")

metadata_keys = (
    "generator",
    "language",
    "label_policy",
    "evidence_cutoff",
    "generated_for_release",
    "canvas_inches",
    "preview_dpi",
    "png_dpi",
    "png_default_for_slides",
    "source_data",
    "chart_contracts",
)
for key in metadata_keys:
    if published.get(key) != regenerated.get(key):
        raise SystemExit(f"regenerated manifest metadata mismatch: {key}")
PY
  then
    echo "ENGLISH_VISUAL_NONDETERMINISTIC_OR_STALE" >&2
    failed=1
  fi
fi

cleanup_regen
trap - EXIT

if ! git -C "$project_root" diff --check -- scripts/verify_english_visual_pack.sh; then
  failed=1
fi

if [[ "$failed" -ne 0 ]]; then
  exit 1
fi

echo "ENGLISH_VISUAL_PACK_QA_PASS"
