import click

@click.command()
@click.argument('name')
def cli(name):
    click.echo("Hello, {0}!".format(name))

if __name__ == '__main__':
    cli()
