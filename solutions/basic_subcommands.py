import click

@click.group(name='pytn')
def cli():
    """
    A command with sub-commands.
    """

@cli.command()
def status():
    """
    Output status info.
    """
    click.echo("status: ok")

if __name__ == '__main__':
    cli()
