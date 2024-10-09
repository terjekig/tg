#!/bin/bash

BRANCH=$(git rev-parse --abbrev-ref HEAD)

README_TEMPLATE="# PROBLEM_TITLE

### PROBLEM_SUMMARY

problem_description


#### Example 1:

    example_1

#### Example 2:

    example_2

#### Example 3:

    example_3


#### Constraints:

    constraints

"


if [ ! -d ./$BRANCH ]; then
    mkdir -p ./$BRANCH/{py,cpp} && echo "$README_TEMPLATE" > ./$BRANCH/README.md && echo "Folders created"
    for ext in py cpp; do touch ./$BRANCH/$ext/$BRANCH.$ext; done && echo "Files created"
else
    echo "$BRANCH folder already exists"
fi

