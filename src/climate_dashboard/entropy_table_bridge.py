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
            from importlib.metadata import PackageNotFoundError
            from importlib.metadata import version as _version

            try:
                _installed_version = _version("entropy-table")
            except PackageNotFoundError:
                _installed_version = None
        except Exception:  # pragma: no cover - defensive only
            _installed_version = None

        try:
            from entropy_table import EntropyTable  # type: ignore[import]
        except ImportError as exc:
            if _installed_version is None:
                raise ImportError(
                    "entropy-table is not installed. "
                    "Install the stack extras: pip install climate-dashboard[stack]"
                ) from exc
            # entropy-table >=2.0 removed the EntropyTable class entirely
            # and replaced it with a different "contract-first" case/claim
            # -ID data model (see entropy_table.core.bindings). This bridge
            # was written against the pre-2.0 API
            # (EntropyTable(domain=...).add_relation()/.export()) and was
            # never updated, so it previously raised a misleading "not
            # installed" error even when a real, installed entropy-table
            # package was present -- see climate-dashboard-blindtest.
            raise RuntimeError(
                f"entropy-table {_installed_version} is installed, but its API no "
                "longer matches what this bridge expects (no EntropyTable class "
                "-- entropy-table >=2.0 replaced the domain-relation model "
                "entirely). This bridge needs updating for the current "
                "entropy-table API; it is not simply a missing dependency."
            ) from exc

        self.table = EntropyTable(domain="climate-dashboard")

    def add_metric(self, key: str, value: float) -> None:
        """Register a key/value metric in the entropy table."""
        self.table.add_relation(key, value)

    def export(self, filepath: Path | str = "domains.yaml") -> Path | str:
        """Export the current table to a YAML file."""
        self.table.export(filepath)
        return filepath
