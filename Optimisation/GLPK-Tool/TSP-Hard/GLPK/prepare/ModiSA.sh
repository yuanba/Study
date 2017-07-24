#!/bin/bash

number=${1}

if [ ! $number ]
then
    echo "Please input the size of the question (50,100)."
    exit 1
fi

cd ~/File/Study\ Coding/Optimisation/GLPK-Tool/TSP-Hard/GLPK/prepare/PnD_${number}/

mkdir ../PSO_${number}

p=`ls | grep 'pnd.*.dat'`
data=($p)

k=0
tag=()
for i in ${data[*]}
do
    if [ $number -eq 100 ]
    then
        tag[k]=`expr substr $i 9 2`
    else
        tag[k]=`expr substr $i 8 2`
    fi
    k=`expr $k + 1`
done

k=0
for i in ${data[*]}
do
    python3 ../PSO.py ${tag[k]} 40 500 < $i
    k=`expr $k + 1`
done

