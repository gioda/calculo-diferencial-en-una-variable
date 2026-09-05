#!/usr/bin/env python3
# Copyright (c) 2026 Giovanni Dalmasso
# SPDX-License-Identifier: MIT
# Source traceability: CDV1-E0259

"""Comparación de dos mallas para observar aliasing en sen(40x)."""

import matplotlib.pyplot as plt
import numpy as np


# Parámetros que puedes modificar
frecuencia = 40
puntos_malla_gruesa = 41
puntos_malla_fina = 4001


def main():
    if puntos_malla_gruesa < 2 or puntos_malla_fina < 2:
        raise ValueError("Cada malla debe contener al menos dos puntos.")

    x_gruesa = np.linspace(0, 2 * np.pi, puntos_malla_gruesa)
    x_fina = np.linspace(0, 2 * np.pi, puntos_malla_fina)

    fig, axes = plt.subplots(2, 1, figsize=(9, 6), sharex=True)
    axes[0].plot(x_gruesa, np.sin(frecuencia * x_gruesa), "o-", markersize=3)
    axes[0].set_title("Malla gruesa: aliasing")
    axes[1].plot(x_fina, np.sin(frecuencia * x_fina), linewidth=1)
    axes[1].set_title("Malla fina")
    for ax in axes:
        ax.grid(alpha=0.25)
    axes[1].set_xlabel("x")
    fig.suptitle("Ejercicio 5.28: aliasing y resolución")
    fig.tight_layout()
    print(
        f"Puntos usados: {puntos_malla_gruesa} en la malla gruesa "
        f"y {puntos_malla_fina} en la fina."
    )
    plt.show()


if __name__ == "__main__":
    main()
