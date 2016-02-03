import click
import json
import os
import pkg_resources
import re
import sys

from .tutorial import get_lessons, list_lesson_ids, run_lesson, save_lesson_statuses

STATUS_FILE = 'status.json'

@click.group(name='tutorial')
@click.option('--verbose', '-v')
@click.pass_context
def cli(ctx, verbose):
    """
    This runs the tutorial
    """
    ctx.obj = {'status_filename': os.path.join(
            click.get_app_dir('Click Tutorial'), STATUS_FILE)}
    ctx.obj['lessons'] = get_lessons(ctx.obj['status_filename'])


@cli.command()
@click.argument('lesson_id', type=click.Choice(list_lesson_ids()))
@click.pass_context
def lesson(ctx, lesson_id):
    """
    Run tests to check given LESSON_ID.
    """
    lessons = ctx.obj['lessons']
    lesson = lessons[lesson_id]
    if lesson['status'] == 'complete':
        click.confirm(
                "This less was already completed. Do you want to re-run?", abort=True)

    click.echo("Running tests for lesson {0} {1}...".format(lesson_id, lesson['title']))

    result = run_lesson(lesson['test_file'])
    if result:
        lessons[lesson_id]['status'] = 'complete'
        click.secho("Good job!", fg='green')
    else:
        lessons[lesson_id]['status'] = 'in-progress'
        click.secho("\nHint: {0}".format(lesson.get('hint')), fg='blue')
        click.secho("URL: {0}".format(lesson.get('url', 'n/a')), fg='blue')

    save_lesson_statuses(ctx.obj['status_filename'], lessons)


@cli.command()
@click.pass_context
def reset(ctx):
    """
    Reset the status for all lessons (start-over)
    """

    click.confirm("Are you sure you want to reset the status of all lessons (start over?)", abort=True)
    lessons = {}
    save_lesson_statuses(ctx.obj['status_filename'], lessons)
    click.echo("Tutorial reset.")


@cli.command()
@click.argument('lesson_id', type=click.Choice(list_lesson_ids()))
def solve(lesson_id):
    """
    Mark LESSON_ID complete and display solution.
    """
    # TODO: mark lesson solved
    # TODO: output solution
    click.echo("Copying solution to click_tutorial/cli.py...")


@cli.command()
@click.pass_context
def status(ctx):
    """
    Show the status of the tutorial lessons.
    """
    click.secho("### Lesson Name                    status\n"
            "---------------------------------------------", bold=True, color='white')
    for lesson_number, lesson_details in sorted(ctx.obj['lessons'].items()):
        status = lesson_details.get('status')
        if status == 'complete':
            color = 'green'
        elif status == 'in-progress':
            color = 'yellow'
        else:
            color = 'red'

        click.secho("{0} {1:30} {2}".format(
            lesson_number, lesson_details.get('title'), status), fg=color)


if __name__ == '__main__':
    cli()
