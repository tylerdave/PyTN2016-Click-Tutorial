import click

@click.command()
@click.argument('url')
def cli(url):
    click.echo("GET {0}".format(url))

if __name__ == '__main__':
    cli()
