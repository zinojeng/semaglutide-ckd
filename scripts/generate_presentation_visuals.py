#!/usr/bin/env python3
"""Generate public-safe, original presentation visuals from verified project data.

The script reads the five reviewed CSV files in ``presentation_zh_tw/chart_data``
and writes 16:9 SVG plus 2x PNG assets.  It intentionally does not reproduce any
publisher layout, table, or figure.  A small number of annotations that are not
present in the CSVs (for example, the post hoc cystatin-C SGLT2i estimate and MRA
composition) are copied from the project's audited numeric source maps; their
source IDs and exact locators are embedded in the corresponding figure.

Run from anywhere:

    python3 scripts/generate_presentation_visuals.py
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
from typing import Mapping, Sequence

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.ticker import FixedLocator, FuncFormatter, NullFormatter


REPO_ROOT = Path(__file__).resolve().parents[1]
PACK_DIR = REPO_ROOT / "research/semaglutide_ckd_flow/2026-09-05/presentation_zh_tw"
DATA_DIR = PACK_DIR / "chart_data"
DEFAULT_OUTPUT_DIR = PACK_DIR / "public_assets/redrawn"
SLIDE_WIDTH_IN = 40 / 3
SLIDE_HEIGHT_IN = 7.5
PREVIEW_DPI = 144
PNG_DPI = 288

CANVAS = "#FFFFFF"
PANEL = "#F7F9FC"
INK = "#172B4D"
MUTED = "#5B6577"
GRID = "#D8DEE8"
GRID_DARK = "#AAB4C3"
BLUE = "#1565C0"
BLUE_DARK = "#0B3D91"
BLUE_LIGHT = "#DCEBFA"
ORANGE = "#E67E22"
ORANGE_DARK = "#A94B00"
ORANGE_LIGHT = "#FCE8D5"
NEUTRAL = "#7A8494"
NEUTRAL_LIGHT = "#E9EDF3"

FONT_FAMILY = "Arial Unicode MS"

plt.rcParams.update(
    {
        "font.family": FONT_FAMILY,
        "font.size": 12,
        "text.color": INK,
        "axes.labelcolor": INK,
        "axes.edgecolor": GRID_DARK,
        "axes.titlecolor": INK,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "axes.unicode_minus": False,
        "svg.fonttype": "path",
        "svg.hashsalt": "semaglutide-ckd-2026-09-06",
        "savefig.facecolor": CANVAS,
        "figure.facecolor": CANVAS,
    }
)


def read_rows(filename: str) -> list[dict[str, str]]:
    path = DATA_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Missing verified chart data: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def number(value: str | float | int) -> float:
    if isinstance(value, (int, float)):
        return float(value)
    return float(value.strip().replace("+", ""))


def parse_ci(value: str) -> tuple[float, float]:
    cleaned = value.strip().replace("−", "-").replace("–", "-")
    left, right = cleaned.split("-", 1)
    return float(left.strip()), float(right.strip())


def rounded_box(
    target,
    x: float,
    y: float,
    w: float,
    h: float,
    *,
    facecolor: str = PANEL,
    edgecolor: str = GRID,
    linewidth: float = 1.2,
    radius: float = 0.02,
    transform=None,
    zorder: float = 0,
) -> FancyBboxPatch:
    if transform is None:
        transform = target.transAxes
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        transform=transform,
        boxstyle=f"round,pad=0.008,rounding_size={radius}",
        facecolor=facecolor,
        edgecolor=edgecolor,
        linewidth=linewidth,
        clip_on=False,
        zorder=zorder,
    )
    target.add_artist(patch)
    return patch


def new_figure(title: str, subtitle: str, *, tag: str = "原始數據重繪"):
    fig = plt.figure(figsize=(SLIDE_WIDTH_IN, SLIDE_HEIGHT_IN), dpi=PREVIEW_DPI, facecolor=CANVAS)
    fig.text(0.055, 0.955, title, ha="left", va="top", fontsize=28, fontweight="bold", color=INK)
    fig.text(0.055, 0.892, subtitle, ha="left", va="top", fontsize=15, color=MUTED)
    fig.text(
        0.948,
        0.948,
        tag,
        ha="right",
        va="top",
        fontsize=10,
        color=BLUE_DARK,
        bbox=dict(boxstyle="round,pad=0.42", facecolor=BLUE_LIGHT, edgecolor="none"),
    )
    return fig


def add_footer(fig, source: str, note: str | None = None) -> None:
    if note:
        fig.text(0.055, 0.070, note, ha="left", va="bottom", fontsize=11, color=INK)
    fig.text(0.055, 0.030, source, ha="left", va="bottom", fontsize=10, color=MUTED)


def save_figure(fig, output_dir: Path, stem: str) -> dict[str, object]:
    output_dir.mkdir(parents=True, exist_ok=True)
    svg = output_dir / f"{stem}.svg"
    png = output_dir / f"{stem}@2x.png"
    fig.savefig(
        svg,
        format="svg",
        dpi=100,
        metadata={"Creator": "semaglutide-ckd reproducible chart generator", "Date": "2026-09-06"},
    )
    # Matplotlib emits trailing spaces on many SVG path lines.  Normalize them
    # so generated assets pass Git's whitespace checks without changing the
    # rendered geometry; always retain exactly one final newline.
    svg_text = svg.read_text(encoding="utf-8")
    svg.write_text(
        "\n".join(line.rstrip() for line in svg_text.splitlines()) + "\n",
        encoding="utf-8",
    )
    fig.savefig(
        png,
        format="png",
        dpi=PNG_DPI,
        metadata={"Software": "semaglutide-ckd reproducible chart generator"},
    )
    plt.close(fig)

    def manifest_reference(path: Path) -> str:
        """Use repo-relative paths for release, filenames for external QA runs."""
        try:
            return str(path.relative_to(REPO_ROOT))
        except ValueError:
            return path.name

    return {
        "stem": stem,
        "svg": manifest_reference(svg),
        "png": manifest_reference(png),
        "svg_sha256": hashlib.sha256(svg.read_bytes()).hexdigest(),
        "png_sha256": hashlib.sha256(png.read_bytes()).hexdigest(),
        "png_pixels": [3840, 2160],
    }


def chart_flow_endpoints(output_dir: Path) -> dict[str, object]:
    rows = {int(row["display_order"]): row for row in read_rows("01_flow_primary_outcomes.csv")}
    ordered = [rows[i] for i in (1, 7, 2, 3, 4, 5, 6)]
    labels = [
        "五項主要複合（含 CV death）",
        "四項腎臟複合（排除 CV death）",
        "持續 ≥50% eGFR 下降",
        "持續 eGFR <15",
        "開始慢性 KRT",
        "腎因性死亡",
        "CV death",
    ]
    status = [
        "確認性主要終點",
        "支持性；確認性階層外",
        "個別組成；支持性",
        "個別組成；CI 跨 1",
        "個別組成；CI 跨 1",
        "個別組成；事件極少",
        "個別組成；支持性",
    ]
    y_positions = list(reversed(range(len(ordered))))

    fig = new_figure(
        "FLOW：主要、腎臟專屬終點與個別組成",
        "五項＝四個腎臟項目＋CV death；四項＝排除 CV death。HR <1 偏向 semaglutide。",
    )
    gs = fig.add_gridspec(
        1,
        3,
        left=0.055,
        right=0.955,
        bottom=0.16,
        top=0.78,
        width_ratios=[3.25, 2.55, 1.85],
        wspace=0.04,
    )
    ax_label = fig.add_subplot(gs[0, 0])
    ax_plot = fig.add_subplot(gs[0, 1])
    ax_num = fig.add_subplot(gs[0, 2])
    for ax in (ax_label, ax_num):
        ax.set_xlim(0, 1)
        ax.set_ylim(-0.75, 6.75)
        ax.axis("off")

    ax_label.text(0, 6.68, "終點｜事件（semaglutide vs placebo）", fontsize=11, fontweight="bold", color=MUTED)
    ax_num.text(0.02, 6.68, "HR（95% CI）", fontsize=11, fontweight="bold", color=MUTED)

    for idx, (row, label, stat, y) in enumerate(zip(ordered, labels, status, y_positions)):
        if idx in (0, 1):
            face = BLUE_LIGHT if idx == 0 else PANEL
            ax_label.axhspan(y - 0.43, y + 0.43, color=face, zorder=-3)
            ax_plot.axhspan(y - 0.43, y + 0.43, color=face, zorder=-3)
            ax_num.axhspan(y - 0.43, y + 0.43, color=face, zorder=-3)
        label_weight = "bold" if idx in (0, 1, 6) else "normal"
        label_color = ORANGE_DARK if idx == 6 else INK
        ax_label.text(0, y + 0.12, label, va="center", fontsize=18, fontweight=label_weight, color=label_color)
        ax_label.text(
            0,
            y - 0.25,
            f"{row['sema_n']}（{row['sema_pct']}%） vs {row['placebo_n']}（{row['placebo_pct']}%）｜{stat}",
            va="center",
            fontsize=10.5,
            color=MUTED,
        )

        effect = number(row["effect"])
        low = number(row["ci_low"])
        high = number(row["ci_high"])
        if idx == 0:
            color, marker, fill, size, lw = BLUE_DARK, "D", BLUE_DARK, 76, 2.8
        elif idx == 1:
            color, marker, fill, size, lw = BLUE, "D", CANVAS, 72, 2.4
        elif idx == 6:
            color, marker, fill, size, lw = ORANGE_DARK, "s", ORANGE, 72, 2.4
        else:
            color, marker, fill, size, lw = NEUTRAL, "o", CANVAS, 62, 2.0
        ax_plot.plot([low, high], [y, y], color=color, linewidth=lw, solid_capstyle="round", zorder=2)
        ax_plot.scatter(
            [effect],
            [y],
            s=size,
            marker=marker,
            facecolor=fill,
            edgecolor=color,
            linewidth=2,
            zorder=3,
        )
        ax_num.text(0.02, y, f"{effect:.2f}（{low:.2f}–{high:.2f}）", va="center", fontsize=18, color=label_color)

    ax_plot.set_xscale("log")
    ax_plot.set_xlim(0.2, 4.2)
    ax_plot.set_ylim(-0.75, 6.75)
    ax_plot.axvline(1, color=INK, linewidth=1.5, linestyle=(0, (4, 4)), zorder=0)
    ax_plot.xaxis.set_major_locator(FixedLocator([0.25, 0.5, 1, 2, 4]))
    ax_plot.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:g}"))
    ax_plot.grid(axis="x", color=GRID, linewidth=0.8)
    ax_plot.set_yticks([])
    ax_plot.spines[["top", "right", "left"]].set_visible(False)
    ax_plot.set_xlabel("Hazard ratio（95% CI）", fontsize=13, labelpad=7)
    ax_plot.text(0.22, -0.58, "← semaglutide", fontsize=10, color=MUTED, ha="left")
    ax_plot.text(4.05, -0.58, "placebo →", fontsize=10, color=MUTED, ha="right")

    add_footer(
        fig,
        "資料：FLOW-PRIMARY-2024｜Table 2，N Engl J Med 2024;391:109–121，journal p.116；Results p.115；DOI 10.1056/NEJMoa2403347。",
        "五項主要終點為確認性；四項與個別組成屬支持性／階層外。NNT 20 只屬五項；KRT、eGFR<15、腎死未個別確認。",
    )
    return save_figure(fig, output_dir, "01_flow_endpoints_forest_zh_tw")


def chart_egfr_phases(output_dir: Path) -> dict[str, object]:
    rows = {int(row["display_order"]): row for row in read_rows("02_flow_egfr_uacr.csv")}
    configs = [
        {
            "row": rows[1],
            "title": "0–12 週",
            "status": "絕對變化｜非每年斜率",
            "unit": "mL/min/1.73m²（非每年斜率）",
            "xlim": (-3.8, 0.4),
            "diff_xlim": (-0.8, 0.8),
            "message": "至 week 12 未見差異性 dip",
        },
        {
            "row": rows[2],
            "title": "Week 12 後",
            "status": "慢性斜率｜支持性分解",
            "unit": "mL/min/1.73m²／年",
            "xlim": (-3.8, 0.4),
            "diff_xlim": (0.0, 1.5),
            "message": "慢性流失較緩",
        },
        {
            "row": rows[3],
            "title": "全追蹤期",
            "status": "總斜率｜確認性次要 #1",
            "unit": "mL/min/1.73m²／年",
            "xlim": (-3.8, 0.4),
            "diff_xlim": (0.0, 1.75),
            "message": "平均下降速率減緩",
        },
    ]

    fig = new_figure(
        "FLOW：eGFR 的早期變化、慢性斜率與總斜率",
        "三個 estimand 分開呈現；0–12 週是絕對變化，慢性與總體才是每年斜率。",
    )
    gs = fig.add_gridspec(1, 3, left=0.055, right=0.955, bottom=0.17, top=0.80, wspace=0.08)

    for col, config in enumerate(configs):
        row = config["row"]
        ax = fig.add_subplot(gs[0, col])
        ax.set_facecolor(PANEL)
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.set_xlim(*config["xlim"])
        ax.set_ylim(0, 1)
        ax.set_yticks([])
        ax.grid(axis="x", color=GRID, linewidth=0.8)
        ax.axvline(0, color=GRID_DARK, linewidth=1.0)
        ax.tick_params(axis="x", labelbottom=False, length=0)
        ax.set_title(config["title"], loc="left", fontsize=20, fontweight="bold", pad=15)
        ax.text(
            0.02,
            0.94,
            config["status"],
            transform=ax.transAxes,
            ha="left",
            va="top",
            fontsize=11,
            color=BLUE_DARK if col == 2 else MUTED,
        )
        sema = number(row["sema_value"])
        placebo = number(row["placebo_value"])
        ax.plot([min(sema, placebo), max(sema, placebo)], [0.67, 0.67], color=GRID_DARK, linewidth=2.0, zorder=1)
        ax.scatter([sema], [0.67], s=180, marker="o", facecolor=BLUE, edgecolor=BLUE_DARK, linewidth=1.8, zorder=3)
        ax.scatter([placebo], [0.67], s=185, marker="s", facecolor="none", edgecolor=ORANGE, linewidth=2.2, zorder=4)
        ax.annotate(
            f"Semaglutide  {sema:.2f}",
            xy=(sema, 0.67),
            xytext=(0, 21),
            textcoords="offset points",
            ha="center",
            fontsize=18,
            color=BLUE_DARK,
            fontweight="bold",
        )
        ax.annotate(
            f"Placebo  {placebo:.2f}",
            xy=(placebo, 0.67),
            xytext=(0, -29),
            textcoords="offset points",
            ha="center",
            fontsize=18,
            color=ORANGE_DARK,
            fontweight="bold",
        )
        ax.text(0.5, 0.48, config["unit"], transform=ax.transAxes, ha="center", fontsize=12, color=MUTED)

        inset = ax.inset_axes([0.09, 0.10, 0.82, 0.27])
        inset.set_facecolor(CANVAS)
        inset.set_xlim(*config["diff_xlim"])
        inset.set_ylim(-0.55, 0.55)
        inset.axvline(0, color=INK, linewidth=1.2, linestyle=(0, (4, 4)))
        diff = number(row["difference"])
        low = number(row["ci_low"])
        high = number(row["ci_high"])
        inset.plot([low, high], [0, 0], color=BLUE_DARK, linewidth=3.0, solid_capstyle="round")
        inset.scatter([diff], [0], s=68, color=BLUE, edgecolor=BLUE_DARK, linewidth=1.4, zorder=3)
        inset.set_yticks([])
        inset.grid(axis="x", color=GRID, linewidth=0.7)
        inset.spines[["top", "right", "left"]].set_visible(False)
        inset.tick_params(axis="x", labelsize=10)
        sign = "+" if diff > 0 else ""
        inset.text(
            0.02,
            0.90,
            "組間差（95% CI）",
            transform=inset.transAxes,
            ha="left",
            va="center",
            fontsize=10,
            color=MUTED,
        )
        inset.text(
            0.02,
            0.61,
            f"Δ {sign}{diff:.2f}［{low:+.2f}, {high:+.2f}］",
            transform=inset.transAxes,
            ha="left",
            va="center",
            fontsize=18,
            fontweight="bold",
            color=INK,
        )
        inset.text(0.5, -0.20, config["message"], transform=inset.transAxes, ha="center", va="top", fontsize=11, color=INK)

    add_footer(
        fig,
        "資料：FLOW-PRIMARY-2024｜Figure 1D（journal p.114）、Table 2（p.116）、Discussion（pp.119–120）；DOI 10.1056/NEJMoa2403347。",
        "解讀：只能說基線至 week 12 未見 semaglutide 專屬差異性下降；不排除更早且已消退的短暫變化。斜率不得換算為延後透析若干年。",
    )
    return save_figure(fig, output_dir, "02_flow_egfr_phases_zh_tw")


def _subgroup_forest(
    *,
    output_dir: Path,
    stem: str,
    title: str,
    subtitle: str,
    rows: Sequence[Mapping[str, str]],
    outcome_labels: Sequence[str],
    xlim: tuple[float, float],
    ticks: Sequence[float],
    user_label: str,
    nonuser_label: str,
    bottom_heading: str,
    bottom_lines: Sequence[str],
    event_notes: Sequence[str],
    source: str,
    note: str,
) -> dict[str, object]:
    fig = new_figure(title, subtitle)
    gs = fig.add_gridspec(
        1,
        3,
        left=0.055,
        right=0.955,
        bottom=0.29,
        top=0.78,
        width_ratios=[3.2, 2.5, 3.3],
        wspace=0.035,
    )
    ax_label = fig.add_subplot(gs[0, 0])
    ax_plot = fig.add_subplot(gs[0, 1])
    ax_num = fig.add_subplot(gs[0, 2])
    y_positions = list(reversed(range(len(rows))))
    for ax in (ax_label, ax_num):
        ax.set_xlim(0, 1)
        ax.set_ylim(-0.65, len(rows) - 0.35)
        ax.axis("off")
    ax_label.text(0, len(rows) - 0.42, "終點｜事件數", fontsize=11, fontweight="bold", color=MUTED)
    ax_num.text(0.02, len(rows) - 0.42, "HR（95% CI）｜P-interaction", fontsize=11, fontweight="bold", color=MUTED)

    for row, label, y in zip(rows, outcome_labels, y_positions):
        ax_label.axhspan(y - 0.42, y + 0.42, color=PANEL, zorder=-3)
        ax_plot.axhspan(y - 0.42, y + 0.42, color=PANEL, zorder=-3)
        ax_num.axhspan(y - 0.42, y + 0.42, color=PANEL, zorder=-3)
        ax_label.text(0, y + 0.16, label, fontsize=18, fontweight="bold", va="center")
        event_note = event_notes[y_positions.index(y)]
        ax_label.text(0, y - 0.22, event_note, fontsize=10, color=MUTED, va="center")

        user_effect = number(row["users_effect"])
        user_low, user_high = parse_ci(row["users_ci"])
        non_effect = number(row["nonusers_effect"])
        non_low, non_high = parse_ci(row["nonusers_ci"])
        for effect, low, high, offset, color, marker, face in (
            (user_effect, user_low, user_high, +0.13, BLUE_DARK, "o", BLUE),
            (non_effect, non_low, non_high, -0.13, ORANGE, "s", CANVAS),
        ):
            ax_plot.plot([low, high], [y + offset, y + offset], color=color, linewidth=2.3, solid_capstyle="round")
            ax_plot.scatter(
                [effect],
                [y + offset],
                s=78,
                marker=marker,
                facecolor=face,
                edgecolor=color,
                linewidth=2.0,
                zorder=3,
            )
        p_text = row["p_interaction"]
        p_note = ""
        if p_text == "0.023" or p_text == "0.027":
            p_note = "（名目、未校正）"
        ax_num.text(
            0.02,
            y + 0.24,
            f"{user_effect:.2f}（{user_low:.2f}–{user_high:.2f}）",
            fontsize=18,
            color=BLUE_DARK,
            va="center",
            fontweight="bold",
        )
        ax_num.text(
            0.02,
            y - 0.05,
            f"{non_effect:.2f}（{non_low:.2f}–{non_high:.2f}）",
            fontsize=18,
            color=ORANGE_DARK,
            va="center",
            fontweight="bold",
        )
        p_display = f"P-int {p_text}" if not p_note else f"P-int {p_text}（名目、未校正）"
        ax_num.text(0.02, y - 0.31, p_display, fontsize=18, color=ORANGE_DARK if p_note else MUTED, ha="left", va="center")

    ax_plot.set_xscale("log")
    ax_plot.set_xlim(*xlim)
    ax_plot.set_ylim(-0.65, len(rows) - 0.35)
    ax_plot.axvline(1, color=INK, linewidth=1.5, linestyle=(0, (4, 4)), zorder=0)
    ax_plot.xaxis.set_major_locator(FixedLocator(ticks))
    ax_plot.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:g}"))
    ax_plot.xaxis.set_minor_formatter(NullFormatter())
    ax_plot.grid(axis="x", color=GRID, linewidth=0.8)
    ax_plot.set_yticks([])
    ax_plot.spines[["top", "right", "left"]].set_visible(False)
    ax_plot.set_xlabel("Hazard ratio（95% CI）", fontsize=13, labelpad=8)
    ax_plot.tick_params(axis="x", labelsize=11)

    fig.text(0.055, 0.247, "●", color=BLUE, fontsize=18, va="center")
    fig.text(0.074, 0.247, user_label, color=BLUE_DARK, fontsize=12, va="center")
    fig.text(0.270, 0.247, "□", color=ORANGE, fontsize=19, va="center")
    fig.text(0.290, 0.247, nonuser_label, color=ORANGE_DARK, fontsize=12, va="center")

    panel_ax = fig.add_axes([0.055, 0.105, 0.90, 0.105])
    panel_ax.axis("off")
    rounded_box(panel_ax, 0, 0, 1, 1, facecolor=ORANGE_LIGHT, edgecolor="none", radius=0.025)
    panel_ax.text(0.025, 0.75, bottom_heading, fontsize=12, fontweight="bold", color=ORANGE_DARK, va="center")
    for i, line in enumerate(bottom_lines):
        panel_ax.text(0.025, 0.47 - i * 0.27, line, fontsize=10, color=INK, va="center")

    add_footer(fig, source, note)
    return save_figure(fig, output_dir, stem)


def chart_sglt2_subgroup(output_dir: Path) -> dict[str, object]:
    rows = [row for row in read_rows("03_flow_background_subgroups.csv") if row["background"] == "SGLT2i"]
    return _subgroup_forest(
        output_dir=output_dir,
        stem="03_flow_sglt2_subgroup_forest_zh_tw",
        title="FLOW：基線 SGLT2i 次族群",
        subtitle="基線使用者 N=550、主要終點僅 79 事件；這不是 SGLT2i × semaglutide 的析因隨機試驗。",
        rows=rows,
        outcome_labels=["五項主要複合（含 CV death）", "四項腎臟專屬複合", "持續 ≥50% eGFR 下降（單一組成）"],
        xlim=(0.42, 2.55),
        ticks=(0.5, 0.75, 1, 1.5, 2.5),
        user_label="基線使用 SGLT2i（N=550）",
        nonuser_label="基線未使用（N=2,983）",
        bottom_heading="不同 estimand：不可挑選、平均或互相推翻",
        bottom_lines=(
            "Creatinine 五項 1.07（0.69–1.67）；post hoc cystatin-C modified 五項 0.74（0.47–1.16）。",
            "終點／marker 不同；P-int 0.109／0.100＝未偵測異質性，不等於證明加成。",
        ),
        event_notes=(
            "使用：41/277 vs 38/273｜未使用：290/1,490 vs 372/1,493",
            "使用：32/277 vs 27/273｜未使用：186/1,490 vs 233/1,493",
            "使用：30/277 vs 23/273｜未使用：135/1,489 vs 190/1,493",
        ),
        source="資料：FLOW-SGLT2-2024｜Figures 1–2、Table 1、Results；Nat Med 2024;30:2849–2856；DOI 10.1038/s41591-024-03133-0。",
        note="裁決：semaglutide 疊加於 SGLT2i 的增量硬腎臟效益與傷害均未被辨識（unknown）；P-int=.023 為個別組成之名目、未校正訊號。",
    )


def chart_mra_subgroup(output_dir: Path) -> dict[str, object]:
    rows = [row for row in read_rows("03_flow_background_subgroups.csv") if row["background"] == "MRA"]
    return _subgroup_forest(
        output_dir=output_dir,
        stem="04_flow_mra_subgroup_forest_zh_tw",
        title="FLOW：基線 MRA 次族群",
        subtitle="MRA 使用者 N=257；主要為 spironolactone／eplerenone，基線 finerenone 使用者為 0。",
        rows=rows,
        outcome_labels=["五項主要複合（含 CV death）", "四項腎臟專屬複合", "開始腎替代治療（單一組成）"],
        xlim=(0.02, 2.05),
        ticks=(0.025, 0.05, 0.1, 0.25, 0.5, 1, 2),
        user_label="基線使用 MRA（N=257）",
        nonuser_label="基線未使用（N=3,276）",
        bottom_heading="不是 finerenone 組合證據",
        bottom_lines=(
            "MRA：spironolactone 218、eplerenone 38、esaxerenone 1、finerenone 0；非隨機背景治療。",
            "主要 P-int=.12；RRT P-int=.027 僅 11 個 MRA-user 事件，屬名目、未校正訊號。",
        ),
        event_notes=(
            "MRA 使用者共 59 事件；未使用者共 682 事件",
            "來源未另列此列事件總數",
            "MRA 使用者次族群總共僅 11 事件",
        ),
        source="資料：FLOW-MRA-2025｜Figures 1–2、Supplementary Tables 1–2、Results；DOI 10.2337/dc25-0472；PMCID PMC12583412。",
        note="裁決：可依表現型務實疊加治療，但 FLOW 未證明 semaglutide＋finerenone 的加成硬腎臟效益，也未驗證固定四藥順序。",
    )


def _cross_trial_panel(
    ax,
    *,
    heading: str,
    population: str,
    dose: str,
    hr_rows: Sequence[tuple[str, float, float, float, str]],
    slope_main: str,
    slope_unit: str,
    caveat: str,
    source: str,
    marker: str,
    color: str,
    fill: str,
) -> None:
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    rounded_box(ax, 0, 0, 1, 1, facecolor=PANEL, edgecolor=GRID, radius=0.025)
    ax.text(0.055, 0.95, heading, fontsize=22, fontweight="bold", va="top")
    ax.text(0.055, 0.875, population, fontsize=11, color=MUTED, va="top")
    ax.text(
        0.945,
        0.835,
        dose,
        fontsize=10.5,
        color=BLUE_DARK,
        ha="right",
        va="top",
        bbox=dict(boxstyle="round,pad=0.32", facecolor=BLUE_LIGHT, edgecolor="none"),
    )
    # Manual within-panel forest prevents labels from spilling into neighbouring
    # panels while keeping the same honest HR scale in all three panels.
    x_min, x_max = math.log(0.55), math.log(1.2)

    def map_x(value: float) -> float:
        return 0.08 + 0.84 * (math.log(value) - x_min) / (x_max - x_min)

    null_x = map_x(1.0)
    row_y = [0.69] if len(hr_rows) == 1 else [0.75, 0.53]
    forest_y = [y - 0.13 for y in row_y]
    ax.plot(
        [null_x, null_x],
        [min(forest_y) - 0.02, max(forest_y) + 0.02],
        transform=ax.transAxes,
        color=INK,
        linewidth=1.2,
        linestyle=(0, (4, 4)),
    )
    for tick in (0.6, 0.8, 1.0, 1.2):
        tx = map_x(tick)
        ax.plot([tx, tx], [0.355, 0.365], transform=ax.transAxes, color=GRID_DARK, linewidth=0.9)
        ax.text(tx, 0.345, f"{tick:g}", transform=ax.transAxes, ha="center", va="top", fontsize=10, color=MUTED)
    for (label, effect, low, high, p), y in zip(hr_rows, row_y):
        ax.text(0.055, y, label, transform=ax.transAxes, ha="left", va="bottom", fontsize=18, color=INK)
        ax.text(
            0.055,
            y - 0.065,
            f"HR {effect:.2f}（{low:.2f}–{high:.2f}）",
            transform=ax.transAxes,
            ha="left",
            va="bottom",
            fontsize=18,
            fontweight="bold",
            color=color,
        )
        if p:
            ax.text(
                0.945,
                y - 0.105,
                p.lstrip("；"),
                transform=ax.transAxes,
                ha="right",
                va="center",
                fontsize=11,
                color=ORANGE_DARK if "未校正" in p else MUTED,
            )
        plot_y = y - 0.13
        ax.plot([map_x(low), map_x(high)], [plot_y, plot_y], transform=ax.transAxes, color=color, linewidth=2.6, solid_capstyle="round")
        ax.scatter(
            [map_x(effect)],
            [plot_y],
            transform=ax.transAxes,
            s=82,
            marker=marker,
            facecolor=fill,
            edgecolor=color,
            linewidth=1.9,
            zorder=3,
        )

    rounded_box(ax, 0.055, 0.235, 0.89, 0.09, facecolor=BLUE_LIGHT, edgecolor="none", radius=0.018)
    ax.text(0.08, 0.285, slope_main, fontsize=18, color=BLUE_DARK, va="center", fontweight="bold")
    ax.text(0.08, 0.248, slope_unit, fontsize=10.5, color=BLUE_DARK, va="center")
    ax.text(0.055, 0.205, caveat, fontsize=10.5, color=INK, va="top", linespacing=1.25)
    ax.text(0.055, 0.035, source, fontsize=10, color=MUTED, va="bottom")


def chart_cross_trial_context(output_dir: Path) -> dict[str, object]:
    rows = read_rows("04_select_soul_pooled.csv")
    select = next(row for row in rows if row["study"] == "SELECT" and "composite" in row["outcome"])
    select_slope = next(row for row in rows if row["study"] == "SELECT" and row["outcome"] == "total eGFR slope")
    soul_five = next(row for row in rows if row["study"] == "SOUL" and "five-point" in row["outcome"])
    soul_four = next(row for row in rows if row["study"] == "SOUL" and "four-point" in row["outcome"])
    soul_slope = next(row for row in rows if row["study"] == "SOUL" and row["outcome"] == "total eGFR slope")
    pooled = [row for row in rows if row["study"] == "SELECT+FLOW+SOUL pooled"]

    def hr_tuple(label: str, row: Mapping[str, str], p: str = "") -> tuple[str, float, float, float, str]:
        low, high = parse_ci(row["ci"])
        return label, number(row["effect"]), low, high, p

    fig = new_figure(
        "跨試驗腎臟結果：SELECT、SOUL 與 pooled",
        "各 panel 依自身 estimand 解讀；pooled 有一致定義，但不可拿 component-trial 點估計做排名。",
    )
    gs = fig.add_gridspec(1, 3, left=0.045, right=0.955, bottom=0.145, top=0.80, wspace=0.055)
    axes = [fig.add_subplot(gs[0, i]) for i in range(3)]
    _cross_trial_panel(
        axes[0],
        heading="SELECT",
        population="肥胖＋ASCVD；無已診斷糖尿病｜N=17,604",
        dose="2.4 mg SC",
        hr_rows=[hr_tuple("腎臟複合*", select, "；P=.02（未校正）")],
        slope_main=f"Δ總斜率 +{number(select_slope['effect']):.2f}（{select_slope['ci']}）",
        slope_unit="mL/min/1.73m²／年",
        caveat="*含新發持續性巨量白蛋白尿；不含 CV death。\n次要結果；P=.02 未校正。\n非 dedicated CKD trial。",
        source="SELECT-KIDNEY-2024｜Figure 1、Table 1、Results\nDOI 10.1038/s41591-024-03015-5",
        marker="o",
        color=BLUE_DARK,
        fill=BLUE,
    )
    _cross_trial_panel(
        axes[1],
        heading="SOUL",
        population="T2D＋ASCVD／CKD｜N=9,650",
        dose="14 mg oral",
        hr_rows=[
            hr_tuple("五項：含 CV death", soul_five, "；P=.19"),
            hr_tuple("四項：排除 CV death", soul_four, "；P=.22"),
        ],
        slope_main=f"Δ總斜率 +{number(soul_slope['effect']):.2f}（{soul_slope['ci']}）",
        slope_unit="mL/min/1.73m²／年",
        caveat="五項腎臟 gate 未達顯著；後續斜率因此形式上屬探索性。\n不得將結果單獨歸因於口服途徑。",
        source="SOUL-KIDNEY-2026｜PubMed structured abstract, Results\nPMID 41380027",
        marker="s",
        color=ORANGE,
        fill=CANVAS,
    )
    _cross_trial_panel(
        axes[2],
        heading="三試驗 pooled",
        population="混合族群與基線風險｜N=30,787",
        dose="混合劑量／途徑",
        hr_rows=[
            hr_tuple("主要 pooled：含 CV death", pooled[0]),
            hr_tuple("腎臟專屬：排除 CV death", pooled[1]),
        ],
        slope_main="未報 pooled slope",
        slope_unit="不可與 SELECT／SOUL 斜率直接對齊",
        caveat="定義：≥50% eGFR↓／腎衰竭／腎死；\n主要另含 CV death。\n與 component trials 統計相依；禁做排名／途徑因果。",
        source="SELECT-FLOW-SOUL-POOLED-2026｜Methods／Findings\nPMID 42567173",
        marker="D",
        color=BLUE_DARK,
        fill=CANVAS,
    )
    add_footer(
        fig,
        "數據來源與精確定位如各 panel；CSV：presentation_zh_tw/chart_data/04_select_soul_pooled.csv。Data redrawn; no publisher figure/table reproduced.",
        "底線：pooled endpoint 已結構性 harmonize；但 pooled 與 component trials 統計相依，不能據此做跨試驗排名或劑量／途徑因果比較。",
    )
    return save_figure(fig, output_dir, "05_select_soul_pooled_context_zh_tw")


def chart_flow_safety(output_dir: Path) -> dict[str, object]:
    rows = read_rows("05_flow_safety.csv")
    labels = [
        "嚴重不良事件（SAE）",
        "因任何 AE 永久停藥",
        "因 GI AE 永久停藥*",
        "嚴重 AE preferred term：AKI",
        "嚴重 AE preferred term：脫水",
        "至少一次嚴重低血糖",
        "系統性收集糖尿病視網膜病變",
    ]
    short_locators = [
        "FLOW-PRIMARY-2024｜Table 3, p.120",
        "FLOW-SUPPLEMENT-2024｜Table S5, p.32",
        "FLOW-SUPPLEMENT-2024｜Table S5, p.32",
        "FLOW-SUPPLEMENT-2024｜Table S4, p.29",
        "FLOW-SUPPLEMENT-2024｜Table S4, p.30",
        "FLOW-PRIMARY-2024｜Table 3, p.120",
        "FLOW-PRIMARY-2024｜Table 3, p.120",
    ]
    source_notes = [
        "全試驗 SAE；不代表每種晚期 CKD 表現型皆已證實安全",
        "所有不良事件原因",
        "前列永久停藥的子集合；不可另作分母相加",
        "整體數值平衡；未依 KDIGO 分層",
        "臨床仍須監測容量耗竭",
        "以受試者計數；不同於 47 vs 46 次事件",
        "試驗排除不穩定視網膜病變；不取消仿單警語",
    ]
    y_positions = list(reversed(range(len(rows))))

    fig = new_figure(
        "FLOW 安全性：事件與永久停藥（受試者%）",
        "同一列比較 semaglutide 與 placebo；不同列來自不同表格／事件定義，不能相加或換成 hazard ratio。",
    )
    gs = fig.add_gridspec(
        1,
        3,
        left=0.055,
        right=0.955,
        bottom=0.18,
        top=0.80,
        width_ratios=[3.0, 3.25, 2.25],
        wspace=0.025,
    )
    ax_label = fig.add_subplot(gs[0, 0])
    ax_plot = fig.add_subplot(gs[0, 1])
    ax_source = fig.add_subplot(gs[0, 2])
    for ax in (ax_label, ax_source):
        ax.set_xlim(0, 1)
        ax.set_ylim(-0.65, 6.65)
        ax.axis("off")
    ax_label.text(0, 6.58, "結果｜n（%）", fontsize=11, color=MUTED, fontweight="bold")
    ax_source.text(0.03, 6.58, "來源代號｜精確定位", fontsize=11, color=MUTED, fontweight="bold")

    for row, label, locator, _source_note, y in zip(rows, labels, short_locators, source_notes, y_positions):
        if y % 2 == 0:
            for ax in (ax_label, ax_plot, ax_source):
                ax.axhspan(y - 0.43, y + 0.43, color=PANEL, zorder=-4)
        sema = number(row["sema_pct"])
        placebo = number(row["placebo_pct"])
        ax_label.text(0, y + 0.10, label, fontsize=18, fontweight="bold" if y in (6, 4) else "normal", va="center")
        ax_label.text(
            0,
            y - 0.23,
            f"{row['sema_n']}（{sema:.1f}%） vs {row['placebo_n']}（{placebo:.1f}%）",
            fontsize=10.5,
            color=MUTED,
            va="center",
        )
        ax_plot.plot([min(sema, placebo), max(sema, placebo)], [y, y], color=GRID_DARK, linewidth=2.0, zorder=1)
        ax_plot.scatter([sema], [y], s=88, marker="o", facecolor=BLUE, edgecolor=BLUE_DARK, linewidth=1.7, zorder=3)
        ax_plot.scatter([placebo], [y], s=112, marker="s", facecolor="none", edgecolor=ORANGE, linewidth=2.2, zorder=4)
        if math.isclose(sema, placebo, abs_tol=0.04):
            ax_plot.annotate(f"兩組 {sema:.1f}%", (sema, y), xytext=(12, 0), textcoords="offset points", va="center", fontsize=18, color=INK)
        else:
            ax_plot.annotate(f"{sema:.1f}", (sema, y), xytext=(0, 13), textcoords="offset points", ha="center", fontsize=18, color=BLUE_DARK, fontweight="bold")
            ax_plot.annotate(f"{placebo:.1f}", (placebo, y), xytext=(0, -22), textcoords="offset points", ha="center", fontsize=18, color=ORANGE_DARK, fontweight="bold")
        ax_source.text(0.03, y, locator, fontsize=10.5, va="center", color=INK)

    ax_plot.set_xlim(0, 58)
    ax_plot.set_ylim(-0.65, 6.65)
    ax_plot.set_yticks([])
    ax_plot.set_xlabel("發生至少一件事件之受試者（%）", fontsize=13, labelpad=8)
    ax_plot.grid(axis="x", color=GRID, linewidth=0.8)
    ax_plot.spines[["top", "right", "left"]].set_visible(False)
    ax_plot.tick_params(axis="x", labelsize=11)
    fig.text(0.375, 0.817, "● Semaglutide", fontsize=12, color=BLUE_DARK, va="center")
    fig.text(0.500, 0.817, "□ Placebo", fontsize=12, color=ORANGE_DARK, va="center")

    add_footer(
        fig,
        "資料：FLOW-PRIMARY-2024 Table 3（journal p.120／local PDF p.12）；FLOW-SUPPLEMENT-2024 Tables S4（PDF pp.29–30）與 S5（p.32）。",
        "*GI-specific 永久停藥是 AE-driven permanent discontinuation 的子集合，不可另加。AKI 的整體數值平衡不取消 GI loss／容量耗竭情境下的個別監測。",
    )
    return save_figure(fig, output_dir, "06_flow_safety_dotplot_zh_tw")


CHART_BUILDERS = {
    "01": chart_flow_endpoints,
    "02": chart_egfr_phases,
    "03": chart_sglt2_subgroup,
    "04": chart_mra_subgroup,
    "05": chart_cross_trial_context,
    "06": chart_flow_safety,
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument(
        "--only",
        nargs="*",
        choices=sorted(CHART_BUILDERS),
        help="Generate only selected chart numbers (for example: --only 01 03).",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        help="Manifest path (default: MANIFEST.json inside the output directory).",
    )
    args = parser.parse_args()

    selected = args.only or sorted(CHART_BUILDERS)
    output_dir = args.output_dir.resolve()
    outputs = [CHART_BUILDERS[key](output_dir) for key in selected]
    manifest = {
        "generator": str(Path(__file__).resolve().relative_to(REPO_ROOT)),
        "evidence_cutoff": "2026-09-05",
        "generated_for_release": "2026-09-06",
        "canvas_inches": [SLIDE_WIDTH_IN, SLIDE_HEIGHT_IN],
        "preview_dpi": PREVIEW_DPI,
        "png_dpi": PNG_DPI,
        "png_default_for_slides": True,
        "outputs": outputs,
    }
    manifest_path = args.manifest.resolve() if args.manifest else output_dir / "MANIFEST.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
