# test_cli.py
from typer.testing import CliRunner
from src.cli import app


runner = CliRunner()


def test_cmd1():
    result = runner.invoke(app, ["cmd1", "world"])
    assert result.exit_code == 0
    assert "hello, world.\n" in result.output


def test_cmd2_with_option():
    result = runner.invoke(app, ["cmd2", "--opt2", "42"])
    assert result.exit_code == 0
    assert "42" in result.output