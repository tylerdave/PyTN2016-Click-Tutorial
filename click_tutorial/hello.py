import click

@click.command(name='hello')
@click.argument('name')
@click.option('--excited', '-e', is_flag=True)
def cli(name, excited):
    """ Given a NAME, outputs a greeting. """
    if excited:
        click.echo("Hello, {0}!".format(name))
    else:
        click.echo("Hello, {0}.".format(name))

if __name__ == '__main__':
    cli()
