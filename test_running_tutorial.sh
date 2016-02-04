#!/bin/bash

set -e

lesson_ids=$(tutorial lesson-ids | sed "s/,/ /g")

tutorial reset --yes

for id in $lesson_ids
do
    echo "Testing lesson $id..."
    tutorial solve "$id"
    tutorial lesson "$id"
done
