#!/bin/bash

BRANCH=$(git rev-parse --abbrev-ref HEAD)

if [ ! -d ./$BRANCH ]; then
    mkdir -p ./$BRANCH/{py,cpp} && echo "$BRANCH" > ./$BRANCH/README.md && echo "Folders created"
    for ext in py cpp; do touch ./$BRANCH/$ext/$BRANCH.$ext; done && echo "Files created"
else
    echo "$BRANCH folder already exists"
fi

