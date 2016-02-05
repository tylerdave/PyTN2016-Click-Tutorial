#!/bin/bash
set -e

TEST_STATUS_FILE="test_running_tutorial.json"

lesson_ids=$(tutorial lesson-ids | sed "s/,/ /g")

tutorial --status-file "$TEST_STATUS_FILE" reset --yes

for id in $lesson_ids
do
    echo "Testing lesson $id..."
    tutorial --status-file "$TEST_STATUS_FILE" solve "$id"
    tutorial --status-file "$TEST_STATUS_FILE" lesson "$id"
done

tutorial --status-file "$TEST_STATUS_FILE" reset --yes

set +e
git checkout click_tutorial/cli.py
