class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        m = len(grid)
        n = len(grid[0])
        p = len(pattern)
        val = 0
        d = 256
        MOD = 10**9+7
        for x in pattern:
            val = (val*d)+ord(x)
            val %= MOD
        highest = pow(d,p-1,MOD)
        def find(grid,m,n):
            nonlocal val,d,p,highest
            count = [0]*(m*n)
            arr = []
            for x in grid:
                arr.extend(x)
            # print(arr)
            v = 0
            total = m*n
            l,r = 0,-1
            while r<p-1 and r<total-1:
                r+=1
                v = (v*d)+ord(arr[r])
                v %= MOD
            while r<total:
                r+=1            
                if v==val:
                    # x = (r+1) // m
                    # y = (r+1) % m
                    if r<total:
                        count[r]-=1
                    count[l]+=1
                # print(l,r,v,val)
                if r<total:
                    v = v-(ord(arr[l])*highest)
                    v %= MOD 
                    v = v* d + ord(arr[r])
                    v %= MOD
                else:
                    break
                l+=1
            return count
        count = find(grid,m,n)
        s = 0
        print(count)
        g = [[0]*n for _ in range(m)]
        for idx,x in enumerate(count):
            s+=x
            a,b = idx//n , idx%n
            g[a][b]=s
        ar = find(map(list,zip(*grid)),m,n)
        s = 0
        c = 0
        for idx,x in enumerate(ar):
            s+=x
            a,b = idx%m, idx //m
            if g[a][b]>=1 and s>=1:
                c+=1
        return c