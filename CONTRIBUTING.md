# Contributing

Thanks for your interest in contributing to climate-dashboard!

## Licensing of contributions

This project is dual-licensed: source code under **GPL-3.0-or-later**
(`LICENSE-CODE`) and documentation under **CC BY 4.0** (`LICENSE-DOCS`).
By submitting a contribution, you agree it will be distributed under the
license matching the type of file you changed (code vs. documentation).

## Getting started

1. Fork and clone the repository.
2. Create a virtual environment: `python -m venv .venv && source .venv/bin/activate`.
3. Install in editable mode with dev dependencies: `pip install -e ".[dev]"`.
4. Run the test suite: `pytest`.

## Code style

- Format and lint with `ruff check` / `ruff format`.
- Type-check with `mypy src`.
- Keep functions documented with docstrings.

## Pull requests

- One logical change per PR.
- Add or update tests for any behavioral change.
- Update `CHANGELOG.md` under an `## [Unreleased]` section.
- Fill out the PR template (`.github/PULL_REQUEST_TEMPLATE.md`).

## Reporting issues

Please use the issue templates in `.github/ISSUE_TEMPLATE/`.
