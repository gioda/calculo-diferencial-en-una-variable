#!/usr/bin/env python3
# Copyright (c) 2026 Giovanni Dalmasso
# SPDX-License-Identifier: MIT
# Source traceability: CDV1-E0263

"""Estimación del orden de contacto de sen(x) cerca de 0."""

import matplotlib.pyplot as plt
import numpy as np


# Parámetros que puedes modificar
x_min = 1e-4
x_max = 10**-0.2
num_puntos = 500


def main():
    if not 0 < x_min < x_max:
        raise ValueError("El intervalo debe cumplir 0 < x_min < x_max.")

    x = np.logspace(np.log10(x_min), np.log10(x_max), num_puntos)
    error_lineal = np.abs(np.sin(x) - x)
    p3 = x - x**3 / 6
    error_cubico = np.abs(np.sin(x) - p3)

    pendiente_lineal = np.polyfit(
        np.log(x[:300]), np.log(error_lineal[:300]), 1
    )[0]
    zona_estable = error_cubico > 1e-16
    pendiente_cubica = np.polyfit(
        np.log(x[zona_estable]), np.log(error_cubico[zona_estable]), 1
    )[0]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.loglog(x, error_lineal, label="|sen x - x|")
    ax.loglog(x, error_cubico, "--", label="|sen x - P3|")
    ax.set(
        title="Ejercicio 6.4: orden de contacto",
        xlabel="|x|",
        ylabel="error",
    )
    ax.grid(True, which="both", alpha=0.25)
    ax.legend()
    fig.tight_layout()
    print(f"Pendiente para |sen x - x|: {pendiente_lineal:.3f}")
    print(f"Pendiente para |sen x - P3|: {pendiente_cubica:.3f}")
    plt.show()


if __name__ == "__main__":
    main()
