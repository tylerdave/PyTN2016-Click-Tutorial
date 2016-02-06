import click
import json
import os
import pkg_resources
import pytest
import re
import sys


PACKAGE_NAME = 'click_tutorial'
LESSONS_FILE = 'data/tutorial_lessons.json'
STATUS_FILE = 'status.json'

def load_lessons():
    try:
        with open(pkg_resources.resource_filename(PACKAGE_NAME, LESSONS_FILE)) as lessons_file:
            return json.load(lessons_file)
    except Exception as e:
        click.secho("Unable to load lessons file: {0}".format(e), err=True, fg='red')
        return None

def load_lesson_statuses(status_file_name):
    try:
        with open(status_file_name) as status_file:
            return json.load(status_file)
    except:
        click.secho("Unable to load lesson statuses. Starting from the beginning...",
                err=True, fg='yellow')
        return {}


def save_lesson_statuses(status_file_name, statuses):
    try:
        os.makedirs(os.path.dirname(status_file_name))
    except OSError as e:
        if e.errno != os.errno.EEXIST:
            raise
    with open(status_file_name, 'w') as status_file:
        json.dump(statuses, status_file, indent=2)

def get_lessons(status_file_name):
    lessons = load_lessons()
    if not lessons:
        return None
    statuses = load_lesson_statuses(status_file_name)
    for lesson_id, lesson_details in lessons.items():
        lesson_details['status'] = statuses.get(lesson_id, {}).get('status') or 'incomplete'
    return lessons

def get_next_lesson_id(lessons):
    for lesson_id in sorted(lessons):
        if lessons[lesson_id]['status'] != 'complete':
            return lesson_id
    return None

def list_lesson_ids():
    lessons = load_lessons()
    if lessons:
        return sorted(lessons)

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

def run_lesson(lesson_test_file):
    result = pytest.main(['-vx', 'tutorial/{0}'.format(lesson_test_file)])
    if result == 0:
        return True
    else:
        return False
