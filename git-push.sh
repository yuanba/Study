#!/bin/bash

dating=`date`

git st    # Git show the status
git add .   # Git add the changes into the workspace
git ci -m "$dating $1"   # commit the changes
git push origin master &   # push commit into the Github in the back station and kill the output.
git lg    # show the log
