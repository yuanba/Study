import sys
from random import *

def item_constraint(n):
    '''Create the constraint of the random data'''
    pmax = 99
    cmaxest = int(n * pmax * 0.6)
    dmin = pmax // 2
    dmax = cmaxest
    return (pmax , dmin , dmax)

def create_item(constraint):
    '''According to the constraint , create one corresponding item'''
    pmax = constraint[0]
    dmin = constraint[1]
    dmax = constraint[2]
    p1 = randint(pmax // 4,pmax)
    p2 = randint(pmax // 4,pmax)
    d = randint(dmin,dmax)
    return (p1 , p2 , d)

def create_all(n):
    '''Create the constraint and create a set of the data'''
    cons = item_constraint(n)
    ans = {}
    for i in range(n):
        ans[i] = create_item(cons)
    return ans

def tbar(ans , queue , n):
    '''queue: The number of the jobs in the queue , counting from 0 to n-1
       ans: Every item of the job has its p1 ,p2 ,deadline which is the tuple
       O(n)
    '''
    c1 = [0 for i in range(n)]    #The end time which belongs to every jobs on machine one
    c2 = [0 for i in range(n)]    #..........machine two
    for i in range(n):
        if i == 0 and i-1<0:
            c1[i] = ans[queue[0]][0]
        else:
            assert i<len(queue) , (queue,i)
            c1[i] = c1[i-1] + ans[queue[i]][0]
    for i in range(n):
        if i == 0:c2[i] = c1[0] + ans[queue[0]][1]
        else:c2[i] = max(c2[i-1] , c1[i]) + ans[queue[i]][1]
    late = [0 for i in range(n)]
    for i in range(n):
        late[i] = c2[i] - ans[queue[i]][2]
        if late[i] < 0:late[i] = 0
    return sum(late)

