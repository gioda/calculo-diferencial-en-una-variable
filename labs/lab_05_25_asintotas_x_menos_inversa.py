#!/usr/bin/env python3
# Copyright (c) 2026 Giovanni Dalmasso
# SPDX-License-Identifier: MIT
# Source traceability: CDV1-E0025

"""Representación de f(x) = x - 1/x y de sus asíntotas."""

import matplotlib.pyplot as plt
import numpy as np


# Parámetros que puedes modificar
x_min = -5.0
x_max = 5.0
distancia_al_cero = 0.15
puntos_por_rama = 700


def f(x):
    return x - 1 / x


def main():
    if not x_min < -distancia_al_cero < 0 < distancia_al_cero < x_max:
        raise ValueError("El intervalo debe contener 0 y dejar un hueco positivo.")

    rama_izquierda = np.linspace(x_min, -distancia_al_cero, puntos_por_rama)
    rama_derecha = np.linspace(distancia_al_cero, x_max, puntos_por_rama)

    fig, ax = plt.subplots(figsize=(8, 5))
    for x in (rama_izquierda, rama_derecha):
        ax.plot(x, f(x), color="#126782", linewidth=2)

    x_asintota = np.linspace(x_min, x_max, puntos_por_rama)
    ax.plot(x_asintota, x_asintota, "--", color="#d95f02", label="y = x")
    ax.axvline(0, linestyle=":", color="#333333", label="x = 0")
    ax.set(
        xlim=(x_min, x_max),
        ylim=(-8, 8),
        title="Ejercicio 5.25: f(x) = x - 1/x",
        xlabel="x",
        ylabel="y",
    )
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()
    print("Ramas representadas: 2. Asíntotas: x = 0 e y = x.")
    plt.show()


if __name__ == "__main__":
    main()
