"""Climate Dashboard – Interactive Entropy Dashboard for the GenesisAeon stack."""

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _version

try:
    __version__ = _version("climate-dashboard")
except PackageNotFoundError:  # pragma: no cover - not installed, e.g. running from source
    __version__ = "0.0.0+unknown"

__author__ = "GenesisAeon Team"
