class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:        
        q = collections.deque()
        sx,sy = -1,-1
        m = len(grid)
        n = len(grid[0])

        key = 0
        for i in range(m):
            for j in range(n):
                # print(grid[i][j])
                if grid[i][j]=='@':
                    sx,sy = i,j
                c = grid[i][j] 
                if 97 <= ord(c) <= 122:
                    key+=1
        q.append((sx,sy,0)) # 0 represent currenct availability of key
        level = 0
        dir= [(-1,0),(1,0),(0,-1),(0,1)]
        vis = set()
        # print(q)
        while q:
            size = len(q)
            while size>0:
                x,y ,val = q.popleft()
                # print(x,y,bin(val))
                if (val,x,y) in vis:
                    size-=1
                    continue
                if bin(val)[2:].count('1')==key:
                    return level
                # print('k;',level)
                vis.add((val,x,y))
                for dx,dy in dir:
                    nx,ny = x+dx,y+dy
                    if 0<= nx <m and 0<= ny<n and grid[nx][ny]!='#':
                        c = grid[nx][ny]
                        if (val,nx,ny) not in vis:
                            if grid[nx][ny]=='.' or grid[nx][ny]=='@':
                                q.append((nx,ny,val))
                            if 65 <= ord(c) <=90:
                                need = ord(c)-ord('A')
                                if (1<< need) & val >0:
                                    q.append((nx,ny,val))
                        if 97 <= ord(c) <=122:
                            need = ord(c) - ord('a')
                            if (val|(1<<need),nx,ny) not in vis:
                                q.append((nx,ny,val|(1<<need)))
                            # elif (val ,nx,ny) not in vis:
                                # q.append((nx,ny,val))
                    # print((x,y),q)
                size-=1
            level+=1
            # print('afdsaf',q,vis)
        return -1