#!/usr/bin/env bash
# ==============================================================================
# Lanzador del Tablero de Control (Paper Command Center) para QMLEEG
# ==============================================================================
set -euo pipefail

PORT="${1:-8080}"
echo "==> Lanzando Paper Command Center de PaperSmith en puerto ${PORT}..."

if command -v smith >/dev/null 2>&1; then
    exec smith ui --port "${PORT}"
elif command -v papersmith >/dev/null 2>&1; then
    exec papersmith ui --port "${PORT}"
else
    exec /Users/andresalvarez/Library/Caches/papersmith-envs/papersmith-ai/.venv/bin/smith ui --port "${PORT}"
fi
