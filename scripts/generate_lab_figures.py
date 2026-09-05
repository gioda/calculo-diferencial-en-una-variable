#!/usr/bin/env python3
# Copyright (c) 2026 Giovanni Dalmasso
# SPDX-License-Identifier: MIT
"""Run the eight public laboratories headlessly and save their figures."""

from __future__ import annotations

import runpy
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "src" / "problems" / "assets" / "lab_figures"
LABS = (
    ("lab_05_04_estudio_funcion_racional.py", "lab_05_04_estudio_funcion_racional.png"),
    ("lab_05_24_ramas_y_asintotas.py", "lab_05_24_ramas_y_asintotas.png"),
    ("lab_05_25_asintotas_x_menos_inversa.py", "lab_05_25_asintotas_x_menos_inversa.png"),
    ("lab_05_28_aliasing_y_mallas.py", "lab_05_28_aliasing_y_mallas.png"),
    ("lab_06_04_orden_de_contacto.py", "lab_06_04_orden_de_contacto.png"),
    ("lab_06_16_resto_de_lagrange.py", "lab_06_16_resto_de_lagrange.png"),
    ("lab_06_20_taylor_del_seno.py", "lab_06_20_taylor_del_seno.png"),
    ("lab_06_26_grado_para_exponencial.py", "lab_06_26_grado_para_exponencial.png"),
)


def run_lab(script_name: str, output_name: str) -> None:
    output_path = OUTPUT / output_name
    original_show = plt.show

    def save_current_figure(*_args: object, **_kwargs: object) -> None:
        plt.gcf().savefig(output_path, dpi=180, bbox_inches="tight")

    plt.show = save_current_figure
    try:
        runpy.run_path(str(ROOT / "labs" / script_name), run_name="__main__")
    finally:
        plt.show = original_show
        plt.close("all")
    if not output_path.is_file() or output_path.stat().st_size == 0:
        raise RuntimeError(f"No figure was generated for {script_name}")


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for script_name, output_name in LABS:
        run_lab(script_name, output_name)
    print("PUBLIC_LAB_FIGURES_PASS")


if __name__ == "__main__":
    main()
