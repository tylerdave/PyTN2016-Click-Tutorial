import click
import sys
import time

@click.group(name='pytn')
def cli():
    """
    Outputs messages.
    """

@cli.command(name='iterable-bar')
def iterable_bar():
    """
    Outputs a status bar that uses an iterator.
    """

    items = range(100)
    with click.progressbar(items, file=sys.stdout) as bar:
        for item in bar:
            time.sleep(0.01)  # would normally process the item here

@cli.command(name='explicit-bar')
def explicit_bar():
    """
    Outputs a status bar using explicit length.
    """

    data = 'X' * 100

    with click.progressbar(length=len(data)) as bar:
        for char in data:
            time.sleep(0.01)  # would normally process the item here
            bar.update(1)

if __name__ == '__main__':
    cli()
