import click
import sys
import time

COLORS = ['white', 'red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'black']

@click.group(name='pytn')
def cli():
    """
    Outputs messages.
    """

@cli.command()
@click.option('--err', is_flag=True)
@click.option('--new-line/--no-new-line', default=True)
def echo(err, new_line):
    """
    Output text using the echo command.
    """
    click.echo("This is always sent to stdout.")
    click.echo("This is a message.", nl=new_line, err=err)
    click.echo("This is always sent to stderr.", err=True)

@cli.command()
@click.option('--fg', type=click.Choice(COLORS))
def style(fg):
    """
    Apply style to output text.
    """
    click.echo(click.style("This is a message.", fg=fg))

@cli.command()
@click.option('--err', is_flag=True)
@click.option('--fg', type=click.Choice(COLORS))
@click.option('--new-line/--no-new-line', default=True)
def secho(err, fg, new_line):
    """
    Combine style & echo using secho helper.
    """
    click.secho("This is a message.", err=err, fg=fg, nl=new_line)

if __name__ == '__main__':
    cli()
