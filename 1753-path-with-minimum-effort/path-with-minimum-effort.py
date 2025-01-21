class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        q = []
        def push(val):
            heapq.heappush(q,val)
        def pop():
            return heapq.heappop(q)
        INF = 10**20
        dp = [ [INF]*n for _ in range(m)]
        q.append((0,0,0))
        dir = [(-1,0),(1,0),(0,-1),(0,1)]
        while q:
            val,x,y = pop()
            if dp[x][y]<val:
                continue
            dp[x][y]=val
            for dx,dy in dir:
                nx,ny = x+dx, y+dy
                if 0<=nx <m and 0<= ny <n and dp[nx][ny]>max(val,abs(heights[nx][ny]-heights[x][y])):
                    s = max(val,abs(heights[nx][ny]-heights[x][y]))
                    push((s,nx,ny))
                    dp[nx][ny]=s
        return dp[-1][-1]
