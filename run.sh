#!/bin/bash
# My first script

echo "Things are pushed to github. Changelog:$1"


git submodule foreach git pull origin master
git add .
git commit -m "$1"
git push origin master
echo "copying."
cp -r turjeeman-client/src/ static
