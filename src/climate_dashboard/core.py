"""Data aggregator and dashboard components for the GenesisAeon climate stack.

Wires real calls into entropy-governance, medium-modulation, and utac-core
(the "stack" optional-dependency group in pyproject.toml) instead of the
placeholder formulas this module used until 2026-08-02 -- those had
comments claiming provenance ("from entropy-governance" etc.) with no
actual imports. See CHANGELOG.md / DISCLAIMER.md for the fix record and an
honest note about what these three packages composed together does and
does not mean (there is no domain-authoritative pipeline connecting them;
this is one illustrative composition of their real public APIs, not the
one true way to chain them).
"""

import numpy as np
import pandas as pd
from entropy_governance.core import duality_factor
from medium_modulation.core import modulated_entropy
from utac_core.core import v_rig


def aggregate_entropy_data(steps: int = 100) -> pd.DataFrame:
    """Aggregate stack data: duality → modulation → UTAC → mandala peaks.

    Args:
        steps: Number of time steps to simulate.

    Returns:
        DataFrame with columns: time, duality, modulated, utac_threshold, mandala_peaks.
    """
    t = np.linspace(0, 10, steps)

    # Real entropy_governance.duality_factor(action, volume, alpha) call per
    # step. "action" and "volume" have no single canonical meaning across
    # this ecosystem's packages -- t itself stands in for action, and a
    # constant reference volume (1.0) keeps ln(volume) defined and stable.
    duality = np.array([duality_factor(action=ti, volume=1.0) for ti in t])

    # Real medium_modulation.modulated_entropy(S_A, S_V, depth, freq, t)
    # call per step, feeding the duality signal in as S_A and a constant
    # reference S_V.
    modulation = np.array(
        [
            modulated_entropy(S_A=d, S_V=1.0, depth=0.5, freq=1.0, t=ti)
            for d, ti in zip(duality, t, strict=True)
        ]
    )

    # Real utac_core.v_rig(t) call -- this is a direct drop-in, no
    # illustrative-composition caveat needed.
    utac = np.array([v_rig(ti) for ti in t])

    # Per-row peak indicator (1 where `modulation` exceeds its own mean,
    # 0 otherwise). Previously this column held the *count* of peak
    # indices broadcast identically to every row (a single repeated
    # scalar, not real per-row peak detection -- see
    # climate-dashboard-blindtest), which made the column useless for
    # actually locating where peaks occur along the time series.
    mandala_peaks = (modulation > np.mean(modulation)).astype(int)

    df = pd.DataFrame(
        {
            "time": t,
            "duality": duality,
            "modulated": modulation,
            "utac_threshold": utac,
            "mandala_peaks": mandala_peaks,
        }
    )
    return df
