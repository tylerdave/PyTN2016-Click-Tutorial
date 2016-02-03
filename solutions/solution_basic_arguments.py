import click

@click.command()
@click.argument('names', nargs=-1)
def cli(names):
    """
    Given NAME(S), output each on a new line.
    """
    for name in names:
        click.echo("name: {0}".format(name))

if __name__ == '__main__':
    cli()
