"""Tests for climate_dashboard.entropy_table_bridge.

This module previously had zero test coverage and was never actually
invoked from cli.py/app.py -- entirely dead code (see
climate-dashboard-blindtest). It also raised a misleading "entropy-table
is not installed" error even when entropy-table *is* installed, because
its pre-2.0 API (EntropyTable class with add_relation()/export()) was
removed in entropy-table>=2.0. These tests pin down the corrected,
honest error message.
"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _version

import pytest

from climate_dashboard.entropy_table_bridge import ClimateDashboardBridge

try:
    _version("entropy-table")
    _ENTROPY_TABLE_INSTALLED = True
except PackageNotFoundError:
    _ENTROPY_TABLE_INSTALLED = False


@pytest.mark.skipif(
    not _ENTROPY_TABLE_INSTALLED, reason="entropy-table [stack] extra not installed"
)
def test_bridge_reports_api_mismatch_not_missing_dependency():
    """When entropy-table *is* installed but with its incompatible >=2.0
    API (no EntropyTable class), the bridge must say so clearly instead
    of claiming the package isn't installed at all."""
    with pytest.raises(RuntimeError, match="API no longer matches"):
        ClimateDashboardBridge()


def test_bridge_raises_helpful_error_when_missing():
    """When entropy-table isn't installed at all, the original
    "not installed" message is still correct and should be preserved."""
    if _ENTROPY_TABLE_INSTALLED:
        pytest.skip("entropy-table is installed in this environment")
    with pytest.raises(ImportError, match="not installed"):
        ClimateDashboardBridge()
