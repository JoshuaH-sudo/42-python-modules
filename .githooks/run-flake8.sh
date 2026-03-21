#!/bin/sh

set -eu

if [ "$#" -eq 0 ]; then
    exit 0
fi

repo_root=$(git rev-parse --show-toplevel)

if [ -x "$repo_root/.venv/bin/python" ] && \
    "$repo_root/.venv/bin/python" -m flake8 --version >/dev/null 2>&1; then
    exec "$repo_root/.venv/bin/python" -m flake8 "$@"
fi

if command -v python3 >/dev/null 2>&1 && \
    python3 -m flake8 --version >/dev/null 2>&1; then
    exec python3 -m flake8 "$@"
fi

if command -v python >/dev/null 2>&1 && \
    python -m flake8 --version >/dev/null 2>&1; then
    exec python -m flake8 "$@"
fi

if command -v flake8 >/dev/null 2>&1; then
    exec flake8 "$@"
fi

printf '%s\n' 'flake8 is not installed in the active environment.' >&2
printf '%s\n' 'Install it before committing or pushing.' >&2
exit 1