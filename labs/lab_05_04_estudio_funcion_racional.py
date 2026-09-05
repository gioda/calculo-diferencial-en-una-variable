#!/usr/bin/env python3
# Copyright (c) 2026 Giovanni Dalmasso
# SPDX-License-Identifier: MIT
# Source traceability: CDV1-E0235

"""Estudio gráfico de f(x) = (x² - 1)/(x² + 1)."""

import matplotlib.pyplot as plt
import numpy as np


# Parámetros que puedes modificar
x_min = -4.0
x_max = 4.0
num_puntos = 1201


def main():
    if x_min >= x_max:
        raise ValueError("El intervalo debe cumplir x_min < x_max.")

    x = np.linspace(x_min, x_max, num_puntos)
    denominador = (x**2 + 1) ** 3
    f = (x**2 - 1) / (x**2 + 1)
    derivada = 4 * x / (x**2 + 1) ** 2
    segunda_derivada = 4 * (1 - 3 * x**2) / denominador

    fig, axes = plt.subplots(3, 1, figsize=(8, 9), sharex=True)
    etiquetas = ("f", "f'", "f''")
    for ax, y, etiqueta in zip(axes, (f, derivada, segunda_derivada), etiquetas):
        ax.plot(x, y, linewidth=2, label=etiqueta)
        ax.axhline(0, color="#333333", linewidth=0.7)
        ax.grid(alpha=0.25)
        ax.legend()

    axes[0].axhline(1, color="#d95f02", linestyle="--", label="y = 1")
    axes[0].legend()
    axes[-1].set_xlabel("x")
    fig.suptitle("Ejercicio 5.4: estudio y verificación")
    fig.tight_layout()
    print("Puntos de inflexión: x = ±1/√3.")
    plt.show()


if __name__ == "__main__":
    main()
