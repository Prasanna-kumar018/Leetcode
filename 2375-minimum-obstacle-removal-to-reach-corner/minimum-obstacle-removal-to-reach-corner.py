class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        dir = [(-1,0),(1,0),(0,1),(0,-1)]
        q = []
        def push(val):
            heapq.heappush(q,val)
        def pop():
            return heapq.heappop(q)
        INF = 10**20   
        m = len(grid)
        n = len(grid[0])
        dis = [[INF]*n for _ in range(m)]
        push((0,0,0))
        dis[0][0]=0
        while q:
            val,x,y = pop()
            if dis[x][y]<val:
                continue
            for dx,dy in dir:
                nx,ny = x+dx ,y+dy
                if 0<= nx<m and 0<= ny<n:
                    c = val + (1 if grid[nx][ny]==1 else 0)
                    if dis[nx][ny]>c:
                        dis[nx][ny]=c
                        push((c,nx,ny))
        return dis[-1][-1]