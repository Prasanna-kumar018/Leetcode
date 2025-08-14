class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        q = []
        m = len(grid)
        n = len(grid[0])
        INF = 10**9
        fire = [[INF]*n for _ in range(m)]
        def push(val):
            heapq.heappush(q,val)
        def pop():
            return heapq.heappop(q)
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    push((0,i,j))
        dir = [(-1,0),(1,0),(0,1),(0,-1)]
        vis = set()
        while q:
            val,i,j = pop()
            if (i,j) in vis:
                continue
            vis.add((i,j))
            fire[i][j]=val
            for dx,dy in dir:
                nx,ny = i+dx,j+dy
                if 0<= nx<m and 0<= ny < n and grid[nx][ny]!=2 and (nx,ny) not in vis:
                    push((val+1,nx,ny))
        print(fire)
        q = collections.deque([(0,0,0,INF)])
        vis = set()
        ans = -1
        while q:
            step, x,y , val = q.popleft()
            # print(step,fire[x][y],x,y,vis)
            if x==m-1 and y==n-1:
                if val==INF-step:
                    return INF
                ans = max(ans,val)
            # print(step,fire[x][y],x,y,vis)
            if (x,y) in vis:
                continue
            vis.add((x,y))
            for dx,dy in dir:
                nx,ny = x+dx , y+dy
                if 0<= nx <m and 0<= ny < n and grid[nx][ny]!=2 and (nx,ny) not in vis and step+1<=fire[x][y]:
                    if nx==m-1 and ny==n-1:
                        q.append((step+1,nx,ny,min(val,fire[nx][ny]-(step+1))))
                    else:
                        q.append((step+1,nx,ny,min(val,fire[nx][ny]-(step+1)-1)))
            # print(q)
        return ans 

