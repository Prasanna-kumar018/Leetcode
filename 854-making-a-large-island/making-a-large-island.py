class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        parent = {}
        size = {}
        def find(x):
            if x not in parent:
                parent[x]=x
                size[x]=1
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def ufind(a,b):
            x  = find(a)
            y  = find(b)
            if x==y:
                return 
            parent[x]=y
            size[y]+= size[x]

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    if i+1<m and grid[i+1][j]==1:
                        ufind((i,j),(i+1,j))
                    if j+1<n and grid[i][j+1]==1:
                        ufind((i,j),(i,j+1))
        
        ans = max(size.values()) if size else 1 # atmost we can change one
        dir = [(-1,0),(1,0),(0,1),(0,-1)]
        for i in range(m):
            for j in range(n):
                count = 1               
                if grid[i][j]==0:
                    islands = set()
                    for dx,dy in dir:
                        nx = i+dx
                        ny = j+dy
                        if 0<= nx <m and 0<= ny<n and grid[nx][ny]==1:
                            islands.add(find((nx,ny)))
                    for x in islands:
                        count += size[x]
                ans = max(ans,count)

        return ans 