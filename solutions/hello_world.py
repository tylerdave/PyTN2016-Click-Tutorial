import click

@click.command(name='pytn')
def cli():
    """
    Output a greeting to PyTennessee!
    """
    click.echo("Hello, PyTN!")

if __name__ == '__main__':
    cli()
