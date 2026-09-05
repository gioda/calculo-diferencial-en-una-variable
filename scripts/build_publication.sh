#!/usr/bin/env bash
# Copyright (c) 2026 Giovanni Dalmasso
# SPDX-License-Identifier: MIT
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"
cache_root="$(mktemp -d cduv-public-build-cache.XXXXXX)"
cleanup() {
  rm -rf "$cache_root"
}
trap cleanup EXIT
export TEXMFCACHE="$cache_root/texmf-cache"
export TEXMFVAR="$cache_root/texmf-var"
export XDG_CACHE_HOME="$cache_root/xdg-cache"
mkdir -p "$TEXMFCACHE" "$TEXMFVAR" "$XDG_CACHE_HOME"

build_one() {
  source_file="$1"
  destination="$2"
  job_name="$3"
  build_dir=".build/$job_name"
  mkdir -p "$build_dir" "$(dirname "$destination")"
  lualatex -interaction=nonstopmode -halt-on-error -file-line-error \
    -recorder -output-directory="$build_dir" -jobname="$job_name" "$source_file" >/dev/null
  lualatex -interaction=nonstopmode -halt-on-error -file-line-error \
    -recorder -output-directory="$build_dir" -jobname="$job_name" "$source_file" >/dev/null
  lualatex -interaction=nonstopmode -halt-on-error -file-line-error \
    -recorder -output-directory="$build_dir" -jobname="$job_name" "$source_file" >/dev/null
  cp "$build_dir/$job_name.pdf" "$destination"
}

build_one src/theory/main.tex books/calculo_diferencial_teoria_v1.0.pdf teoria_v1_0
build_one src/problems/main.tex books/calculo_diferencial_problemas_practicas_estudio_v1.0.pdf problemas_v1_0

for source_file in src/problems/handouts/P*.tex; do
  stem="$(basename "$source_file" .tex)"
  lower_stem="$(printf '%s' "$stem" | tr '[:upper:]' '[:lower:]')"
  build_one "$source_file" "handouts/${lower_stem}_estudiantes_v1.0.pdf" "${lower_stem}_v1_0"
done
