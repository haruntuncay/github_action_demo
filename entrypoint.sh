#!/bin/sh

echo $(ls /github/workspace)

python3 /github/workspace/src/a.py

python3 /src/test_a.py