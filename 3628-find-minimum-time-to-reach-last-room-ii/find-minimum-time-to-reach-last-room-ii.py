class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m = len(moveTime)
        n = len(moveTime[0])
        INF = 10**20
        dis = [[INF]*n for _ in range(m)]
        q = []
        def push(val):
            heapq.heappush(q,val)
        def pop():
            return heapq.heappop(q)
        push((0,0,0,1))
        dis[0][0]=0
        dir = [(-1,0),(1,0),(0,-1),(0,1)]
        while q:
            val,x,y,last = pop()
            if dis[x][y]<val:
                continue
            for dx,dy in dir:
                nx,ny = x+dx,y+dy
                if 0<= nx<m and 0<=ny<n and dis[nx][ny]>max(dis[x][y],moveTime[nx][ny])+last:
                    dis[nx][ny]= max(dis[x][y],moveTime[nx][ny])+last
                    push((dis[nx][ny],nx,ny,(3-last)))
        return dis[-1][-1]
