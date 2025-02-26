class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        q = []
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if (grid[i][j]%2) != ((i+j)%2):
                    grid[i][j]+=1
        if grid[0][1]>1 and grid[1][0]>1:
            return -1
        def push(val):
            heapq.heappush(q,val)    #  Using heap is the best (Always).....
        def pop():
            return heapq.heappop(q)
        push((0,0,0)) # time,x,y
        INF = 10**20
        dir = [(-1,0),(1,0),(0,1),(0,-1)]
        d = collections.defaultdict(lambda : collections.defaultdict(lambda : INF))
        d[0][0]=0
        while q:
            time,x,y = pop()
            if d[x][y] < time:
                continue
            for dx,dy in dir:
                nx,ny = x+dx,y+dy
                if 0<= nx < m and 0<= ny<n:
                    nd = max(time+1,grid[nx][ny])
                    if d[nx][ny]>nd:
                        d[nx][ny]=nd
                        push((d[nx][ny],nx,ny))
            # print(q)
        return d[m-1][n-1]