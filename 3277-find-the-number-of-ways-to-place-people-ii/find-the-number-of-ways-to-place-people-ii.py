class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        xx = set()
        yy = set()
        for x,y in points:
            xx.add(x)
            yy.add(y)
        xx = sorted(list(xx))
        yy = sorted(list(yy))
        R  = len(xx)
        C  = len(yy)
        vix = {}
        ivx = {}
        for i in range(R):
            vix[xx[i]]= i
            ivx[i]=xx[i]
        viy = {}
        ivy = {}
        for i in range(C):
            viy[yy[i]]= i
            ivy[i]=yy[i]
        dp = [[0]*C for _ in range(R)]
        for x,y in points:
            dp[vix[x]][viy[y]]+=1

        def go(arr,r,c):

            for i in range(r):
                for j in range(1,c):
                    arr[i][j]+=arr[i][j-1]
            for j in range(c):
                for i in range(1,r):
                    arr[i][j]+=arr[i-1][j]
            
        go(dp,R,C)
        def get(sx,sy,ex,ey):
            return dp[ex][ey]-(dp[sx-1][ey] if sx-1>=0 else 0)-(dp[ex][sy-1] if sy-1>=0 else 0) + (dp[sx-1][sy-1] if sx-1>=0 and sy-1>=0 else 0)
        count = 0
        for x in points:
            for y in points:
                if x==y:
                    continue
                if y[0]<=x[0] and y[1]>=x[1]:
                    minx,maxx = min(x[0],y[0]),max(x[0],y[0])
                    miny,maxy = min(x[1],y[1]),max(x[1],y[1])
                    if get(vix[minx],viy[miny],vix[maxx],viy[maxy])==2:
                        count+=1
        return count
                
                