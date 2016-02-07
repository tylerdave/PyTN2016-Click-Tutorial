import click

@click.command(name='hello')
@click.argument('name')
@click.option('--excited', '-e', is_flag=True)
def cli(name, excited):
    """ Given a NAME, outputs a greeting. """
    punctuation = '!' if excited else '.'
    click.echo("Hello, {0}{1}".format(name, punctuation))

if __name__ == '__main__':
    cli()
