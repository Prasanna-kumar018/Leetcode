class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dir = [(-1,1),(1,1),(1,-1),(-1,-1)]
        @cache
        def recur(x,y,last,used,d): # d denotes direction
            best = 0
            nx,ny = x+dir[d][0],y+dir[d][1]
            if 0<= nx <m and 0<= ny<n and grid[nx][ny]==(2-last):
                best = max(best,recur(nx,ny,(2-last),used,d)+1)
            if not used:
                d = (d+1)%4
                nx,ny = x+dir[d][0],y+dir[d][1]
                if 0<= nx <m and 0<= ny<n and grid[nx][ny]==(2-last):
                    best = max(best,recur(nx,ny,(2-last),True,d)+1)
            return best
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    ans = max(ans,1)
                    for idx,(dx,dy) in enumerate(dir):
                        nx,ny=i+dx,j+dy
                        if 0<= nx <m and 0<= ny<n and grid[nx][ny]==2:
                            # print(recur(nx,ny,2,False,idx),i,j)
                            ans = max(ans,recur(nx,ny,2,False,idx)+2) 
        return ans

