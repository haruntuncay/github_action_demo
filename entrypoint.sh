#!/bin/sh

echo $(ls /)
echo $(/github)
echo $(/github/workspace)
echo "::set-output name=pdf-path::name-value"
cat /github/workspace/README.md
