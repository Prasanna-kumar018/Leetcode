class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rowmax= [0]*n
        colmax= [0]*n
        for i in range(n):
            maxi = max(grid[i])
            rowmax[i]=maxi
        for j in range(n):
            maxi = float('-inf')
            for i in range(n):
                maxi= max(maxi,grid[i][j])
            colmax[j]=maxi
        res = 0
        for i in range(n):
            for j in range(n):
                res+=(min(rowmax[i],colmax[j])-grid[i][j])
        return res