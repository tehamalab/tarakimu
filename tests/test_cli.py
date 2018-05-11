#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `tarakimu` CLI."""

from click.testing import CliRunner
from tarakimu import cli


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()

    result = runner.invoke(cli.cli)
    assert result.exit_code == 0
    assert 'cli' in result.output
    assert 'numtowords' in result.output

    help_result = runner.invoke(cli.cli, ['--help'])
    assert help_result.exit_code == 0
    assert '--help' in help_result.output


def test_numtowords(numwords):
    """Test the CLI."""

    runner = CliRunner()

    for n, w in numwords.items():
        result = runner.invoke(cli.cli, ['numtowords', '--', n])
        assert result.exit_code == 0
        assert w == result.output.strip()


def test_invalid_numtowords(invalid_nums):
    """Test the CLI."""

    runner = CliRunner()

    for n in invalid_nums:
        result = runner.invoke(cli.cli, ['numtowords', n])
        assert result.exit_code != 0
        assert result.output == ''
