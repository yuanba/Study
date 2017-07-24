from random import *
from time import *

def check(data , w):
    l = 0
    p = 0
    for i in range(1,len(w)):
        p += w[data[i]]
        l += p
        if p < 0:return True
    return False

def count(seq,data):
    l = 0
    p = 0
    for i in range(1, len(data)):
        p += data[seq[i]]
        l += p
    return l

def solve(seq , data , maxp):
    '''
    This function is anthor method which can compared with the method onepass . In this case , I choose two random sequnece's number and try to swap them . And if the new point is better than now , I try to choose it as the now point.
    But , We should remember that because I use the builtin.method from random.sample (Which can return n(You decide) random number from the sequence) so I really need to choose the max number of trying to sqap two random number . So I set a input function to hold this tag.
    If I try to use the SA Algorithm to upgrade the Climbing-Hills Algorithm , I can decrease the maxp.
    Input:
        seq - The sequence I got from init.
        data - The weight of each city.
        maxp - The number of the max to hold decide the times of our iterations.
    Output:
        (ptime , best , origin , seq) - the local Optimisation of the result
    Side affect:
        seq - sequence maybe changed after the fucntion . But  We only care about the optimal. So it doesn't matter.
    '''
    a = time()
    origin = best = count(seq , data)
    #maxp = int(input('Please input the maximize numher: '))
    for i in range(maxp):
        lucky = sample(seq , 2)
        seq[lucky[0]] , seq[lucky[1]] = seq[lucky[1]] , seq[lucky[0]]
        if check(seq,  data) == False:
            new = count(seq , data)
            if new < best:
                best = new
                continue
        seq[lucky[0]] , seq[lucky[1]] = seq[lucky[1]] , seq[lucky[0]]
    b = time()
    return (b - a , best , origin , seq)
