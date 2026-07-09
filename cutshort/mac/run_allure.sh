#!/bin/sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PROJECT_ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/../.." && pwd)

cd "$PROJECT_ROOT"

run_allure() {
    if command -v allure >/dev/null 2>&1; then
        allure "$@"
        return
    fi

    if command -v npx >/dev/null 2>&1; then
        npx --no-install allure "$@"
        return
    fi

    echo "Allure command not found. Install allure or run npm install first." >&2
    exit 127
}

"$SCRIPT_DIR/clean_pycache.sh"

echo "Generating Allure HTML report..."
run_allure generate reports/allure-results -o reports/allure-report --clean

echo "Opening Allure report..."
run_allure open reports/allure-report
