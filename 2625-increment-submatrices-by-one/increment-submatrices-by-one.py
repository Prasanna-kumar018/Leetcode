class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        res = [[0]*n for _ in range(n)]
        """
            1 1 
            1 1 

            1 0 -1
            0 0
           -1    1
        """
        for sx,sy,ex,ey in queries:
            res[sx][sy]+=1
            if ey+1<n:
                res[sx][ey+1]-=1
            if ex+1<n:
                res[ex+1][sy]-=1
            if ex+1<n and ey+1<n:
                res[ex+1][ey+1]+=1
        for i in range(n):
            for j in range(1,n):
                res[i][j]+=res[i][j-1]
            
        for i in range(1,n):
            for j in range(n):
                res[i][j]+=res[i-1][j]
        return res