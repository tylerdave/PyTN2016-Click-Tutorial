import click

@click.command(name='pytn')
@click.option('--int-option', type=click.INT)
@click.option('--float-option', type=click.FLOAT)
@click.option('--bool-option', type=click.BOOL)
def cli(int_option, float_option, bool_option):
    """
    Validates input types.
    """

    click.echo("int: {0}".format(int_option))
    click.echo("float: {0}".format(float_option))
    click.echo("bool: {0}".format(bool_option))

if __name__ == '__main__':
    cli()
