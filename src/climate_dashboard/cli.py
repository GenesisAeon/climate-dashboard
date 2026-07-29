"""Climate-Dashboard CLI – interactive entropy visualization."""

import sys

import typer
from rich.console import Console

# Windows consoles default to a non-UTF-8 codepage. Depending on the Rich
# version this either raises UnicodeEncodeError or silently substitutes a
# mojibake placeholder for non-ASCII characters instead of crashing. Force
# UTF-8 stdout/stderr so behavior matches Linux/macOS terminals.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

app = typer.Typer(
    name="cdash",
    help="Climate-Dashboard CLI – entropy visualization for the GenesisAeon stack.",
    add_completion=False,
)
console = Console()


@app.command()
def run(
    port: int = typer.Option(8050, "--port", "-p", help="Dashboard port."),
    debug: bool = typer.Option(False, "--debug", help="Enable Dash debug mode."),
) -> None:
    """Launch the interactive Dash dashboard."""
    from .app import create_dashboard

    dashboard = create_dashboard()
    console.print(f"[bold green]Dashboard running at http://127.0.0.1:{port}[/]")
    console.print("[dim]Press Ctrl+C to stop.[/]")
    dashboard.run(debug=debug, port=port)


@app.command()
def aggregate(
    steps: int = typer.Option(100, "--steps", "-s", help="Number of time steps."),
) -> None:
    """Aggregate and print entropy data summary."""
    from .core import aggregate_entropy_data

    df = aggregate_entropy_data(steps=steps)
    console.print(f"\n[bold cyan]Entropy Data Summary ({steps} steps)[/]\n")
    console.print(df.describe().to_string())
    console.print()


@app.command()
def export(
    steps: int = typer.Option(100, "--steps", "-s", help="Number of time steps."),
    output: str = typer.Option("domains.yaml", "--output", "-o", help="Output YAML path."),
) -> None:
    """Export the aggregated entropy summary to entropy-table via the
    optional [stack] extra.

    Requires: pip install climate-dashboard[stack]
    """
    from .core import aggregate_entropy_data
    from .entropy_table_bridge import ClimateDashboardBridge

    df = aggregate_entropy_data(steps=steps)
    bridge = ClimateDashboardBridge()
    bridge.add_metric("duality_mean", float(df["duality"].mean()))
    bridge.add_metric("modulated_mean", float(df["modulated"].mean()))
    bridge.add_metric("utac_threshold_mean", float(df["utac_threshold"].mean()))
    bridge.add_metric("mandala_peak_fraction", float(df["mandala_peaks"].mean()))
    path = bridge.export(output)
    console.print(f"[bold green]Exported to {path}[/]")


if __name__ == "__main__":
    app()
