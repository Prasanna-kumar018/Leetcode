class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        INF = 10**10
        res = {}
        # @cache
        # def recur(idx1,idx2):
        #     if idx1==m and idx2==n:
        #         return 0
        #     best = INF
        #     if idx1<m and idx2<n and str1[idx1]==str2[idx2]:
        #         best = min(best,recur(idx1+1,idx2+1)+1)
        #         res[(idx1,idx2)]=(idx1+1,idx2+1)
        #     if idx1<m:
        #         x = recur(idx1+1,idx2)+1
        #         if x<best:
        #             best = x
        #             res[(idx1,idx2)]=(idx1+1,idx2)
        #     if idx2<n:
        #         x = recur(idx1,idx2+1)+1
        #         if x<best:
        #             best = x
        #             res[(idx1,idx2)]=(idx1,idx2+1)
        #     return best
        # print(recur(0,0))
        dp = [[INF]*(n+1) for _ in range(m+1)]
        dp[m][n]=0
        for idx1 in range(m,-1,-1):
            for idx2 in range(n,-1,-1):
                if idx1==m and idx2==n:
                    continue
                best = INF
                if idx1<m and idx2<n and str1[idx1]==str2[idx2]:
                    best = min(best,dp[idx1+1][idx2+1]+1)
                    res[(idx1,idx2)]=(idx1+1,idx2+1)
                if idx1<m:
                    x = dp[idx1+1][idx2]+1
                    if x<=best:
                        best = x
                        res[(idx1,idx2)]=(idx1+1,idx2)
                if idx2<n:
                    x = dp[idx1][idx2+1]+1
                    if x<=best:
                        best = x
                        res[(idx1,idx2)]=(idx1,idx2+1)
                dp[idx1][idx2]=best
        # print(dp[0][0])
        sx,sy = 0,0
        ans = []
        while (sx,sy) in res:
            nx,ny = res[(sx,sy)]
            x,y = nx-sx , ny-sy
            if x==1:
                ans.append(str1[sx])
            elif y==1:
                ans.append(str2[sy]) 
            sx,sy = nx,ny
        return ''.join(ans)