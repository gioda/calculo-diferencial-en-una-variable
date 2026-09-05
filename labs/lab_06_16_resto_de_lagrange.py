#!/usr/bin/env python3
# Copyright (c) 2026 Giovanni Dalmasso
# SPDX-License-Identifier: MIT
# Source traceability: CDV1-E0275

"""Comparación del error de Taylor de exp(x) con la cota de Lagrange."""

import matplotlib.pyplot as plt
import numpy as np


# Parámetros que puedes modificar
x_min = -1.0
x_max = 1.0
num_puntos = 1201


def main():
    if x_min >= x_max:
        raise ValueError("El intervalo debe cumplir x_min < x_max.")

    x = np.linspace(x_min, x_max, num_puntos)
    p3 = 1 + x + x**2 / 2 + x**3 / 6
    error = np.abs(np.exp(x) - p3)
    cota = np.e * np.abs(x) ** 4 / 24
    if np.any(error > cota + 1e-13):
        raise ValueError("La comprobación numérica de la cota no se cumple.")

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.semilogy(x, np.maximum(error, 1e-18), label="error real")
    ax.semilogy(x, np.maximum(cota, 1e-18), "--", label="cota")
    ax.set(
        title="Ejercicio 6.16: resto de Lagrange",
        xlabel="x",
        ylabel="magnitud",
    )
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()
    print(f"Error máximo observado: {error.max():.6g}")
    print("La cota se cumple en todos los puntos de la malla.")
    plt.show()


if __name__ == "__main__":
    main()
