from copy import *
from time import *
from random import *

#from Main import check 
def check(data , w):
    l = 0
    p = 0
    for i in range(1 , len(w)):
        p += w[data[i]]
        l += p
        if p < 0:return True
    return False

def count(seq , data):
    l = 0
    p = 0
    #print(len(seq) , seq)
    #print(len(data) , data)
    for i in range(1 , len(data)):
        try:
            p += data[seq[i]]
            l += p
        except IndexError:
            print(i)
    return l

def solve(seq , data , step = 5 , w = 5):
    '''
    This function try to solve the init sequence and create the local Optimisation result.
    If I use the SA Algorithm to upgrade the Climbing-Hill Algorithm , I can enlarge the step and decrease the w.
    Input:
        seq - the init sequence of the city
        data - the weight of each city
        step - the step of the onepass moving
        w - the length of the interval
    Output:
        (ptime , best , origin , seq) - the local Optimisation of the result
    Side affect:
        seq - seq maybe changed after every search , but we will return the most Optimisation result which is satified
        In the Python , It must not be changed , becaouse i use the  = operator.But it is also risky.
    '''
    a = time()
    n = len(data)  # Calculate the size of the city.
    origin = best = count(seq , data)
    limite = 1
    for i in range(1,w+1):
        limite = limite * i
    for i in range(1,n+1,step):
        begin = i
        end = i + w - 1
        if end > n:break
        pause = seq[begin:end + 1]
        now = deepcopy(seq)
        for k in range(limite):
            shuffle(pause)
            now[begin:end + 1] = pause
            if check(now , data) == False:
                new = count(now , data)
                if new < best:
                    best = new
                    seq = now
                    break
    b = time()
    return (b - a,best,origin,seq)



