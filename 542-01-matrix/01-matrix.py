class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        INF = 10**10
        m = len(mat)
        n = len(mat[0])
        q = collections.deque()
        res = [[INF]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append((i,j))
        dir = [(-1,0),(1,0),(0,1),(0,-1)]
        level = 0
        while q:
            size = len(q)
            while size>0:
                x,y = q.popleft()
                if res[x][y]<level:
                    size-=1
                    continue
                res[x][y]=level
                for dx,dy in dir:
                    if 0 <= x+dx <m and 0<= y+dy <n and res[x+dx][y+dy]>(level+1):
                        q.append((x+dx,y+dy))
                size-=1
            level+=1
        return res