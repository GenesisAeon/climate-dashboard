# climate-dashboard

**Interactive Climate Entropy Dashboard** – visualizes the GenesisAeon stack in real-time: duality waves, UTAC thresholds, cosmic moments, mandala resonance and sonified output.

[![CI](https://github.com/GenesisAeon/climate-dashboard/actions/workflows/ci.yml/badge.svg)](https://github.com/GenesisAeon/climate-dashboard/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/climate-dashboard)](https://pypi.org/project/climate-dashboard/)

---

## Install

```bash
pip install climate-dashboard
# or with full GenesisAeon stack bindings
pip install "climate-dashboard[stack]"
```

## Usage

```bash
# Launch interactive Dash dashboard (default port 8050)
cdash run

# Custom port
cdash run --port 8080

# CLI summary of entropy data
cdash aggregate

# Custom time steps
cdash aggregate --steps 200
```

## What you get

`cdash run` opens an interactive Plotly/Dash dashboard at `http://127.0.0.1:8050` displaying:

- **Duality wave** – entropy-governance placeholder (φ-modulated sine)
- **Modulated signal** – medium-modulation output (duality × 0.618)
- **UTAC threshold** – utac-core logarithmic boundary curve

## Project structure

```
climate-dashboard/
├── pyproject.toml
├── README.md
├── domains.yaml
├── src/
│   └── climate_dashboard/
│       ├── __init__.py
│       ├── core.py                  # Data aggregator
│       ├── app.py                   # Dash/Plotly web app
│       ├── cli.py                   # Typer CLI (cdash)
│       └── entropy_table_bridge.py  # entropy-table integration
├── tests/
│   ├── test_core.py
│   └── test_cli.py
└── mkdocs.yml
```

## Stack integration

Install the optional `[stack]` extras to bind all GenesisAeon packages:

| Package | Role |
|---|---|
| `entropy-governance` | Duality wave source |
| `medium-modulation` | Signal modulation |
| `utac-core` | UTAC threshold curves |
| `mandala-visualizer` | Mandala resonance plots |
| `sonification` | Audio export layer |
| `entropy-table` | Domain metric registry |
| `cosmic-moment` | Cosmic event markers |
| `fieldtheory` | Unified field helpers |
| `sigillin` | Sigil generation |
| `implosive-genesis` | Genesis core events |

## DOI

**DOI**: [10.5281/zenodo.19091880](https://doi.org/10.5281/zenodo.19091880)
**PyPI**: `pip install climate-dashboard` (oder `pip install "climate-dashboard[stack]"` für den vollen GenesisAeon-Stack)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19091880.svg)](https://doi.org/10.5281/zenodo.19091880)

---

Built with [Dash](https://dash.plotly.com/) · [Plotly](https://plotly.com/python/) · [Typer](https://typer.tiangolo.com/) · [Rich](https://rich.readthedocs.io/)
