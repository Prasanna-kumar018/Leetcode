class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q = collections.deque()
        m = len(isWater)
        n = len(isWater[0])
        for i in range(m):
            for j in range(n):
                if isWater[i][j]==1:
                    q.append((i,j))
                isWater[i][j]=-1
        level=0
        dir = [(-1,0),(1,0),(0,-1),(0,1)]
        while q:
            size = len(q)
            while size>0:
                x,y = q.popleft()
                if isWater[x][y]!=-1:
                    size-=1
                    continue
                isWater[x][y]=level
                for dx,dy in dir:
                    nx,ny = x+dx,y+dy
                    if 0<= nx <m and 0<= ny<n and isWater[nx][ny]==-1:
                        q.append((nx,ny))
                size-=1
            level+=1
        return isWater