#!/bin/bash

git add .
git commit -m 'f'
git tag -a -m 'tag' $1
git push --follow-tags