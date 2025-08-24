class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        dir = [(1,0),(0,1)]
        M = len(grid)
        N = len(grid[0])
        MOD = 10**9 + 7
        @cache
        def recur(x,y,mod):
            if x==M-1 and y==N-1:
                return int(mod==0)
            res = 0
            for dx,dy in dir:
                nx,ny = x+dx,y+dy
                if 0 <= nx < M and 0 <= ny <N:
                    res += recur(nx,ny,(mod+grid[nx][ny])%k)
            return res % MOD
        x = recur(0,0,(grid[0][0])%k)
        return x