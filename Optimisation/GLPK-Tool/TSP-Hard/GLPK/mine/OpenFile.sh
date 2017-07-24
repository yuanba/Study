#!/bin/bash

number=${1}

# Change dir

if [ ! $number ] 
then
    echo "Please input some data (50 , 100)"
    exit 1
fi

cd /home/lantian/File/Study\ Coding/Optimisation/GLPK-Tool/TSP-Hard/GLPK/prepare/PnD_${number}/

mkdir ../../mine/newPnd_${number}

# Main.py solve one file ine time , And the first argv is the number of the file sequence.
# And in the Main , I try to import some other py module and use pymysql to write the ansswer of some Optimisation of each module into the file I point.

#source ../../mine/Main.py 

p=`ls | grep pnd.*.dat`
cd ../../mine/
data=($p)
tag=()

k=0
for i in ${data[*]}
do
    if [ $number -eq 100 ]
    then
        tag[k]=`expr substr ${i} 9 2`
    else
        tag[k]=`expr substr ${i} 8 2`
    fi
    k=`expr $k + 1`
done

k=0
for i in ${data[*]}
do
    for j in 1 2
    do
#        touch ./newPnd_${number}/pnd_${tag[k]}_${j}.res
        python3 Main.py ${tag[k]} ${number} < ../prepare/PnD_${number}/$i
        # The p present the instance the k present the number of the function.
    done
    k=`expr $k + 1`
done
