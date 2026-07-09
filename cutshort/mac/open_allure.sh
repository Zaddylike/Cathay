#!/bin/sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PROJECT_ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/../.." && pwd)

cd "$PROJECT_ROOT"

if command -v allure >/dev/null 2>&1; then
    allure open reports/allure-report
elif command -v npx >/dev/null 2>&1; then
    npx --no-install allure open reports/allure-report
else
    echo "Allure command not found. Install allure or run npm install first." >&2
    exit 127
fi
