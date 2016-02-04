import click

@click.group(name='pytn')
@click.option('--input-string1', help='Optional input string.')
@click.option('--input-string2', metavar='<string>', help='Another optional input string.')
def cli(do_stuff, input_string1, input_string2):
    """
    Outputs messages.
    """

@cli.command()
def hello():
    """
    Says hello.
    """
    click.echo("Hello, PyTN!")

if __name__ == '__main__':
    cli()
