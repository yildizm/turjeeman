#!/bin/bash
# to put things into github. $1 takes remote branch, $2 takes commit message

echo "Things are pushed to github. Changelog:$1"


git submodule foreach git pull origin master
git add .
git commit -m "$2"
git push origin $1
echo "copying."
#cp -r turjeeman-client/src/ static
