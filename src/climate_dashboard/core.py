"""Data aggregator and dashboard components for the GenesisAeon climate stack."""

import numpy as np
import pandas as pd


def aggregate_entropy_data(steps: int = 100) -> pd.DataFrame:
    """Aggregate stack data: duality → modulation → UTAC → mandala peaks.

    Args:
        steps: Number of time steps to simulate.

    Returns:
        DataFrame with columns: time, duality, modulated, utac_threshold, mandala_peaks.
    """
    t = np.linspace(0, 10, steps)
    duality = np.sin(t * 1.618)  # placeholder from entropy-governance
    modulation = duality * 0.618  # from medium-modulation
    utac = 0.0625 * np.log(t + 1)  # from utac-core
    mandala_peaks = np.where(modulation > np.mean(modulation))[0]

    df = pd.DataFrame(
        {
            "time": t,
            "duality": duality,
            "modulated": modulation,
            "utac_threshold": utac,
            "mandala_peaks": [len(mandala_peaks)] * steps,
        }
    )
    return df
