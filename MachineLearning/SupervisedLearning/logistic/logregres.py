#!/usr/bin/python3

from math import *
from numpy import *

def loadtext():
    datamat = []
    label = []
    with open('test') as f:
        for i in f.readlines():
            p = i.strip().split()
            datamat.append([1 , float(p[0]) , float(p[1])])
            label.append(int(p[2]))
    return datamat , label

def sigmod(inx):
    return 1.0 / (1 + exp(-inx))

def logistic(datamat , label):
    datamatrix = mat(datamat)
    labelmat = mat(label).transpose()
    m , n = shape(datamatrix)
    alpha = 0.001
    step = 500
    weights = ones((n,1))
    for i in range(step):
        h = sigmod(datamatrix * weights)
        error = (labelmat - h)
        weights += alpha * datamatrix.transpose() * error
    return weights

def soclogistic(datamat , label):
    import random
    datamatrix = array(datamat)
    m , n = shape(datamat)
    weights = ones(n)
    for j in range(500):
        dataindex = list(range(m))
        for i in range(m):
            alpha = 4 / (i + j + 1.0) + 0.01
            randomindex = random.randint(0,len(dataindex) - 1)
            h = sigmod(sum(datamatrix[randomindex] * weights))
            error = label[randomindex] - h
            weights = weights + alpha * error * datamatrix[randomindex]
            del(dataindex[randomindex])
        return weights

def plotfit(weights):
    import matplotlib.pyplot as plt
    data , label = loadtext()
    dataarr = array(data)
    n = shape(dataarr)[0]
    x1 = [] ; y1 = []
    x2 = [] ; y2 = []
    for i in range(n):
        if int(label[i]) == 1:
            x1.append(dataarr[i,1]) ; y1.append(dataarr[i,2])
        else:
            x2.append(dataarr[i,1]) ; y2.append(dataarr[i,2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x1 , y1 , s = 30 , c = 'red' , marker = 's')
    ax.scatter(x2 , y2 , s = 30 , c = 'green')
    x = arange(-3.0 , 3.0 , 0.1)
    y = (-weights[0] - weights[1] * x) / weights[2]
    ax.plot(x , y)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.show()

if __name__ == "__main__":
    data , label = loadtext()
    weights = soclogistic(data , label)
    plotfit(weights)
