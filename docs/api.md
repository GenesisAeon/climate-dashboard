# API Reference

## `climate_dashboard.core`

### `aggregate_entropy_data`

```python
def aggregate_entropy_data(steps: int = 100) -> pd.DataFrame
```

Aggregate stack data: duality → modulation → UTAC → mandala peaks.

**Parameters**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `steps` | `int` | `100` | Number of time steps to simulate |

**Returns**

`pd.DataFrame` with columns:

| Column | Description |
|--------|-------------|
| `time` | Linearly spaced time axis (0–10) |
| `duality` | φ-modulated sine wave (entropy-governance placeholder) |
| `modulated` | Duality × 0.618 (medium-modulation output) |
| `utac_threshold` | Logarithmic UTAC boundary curve (utac-core) |
| `mandala_peaks` | Count of above-mean modulation samples (mandala-visualizer) |

## `climate_dashboard.app`

Dash/Plotly web application. Launch via `cdash run`.

## `climate_dashboard.cli`

Typer CLI — see [CLI Reference](cli.md).
