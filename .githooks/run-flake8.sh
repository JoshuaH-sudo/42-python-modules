#!/bin/sh

set -eu

if [ "$#" -eq 0 ]; then
    exit 0
fi

repo_root=$(git rev-parse --show-toplevel)

run_python_module() {
    module_name=$1
    shift

    if [ -x "$repo_root/.venv/bin/python" ] && \
        "$repo_root/.venv/bin/python" -m "$module_name" --version >/dev/null 2>&1; then
        "$repo_root/.venv/bin/python" -m "$module_name" "$@"
        return $?
    fi

    if command -v python3 >/dev/null 2>&1 && \
        python3 -m "$module_name" --version >/dev/null 2>&1; then
        python3 -m "$module_name" "$@"
        return $?
    fi

    if command -v python >/dev/null 2>&1 && \
        python -m "$module_name" --version >/dev/null 2>&1; then
        python -m "$module_name" "$@"
        return $?
    fi

    return 127
}

printf '%s\n' 'Running flake8...'
if run_python_module flake8 "$@"; then
    :
else
    status=$?
    if [ "$status" -eq 127 ]; then
        if command -v flake8 >/dev/null 2>&1; then
            flake8 "$@"
        else
            printf '%s\n' 'flake8 is not installed in the active environment.' >&2
            printf '%s\n' 'Install it before committing or pushing.' >&2
            exit 1
        fi
    else
        exit "$status"
    fi
fi

mypy_args=''
for file in "$@"; do
    case "$file" in
        module_07/*)
            ;;
        *)
            mypy_args="$mypy_args
$file"
            ;;
    esac
done

if [ -z "$mypy_args" ]; then
    printf '%s\n' 'Skipping mypy: only module_07 files were provided.'
    exit 0
fi

set --
while IFS= read -r file; do
    if [ -n "$file" ]; then
        set -- "$@" "$file"
    fi
done <<EOF
$mypy_args
EOF

printf '%s\n' 'Running mypy...'
if run_python_module mypy "$@"; then
    :
else
    status=$?
    if [ "$status" -eq 127 ]; then
        if command -v mypy >/dev/null 2>&1; then
            mypy "$@"
        else
            printf '%s\n' 'mypy is not installed in the active environment.' >&2
            printf '%s\n' 'Install it before committing or pushing.' >&2
            exit 1
        fi
    else
        exit "$status"
    fi
fi