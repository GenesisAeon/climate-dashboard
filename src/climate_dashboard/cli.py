"""Climate-Dashboard CLI – interactive entropy visualization."""

import typer
from rich.console import Console

app = typer.Typer(
    name="cdash",
    help="Climate-Dashboard CLI – interactive entropy visualization for the GenesisAeon stack.",
    add_completion=False,
)
console = Console()


@app.command()
def run(
    port: int = typer.Option(8050, "--port", "-p", help="Port to run the dashboard on."),
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


if __name__ == "__main__":
    app()
