# -*- coding: utf-8 -*-

"""Console script for tarakimu."""

import click
from ..utils import num_to_words


@click.command(name='numtowords')
@click.argument('number', type=str)
@click.option('--lang', '-l',
              type=click.Choice(['en', 'sw']), default='sw',
              help='language code')
@click.option('--use_lakh', '-L',
              is_flag=True,
              help='use lakh numbering format (Swahili only).')
def numtowords(number, lang='sw', use_lakh=False):
    """Convert number to words."""
    click.echo(num_to_words(number, lang=lang, use_lakh=use_lakh))
