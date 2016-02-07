import click

@click.group(name='pytn')
def cli():
    """
    Output a greeting to PyTennessee!
    """

@cli.command()
@click.option('--data', prompt=True)
def prompt1(data):
    """
    Prompt for data if it is not specified.
    """
    click.echo("data: {0}".format(data))

@cli.command()
@click.option('--data', prompt="Custom prompt text")
def prompt2(data):
    """
    Prompt for data w/ custom text.
    """
    click.echo("data: {0}".format(data))


@cli.command()
@click.option('--password', prompt=True, hide_input=True,
        confirmation_prompt=True)
def prompt3(password):
    """
    Prompt for password.
    """
    click.echo("password: {0}".format(password))

@cli.command()
@click.password_option()
def prompt4(password):
    """
    Prompt for password.
    """
    click.echo("password: {0}".format(password))

@cli.command()
@click.confirmation_option(prompt="Are you sure?")
def prompt5():
    """
    Prompt for password.
    """
    click.echo("Doing something...")

if __name__ == '__main__':
    cli()
