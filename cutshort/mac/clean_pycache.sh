#!/bin/sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PROJECT_ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/../.." && pwd)

cd "$PROJECT_ROOT"

echo "=============================="
echo "Cleaning __pycache__ folders..."
echo "=============================="
find "$PROJECT_ROOT" -type d -name "__pycache__" -prune -print -exec rm -rf {} +

echo
echo "=============================="
echo "Cleaning .pyc files..."
echo "=============================="
find "$PROJECT_ROOT" -type f -name "*.pyc" -print -delete

echo
echo "=============================="
echo "Clean completed."
echo "=============================="
