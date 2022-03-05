#!/bin/bash

git add .
git commit -m 'f'
git tag -a -m '' $1
git push origin head