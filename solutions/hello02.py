import click

@click.command()
@click.argument('name')
@click.option('--count', '-c', default=1)
def cli(name, count):
    for i in xrange(count):
        click.echo("Hello, {0}!".format(name))

if __name__ == '__main__':
    cli()
