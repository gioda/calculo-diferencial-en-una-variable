# Construcción

## Requisitos

- LuaLaTeX con `fontspec`, Libertinus, TikZ y los paquetes usados por las fuentes;
- Python ≥ 3.9;
- NumPy y Matplotlib, según [requirements.txt](requirements.txt).

Desde la raíz de esta carpeta:

```sh
make all
```

`make figures` regenera las dos figuras de Taylor y las ocho figuras de los
laboratorios. `make pdfs` construye los dos libros y las hojas P01--P13. Los PDF
quedan en `books/` y `handouts/`.

La construcción usa únicamente rutas relativas y no necesita los registros,
renderizadores ni soluciones completas del proyecto privado.
