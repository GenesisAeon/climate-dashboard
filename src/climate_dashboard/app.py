"""Dash/Plotly web application for the Climate Entropy Dashboard."""

from dash import Dash, dcc, html
import plotly.express as px

from .core import aggregate_entropy_data


def create_dashboard() -> Dash:
    """Create and configure the Dash web application.

    Returns:
        Configured Dash app instance ready to run.
    """
    app = Dash(__name__)
    df = aggregate_entropy_data()

    fig = px.line(
        df,
        x="time",
        y=["duality", "modulated", "utac_threshold"],
        title="GenesisAeon Climate Entropy Dashboard",
        labels={"value": "Amplitude", "variable": "Signal"},
        template="plotly_dark",
    )
    fig.update_layout(
        legend_title_text="Signal",
        xaxis_title="Time",
        yaxis_title="Amplitude",
    )

    app.layout = html.Div(
        [
            html.H1(
                "Climate Entropy Dashboard",
                style={"textAlign": "center", "color": "#00ff88"},
            ),
            html.P(
                "Visualizing duality waves, UTAC thresholds and mandala modulation.",
                style={"textAlign": "center", "color": "#aaaaaa"},
            ),
            dcc.Graph(figure=fig, style={"height": "70vh"}),
            html.Footer(
                "GenesisAeon Stack – climate-dashboard v0.1.0",
                style={"textAlign": "center", "color": "#555555", "marginTop": "2rem"},
            ),
        ],
        style={"backgroundColor": "#111111", "minHeight": "100vh", "padding": "1rem"},
    )

    return app
