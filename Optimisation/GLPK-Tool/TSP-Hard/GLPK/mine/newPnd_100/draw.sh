#!/bin/bash

cd ~/File/Study\ Coding/Optimisation/GLPK-Tool/TSP-Hard/GLPK/mine/newPnd_100/

p=`ls | grep pnd.*`
data=($p)
k=0

#echo "${data[*]}"

tag=()
for i in ${data[*]}
do
    tag[k]=`expr substr $i 8 1`
    k=`expr $k + 1`
done

#echo "HERE?"

origin=()
result1=()
result2=()
k=0
t=0

#echo ${tag[*]}

for i in ${data[*]}
do
#    echo "$i"
#    origin[t]=`awk '$3=="Origin"{print $5}' $i`
    if [ ${tag[k]} -eq 1 ]
    then
        result1[t]=`awk '$4=="Optimal"{print $6}' $i`
        origin[t]=`awk '$3=="Origin"{print $5}' $i`
    else
        result2[t]=`awk '$4=="Optimal"{print $6}' $i`
        origin[t]=`awk '$3=="Origin"{print $5}' $i`
    fi
    t=`expr $t + 1`
    k=`expr $k + 1`
done

echo "origin: ${origin[*]}"
echo "result1: ${result1[*]}"
echo "result2: ${result2[*]}"
