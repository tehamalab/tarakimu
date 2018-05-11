# -*- coding: utf-8 -*-

"""Console script for tarakimu."""

import click
from ..utils import num_to_words


@click.command(name='numtowords')
@click.argument('number', type=str)
@click.option('--use_lakh', '-L', help='use lakh numbering format', is_flag=True)
def numtowords(number, use_lakh=False):
    """Convert number to words."""
    try:
        click.echo(num_to_words(number, use_lakh=use_lakh))
    except Exception as e:
        click.abort()
