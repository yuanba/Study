n = int(raw_input())
map = [[0]*15 for i in range(15)]
minp = 10000000
book = [0 for i in range(15)]

for i in range(n):
    data = (raw_input()).split()
    for j in range(len(data)):
        map[i][j] = int(data[j])

def dfs(step , sump):
    global minp
    if step == n:
        if sump < minp:minp = sump
        return
    else:
        k = 0
        for i in range(n):
            p = 10000000
            if book[i] == 1:continue
            for j in range(step,n):
                if map[j][i] < p:p = map[j][i]
            k += p
        for i in range(n):
            if book[i] == 0 and (sump + k) < minp:
                book[i] = 1
                dfs(step + 1,sump + map[step][i])
                book[i] = 0


dfs(0,0)
print minp
