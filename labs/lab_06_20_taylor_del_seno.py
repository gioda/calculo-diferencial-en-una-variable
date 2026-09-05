#!/usr/bin/env python3
# Copyright (c) 2026 Giovanni Dalmasso
# SPDX-License-Identifier: MIT
# Source traceability: CDV1-E0027

"""Comparación de sen(x) con sus polinomios de Taylor P3 y P5."""

import matplotlib.pyplot as plt
import numpy as np


# Parámetros que puedes modificar
x_min = -2.0
x_max = 2.0
num_puntos = 1001


def main():
    if x_min >= x_max:
        raise ValueError("El intervalo debe cumplir x_min < x_max.")

    x = np.linspace(x_min, x_max, num_puntos)
    seno = np.sin(x)
    p3 = x - x**3 / 6
    p5 = p3 + x**5 / 120
    error_p3 = np.abs(seno - p3)
    error_p5 = np.abs(seno - p5)

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    axes[0].plot(x, seno, label="sen x", linewidth=2)
    axes[0].plot(x, p3, "--", label="P3")
    axes[0].plot(x, p5, ":", label="P5")
    axes[0].set_title("Aproximaciones")
    axes[0].legend()
    axes[0].grid(alpha=0.25)

    axes[1].semilogy(x, np.maximum(error_p3, 1e-18), label="|sen - P3|")
    axes[1].semilogy(x, np.maximum(error_p5, 1e-18), "--", label="|sen - P5|")
    axes[1].set_title("Errores absolutos")
    axes[1].legend()
    axes[1].grid(alpha=0.25)

    fig.suptitle("Ejercicio 6.20: Taylor del seno")
    fig.tight_layout()
    print(f"Error máximo de P3 en la malla: {error_p3.max():.6g}")
    print(f"Error máximo de P5 en la malla: {error_p5.max():.6g}")
    plt.show()


if __name__ == "__main__":
    main()
