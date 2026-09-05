#!/usr/bin/env python3
# Copyright (c) 2026 Giovanni Dalmasso
# SPDX-License-Identifier: MIT
# Source traceability: CDV1-E0256

"""Representación separada de las tres ramas de x²/(x² - 1)."""

import matplotlib.pyplot as plt
import numpy as np


# Parámetros que puedes modificar
x_min = -5.0
x_max = 5.0
distancia_a_asintota = 0.05
puntos_por_rama = 900


def f(x):
    return x**2 / (x**2 - 1)


def main():
    if not x_min < -1 - distancia_a_asintota < 1 + distancia_a_asintota < x_max:
        raise ValueError("El intervalo debe contener las asíntotas x = -1 y x = 1.")

    ramas = (
        np.linspace(x_min, -1 - distancia_a_asintota, puntos_por_rama),
        np.linspace(-1 + distancia_a_asintota, 1 - distancia_a_asintota, puntos_por_rama),
        np.linspace(1 + distancia_a_asintota, x_max, puntos_por_rama),
    )

    fig, ax = plt.subplots(figsize=(8, 5))
    for x in ramas:
        ax.plot(x, f(x), color="#126782", linewidth=2)

    ax.axhline(1, linestyle="--", color="#d95f02", label="y = 1")
    ax.axvline(-1, linestyle=":", color="#333333", label="x = ±1")
    ax.axvline(1, linestyle=":", color="#333333")
    ax.set(
        xlim=(x_min, x_max),
        ylim=(-6, 6),
        title="Ejercicio 5.24: tres ramas separadas",
        xlabel="x",
        ylabel="f(x)",
    )
    ax.legend()
    ax.grid(alpha=0.25)
    fig.tight_layout()
    print("Ramas representadas: 3, sin unir la gráfica en x = -1 ni x = 1.")
    plt.show()


if __name__ == "__main__":
    main()
