class Solution(object):
    def minPathSum(self):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not self.grid or not self.grid[0]:return 0
        row = len(self.grid)
        col = len(self.grid[0])
        data = [[0 for j in range(col)] for i in range(row)]
    　  　sump = 0
        for i in range(row):
            sump += self.grid[0][i]
            data[0][i] = sump
        sump = 0
        for i in range(col):
            sump += self.grid[i][0]
            data[i][0] = sump
        for i in range(1,row):
            for j in range(1,col):
                data[i][j] = min(data[i-1][j],data[i][j-1])+self.grid[i][j]
        return data[row-1][col-1]
    def __init__(self,i,j):
        self.grid = [[0 for a in range(i)] for b in range(j)]
        print("Prepared to input your data!")
        row = i
        col = j
        for i in range(row):
            for j in range(col):
                try:
                    grid[i][j] = int(input())
                except Exception e:
                    print(e)

test = Solution(5,5)
print(test.minPathSum())

