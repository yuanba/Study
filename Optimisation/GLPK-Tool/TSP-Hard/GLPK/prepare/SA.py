from random import *
from time import *
from math import *
from copy import *
import sys

# Import the package only once.
sys.path.append('/home/lantian/File/Study Coding/Optimisation/GLPK-Tool/TSP-Hard/GLPK/')

from mine.Main import create_init , check
from mine.onepass import count
from mine.check_optimal import optimal

func_number = int(sys.argv[1])

T0 = 1000    # The Begining temp of the question
Tn = 1e-6    # The Last temp of the question
INNERL = 1000    # Inner limite of the search
OUTTERL = 1000    # Outter limite of the search 
CHOOSELIMIT = 1000    # We must control the time of Not-Good choose

buf = [0,0,0]    # Save the buf in order to redo the bad move.

def COLD(t):
    '''
    This function is the decrease the temperature function.
    Input:
        t - input the data of the and try to calulate the next temperature.
        T0 - The init temperature of the question.
    Output:
        return the next decrease temperature.
    Side affect:~

    I have some question for this ?????
    '''
    #return T0/log(1+t)
    return 0.98*t

# Function 1
def fun_onepass(seq , data):
    n = len(data)
    # Define the shuffle space (begin , end)
    begin = randint(1, n - 2)
    end = randint(begin + 1 ,n - 1)
    best = count(seq , data)
    limite = 1
    for i in range(begin , end + 1):
        limite = limite * i
    for i in range(limite):
        pause = seq[begin:end + 1]
        tty = deepcopy(pause)
        shuffle(pause)
        seq[begin:end + 1] = pause
        if check(seq , data) == False:
            buf[0] , buf[1] ,buf[2]= begin , end , tty
            return count(seq , data)
        else:seq[begin:end + 1] = tty
    return 0
    
# Function 2
def fun_twochoose(seq , data):
    n = len(data)
    # Define the change position
    limite = n*(n-1)//2
    for i in range(limite):
        begin , end = sample(range(1,len(seq)) , 2)
        seq[begin] , seq[end] = seq[end] , seq[begin]
        if check(seq , data) == False:
            buf[0] , buf[1] = begin , end
            return count(seq , data)
        else:seq[begin] , seq[end] = seq[end] , seq[begin]
    return 0

def read_file():
    '''
    This function read the data from the file
    Output:
        n - the size of the data.
        m - the weight of each city (point).
    '''
    n = int(input())
    m = list(map(lambda x:int(x) , input().split()))
    return (n,m)

# Write the solution into  ../mine/SA_50 or ../mine/SA_100
def write_file(n , func_num , ptime , nbest , oldbest , seq):
    func_num = str(func_num)
    num_instance = sys.argv[2]
    # Python 只能用绝对路径创建不存在的文件
    filename = '/home/lantian/File/Study Coding/Optimisation/GLPK-Tool/TSP-Hard/GLPK/prepare/SA_' + str(n) + '/' + str(n) + '_' + num_instance + '_' + func_num
    with open(filename , 'w') as f:
        f.write('Time: ' + str(ptime) + '\n')
        f.write('Result before optimal: ' + str(oldbest) + '\n')
        f.write('Result after optimal: ' + str(nbest) + '\n')
        f.write('Result of the sequence: ' + str(seq) + '\n')

# The main function below is that most important things in the SA Algorithm.
if __name__ == '__main__':
    a = time()
    n , data = read_file()
    origin = create_init(n , data)    # The init solution of the question.
    #print(origin)
    data[0:0] = [0]    # hold the data to n + 1
    p = list(range(n + 1))
    for i in range(1 , n+1):
        p[i] = origin[i - 1] + 1
    origin = p
    oldbest = best = count(origin , data)
    #print(0,oldbest)
    i = 1
    if func_number == 1:
        print("Too slow,Try to exit.")
        exit(0)
    else:fun = fun_twochoose
    T = T0
    while True:
        T = COLD(T)    
        i += 1
        limiteInner = 0
        limiteOutter = 0
        for j in range(INNERL):
            nextp = fun(origin , data)
            if nextp == 0:E = 0
            else:E = nextp - best
            if E < 0:
                best = nextp    # If the solution is better than the origin , then renew it.
                limiteInner = 0
            else:
                p = uniform(0 , 1)
                if 0 <= p <= e**(-E / T):
                    if nextp != 0:best = nextp
                else:
                    if func_number == 1:origin[buf[0]:buf[1] + 1] = buf[2]
                    else:origin[buf[0]],origin[buf[1]] = origin[buf[1]],origin[buf[0]]
                limiteInner += 1    # If this solution is not better than the current solution , do this job.
            if limiteInner > CHOOSELIMIT:
                limiteOutter += 1
                break
        if T < Tn or limiteOutter > OUTTERL:
            break
        #print(T , best)
    #print(best,origin)
    nbest = optimal(origin , best , data)
    print(best,nbest)
    b = time()
    write_file(n , func_number , b - a , best , oldbest , origin)
