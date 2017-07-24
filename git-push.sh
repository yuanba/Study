#!/bin/bash

dating=`date`

git st    # Git show the status
git add .   # Git add the changes into the workspace
git ci -m "$dating"   # commit the changes
git push origin master > /dev/null &   # push commit into the Github in the back station and kill the output.
