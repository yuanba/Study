import sys
import time
from random import *
from copy import *
# import othe module and use some function to solve the instance in different ways

def check(data , w):
    '''
    This function will be called by create_init function to check whether the sequence satisfied the constraints
    Input:
        data - the sequence of the city
        w - the data from the file means the count of each city
    Output:
        bool - when satisfied return False , else return True
    Side affect:~
    '''
    l = 0
    for i in range(len(w)):
        l += w[data[i]]
        if l < 0:return True
    return False

def create_init(n , w):
    '''
    This function try to use the random module to create the random sequence of the city and check correction.
    Input:
        n - the number of the citys
        w - the data from the file means the count of each city
    Output:
        data - the list which hold the sequence , data[i] means the ith city is data[i].
    Side affect:~
    '''
    data = list(range(0,n))
    while check(data , w):
        shuffle(data)
    return data

# This Module Main.py do not write the data into the mysql , we use another module to do this job.
if __name__ == '__main__':
    n = int(input())
    m = list(map(lambda x:int(x) , input().split()))
    num = sys.argv[1]
    kk = sys.argv[2]
    seq = create_init(n,m)
    p = list(range(n+1))
    for i in range(1,n+1):
        p[i] = seq[i-1] + 1
    seq = p
    print("Create init successfully!")
    m[0:0] = [0]

    save = deepcopy(seq)

    #print(seq)
    func = 1
    import onepass as op
    ptime,result,origin,seq = op.solve(seq , m , step = 5 , w = 5)
    filename = '/home/lantian/File/Study Coding/Optimisation/GLPK-Tool/TSP-Hard/GLPK/mine/newPnd_' + kk + '/pnd_'  + num + '_1.res'
    f=open(filename,'w')
    f.write('Time: ' + str(ptime) + '\n')
    f.write('Result of Solve ' + str(func) + ': ' + str(result) + '\n')
    f.write('Result of Origin ' + str(func) + ': ' + str(origin) + '\n')
    import check_optimal as co
    nbest = co.optimal(seq , result , m)
    f.write('Result of new Optimal ' + str(func) + ': ' + str(nbest) + '\n')
    f.write('The last sequence of the solution: ' + str(func) + ':' + str(seq) + '\n')
    print('Function ' + str(func) + ' has been created!')
    f.close()

    #print(seq)
    seq = save
    #print("last",seq)
    func += 1
    import twochoose as tc
    if int(kk) == 50:cons = 50*49//2
    else:cons = 100*99//2
    ptime , result  ,origin , seq = tc.solve(seq , m , cons)
    filename = '/home/lantian/File/Study Coding/Optimisation/GLPK-Tool/TSP-Hard/GLPK/mine/newPnd_' + kk + '/pnd_'  + num + '_2.res'
    f = open(filename , 'w')
    f.write('Time: ' + str(ptime) + '\n')
    f.write('Result of Solve ' + str(func) + ': ' + str(result) + '\n')
    f.write('Result of Origin ' + str(func) + ': ' + str(origin) + '\n')
    import check_optimal as co
    nbest = co.optimal(seq , result , m)
    f.write('Result of new Optimal ' + str(func) + ': ' + str(nbest) + '\n')
    f.write('The last sequence of the solution: ' + str(func) + ': ' + str(seq) + '\n') 
    print('Function ' + str(func) + ' has been created!')
    
    '''func = 2
    import swap
    ptime,result = swap.solve(seq , m)
    filename = '/home/lantian/File/Study Coding/Optimisation/GLPK-Tool/TSP-Hard/GLPK/mine/newPnd_' + kk + '/pnd_'  + num + '_2.res'
    f=open(filename,'w')
    f.write('Time: ' + str(ptime) + '\n')
    f.write('Result of Solve ' + str(func) + ': ' + str(result) + '\n')
    print('Function ' + str(func) + ' has been created!')
    f.close()
    elif func == 3:
        import EBSR
        ptime,result = EBSR.solve()
        filename = '/home/lantian/File/Study Coding/Optimisation/GLPK-Tool/TSP-Hard/GLPK/mine/newPnd_' + kk + '/pnd_'  + num + '_3.res'
    else:
        import EFSR
        ptime.result = EFSR.solve()
        filename = '/home/lantian/File/Study Coding/Optimisation/GLPK-Tool/TSP-Hard/GLPK/mine/newPnd_' + kk + '/pnd_'  + num + '_4.res'
    # use the function to get the answer , (ptime , result) is the return data.
    # Ready to write into the file
    f=open(filename,'w')
    f.write('Time: ' + str(ptime) + '\n')
    f.write('Result of Solve ' + str(func) + ': ' + str(result) + '\n')
    print('Function ' + str(func) + ' has been created!')
    f.close()'''
