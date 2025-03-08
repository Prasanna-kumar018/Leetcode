class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        dir = [(-1,0),(1,0),(0,1),(0,-1)]
        MOD = 10**9+7
        @cache
        def dfs(prev,x,y):
            if x<0 or y<0 or x>=m or y>=n or grid[x][y]<=prev:
                return 0
            res = 1
            for dx,dy in dir:
                nx,ny = x+dx,y+dy
                res += dfs(grid[x][y],nx,ny)
            return res
        m = len(grid)
        total = 0
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                total += dfs(-1,i,j)
        return total%MOD