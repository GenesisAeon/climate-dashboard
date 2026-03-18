"""Tests for climate_dashboard.cli commands."""

from typer.testing import CliRunner

from climate_dashboard.cli import app

runner = CliRunner()


def test_aggregate_command_runs():
    result = runner.invoke(app, ["aggregate"])
    assert result.exit_code == 0


def test_aggregate_output_contains_stats():
    result = runner.invoke(app, ["aggregate"])
    assert "count" in result.output
    assert "mean" in result.output


def test_aggregate_custom_steps():
    result = runner.invoke(app, ["aggregate", "--steps", "50"])
    assert result.exit_code == 0
    assert "50" in result.output


def test_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "cdash" in result.output.lower() or "climate" in result.output.lower()


def test_aggregate_help():
    result = runner.invoke(app, ["aggregate", "--help"])
    assert result.exit_code == 0
