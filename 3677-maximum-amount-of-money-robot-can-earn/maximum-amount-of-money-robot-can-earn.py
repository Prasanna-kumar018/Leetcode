class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        dir = [(1,0),(0,1)]
        m = len(coins)
        n = len(coins[0])
        INF = 10**20
        @cache
        def recur(x,y,used):
            if x==m-1 and y==n-1:
                return 0
            res = -INF
            for dx,dy in dir:
                nx,ny = x+dx,y+dy
                if 0<= nx <m and 0<= ny<n:
                    if coins[nx][ny]>=0:
                        res = max(res,recur(nx,ny,used)+coins[nx][ny])
                    else:
                        res = max(res,recur(nx,ny,used)+coins[nx][ny])
                        if used>0:
                            res = max(res,recur(nx,ny,used-1))
            return res
        return recur(-1,0,2)