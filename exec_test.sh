#!/usr/bin/env bash
set -euo pipefail

VENV_DIR="${VENV_DIR:-.venv}"

if [[ ! -d "$VENV_DIR" ]]; then
  python3 -m venv "$VENV_DIR"
fi

source "$VENV_DIR/bin/activate"
python -m pip install -r requirements.txt
pytest "$@"

if command -v allure >/dev/null 2>&1; then
  allure generate ./allure-results/ -o ./allure-report/ --clean
else
  echo "Allure CLI not found; skipping HTML report generation."
fi
