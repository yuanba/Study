#!/usr/bin/python3

from math import log

def calShannoneEnt(dataset):
    '''
    This function calculate the shannon entropy for the dataset
    Input :
        dataset : a set of data wait to analyse
    Output :
        float number represents the shannonEnt for the dataset
    Side affect :
        None
    Algorithm : 
        1. p(x) : num(x) / num_sum
        2. shannonEnt = - sum(i = 1 , n) p(i) * log(2 , p(i))
    '''
    length = len(dataset)
    label = {}
    for i in dataset:
        currentlabel = i[-1]
        if currentlabel not in label.keys():
            label[currentlabel] = 0
        label[currentlabel] += 1
    shannonEnt = 0.0
    for key in label:
        p = float(label[key]) / length
        shannonEnt -= p * log(p , 2)
    return shannonEnt

def splitDataset(dataset , axis , value):
    '''
    This function splite the dataset with the assured argument axis (the indec of the feature) and the value of this feature in one time
    Input :
        1. dataset : a set of data wait to analyse
        2. axis : the index of the feature
        3. value : the value of this feature 
    Output :
        new_dataset : the sub set of the dataset which only have the feature = value data
    Side affect :
        None
    '''
    new_dataset = []
    for i in dataset:
        if i[axis] == value:
            new_dataset.append(i)
    return new_dataset

def choosebestfeature(dataset):
    '''
    This function choose the best feature for the dataset right now
    Input :
        dataset : a set of the data , wait to split into some sub_datasets
    Output :
        int number : the best feature for the dataset , the index of the feature
    Side affext :
        None
    '''
    numfeatures = len(dataset[0]) - 1
    baseentroy = calShannoneEnt(dataset)
    baseinfogain = 0
    basefeature = -1
    for i in range(numfeatures):
        featureset = set([x[i] for x in dataset])
        new_entroy = 0.0
        for value in featureset:
            subdataset = splitDataset(dataset , i , value)
            p = len(subdataset) / float(len(dataset))
            new_entroy += p * calShannoneEnt(subdataset)
        infogain = baseentroy - new_entroy
        if infogain > baseinfogain : 
            baseinfogain = infogain
            basefeature = i
    return basefeature

# the test dataset
mydata = [[1,1,'y'],[1,1,'y'],[1,0,'n'],[0,1,'n'],[0,1,'n']]

# print(calShannoneEnt(mydata))

