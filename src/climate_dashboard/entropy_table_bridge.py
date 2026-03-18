"""Bridge between climate-dashboard and entropy-table for domain metric tracking."""

from __future__ import annotations

from pathlib import Path


class ClimateDashboardBridge:
    """Bridge to the entropy-table domain registry.

    Requires the optional [stack] dependency group:
        pip install climate-dashboard[stack]
    """

    def __init__(self) -> None:
        try:
            from entropy_table import EntropyTable  # type: ignore[import]

            self.table = EntropyTable(domain="climate-dashboard")
        except ImportError as exc:
            raise ImportError(
                "entropy-table is not installed. "
                "Install the stack extras: pip install climate-dashboard[stack]"
            ) from exc

    def add_metric(self, key: str, value: float) -> None:
        """Register a key/value metric in the entropy table."""
        self.table.add_relation(key, value)

    def export(self, filepath: Path | str = "domains.yaml") -> Path | str:
        """Export the current table to a YAML file."""
        self.table.export(filepath)
        return filepath
