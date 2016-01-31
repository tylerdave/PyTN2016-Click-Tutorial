import click
import importlib
import os
import pytest
import re
import sys

def get_valid_tutorial_steps():
    """ Find and return a list of test step modules in the tutorial dir. """

    try:
        return sorted([f[4:6] for f in os.listdir('tutorial') if \
                re.search('step\d{2}\.py', f)])
    except OSError as e:
        click.secho(str(e), err=True, fg='red')
        click.secho("No tutorial files found. (This command must be run from" \
                " within the repo root dir.)", err=True)
        sys.exit(1)

@click.argument('step', type=click.Choice(get_valid_tutorial_steps()))
@click.command()
def cli(step):
    """
    This runs the tutorial
    """
    click.echo("Tutorial step {0}".format(step))

    result = pytest.main(['-v', 'tutorial/step{0}.py'.format(step)])

    if result == 0:
        click.secho('Good job!', fg='green')
    else:
        test_module = importlib.import_module('tutorial.step{0}'.format(step))
        click.secho(str(test_module.__doc__), fg='blue')
        try:
            test_class = getattr(test_module, 'TestTutorialStep{0}'.format(step))
            test_class.print_instructions()
        except AttributeError:
            click.secho('No instructions found for this step!', fg='red')



if __name__ == '__main__':
    cli()
