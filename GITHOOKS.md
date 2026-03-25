# Git Hooks Setup

This repository stores its Git hooks in `.githooks/`.

Git does not use that directory automatically in every clone, so after cloning the repository you need to enable it once:

```sh
git config core.hooksPath .githooks
```

## Verify The Setup

Check that Git is using the repository hook directory:

```sh
git config --get core.hooksPath
```

Expected output:

```text
.githooks
```

Check that the hook files are executable:

```sh
ls -l .githooks
```

You should see executable permissions on:

- `pre-commit`
- `pre-push`
- `run-flake8.sh`

## What The Hooks Do

- `pre-commit` runs `flake8` on staged Python files, then runs `mypy` on those same files except anything under `module_07/`
- `pre-push` runs `flake8` on Python files included in the push, then runs `mypy` on those same files except anything under `module_07/`

## Verify Flake8 Works

Run the shared hook script directly against a Python file:

```sh
./.githooks/run-flake8.sh module-06/ft_transmutation.py
```

If there is no output, the file passed the check.

To confirm the hook blocks bad code:

1. Add a temporary flake8 violation to a `.py` file.
2. Stage the file and run `git commit`, or include it in a `git push`.
3. Confirm Git stops with a flake8 error.

## Common Failure Cases

### Hooks do not run at all

Cause: `core.hooksPath` is not configured in the current clone.

Fix:

```sh
git config core.hooksPath .githooks
```

### Hooks run but fail immediately

Cause: `flake8` is not installed in the active environment.

The hook tries these in order:

1. `.venv/bin/python -m flake8`
2. `python3 -m flake8`
3. `python -m flake8`
4. `flake8`

Fix by installing `flake8` in the environment you use for this repository.

## One-Line Setup For A Fresh Clone

```sh
git config core.hooksPath .githooks && ./.githooks/run-flake8.sh module-06/ft_transmutation.py
```