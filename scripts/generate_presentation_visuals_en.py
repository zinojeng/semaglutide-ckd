#!/usr/bin/env python3
"""Generate English, source-faithful presentation visuals from reviewed CSV data.

This generator creates a separate English asset pack.  It does not modify or
overwrite the Traditional Chinese redraws.  Official English endpoint, axis,
and legend wording is retained from the cited source tables or figures.  Any
interpretive caveat added by this project appears only in a footer explicitly
labelled ``Project interpretation``.

Run from anywhere:

    python3 scripts/generate_presentation_visuals_en.py
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
import textwrap
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
DEFAULT_OUTPUT_DIR = PACK_DIR / "public_assets/redrawn_en"

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

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 12,
        "text.color": INK,
        "axes.labelcolor": INK,
        "axes.edgecolor": GRID_DARK,
        "axes.titlecolor": INK,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "axes.unicode_minus": False,
        "svg.fonttype": "path",
        "svg.hashsalt": "semaglutide-ckd-english-2026-09-06",
        "savefig.facecolor": CANVAS,
        "figure.facecolor": CANVAS,
    }
)


# Compact contracts keep chart choice and delivery constraints reviewable.
CHART_CONTRACTS = {
    "01": "Uncertainty forest; seven FLOW time-to-event outcomes; 16:9 static SVG and PNG.",
    "02": "Three-panel comparison; absolute eGFR change and two annual slopes; 16:9 static SVG and PNG.",
    "03": "Faceted dot-and-interval forest; three outcomes by baseline SGLT2i use; 16:9 static SVG and PNG.",
    "04": "Faceted dot-and-interval forest; three outcomes by baseline MRA use; 16:9 static SVG and PNG.",
    "05": "Five-row common-scale forest with two source slope-result bands; SELECT, SOUL, and pooled estimates; 16:9 static SVG and PNG.",
    "06": "Paired dot plot; seven FLOW safety outcomes; 16:9 static SVG and PNG.",
}

COMMON_CAPTION = (
    "Project redraw from verified source data; source wording retained for endpoint labels. "
    "Project notes are editorial and are not source quotations."
)


def read_rows(filename: str) -> list[dict[str, str]]:
    path = DATA_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Missing reviewed chart data: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def number(value: str | float | int) -> float:
    if isinstance(value, (int, float)):
        return float(value)
    return float(value.strip().replace("+", ""))


def source_decimal(value: float) -> str:
    """Format a signed source value without adding a non-source plus sign."""
    if value < 0:
        return f"−{abs(value):.2f}"
    return f"{value:.2f}"


def parse_ci(value: str) -> tuple[float, float]:
    cleaned = value.strip().replace("−", "-").replace("–", "-")
    if " to " in cleaned:
        left, right = cleaned.split(" to ", 1)
    else:
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


def new_figure(title: str, subtitle: str):
    fig = plt.figure(
        figsize=(SLIDE_WIDTH_IN, SLIDE_HEIGHT_IN),
        dpi=PREVIEW_DPI,
        facecolor=CANVAS,
    )
    fig.text(0.055, 0.978, "PROJECT NOTE", ha="left", va="top", fontsize=9.5, fontweight="bold", color=BLUE_DARK)
    fig.text(0.055, 0.947, title, ha="left", va="top", fontsize=25, fontweight="bold", color=INK)
    fig.text(0.055, 0.887, subtitle, ha="left", va="top", fontsize=14, color=MUTED)
    return fig


def add_footer(fig, *, source: str, interpretation: str) -> None:
    wrapped_interpretation = "\n".join(
        textwrap.fill(line, width=126) for line in interpretation.splitlines()
    )
    fig.text(
        0.055,
        0.079,
        "Project interpretation:",
        ha="left",
        va="bottom",
        fontsize=10.5,
        color=INK,
        fontweight="bold",
    )
    fig.text(
        0.225,
        0.079,
        wrapped_interpretation,
        ha="left",
        va="bottom",
        fontsize=10.5,
        color=INK,
        linespacing=1.18,
    )
    fig.text(
        0.055,
        0.012,
        textwrap.fill(f"Source: {source}", width=170),
        ha="left",
        va="bottom",
        fontsize=10.0,
        color=MUTED,
        linespacing=1.15,
    )


def manifest_reference(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return path.name


def save_figure(fig, output_dir: Path, stem: str) -> dict[str, object]:
    output_dir.mkdir(parents=True, exist_ok=True)
    svg = output_dir / f"{stem}.svg"
    png = output_dir / f"{stem}@2x.png"
    fig.savefig(
        svg,
        format="svg",
        dpi=100,
        metadata={"Creator": "semaglutide-ckd English chart generator", "Date": "2026-09-06"},
    )
    # Matplotlib writes trailing spaces in some SVG path data.  Normalize line
    # endings without altering the rendered geometry.
    svg_text = svg.read_text(encoding="utf-8")
    svg.write_text(
        "\n".join(line.rstrip() for line in svg_text.splitlines()) + "\n",
        encoding="utf-8",
    )
    fig.savefig(
        png,
        format="png",
        dpi=PNG_DPI,
        metadata={"Software": "semaglutide-ckd English chart generator"},
    )
    plt.close(fig)
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
    # Locked source wording from FLOW Table 2.  Line breaks do not alter text.
    labels = [
        "Primary outcome: major kidney\ndisease events — no. (%)†",
        "Composite of kidney-specific components\nof the primary outcome",
        "Persistent ≥50% reduction from baseline in eGFR",
        "Persistent eGFR <15 ml/min/1.73 m²",
        "Initiation of kidney-replacement therapy",
        "Death from kidney-related causes",
        "Death from cardiovascular causes",
    ]
    y_positions = list(reversed(range(len(ordered))))

    fig = new_figure(
        "FLOW efficacy outcomes",
        "Semaglutide and placebo event counts, hazard ratios, and 95% confidence intervals",
    )
    gs = fig.add_gridspec(
        1,
        3,
        left=0.055,
        right=0.955,
        bottom=0.205,
        top=0.79,
        width_ratios=[4.85, 2.15, 1.75],
        wspace=0.035,
    )
    ax_label = fig.add_subplot(gs[0, 0])
    ax_plot = fig.add_subplot(gs[0, 1])
    ax_num = fig.add_subplot(gs[0, 2])
    for ax in (ax_label, ax_num):
        ax.set_xlim(0, 1)
        ax.set_ylim(-0.75, 6.75)
        ax.axis("off")

    ax_label.text(0, 6.69, "Outcome, no. (%)", fontsize=11, fontweight="bold", color=MUTED)
    ax_num.text(0.02, 6.69, "Hazard Ratio (95% CI)", fontsize=11, fontweight="bold", color=MUTED)

    for index, (row, label, y) in enumerate(zip(ordered, labels, y_positions)):
        if index in (0, 1):
            face = BLUE_LIGHT if index == 0 else PANEL
            for ax in (ax_label, ax_plot, ax_num):
                ax.axhspan(y - 0.43, y + 0.43, color=face, zorder=-3)

        label_color = ORANGE_DARK if index == 6 else INK
        ax_label.text(
            0,
            y + 0.12,
            label,
            va="center",
            fontsize=18,
            linespacing=0.88,
            fontweight="bold" if index in (0, 1, 6) else "normal",
            color=label_color,
        )
        ax_label.text(
            0,
            y - (0.40 if index == 1 else 0.34),
            f"{row['sema_n']} ({row['sema_pct']}%) vs {row['placebo_n']} ({row['placebo_pct']}%)",
            va="center",
            fontsize=11,
            color=MUTED,
        )

        effect = number(row["effect"])
        low = number(row["ci_low"])
        high = number(row["ci_high"])
        if index == 0:
            color, marker, fill, size, linewidth = BLUE_DARK, "D", BLUE_DARK, 76, 2.8
        elif index == 1:
            color, marker, fill, size, linewidth = BLUE, "D", CANVAS, 72, 2.4
        elif index == 6:
            color, marker, fill, size, linewidth = ORANGE_DARK, "s", ORANGE, 72, 2.4
        else:
            color, marker, fill, size, linewidth = NEUTRAL, "o", CANVAS, 62, 2.0
        ax_plot.plot([low, high], [y, y], color=color, linewidth=linewidth, solid_capstyle="round", zorder=2)
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
        ax_num.text(
            0.02,
            y,
            f"{effect:.2f} ({low:.2f} to {high:.2f})",
            va="center",
            fontsize=18,
            color=label_color,
        )

    ax_plot.set_xscale("log")
    ax_plot.set_xlim(0.2, 4.2)
    ax_plot.set_ylim(-0.75, 6.75)
    ax_plot.axvline(1, color=INK, linewidth=1.5, linestyle=(0, (4, 4)), zorder=0)
    ax_plot.xaxis.set_major_locator(FixedLocator([0.25, 0.5, 1, 2, 4]))
    ax_plot.xaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{value:g}"))
    ax_plot.grid(axis="x", color=GRID, linewidth=0.8)
    ax_plot.set_yticks([])
    ax_plot.spines[["top", "right", "left"]].set_visible(False)
    ax_plot.set_xlabel("Hazard Ratio (95% CI)", fontsize=13, labelpad=7)
    ax_plot.text(0.22, -0.58, "Semaglutide Better", fontsize=10.5, color=MUTED, ha="left")
    ax_plot.text(4.05, -0.58, "Placebo Better", fontsize=10.5, color=MUTED, ha="right")

    add_footer(
        fig,
        source=(
            "FLOW-PRIMARY-2024, Table 2 and Results, NEJM pp.115–117. Project transcription of †: endpoint components "
            "include kidney failure, persistent ≥50% eGFR reduction, kidney death, or cardiovascular death; see Table 2 "
            "footnote, p.117."
        ),
        interpretation=(
            "The primary outcome was confirmatory. The kidney-specific composite and individual components were "
            "outside the multiplicity-controlled hierarchy."
        ),
    )
    return save_figure(fig, output_dir, "01_flow_endpoints_forest_en")


def chart_egfr_phases(output_dir: Path) -> dict[str, object]:
    rows = {int(row["display_order"]): row for row in read_rows("02_flow_egfr_uacr.csv")}
    configs = [
        {
            "row": rows[1],
            "title": "Mean change in eGFR from\nbaseline to week 12",
            "xlim": (-3.8, 0.4),
            "diff_xlim": (-0.8, 0.8),
        },
        {
            "row": rows[2],
            "title": "Mean annual rate of change\nin eGFR from week 12\nto end of trial",
            "xlim": (-3.8, 0.4),
            "diff_xlim": (0.0, 1.5),
        },
        {
            "row": rows[3],
            "title": "Mean annual rate of change\nin eGFR",
            "xlim": (-3.8, 0.4),
            "diff_xlim": (0.0, 1.75),
        },
    ]

    fig = new_figure(
        "FLOW eGFR outcomes",
        "Semaglutide and placebo estimates with Estimated Difference (95% CI)",
    )
    gs = fig.add_gridspec(1, 3, left=0.055, right=0.955, bottom=0.19, top=0.78, wspace=0.08)

    for column, config in enumerate(configs):
        row = config["row"]
        ax = fig.add_subplot(gs[0, column])
        ax.set_facecolor(PANEL)
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.set_xlim(*config["xlim"])
        ax.set_ylim(0, 1)
        ax.set_yticks([])
        ax.grid(False)
        ax.tick_params(axis="x", labelbottom=False, length=0)
        ax.text(
            0.04,
            0.965,
            config["title"],
            transform=ax.transAxes,
            ha="left",
            va="top",
            fontsize=18,
            fontweight="bold",
            linespacing=1.05,
        )

        semaglutide = number(row["sema_value"])
        placebo = number(row["placebo_value"])
        ax.plot(
            [min(semaglutide, placebo), max(semaglutide, placebo)],
            [0.46, 0.46],
            color=GRID_DARK,
            linewidth=2.0,
            zorder=1,
        )
        ax.scatter(
            [semaglutide],
            [0.46],
            s=180,
            marker="o",
            facecolor=BLUE,
            edgecolor=BLUE_DARK,
            linewidth=1.8,
            zorder=3,
        )
        ax.scatter(
            [placebo],
            [0.46],
            s=185,
            marker="s",
            facecolor="none",
            edgecolor=ORANGE,
            linewidth=2.2,
            zorder=4,
        )
        ax.text(
            0.05,
            0.68,
            f"Semaglutide  {source_decimal(semaglutide)}",
            transform=ax.transAxes,
            ha="left",
            va="center",
            fontsize=18,
            color=BLUE_DARK,
            fontweight="bold",
        )
        ax.text(
            0.05,
            0.59,
            f"Placebo  {source_decimal(placebo)}",
            transform=ax.transAxes,
            ha="left",
            va="center",
            fontsize=18,
            color=ORANGE_DARK,
            fontweight="bold",
        )
        ax.text(0.05, 0.52, row["unit"], transform=ax.transAxes, ha="left", fontsize=12, color=MUTED)

        inset = ax.inset_axes([0.09, 0.06, 0.82, 0.30])
        inset.set_facecolor(CANVAS)
        inset.set_xlim(*config["diff_xlim"])
        inset.set_ylim(-1.0, 1.0)
        inset.axvline(0, color=INK, linewidth=1.2, linestyle=(0, (4, 4)))
        difference = number(row["difference"])
        low = number(row["ci_low"])
        high = number(row["ci_high"])
        inset.plot([low, high], [-0.28, -0.28], color=BLUE_DARK, linewidth=3.0, solid_capstyle="round")
        inset.scatter([difference], [-0.28], s=68, color=BLUE, edgecolor=BLUE_DARK, linewidth=1.4, zorder=3)
        inset.set_yticks([])
        inset.grid(axis="x", color=GRID, linewidth=0.7)
        inset.spines[["top", "right", "left"]].set_visible(False)
        inset.tick_params(axis="x", labelsize=10)
        inset.text(
            0.02,
            0.88,
            "Estimated Difference (95% CI)",
            transform=inset.transAxes,
            ha="left",
            va="center",
            fontsize=10,
            color=MUTED,
            bbox={"facecolor": CANVAS, "edgecolor": "none", "pad": 1.5},
            zorder=5,
        )
        inset.text(
            0.02,
            0.62,
            f"{source_decimal(difference)} ({source_decimal(low)} to {source_decimal(high)})",
            transform=inset.transAxes,
            ha="left",
            va="center",
            fontsize=18,
            fontweight="bold",
            color=INK,
        )

    add_footer(
        fig,
        source="FLOW-PRIMARY-2024, Table 2 and Discussion, NEJM pp.116 and 119–120.",
        interpretation=(
            "The baseline-to-week 12 estimate is an absolute change and cannot exclude an earlier transient change that had resolved. "
            "The other estimates are slopes; do not extrapolate either to a time-to-dialysis estimate."
        ),
    )
    return save_figure(fig, output_dir, "02_flow_egfr_phases_en")


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
    yes_label: str,
    no_label: str,
    event_notes: Sequence[str],
    source: str,
    interpretation: str,
) -> dict[str, object]:
    fig = new_figure(title, subtitle)
    gs = fig.add_gridspec(
        1,
        3,
        left=0.055,
        right=0.955,
        bottom=0.245,
        top=0.79,
        width_ratios=[3.85, 2.25, 3.05],
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

    ax_label.text(0, len(rows) - 0.39, "Outcome", fontsize=11, fontweight="bold", color=MUTED)
    ax_num.text(0.02, len(rows) - 0.39, "HR (95% CI), P interaction", fontsize=11, fontweight="bold", color=MUTED)

    for row, label, event_note, y in zip(rows, outcome_labels, event_notes, y_positions):
        for ax in (ax_label, ax_plot, ax_num):
            ax.axhspan(y - 0.42, y + 0.42, color=PANEL, zorder=-3)
        ax_label.text(
            0,
            y + 0.15,
            label,
            fontsize=18,
            fontweight="bold",
            va="center",
            linespacing=1.02,
        )
        if event_note:
            ax_label.text(0, y - 0.22, event_note, fontsize=10.5, color=MUTED, va="center")

        yes_effect = number(row["users_effect"])
        yes_low, yes_high = parse_ci(row["users_ci"])
        no_effect = number(row["nonusers_effect"])
        no_low, no_high = parse_ci(row["nonusers_ci"])
        for effect, low, high, offset, color, marker, face in (
            (yes_effect, yes_low, yes_high, +0.13, BLUE_DARK, "o", BLUE),
            (no_effect, no_low, no_high, -0.13, ORANGE, "s", CANVAS),
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

        ax_num.text(
            0.02,
            y + 0.24,
            f"{yes_effect:.2f} ({yes_low:.2f}, {yes_high:.2f})",
            fontsize=18,
            color=BLUE_DARK,
            va="center",
            fontweight="bold",
        )
        ax_num.text(
            0.02,
            y - 0.05,
            f"{no_effect:.2f} ({no_low:.2f}, {no_high:.2f})",
            fontsize=18,
            color=ORANGE_DARK,
            va="center",
            fontweight="bold",
        )
        ax_num.text(
            0.02,
            y - 0.31,
            f"P interaction {row['p_interaction']}",
            fontsize=18,
            color=MUTED,
            va="center",
        )

    ax_plot.set_xscale("log")
    ax_plot.set_xlim(*xlim)
    ax_plot.set_ylim(-0.65, len(rows) - 0.35)
    ax_plot.axvline(1, color=INK, linewidth=1.5, linestyle=(0, (4, 4)), zorder=0)
    ax_plot.xaxis.set_major_locator(FixedLocator(ticks))
    ax_plot.xaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{value:g}"))
    ax_plot.xaxis.set_minor_formatter(NullFormatter())
    ax_plot.grid(axis="x", color=GRID, linewidth=0.8)
    ax_plot.set_yticks([])
    ax_plot.spines[["top", "right", "left"]].set_visible(False)
    ax_plot.set_xlabel("HR (95% CI)", fontsize=13, labelpad=8)
    ax_plot.tick_params(axis="x", labelsize=11)
    ax_plot.text(
        0.02,
        0.015,
        "Favors\nsemaglutide 1.0 mg",
        transform=ax_plot.transAxes,
        fontsize=10,
        color=MUTED,
        ha="left",
        va="bottom",
        linespacing=1.0,
        bbox={"facecolor": CANVAS, "edgecolor": "none", "pad": 1.5},
        zorder=5,
    )
    ax_plot.text(
        0.98,
        0.015,
        "Favors\nplacebo",
        transform=ax_plot.transAxes,
        fontsize=10,
        color=MUTED,
        ha="right",
        va="bottom",
        linespacing=1.0,
        bbox={"facecolor": CANVAS, "edgecolor": "none", "pad": 1.5},
        zorder=5,
    )

    fig.text(0.055, 0.825, "●", color=BLUE, fontsize=18, va="center")
    fig.text(0.074, 0.825, yes_label, color=BLUE_DARK, fontsize=12, va="center")
    fig.text(0.320, 0.825, "□", color=ORANGE, fontsize=19, va="center")
    fig.text(0.340, 0.825, no_label, color=ORANGE_DARK, fontsize=12, va="center")

    add_footer(fig, source=source, interpretation=interpretation)
    return save_figure(fig, output_dir, stem)


def chart_sglt2_subgroup(output_dir: Path) -> dict[str, object]:
    rows = [row for row in read_rows("03_flow_background_subgroups.csv") if row["background"] == "SGLT2i"]

    def event_note(row: Mapping[str, str]) -> str:
        pairs = re.findall(r"\d+/\d+\s+vs\s+\d+/\d+", row["events_note"])
        if len(pairs) != 2:
            raise ValueError(f"Unexpected subgroup event-count text: {row['events_note']!r}")
        yes_text, no_text = (pair.replace(" vs ", "; ") for pair in pairs)
        return f"SGLT2i: Yes {yes_text}   SGLT2i: No {no_text}"

    return _subgroup_forest(
        output_dir=output_dir,
        stem="03_flow_sglt2_subgroup_forest_en",
        title="FLOW outcomes by SGLT2i use at baseline",
        subtitle="Data from the in-trial period (full analysis set)",
        rows=rows,
        outcome_labels=[
            "Composite renal event\n(primary endpoint)",
            "Kidney-specific,\nfour-component outcome",
            "50% reduction in eGFR",
        ],
        xlim=(0.42, 2.55),
        ticks=(0.5, 0.75, 1, 1.5, 2.5),
        yes_label=f"SGLT2i: Yes (N={rows[0]['users_n']})",
        no_label=f"SGLT2i: No (N={int(rows[0]['nonusers_n']):,})",
        event_notes=[
            event_note(rows[0]),
            event_note(rows[1]),
            event_note(rows[2]),
        ],
        source="FLOW-SGLT2-2024, Figures 1–2, Table 1, and Results.",
        interpretation=(
            "Nonrandomized baseline SGLT2i strata were underpowered; HR 1.07 cannot establish harm, no benefit, or additivity.\n"
            "The component P interaction 0.023 was nominal and unadjusted.\n"
            "Reconciliation: Table 2 and subgroup sums give placebo n=213; the source overall row shows 231. This redraw uses 213."
        ),
    )


def chart_mra_subgroup(output_dir: Path) -> dict[str, object]:
    rows = [row for row in read_rows("03_flow_background_subgroups.csv") if row["background"] == "MRA"]
    return _subgroup_forest(
        output_dir=output_dir,
        stem="04_flow_mra_subgroup_forest_en",
        title="FLOW outcomes by MRA use at baseline",
        subtitle="Data from the in-trial period (full analysis set)",
        rows=rows,
        outcome_labels=[
            "Composite kidney event\n(composite primary end point)",
            "Four-component kidney-specific\ncomposite outcome",
            "Renal replacement therapy",
        ],
        xlim=(0.02, 2.05),
        ticks=(0.025, 0.05, 0.1, 0.25, 0.5, 1, 2),
        yes_label=f"MRA use at baseline: Yes (N={rows[0]['users_n']})",
        no_label=f"MRA use at baseline: No (N={int(rows[0]['nonusers_n']):,})",
        event_notes=[
            "MRA use: 59 events; no MRA use: 682 events",
            "",
            "MRA-use subgroup: 11 events",
        ],
        source="FLOW-MRA-2025, Figures 1–2, Supplementary Tables 1–2, and Results.",
        interpretation=(
            "Baseline MRA use was not randomized, and no baseline participant received finerenone. "
            "The renal replacement therapy interaction was based on 11 events and was not adjusted for multiplicity."
        ),
    )


def chart_cross_trial_context(output_dir: Path) -> dict[str, object]:
    rows = read_rows("04_select_soul_pooled.csv")
    select = next(row for row in rows if row["study"] == "SELECT" and "composite" in row["outcome"])
    select_slope = next(row for row in rows if row["study"] == "SELECT" and row["outcome"] == "total eGFR slope")
    soul_five = next(row for row in rows if row["study"] == "SOUL" and "five-point" in row["outcome"])
    soul_four = next(row for row in rows if row["study"] == "SOUL" and "four-point" in row["outcome"])
    soul_slope = next(row for row in rows if row["study"] == "SOUL" and row["outcome"] == "total eGFR slope")
    pooled = [row for row in rows if row["study"] == "SELECT+FLOW+SOUL pooled"]

    def hr_tuple(label: str, row: Mapping[str, str], p_value: str = "") -> tuple[str, float, float, float, str]:
        low, high = parse_ci(row["ci"])
        return label, number(row["effect"]), low, high, p_value

    fig = new_figure(
        "SELECT, SOUL, and pooled kidney outcomes",
        "Hazard ratios and 95% confidence intervals shown on a common scale",
    )
    ax = fig.add_axes([0.045, 0.325, 0.91, 0.47])
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.65, 5.55)
    ax.axis("off")

    row_specs = [
        {
            "study": "SELECT",
            "context": "Obesity + ASCVD\nNo diagnosed diabetes\nN=17,604 · 2.4 mg SC",
            "result": hr_tuple(
                "Time to first occurrence of the\nmain 5-component kidney\ncomposite endpointᵃ.",
                select,
                "P = 0.02",
            ),
            "color": BLUE_DARK,
            "marker": "o",
            "fill": BLUE,
        },
        {
            "study": "SOUL",
            "context": "T2D + ASCVD and/or CKD\nN=9,650 · oral 14 mg",
            "result": hr_tuple("First 5-point composite\nkidney event", soul_five, "P = 0.19"),
            "color": ORANGE,
            "marker": "s",
            "fill": CANVAS,
        },
        {
            "study": "",
            "context": "",
            "result": hr_tuple("First 4-point composite\nkidney event", soul_four, "P = 0.22"),
            "color": ORANGE,
            "marker": "s",
            "fill": CANVAS,
        },
        {
            "study": "POOLED",
            "context": "SELECT + FLOW + SOUL\nN=30,787 · mixed doses/routes",
            "result": hr_tuple("primary kidney composite", pooled[0]),
            "color": BLUE_DARK,
            "marker": "D",
            "fill": CANVAS,
        },
        {
            "study": "",
            "context": "",
            "result": hr_tuple(
                "a narrower secondary kidney composite\n(excluding cardiovascular-related\ndeath from the primary outcome)",
                pooled[1],
            ),
            "color": BLUE_DARK,
            "marker": "D",
            "fill": CANVAS,
        },
    ]
    y_positions = [4.72, 3.62, 2.52, 1.42, 0.18]
    row_half_heights = [0.50, 0.50, 0.50, 0.50, 0.62]

    ax.text(0.018, 5.38, "PROJECT CONTEXT", fontsize=10, fontweight="bold", color=BLUE_DARK, va="center")
    ax.text(0.190, 5.38, "Source outcome label", fontsize=11, fontweight="bold", color=MUTED, va="center")
    ax.text(0.610, 5.38, "HR (95% CI)", fontsize=11, fontweight="bold", color=MUTED, va="center")
    ax.text(0.825, 5.38, "Common log scale", fontsize=11, fontweight="bold", color=MUTED, va="center")

    x_min, x_max = math.log(0.55), math.log(1.2)

    def map_x(value: float) -> float:
        return 0.815 + 0.165 * (math.log(value) - x_min) / (x_max - x_min)

    for tick in (0.6, 0.8, 1.0, 1.2):
        tick_x = map_x(tick)
        ax.plot([tick_x, tick_x], [-0.27, 5.15], color=GRID, linewidth=0.75, zorder=-2)
        ax.text(tick_x, -0.42, f"{tick:g}", ha="center", va="top", fontsize=10.5, color=MUTED)
    ax.plot([map_x(1.0), map_x(1.0)], [-0.27, 5.15], color=INK, linewidth=1.3, linestyle=(0, (4, 4)))

    for index, (spec, y, half_height) in enumerate(zip(row_specs, y_positions, row_half_heights)):
        ax.axhspan(
            y - half_height,
            y + half_height,
            xmin=0.0,
            xmax=1.0,
            facecolor=BLUE_LIGHT if index == 0 else PANEL,
            alpha=0.82 if index == 0 else 1.0,
            zorder=-4,
        )
        if spec["study"]:
            ax.text(0.018, y + 0.30, spec["study"], fontsize=18, fontweight="bold", va="center", linespacing=0.95)
            ax.text(0.018, y - 0.23, spec["context"], fontsize=10, color=MUTED, va="center", linespacing=0.88)

        label, effect, low, high, p_value = spec["result"]
        ax.text(
            0.190,
            y,
            label,
            fontsize=18,
            va="center",
            linespacing=0.92,
            color=INK,
        )
        ax.text(
            0.610,
            y + (0.16 if p_value else 0),
            f"{effect:.2f} ({low:.2f}–{high:.2f})",
            fontsize=18,
            fontweight="bold",
            color=spec["color"],
            va="center",
        )
        if p_value:
            ax.text(0.610, y - 0.25, p_value, fontsize=18, color=MUTED, va="center")

        ax.plot(
            [map_x(low), map_x(high)],
            [y, y],
            color=spec["color"],
            linewidth=2.6,
            solid_capstyle="round",
            zorder=2,
        )
        ax.scatter(
            [map_x(effect)],
            [y],
            s=82,
            marker=spec["marker"],
            facecolor=spec["fill"],
            edgecolor=spec["color"],
            linewidth=1.9,
            zorder=3,
        )

    slope_select = fig.add_axes([0.045, 0.145, 0.445, 0.170])
    slope_soul = fig.add_axes([0.510, 0.145, 0.445, 0.170])
    for slope_ax in (slope_select, slope_soul):
        slope_ax.set_xlim(0, 1)
        slope_ax.set_ylim(0, 1)
        slope_ax.axis("off")
        rounded_box(slope_ax, 0, 0, 1, 1, facecolor=BLUE_LIGHT, edgecolor=GRID, radius=0.025)

    slope_select.text(0.035, 0.94, "SELECT · SOURCE SLOPE RESULT", fontsize=10, fontweight="bold", color=BLUE_DARK, va="top")
    slope_select.text(0.035, 0.62, "Total eGFR slope, ml min−1 m−2 per year", fontsize=18, va="center")
    slope_select.text(
        0.035,
        0.24,
        f"{number(select_slope['effect']):.2f} ({select_slope['ci'].replace('–', ', ')}); P < 0.001",
        fontsize=18,
        fontweight="bold",
        color=BLUE_DARK,
        va="center",
    )

    slope_soul.text(0.035, 0.94, "SOUL · SOURCE SLOPE RESULT", fontsize=10, fontweight="bold", color=ORANGE_DARK, va="top")
    slope_soul.text(
        0.025,
        0.60,
        "Annual rate of change in eGFR\n(mL/min/1.73 m²)",
        fontsize=18,
        va="center",
        linespacing=0.86,
    )
    slope_soul.text(
        0.035,
        0.19,
        "Oral sema: −1.67; placebo: −2.06\nETD 0.40 (95% CI 0.27, 0.53)",
        fontsize=18,
        fontweight="bold",
        color=ORANGE_DARK,
        va="center",
        linespacing=0.86,
    )

    add_footer(
        fig,
        source=(
            "SELECT-KIDNEY-2024, Figure 1, Table 1, and Results. SOUL-KIDNEY-2026, Results. "
            "SELECT-FLOW-SOUL-POOLED-2026, Methods and Findings. The SELECT label retains the source panel marker ᵃ."
        ),
        interpretation=(
            "SELECT P = 0.02 was not adjusted for multiplicity. After SOUL's five-point gate failed, its displayed slope "
            "was formally exploratory. Pooled estimates reuse component-trial participants and do not support cross-trial, dose, or route ranking."
        ),
    )
    return save_figure(fig, output_dir, "05_select_soul_pooled_context_en")


def chart_flow_safety(output_dir: Path) -> dict[str, object]:
    rows = read_rows("05_flow_safety.csv")
    # Locked source wording from FLOW Table 3 and Supplementary Tables S4–S5.
    labels = [
        "Serious adverse event",
        "Adverse events leading to permanent\ntrial product discontinuation",
        "Gastrointestinal disorders",
        "Acute kidney injury",
        "Dehydration",
        "Severe hypoglycemia*",
        "Diabetic retinopathy*",
    ]
    short_locators = ["Table 3", "Table S5", "Table S5", "Table S4", "Table S4", "Table 3", "Table 3"]
    y_positions = list(reversed(range(len(rows))))

    fig = new_figure(
        "FLOW safety outcomes",
        "No. of participants (%)",
    )
    gs = fig.add_gridspec(
        1,
        3,
        left=0.055,
        right=0.955,
        bottom=0.235,
        top=0.79,
        width_ratios=[4.35, 3.00, 1.65],
        wspace=0.025,
    )
    ax_label = fig.add_subplot(gs[0, 0])
    ax_plot = fig.add_subplot(gs[0, 1])
    ax_source = fig.add_subplot(gs[0, 2])
    for ax in (ax_label, ax_source):
        ax.set_xlim(0, 1)
        ax.set_ylim(-0.65, 6.65)
        ax.axis("off")
    ax_label.text(0, 6.58, "Adverse Event", fontsize=11, color=MUTED, fontweight="bold")
    ax_source.text(0.03, 6.58, "Source locator", fontsize=11, color=MUTED, fontweight="bold")

    for index, (row, label, locator, y) in enumerate(zip(rows, labels, short_locators, y_positions)):
        if y % 2 == 0:
            for ax in (ax_label, ax_plot, ax_source):
                ax.axhspan(y - 0.43, y + 0.43, color=PANEL, zorder=-4)
        semaglutide = number(row["sema_pct"])
        placebo = number(row["placebo_pct"])
        ax_label.text(
            0,
            y + 0.14,
            label,
            fontsize=18,
            fontweight="bold" if y in (6, 4) else "normal",
            linespacing=1.02,
            va="center",
        )
        ax_label.text(
            0,
            y - (0.43 if index == 1 else 0.31),
            f"{row['sema_n']} ({semaglutide:.1f}%) vs {row['placebo_n']} ({placebo:.1f}%)",
            fontsize=10.5,
            color=MUTED,
            va="center",
        )
        ax_plot.plot(
            [min(semaglutide, placebo), max(semaglutide, placebo)],
            [y, y],
            color=GRID_DARK,
            linewidth=2.0,
            zorder=1,
        )
        ax_plot.scatter(
            [semaglutide],
            [y],
            s=88,
            marker="o",
            facecolor=BLUE,
            edgecolor=BLUE_DARK,
            linewidth=1.7,
            zorder=3,
        )
        ax_plot.scatter(
            [placebo],
            [y],
            s=112,
            marker="s",
            facecolor="none",
            edgecolor=ORANGE,
            linewidth=2.2,
            zorder=4,
        )
        if math.isclose(semaglutide, placebo, abs_tol=0.04):
            ax_plot.annotate(
                f"{semaglutide:.1f}% vs {placebo:.1f}%",
                (semaglutide, y),
                xytext=(12, 0),
                textcoords="offset points",
                va="center",
                fontsize=18,
                color=INK,
            )
        else:
            ax_plot.annotate(
                f"{semaglutide:.1f}",
                (semaglutide, y),
                xytext=(0, 13),
                textcoords="offset points",
                ha="center",
                fontsize=18,
                color=BLUE_DARK,
                fontweight="bold",
            )
            ax_plot.annotate(
                f"{placebo:.1f}",
                (placebo, y),
                xytext=(0, -22),
                textcoords="offset points",
                ha="center",
                fontsize=18,
                color=ORANGE_DARK,
                fontweight="bold",
            )
        ax_source.text(0.03, y, locator, fontsize=12, va="center", color=INK)

    ax_plot.set_xlim(-2, 58)
    ax_plot.set_ylim(-0.65, 6.65)
    ax_plot.set_yticks([])
    ax_plot.set_xlabel("No. of participants (%)", fontsize=13, labelpad=8)
    ax_plot.xaxis.set_major_locator(FixedLocator([0, 10, 20, 30, 40, 50]))
    ax_plot.grid(axis="x", color=GRID, linewidth=0.8)
    ax_plot.spines[["top", "right", "left"]].set_visible(False)
    ax_plot.tick_params(axis="x", labelsize=11)
    fig.text(0.405, 0.817, "● Semaglutide", fontsize=12, color=BLUE_DARK, va="center")
    fig.text(0.545, 0.817, "□ Placebo", fontsize=12, color=ORANGE_DARK, va="center")

    add_footer(
        fig,
        source=(
            "FLOW-PRIMARY-2024, Table 3, NEJM p.120; FLOW-SUPPLEMENT-2024, Table S4, PDF pp.29–30, and Table S5, "
            "PDF p.32. * Data were from an additional data-collection form; see Table 3 footnote, p.120."
        ),
        interpretation=(
            "The shared percentage axis is a project harmonization across Table 3 and Tables S4–S5. Gastrointestinal disorders are nested "
            "within permanent-discontinuation events; acute kidney injury and dehydration are preferred terms within serious adverse events."
        ),
    )
    return save_figure(fig, output_dir, "06_flow_safety_dotplot_en")


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
        help="Generate only selected chart numbers, for example: --only 01 03.",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        help="Manifest path. The default is MANIFEST.json inside the output directory.",
    )
    args = parser.parse_args()

    selected = args.only or sorted(CHART_BUILDERS)
    output_dir = args.output_dir.resolve()
    outputs = [CHART_BUILDERS[key](output_dir) for key in selected]
    manifest = {
        "generator": manifest_reference(Path(__file__).resolve()),
        "language": "English",
        "label_policy": (
            "Official English endpoint, axis, and legend wording is retained. "
            "Project interpretation appears only in an explicitly labelled footer."
        ),
        "common_caption": COMMON_CAPTION,
        "evidence_cutoff": "2026-09-05",
        "generated_for_release": "2026-09-06",
        "canvas_inches": [SLIDE_WIDTH_IN, SLIDE_HEIGHT_IN],
        "preview_dpi": PREVIEW_DPI,
        "png_dpi": PNG_DPI,
        "png_default_for_slides": True,
        "source_data": [
            manifest_reference(DATA_DIR / "01_flow_primary_outcomes.csv"),
            manifest_reference(DATA_DIR / "02_flow_egfr_uacr.csv"),
            manifest_reference(DATA_DIR / "03_flow_background_subgroups.csv"),
            manifest_reference(DATA_DIR / "04_select_soul_pooled.csv"),
            manifest_reference(DATA_DIR / "05_flow_safety.csv"),
        ],
        "chart_contracts": CHART_CONTRACTS,
        "outputs": outputs,
    }
    manifest_path = args.manifest.resolve() if args.manifest else output_dir / "MANIFEST.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
