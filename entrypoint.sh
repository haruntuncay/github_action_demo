#!/bin/sh

echo $(ls /)
echo $(ls /src)
echo $(/github)
echo $(/github/workspace)
echo "::set-output name=pdf-path::name-value"
cat /github/workspace/src/a.py

python3 /src/test_a.py