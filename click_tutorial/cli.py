import click

@click.command()
def cli():
    """
    Output a greeting to PyTennessee!
    """
    click.echo("Hello, PyTN!")

if __name__ == '__main__':
    cli()
