class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        """
        you can create a connection in union find but you cannot broke or delete the connection 
        thats why we are coming or traversing from the back
        """
        m = len(grid)
        n = len(grid[0])
        g = copy.deepcopy(grid)

        for x,y in hits:
            g[x][y]=0

        parent = {}
        size = {}
        def find(x):
            if x not in parent:
                parent[x]=x
                size[x]=1
            if parent[x]!=x:
                parent[x]= find(parent[x])
            return parent[x]
        
        def ufind(a,b):
            x = find(a)
            y = find(b)

            if x==y:
                return # sizes should not be counted twice. It should be added only if it is a same parent
            parent[x]=y
            size[y]+=size[x]

        for i in range(m):
            for j in range(n):
                if g[i][j]==1:
                    if i+1<m and g[i+1][j]==1:
                        ufind((i,j),(i+1,j))
                    if j+1<n and g[i][j+1]==1:
                        ufind((i,j),(i,j+1))

        Q = len(hits)
        parent["roof"] = 'roof' # it is assigned here because roof should not take the size of 1
        size['roof']=0
        for j in range(n):
            if g[0][j]==1:
                ufind((0,j),'roof') 
        dir = [(-1,0),(1,0),(0,1),(0,-1)]
        res = []
        for i in range(Q-1,-1,-1):
            x,y = hits[i]
            if grid[x][y]==0:
                res.append(0)
                continue
            count = 0
            found = (x==0)
            for dx,dy in dir:
                nx ,ny = x+dx, y+dy
                if 0<= nx < m and 0<= ny <n and g[nx][ny]==1:
                    if(  find((x,y)) ==find((nx,ny))):
                        continue
                    if find('roof')!=find((nx,ny)): # used to check whether they are connect to the roof
                        count += size[find((nx,ny))]
                    else:
                        found = True
                    ufind((x,y),(nx,ny))
            # print(parent)
            if found: # Found = True it is connected to the roof
            # Found = False it is already an orphan
                res.append(count)
            else:
                res.append(0)
            if x==0:
                ufind('roof',(x,y))
            g[x][y]=1
        res.reverse()
        return res
        
