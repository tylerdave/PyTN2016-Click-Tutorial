import click
import httpbin

@click.option('--host', '-h')
@click.option('--port', '-p')
@click.command()
def run_httpbin(**kwargs):
    app_kwargs = {k:v for k, v in kwargs.iteritems() if v}
    httpbin.core.app.run(**app_kwargs)

if __name__ == '__main__':
    run_httpbin()
