import click

@click.argument('name')
@click.command()
def cli(name):
    click.echo("Hello, {0}!".format(name))

if __name__ == '__main__':
    cli()
