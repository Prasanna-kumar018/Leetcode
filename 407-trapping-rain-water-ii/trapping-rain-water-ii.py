class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        q = []
        def push(val):
            heapq.heappush(q,val)
        def pop():
            return heapq.heappop(q)
        
        m = len(heightMap)
        n = len(heightMap[0])

        for i in range(m):
            push((heightMap[i][0],i,0))
            push((heightMap[i][n-1],i,n-1))
            heightMap[i][0] = heightMap[i][n-1] = -1
        for j in range(n):
            push((heightMap[0][j],0,j))
            push((heightMap[m-1][j],m-1,j))
            heightMap[0][j] = heightMap[m-1][j] = -1

        total = 0
        dir =[(-1,0),(1,0),(0,-1),(0,1)]
        while q:
            cost , x,y = pop()
            for dx,dy in dir:
                nx,ny = x+dx , y+dy
                if 0<= nx <m and 0<= ny <n and heightMap[nx][ny]!=-1:
                    total += max(0,cost-heightMap[nx][ny])
                    push((max(cost,heightMap[nx][ny]),nx,ny))
                    heightMap[nx][ny]=-1
        return total