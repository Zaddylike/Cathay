#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
project_root="$(cd "${script_dir}/../.." && pwd)"
allure_bin="${project_root}/node_modules/.bin/allure"

cd "${project_root}"

if [[ ! -x "${allure_bin}" ]]; then
    echo "Allure CLI not found. Run 'npm ci' first." >&2
    exit 1
fi

"${allure_bin}" open reports/allure-report
