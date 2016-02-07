import click

CHOICES = ['a', 'b', 'c', 'd']

@click.command(name='pytn')
@click.option('--letter', type=click.Choice(CHOICES))
@click.option('--number', type=click.IntRange(0, 100))
@click.option('--clamped-number', type=click.IntRange(0, 100, clamp=True))
def cli(letter, number, clamped_number):
    """
    Validates input types.
    """
    click.echo("letter: {0}".format(letter))
    click.echo("number: {0}".format(number))
    click.echo("clamped_number: {0}".format(clamped_number))


if __name__ == '__main__':
    cli()
