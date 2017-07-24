#!/bin/bash

cd ~/File/Study\ Coding/Optimisation/GLPK-Tool/TSP-Hard/GLPK/prepare/SA_100/

p=`ls | grep 100.*`
data=($p)
k=0

#echo "${data[*]}"

tag=()
for i in ${data[*]}
do
    tag[k]=`expr substr $i 5 2`
    k=`expr $k + 1`
done

#echo "HERE?"

echo "${data[*]}"

origin=()
result2=()
k=0
t=0

#echo ${tag[*]}

for i in ${data[*]}
do
#    echo "$i"
#    origin[t]=`awk '$3=="Origin"{print $5}' $i`
    result2[t]=`awk '$2=="after"{print $4}' $i`
    origin[t]=`awk '$2=="before"{print $4}' $i`
    t=`expr $t + 1`
    k=`expr $k + 1`
done

echo "origin: ${origin[*]}"
echo "lalala"
for i in ${result2[*]}
do
    echo -n "$i,"
done
