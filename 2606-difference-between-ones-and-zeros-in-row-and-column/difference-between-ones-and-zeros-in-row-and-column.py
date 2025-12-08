class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        onei = [0]*m
        onej = [0]*n
        zeroi = [0]*m
        zeroj = [0]*n
        for i in range(m):
            for j in range(n):
                onei[i]+=grid[i][j]
                zeroi[i]+=(1-grid[i][j])
        for j in range(n):
            for i in range(m):
                onej[j]+=grid[i][j]
                zeroj[j]+=(1-grid[i][j])

        res = []
        for i in range(m):
            res.append([ onei[i]+onej[j]-zeroi[i]-zeroj[j] for j in range(n)])
        return res