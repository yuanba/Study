#!/bin/bash

number=$1
if [ ! $number ]
then
    echo "Please input the argument such as 50 , 100 !"
    exit 1
fi

cd /home/lantian/File/Study\ Coding/Optimisation/GLPK-Tool/TSP-Hard/GLPK/prepare/

mkdir GLPK_${number}

cd ./PnD_${number}

p=`ls | grep pnd.*.dat`
cd ../GLPK_${number}
data=($p)

for i in ${data[*]}
do
    python3 ../trans.py $number $i
done
