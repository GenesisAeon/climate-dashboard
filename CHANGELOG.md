# Changelog

## [1.0.0] - 2026

### Added
- `.zenodo.json`, `RELEASE_GUIDE.md`, `CONTRIBUTING.md`, issue/PR templates.

### Changed
- Project metadata (`pyproject.toml`) version bumped to `1.0.0`.
- Relicensed: source code now GPL-3.0-or-later (`LICENSE-CODE`), documentation
  now CC BY 4.0 (`LICENSE-DOCS`); `LICENSE` describes the dual-license split.
- GenesisAeon-ecosystem `[stack]` dependency pins bumped to their released
  1.0.0/2.0.0 floors (`entropy-table>=2.0.0`, others `>=1.0.0`).

## v0.1.0 (2026-03-18)

- Initial release: interactive Dash/Plotly Climate Entropy Dashboard
- Aggregates duality, modulation, UTAC thresholds, mandala peaks
- CLI `cdash run --port 8050` + `cdash aggregate --steps`
- Docs + api.md + mkdocs --strict clean
- [stack] extra mit Versions-Fixes (sonification 0.0.10, fieldtheory ohne Bindestrich)
