#!/bin/sh

pip3 install pyflakes pyyaml

cp /github/workspace/assignment.py /src/assignment.py

cd /src

python3 run.py
