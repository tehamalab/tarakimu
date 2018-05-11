# -*- coding: utf-8 -*-

"""tarakimu console script."""

import click
from .numtowords import numtowords


@click.group()
def cli():
    pass


cli.add_command(numtowords)


if __name__ == "__main__":
    cli()
