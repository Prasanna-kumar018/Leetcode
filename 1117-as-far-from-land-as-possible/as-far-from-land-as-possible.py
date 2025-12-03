class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = []
        def push(x):
            heapq.heappush(q,x)
        def pop():
            return heapq.heappop(q)
        INF = 10**20
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    push((0,i,j))
                    grid[i][j]=0
                else:
                    grid[i][j]=INF
        dir = [(-1,0),(1,0),(0,-1),(0,1)]
        while q:
            cost,x,y = pop()

            for dx,dy in dir:
                nx,ny = x+dx,y+dy
                if 0 <= nx < m and 0<= ny <n and grid[nx][ny]>cost+1:
                    grid[nx][ny]=cost+1
                    push((cost+1,nx,ny))
        aa = max([max(x) for x in grid])
        return aa if aa!=INF and aa!=0 else -1