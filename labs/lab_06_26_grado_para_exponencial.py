#!/usr/bin/env python3
# Copyright (c) 2026 Giovanni Dalmasso
# SPDX-License-Identifier: MIT
# Source traceability: CDV1-E0284

"""Búsqueda de un grado suficiente para aproximar exp(0.5)."""

import math

import matplotlib.pyplot as plt


# Parámetros que puedes modificar
x = 0.5
tolerancia = 1e-8


def main():
    if x < 0:
        raise ValueError("Este ejemplo utiliza un valor x no negativo.")
    if tolerancia <= 0:
        raise ValueError("La tolerancia debe ser positiva.")

    grado = 0
    cotas = []
    while True:
        cota = math.exp(x) * x ** (grado + 1) / math.factorial(grado + 1)
        cotas.append(cota)
        if cota < tolerancia:
            break
        grado += 1

    aproximacion = sum(x**k / math.factorial(k) for k in range(grado + 1))
    error = abs(math.exp(x) - aproximacion)

    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.semilogy(range(len(cotas)), cotas, "o-")
    ax.axhline(tolerancia, color="#d95f02", linestyle="--", label="tolerancia")
    ax.set(
        title="Ejercicio 6.26: criterio de parada",
        xlabel="grado",
        ylabel="cota",
    )
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()
    print(f"Primer grado que cumple la cota: {grado}")
    print(f"Cota: {cota:.6g}; error observado: {error:.6g}")
    plt.show()


if __name__ == "__main__":
    main()
