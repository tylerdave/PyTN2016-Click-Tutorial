import click

@click.command()
@click.option('--single', '-s')
@click.option('--multi', '-m', multiple=True)
@click.option('--enable-feature/--no-enable-feature')
@click.option('--flag', is_flag=True)
@click.option('--verbose', '-v', count=True)
def cli(single, multi, enable_feature, flag, verbose):
    """
    Parse some options.
    """
    click.echo("single: {0}".format(single))
    for m in multi:
        click.echo("multi: {0}".format(m))
    click.echo("enable_feature: {0}".format(enable_feature))
    click.echo("flag: {0}".format(flag))
    click.echo("verbose: {0}".format(verbose))

if __name__ == '__main__':
    cli()
