#!/bin/sh
set -eu

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$repo_root"

if ! command -v uv >/dev/null 2>&1; then
    echo "uv is required to run the test suite. Install it from https://docs.astral.sh/uv/." >&2
    exit 1
fi

uv run --locked python -m unittest discover -s tests -v
