import click
import os
import shutil

from .tutorial import get_lessons, get_next_lesson_id, list_lesson_ids, run_lesson, save_lesson_statuses

STATUS_FILE = 'status.json'

@click.group(name='tutorial')
@click.option('--status-file', default=STATUS_FILE, type=click.Path())
@click.pass_context
def cli(ctx, status_file):
    """
    Runs the tutorial.
    """
    ctx.obj = {'status_filename': os.path.join(
            click.get_app_dir('Click Tutorial'), status_file)}
    lessons = get_lessons(ctx.obj['status_filename'])
    if lessons:
        ctx.obj['lessons'] = lessons
    else:
        ctx.abort()

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

    click.secho("Running tests for lesson {0} {1}...".format(
        lesson_id, lesson['title']), fg='blue')

    result = run_lesson(lesson['test_file'])
    if result:
        lessons[lesson_id]['status'] = 'complete'
        click.secho("Good job!", fg='green')
    else:
        lessons[lesson_id]['status'] = 'in-progress'
        click.secho("\nHint: {0}".format(lesson.get('hint')), fg='blue')
        click.secho("URL: {0}".format(lesson.get('url', 'n/a')), fg='blue')

    save_lesson_statuses(ctx.obj['status_filename'], lessons)

    if not result:
        ctx.exit(2)

@cli.command(name='lesson-ids')
@click.pass_context
def lesson_ids(ctx):
    """
    Output a list of all LESSON_IDs.
    """
    click.echo(','.join(sorted(ctx.obj['lessons'].keys())))

@cli.command()
@click.pass_context
def next(ctx):
    """
    Run the next lesson.
    """
    lessons = ctx.obj['lessons']
    lesson_id = get_next_lesson_id(lessons)
    next_lesson = lessons[lesson_id]

    click.echo("Running next lesson ({0} {1})...".format(lesson_id,
        next_lesson['title']))

    ctx.invoke(lesson, lesson_id=lesson_id)


@cli.command()
@click.option('--yes', is_flag=True, help="Assume Y to confirmation prompts.")
@click.pass_context
def reset(ctx, yes):
    """
    Reset the status for all lessons (start-over)
    """

    if not yes:
        click.confirm("Are you sure you want to reset the status of all lessons (start over?)", abort=True)
    lessons = {}
    save_lesson_statuses(ctx.obj['status_filename'], lessons)
    click.echo("Tutorial reset.")


@cli.command()
@click.argument('lesson_id', type=click.Choice(list_lesson_ids()))
@click.pass_context
def solve(ctx, lesson_id):
    """
    Copy solution for LESSON_ID into place.
    """
    lesson = ctx.obj['lessons'][lesson_id]
    click.echo("Copying solution for lesson {0} {1}".format(lesson_id, lesson['title']))
    source_file = os.path.join('solutions/', lesson['test_file'])
    dest_file = 'click_tutorial/cli.py'
    try:
        click.echo("copy: {0} -> {1}".format(source_file, dest_file))
        shutil.copy(source_file, dest_file)
    except IOError as e:
        click.secho(str(e), fg='red')
        ctx.exit(1)

    click.echo('\nSolution file:')
    with open(dest_file) as solution_file:
        click.secho(solution_file.read(), fg='green')

    click.echo("You may now view the solution file at click_tutorial/cli.py\n" \
               "or run the tests for the lesson with:\n\n" \
               "tutorial lesson {0}".format(lesson_id))

@cli.command()
@click.pass_context
def status(ctx):
    """
    Show the status of the tutorial lessons.
    """
    click.secho("### Lesson Name                         status\n"
            "--------------------------------------------------", bold=True, color='white')
    for lesson_number, lesson_details in sorted(ctx.obj['lessons'].items()):
        status = lesson_details.get('status')
        if status == 'complete':
            color = 'green'
        elif status == 'in-progress':
            color = 'yellow'
        else:
            color = 'magenta'

        click.secho("{0} {1:35} {2}".format(
            lesson_number, lesson_details.get('title'), status), fg=color)


if __name__ == '__main__':
    cli()
