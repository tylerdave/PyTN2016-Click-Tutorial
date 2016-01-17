import click
import httpbin

@click.command()
def cli():
    click.echo("Hello, World!")

@click.option('--host', '-h')
@click.option('--port', '-p')
@click.command()
def run_httpbin(**kwargs):
    app_kwargs = {k:v for k, v in kwargs.iteritems() if v}
    click.echo(app_kwargs)
    httpbin.core.app.run(**app_kwargs)


if __name__ == '__main__':
    cli()
