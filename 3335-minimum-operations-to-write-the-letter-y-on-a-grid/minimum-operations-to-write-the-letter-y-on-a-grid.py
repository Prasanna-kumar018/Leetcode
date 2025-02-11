class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        y, d  = collections.defaultdict(int),collections.defaultdict(int)
        n = len(grid[0])
        mid = n //2  
        for i in range(n):
            for j in range(n):
                if (i==j and i<mid) or (j==n-1-i and i<mid) or (j==mid and i>=mid):
                    y[grid[i][j]]+=1
                else:
                    d[grid[i][j]]+=1
        y_len= sum(y.values())
        rem =  sum(d.values())
        zcy ,zcd = y_len - y[0] , rem- d[0]
        ocy ,ocd = y_len - y[1] , rem- d[1]
        tcy ,tcd = y_len - y[2] , rem- d[2]
        # print(zcy ,zcd,ocy ,ocd,tcy ,tcd)
        return min(zcy+ocd,zcy+tcd,ocy+tcd,ocy+zcd,tcy+ocd,tcy+zcd)
                    

        