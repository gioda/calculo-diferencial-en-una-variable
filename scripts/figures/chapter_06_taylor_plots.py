#!/usr/bin/env python3
# Copyright (c) 2026 Giovanni Dalmasso
# SPDX-License-Identifier: MIT

"""Generate the two deterministic Taylor plots used in the public theory book."""

from __future__ import annotations

from datetime import datetime, timezone
from math import pi, sin
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


OUTPUT_DIR = Path(__file__).resolve().parents[2] / "src" / "theory" / "assets" / "plots"
FIXED_TIME = datetime(2026, 8, 23, 0, 0, 0, tzinfo=timezone.utc)
SAMPLES = 1201
X_MIN = -pi
X_MAX = pi

NAVY = "#17324D"
TEAL = "#16706A"
AMBER = "#A65F00"
RED = "#9A3030"
INK = "#20262D"
GRID = "#C9D1D9"


def sample_points() -> list[float]:
    step = (X_MAX - X_MIN) / (SAMPLES - 1)
    return [X_MIN + index * step for index in range(SAMPLES)]


def p1(x: float) -> float:
    return x


def p3(x: float) -> float:
    return x - x**3 / 6


def p5(x: float) -> float:
    return x - x**3 / 6 + x**5 / 120


def configure() -> None:
    matplotlib.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 9.5,
            "axes.labelcolor": INK,
            "axes.edgecolor": INK,
            "axes.titlecolor": INK,
            "xtick.color": INK,
            "ytick.color": INK,
            "text.color": INK,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "pdf.compression": 9,
            "svg.hashsalt": "cduv-public-v1-ch06",
        }
    )


def save_vector_pair(fig: plt.Figure, stem: str, title: str, subject: str) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    common = {
        "Title": title,
        "Author": "Giovanni Dalmasso",
        "Subject": subject,
        "Creator": "Deterministic Matplotlib plot generator",
    }
    fig.savefig(
        OUTPUT_DIR / f"{stem}.pdf",
        format="pdf",
        bbox_inches="tight",
        metadata={**common, "CreationDate": FIXED_TIME, "ModDate": FIXED_TIME},
    )
    fig.savefig(
        OUTPUT_DIR / f"{stem}.svg",
        format="svg",
        bbox_inches="tight",
        metadata={
            "Title": title,
            "Creator": common["Creator"],
            "Description": subject,
            "Date": "2026-08-23",
            "Language": "es",
        },
    )


def approximation_plot(xs: list[float]) -> None:
    values = [sin(x) for x in xs]
    fig, ax = plt.subplots(figsize=(7.1, 4.15), constrained_layout=True)
    ax.plot(xs, values, color=INK, linewidth=2.5, label=r"$\sin x$")
    ax.plot(xs, [p1(x) for x in xs], color=RED, linestyle=(0, (6, 3)), linewidth=1.8, label=r"$P_1(x)=x$")
    ax.plot(xs, [p3(x) for x in xs], color=AMBER, linestyle="dashdot", linewidth=1.9, label=r"$P_3(x)=x-x^3/6$")
    ax.plot(xs, [p5(x) for x in xs], color=TEAL, linestyle=(0, (2, 2)), linewidth=2.2, label=r"$P_5(x)=x-x^3/6+x^5/120$")
    ax.axvline(0, color=GRID, linewidth=0.9)
    ax.axhline(0, color=GRID, linewidth=0.9)
    ax.set_xlim(X_MIN, X_MAX)
    ax.set_ylim(-2.2, 2.2)
    ax.set_xlabel("x (radianes)")
    ax.set_ylabel("valor")
    ax.set_title(r"Aproximación local de $\sin x$ en torno a $0$")
    ax.grid(True, color=GRID, linewidth=0.55, alpha=0.8)
    ax.legend(loc="upper left", frameon=True, framealpha=0.96, ncol=2)
    save_vector_pair(
        fig,
        "taylor_approximation",
        "Comparación de sin(x) con P1, P3 y P5",
        "Gráfico vectorial original para el Capítulo 6.",
    )
    plt.close(fig)


def error_plot(xs: list[float]) -> None:
    values = [sin(x) for x in xs]
    errors = {
        r"$|\sin x-P_1(x)|$": ([abs(y - p1(x)) for x, y in zip(xs, values)], RED, (0, (6, 3))),
        r"$|\sin x-P_3(x)|$": ([abs(y - p3(x)) for x, y in zip(xs, values)], AMBER, "dashdot"),
        r"$|\sin x-P_5(x)|$": ([abs(y - p5(x)) for x, y in zip(xs, values)], TEAL, (0, (2, 2))),
    }
    fig, ax = plt.subplots(figsize=(7.1, 4.15), constrained_layout=True)
    for label, (ys, color, style) in errors.items():
        ax.plot(xs, ys, color=color, linestyle=style, linewidth=2.1, label=label)
    ax.axvline(0, color=GRID, linewidth=0.9)
    ax.set_xlim(X_MIN, X_MAX)
    ax.set_ylim(0, 3.25)
    ax.set_xlabel("x (radianes)")
    ax.set_ylabel("error absoluto")
    ax.set_title("Error de las aproximaciones de Taylor")
    ax.grid(True, color=GRID, linewidth=0.55, alpha=0.8)
    ax.legend(loc="upper center", frameon=True, framealpha=0.96, ncol=3)
    save_vector_pair(
        fig,
        "taylor_error",
        "Error absoluto de P1, P3 y P5 para sin(x)",
        "Gráfico vectorial original para interpretar el error de aproximación.",
    )
    plt.close(fig)


def main() -> None:
    configure()
    xs = sample_points()
    approximation_plot(xs)
    error_plot(xs)
    print(f"TAYLOR_PLOTS_GENERATED output={OUTPUT_DIR} samples={SAMPLES} interval=[-pi,pi]")


if __name__ == "__main__":
    main()
