class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        dir = [(1,0),(0,1),(0,-1),(-1,0)]
        INF = 10**20
        dis = [[INF]*m for _ in range(n)]
        q = collections.deque()
        dis[0][0]=0
        q.append((0,0,0))
        while q:
            val,x,y = q.popleft()
            if dis[x][y]<val:
                continue
            
            for dx,dy in dir:
                nx,ny = x+dx,y+dy
                if 0<= nx <n and 0<= ny<m and dis[nx][ny]>max(val,moveTime[nx][ny])+1:
                    dis[nx][ny]= max(val,moveTime[nx][ny])+1
                    q.append((dis[nx][ny],nx,ny))
        return dis[-1][-1]