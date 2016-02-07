import click

@click.command(name='pytn')
@click.argument('infile', type=click.File('r'), default='-')
@click.argument('outfile', type=click.File('w'), default='-')
def cli(infile, outfile):
    """
    Reads / writes files.
    """
    text = infile.read()
    click.echo("Input chars: {0}".format(len(text)), err=True)
    click.secho(text, file=outfile, fg='green')

if __name__ == '__main__':
    cli()
