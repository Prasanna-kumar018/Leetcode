class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        m , n= len(grid),len(grid[0])
        res = 10**20
        for i in range(m):
            for j in range(1,n):
                grid[i][j]+=grid[i][j-1]
        for j in range(n):
            grid[1][j]+=grid[0][j]
        def get(sx,sy,ex,ey):
            if sx<=ex and sy<=ey:
                return grid[ex][ey]-(grid[sx-1][ey] if sx-1>=0 else 0)-(grid[ex][sy-1] if sy-1>=0 else 0)+(grid[sx-1][sy-1] if sx-1>=0 and sy-1>=0 else 0)
            return 0
        for j in range(n):
            right_top = get(0,j+1,0,n-1)
            left_down = get(1,0,1,j-1)
            res = min(max(right_top,left_down),res)
        return res 