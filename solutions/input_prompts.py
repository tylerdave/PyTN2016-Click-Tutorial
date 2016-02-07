import click

@click.group(name='pytn')
def cli():
    """
    Output a greeting to PyTennessee!
    """

@cli.command()
def prompt1():
    """
    Prompt for data.
    """
    data = click.prompt("Data")
    click.echo("data: {0}".format(data))

@cli.command()
def prompt2():
    """
    Prompt for data w/ custom text.
    """
    click.confirm("Are you sure?", abort=True)
    click.echo("OK")

if __name__ == '__main__':
    cli()
