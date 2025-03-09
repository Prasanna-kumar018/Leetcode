class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        dp= [[0]*(n+1) for _ in range(m+1)]
        for x,y,z in prices:
            dp[x][y]=z

        for i in range(1,m+1):
            for j in range(1,n+1):
                for k in range(1,i):
                    dp[i][j]=max(dp[i][j],dp[i-k][j]+dp[k][j])
                for k in range(1,j):
                    dp[i][j]=max(dp[i][j],dp[i][j-k]+dp[i][k])
        return dp[m][n]