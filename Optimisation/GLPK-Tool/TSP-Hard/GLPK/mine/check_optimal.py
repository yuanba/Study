def optimal(seq , best , w):
    r'''
    This function get the solution and use three methods to optimal it.
    And should know that I only optimal between two point.
    Input:
        seq - The solution sequence in it. And we should know that seq is counting from 1 to n.but it size is n + 1.
        best - The best solution for this sequence.
        w - The weight of each point (City).
    Output:
        newbest - The new best solution and the new sequence.
    Side affect:
        The solution of the seq may be changed. So remember before call this function you should alreaady write the best into the file.
        And we return the changed sequence.
    DFA:
                  +___2+
                 /    |
                /     |
            +__1+     |-
           /    \     |
          /      \-__1+1-
         /            |
        E             | 
         \            |-
          \           |
           \-__1-__-__2-

        We sort the 6 point in :
        E : 1
        1+ : 2
        2+ : 3
        1+1- ; 4
        1- : 5
        2- : 6
        [Accpet]: 3 4 6
        [Origin]: 1
        And We can see that the DFA for my new solution optimal is up there!'''
    now = 1
    l = 0   # Save the path number of before.
    new = 0   # Save the weight in the city.
    


    a = 0
    b = 0
    #for i in range(1,len(seq)):
    #    b += w[seq[i]]
    #    a += b
    #print(a)
    for i in range(1 , len(seq)):
        l += new   # Count the number first.
        new += w[seq[i]]   # Save the before number for the last compare conveniently.
        #print("first: ",l)
        if now == 1 and w[seq[i]] > 0:now = 2
        elif now == 1 and w[seq[i]] <= 0:now = 5
        elif now == 2 and w[seq[i]] > 0:now = 3
        elif now == 2 and w[seq[i]] <= 0:now = 4
        elif now == 3 and w[seq[i]] <= 0:now = 4
        elif now == 4 and w[seq[i]] <= 0:now = 6
        elif now == 5 and w[seq[i]] <= 0:now = 6
        elif now == 3 and w[seq[i]] > 0:now = 3
        elif now == 4 and w[seq[i]] > 0:now = 2
        elif now == 5 and w[seq[i]] > 0:now = 2
        elif now == 6 and w[seq[i]] <= 0:now = 6
        elif now == 6 and w[seq[i]] > 0:now = 2
        if now == 3 and w[seq[i - 1]] > w[seq[i]]:
            l -= w[seq[i - 1]] - w[seq[i]]
            seq[i] , seq[i - 1] = seq[i - 1] , seq[i]
        elif now == 4 and new - w[seq[i-1]] >= 0:
            l = l - w[seq[i - 1]] + w[seq[i]]
            seq[i] , seq[i - 1] = seq[i - 1] , seq[i]
            now = 2
        elif now == 6 and w[seq[i - 1]] > w[seq[i]]:
            l -= w[seq[i - 1]] - w[seq[i]]
            seq[i] , seq[i - 1] = seq[i - 1] , seq[i]
        #print('last: ',l ,new, w[seq[i]] , w[seq[i - 1]])
        #print(l)
    return l
