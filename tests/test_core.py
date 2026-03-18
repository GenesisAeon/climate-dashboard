"""Tests for climate_dashboard.core."""

import pandas as pd
import pytest

from climate_dashboard.core import aggregate_entropy_data


def test_aggregate_returns_dataframe():
    df = aggregate_entropy_data(steps=50)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 50


def test_aggregate_default_steps():
    df = aggregate_entropy_data()
    assert len(df) == 100


def test_aggregate_columns():
    df = aggregate_entropy_data(steps=10)
    expected_cols = {"time", "duality", "modulated", "utac_threshold", "mandala_peaks"}
    assert expected_cols.issubset(set(df.columns))


def test_aggregate_time_range():
    df = aggregate_entropy_data(steps=50)
    assert df["time"].iloc[0] == pytest.approx(0.0)
    assert df["time"].iloc[-1] == pytest.approx(10.0)


def test_aggregate_utac_non_negative():
    df = aggregate_entropy_data(steps=100)
    assert (df["utac_threshold"] >= 0).all()


def test_aggregate_mandala_peaks_constant_per_run():
    df = aggregate_entropy_data(steps=100)
    # mandala_peaks column holds a scalar repeated across all rows
    assert df["mandala_peaks"].nunique() == 1


def test_aggregate_single_step():
    df = aggregate_entropy_data(steps=1)
    assert len(df) == 1
