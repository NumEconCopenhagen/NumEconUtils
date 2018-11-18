import click
from NumEconUtils import ipynb

@click.group()
def cli():
    pass


@cli.command()
@click.argument('path')
@click.option('-r', '--regex', default="^#fillin", type=str, help="hejsa")
def clearcells(path, regex):
    ipynb.ipynb_clear_regex(path, regex)


if __name__ == "__main__":
    cli()