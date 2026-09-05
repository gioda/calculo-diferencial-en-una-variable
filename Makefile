# Copyright (c) 2026 Giovanni Dalmasso
# SPDX-License-Identifier: MIT

PYTHON ?= python3

.PHONY: all figures pdfs

all: figures pdfs

figures:
	$(PYTHON) scripts/figures/chapter_06_taylor_plots.py
	$(PYTHON) scripts/generate_lab_figures.py

pdfs:
	bash scripts/build_publication.sh
