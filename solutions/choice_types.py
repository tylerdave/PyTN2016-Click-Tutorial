import click

@click.command(name='pytn')
def cli():
    """
    Validates input types.
    """
    click.echo("Hello, PyTN!")

if __name__ == '__main__':
    cli()
