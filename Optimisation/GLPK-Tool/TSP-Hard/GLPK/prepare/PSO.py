from random import *
import sys
from copy import *

class agent_module:
    def __init__(self , n , w):
        self.now  = creat_init(n , w)
        self.pbestseq = []
        self.pbestres = 1e20
        self.pnow = 1e20
    def move(self , n , w , P_BEST_SEQ):
        # Try to move randomly
        SAMPLE = range(n)
        for i in range(5):
            for tt in range(1000):
                k = sample(SAMPLE , 2)
                self.now[k[0]] , self.now[k[1]] = self.now[k[1]] , self.now[k[0]]    # Try to swap
                pause = check_result(self.now , w)
                if pause == False or pause >= self.pnow : 
                    self.now[k[0]] , self.now[k[1]] = self.now[k[1]] , self.now[k[0]]   # REBACK
                    continue
                else :
                    self.pnow = pause
                    break
            if self.pnow > self.pbestres : self.pbest = self.pnow    # RECORD the pbest solution.
        ans1 = make_swap(self.now , self.pbestseq)
        ans2 = make_swap(self.now , P_BEST_SEQ)
        alpha = random()
        beta = random()
        # Random to chang the now sequence!
        if alpha > 0.5 : 
            for i in ans1:
                self.now[i[0]] , self.now[i[1]] = self.now[i[1]] , self.now[i[0]]
            if check_result(self.now , w) == False : 
                while True:
                    t = sample(SAMPLE , 2)
                    self.now[t[0]] , self.now[t[1]] = self.now[t[1]] , self.now[t[0]]
                    if check_result(self.now , w) == False : continue
                    else : break

        if beta > 0.5 : 
            for i in ans2:
                self.now[i[0]] , self.now[i[1]] = self.now[i[1]] , self.now[i[0]]
            if check_result(self.now , w) == False : 
                while True:
                    t = sample(SAMPLE , 2)
                    self.now[t[0]] , self.now[t[1]] = self.now[t[1]] , self.now[t[0]]
                    if check_result(self.now , w) == False : continue
                    else : break

def creat_init(n , w):
    '''
    This function get the size of the problem and try to return
    the init result of the question.
    Maybe use the function - check_result
    Input:
        n - the size of the question
        w - the weight of the cities
        nw - the size of the swap.Default 2.(Can be changed : Quick / Slow)
    Output:
        Tuple :
        (seq , swap)
        seq : the initial sequence of the problem
              the size of the sequence is n,but we only use 
              from 1 to n.
        swap : the iital swap of the problem
    Side effect:
        Nothing can be changed , Only return the things we want.
    '''
    data = list(range(n))
    for i in range(n):
        data[i] += 1
    while not check_result(data , w):
        shuffle(data)
    return data

def check_result(seq,w):
    '''
    This funtion try to check the sequence's correctation.
    If the sequence is not correct , return False
    else return the whole result of this sequence.
    Input:
        seq - the seqence of one solution
        w - the weight of the city
    Output:
         var : when the sequence is correct then return the result.
         False : this squence is not correct
    Side effect:
        Nothing can be changed
    '''
    p = 0   # the weight when we in ith city
    res = 0   # the result of this sequence
    for i in range(n):
        p += w[seq[i]]
        if p < 0:return False
        res += p
    return res

def make_swap(seq1 , seq2):
    '''
    This function try to make the list of the swap from two seqence.
    Input:
        seq1,seq2 - two sequence of the solution
        seq1,seq2 have the order!!
    Output:
        res - the list of the swap
        the res is the list , but the swap is the tuple.
    Side effect:
        Nothing can be changed .
    '''
    res = []
    for i,j in enumerate(seq1):
        p = seq2.index(j)
        if i != p:res.append((i,p))
    return res

def PSO(n , w , nagent , time):
    '''
    This function use the PSO Algorithm to solve the question.
    Input:
        n - the size of the question
        w - the weight of the city
        nagent - the size of the agents
        nw - the Default swap number of a swap list
        time - the time of the iterations
    Output:
        origin - the soluton of the begining
        best - the best solution answer
        bestseq - the best sequence of the question
    Side effect:
        Nothing.
    '''
    #import pdb
    #pdb.set_trace()    # Try to see what make the self.pnow become a False.
    P = []    # the agents set
    P_BEST = 1e20    # Define the INF by myself
    P_BEST_SEQ = []  # Define the sequence of the best , init is the empty list.
    origin = 1e20
    # Up is the param ----------------------------------------------------------
    # Begin to init the agents
    for i in range(nagent):
        P.append(agent_module(n , w))
    # End to init the agents
    for i in range(time):    # the time decressing ...
        for j in range(nagent):
            P[j].pnow = check_result(P[j].now , w)
            if P[j].pnow < P[j].pbestres:    # Renew the agent .
                P[j].pbestres = P[j].pnow
                P[j].pbestseq = deepcopy(P[j].now)
        t = -1
        for j in range(nagent):
            if P[j].pnow < P_BEST:
                P_BEST = P[j].pnow
                t = j
        if i == 0 : origin = P_BEST
        if t != -1 : P_BEST_SEQ = deepcopy(P[t].pbestseq)    # If satisfied , we RENEW the P_BEST
        # Try to MOVE the agent
        for j in range(nagent):
            P[j].move(n , w , P_BEST_SEQ)    # Use n to move 
        if i % (int(0.1 * time)) == 0 : 
            print("Processing %s / %s , BEST_NOW : %s" % (i , time , P_BEST) , end = '\r')
    return (origin , P_BEST , P_BEST_SEQ)

def readfile():
    '''
    This function try to read the data from the file.
    But should know that I use the < to put the data stream into the python script.
    Input：
        the file reading
    Output:
        the tuple of the data:
        (size,data):
        size - the size of the question.(int)
        data - the weight of the cities.(list)
    Side effect:
        Nothing!
    '''
    n = int(input())
    w = input()
    w = w.split()
    for i in range(n):
        w[i] = int(w[i])
    return (n , w)

def writefile(n , origin , best , seq , path):
    '''
    This function try to write the answer into the file.
    Input:
        n - the size of the question
        origin - the origin question of the question
        best - the result after optimisation
        seq - the sequence of the best.
    '''
    with open("/home/lantian/File/Study Coding/Optimisation/GLPK-Tool/TSP-Hard/GLPK/prepare/PSO_" + str(n) + '/' + path, 'w') as f:
        f.write('The size of the question : ' + str(n) + '\n')
        f.write('The origin : ' + str(origin) + '\n')
        f.write('The best : ' + str(best) + '\n')
        f.write('The sequence of the best : ' + str(seq))

if __name__ == "__main__":
    n , w = readfile()
    w[0:0] = [0]   # Save the w is the (n + 1) size
    path = sys.argv[1]
    nagent = int(sys.argv[2])
    time = int(sys.argv[3])
    origin , best , bestseq = PSO(n , w , nagent , time)
    writefile(n , origin , best , bestseq , path)
    print("One of the Instance has been writed into the file!")

