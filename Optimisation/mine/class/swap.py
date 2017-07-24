from component import *
import sys
from random import shuffle
from collections import deque
from pymysql import *
from copy import *

def swap1(n , queue,ans):
    '''Change interfacing item O(n)'''
    best = tbar(ans , queue , n)
    for i in range(n-1):
        queue[i],queue[i+1] = queue[i+1],queue[i]
        tb = tbar(ans , queue, n)
        if tb < best:
            best = tb
        queue[i],queue[i+1] = queue[i+1],queue[i]
    return best

def swap2(n, queue,ans):
    '''Change interfacing item O(n^2)'''
    best = tbar(ans , queue , n)
    for i in range(n):
        for j in range(i+1,n):
            queue[i],queue[j] = queue[j],queue[i]
            tb = tbar(ans ,queue,n)
            if tb < best:
                best = tb
            queue[i],queue[j] = queue[j],queue[i]
    return best

def swap3(n,queue,ans):
    '''Change interfacing item O(n^3)'''
    best = tbar(ans , queue , n)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                queue[i],queue[j],queue[k] = queue[j],queue[k],queue[i]
                tb = tbar(ans,queue,n)
                if tb < best:best = tb
                queue[i],queue[j],queue[k] = queue[j],queue[k],queue[i]
                tb = tbar(ans,queue,n)
                if tb < best:best = tb
                queue[i],queue[j],queue[k] = queue[j],queue[k],queue[i] 
    return best

def swap4(n,queue,ans):
    '''EBFS'''
    best = tbar(ans,queue,n)
    for i in range(n-1,-1,-1):
        for j in range(i-1,-1,-1):
            queue[j],queue[j+1] = queue[j+1],queue[j]
            tb = tbar(ans,queue,n)
            if tb < best:best = tb
        for j in range(i):
            queue[j],queue[j+1] = queue[j+1],queue[j]
    return best

def swap5(n,queue,ans):
    '''EFFS'''
    best = tbar(ans,queue,n)
    for i in range(n):
        for j in range(i+1,n):
            queue[j],queue[j-1] = queue[j-1],queue[j]
            tb = tbar(ans,queue,n)
            if tb < best:best = tb
        for j in range(n-1,i,-1):
            queue[j],queue[j-1] = queue[j-1],queue[j]
    return best

def write(mod,n,ans):
    #mod = int(input('Please to choose one method(0:random,1:EDD,2:NEH)'))
    queue = list(range(n))
    if mod == 0:
        shuffle(queue)
    elif mod == 1:   #The EDD sort with the dealine increasing.
        queue.sort(key = lambda x:ans[x][2])
    else:     #The NEH begin with the EDD up.
        queue.sort(key = lambda x:ans[x][2])
        result = queue[0:2]   #store the final NEH queue.
        ans1 = tbar(ans , result , 2)
        result[0],result[1] = result[1],result[0]
        ans2 = tbar(ans , result , 2)
        qbest = result.copy()
        if ans1 < ans2:
            result[0],result[1] = result[1],result[0]
        for i in range(2,n):
            best = 2**63-1
            for j in range(0,i+1):
                result.insert(j,queue[i])
                tb = tbar(ans,result,i+1)
                if tb < best:
                    best = tb
                    qbest = result.copy()
                result.remove(queue[i])
            result = qbest.copy()
        queue = qbest
    status = [mod]
    status.append(tbar(ans,queue,n))
    status.append(swap1(n,queue,ans))
    status.append(swap2(n,queue,ans))
    status.append(swap3(n,queue,ans))
    status.append(swap4(n,queue,ans))
    status.append(swap5(n,queue,ans))
    return status

def final():
    size = int(sys.argv[1])     #The number of one kind of the instance
    jobsize = int(sys.argv[2])
    res = []
    pos = 1
    for j in range(size):
        for i in range(3):
            ans = create_all(jobsize)
            k = write(i,jobsize,ans)
            k.insert(0,pos)
            res.append(k)
        pos += 1
    conn = connect(host="localhost",port=3306,user='root',passwd='lt970106',db='flowshop')
    cur = conn.cursor()
    cur.execute('CREATE TABLE res(id int,sta int,s0 int,s1 int,s2 int,s3 int,s4 int,s5 int,constraint pk primary key(id,sta))')
    cur.executemany('insert into res values(%s,%s,%s,%s,%s,%s,%s,%s);',res)
    conn.commit()
    conn.close()

if __name__ =='__main__':
    final()
    #size = int(sys.argv[1])
    #jobsize = int(sys.argv[2])
    #queue=list(range(jobsize))
    #shuffle(queue)
    #ans = create_all(jobsize)
    #print(ans)
    #print(queue)
    #print(tbar(ans,queue,jobsize))
