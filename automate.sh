#!/usr/bin/sh
branch=$(git branch --show-current)
git add .
git commit -m "$1"
git push -u origin ${branch}
