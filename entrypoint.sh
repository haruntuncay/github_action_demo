#!/bin/sh

pip3 install pyflakes, pyyaml

cp /github/workspace/assignment.py /src/assignment.py

python3 /src/run.py
