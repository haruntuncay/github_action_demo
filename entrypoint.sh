#!/bin/sh

cp /src/runner.py /github/runner.py
cp /src/tests.py /github/tests.py

python3 /github/runner.py