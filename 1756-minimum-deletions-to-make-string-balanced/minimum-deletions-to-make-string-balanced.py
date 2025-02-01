class Solution:
    def minimumDeletions(self, s: str) -> int:
        INF = 10**20
        n = len(s)
        # @cache
        # def recur(idx,isb):
        #     if idx==n:
        #         return 0
        #     res = INF
        #     res = min(res,recur(idx+1,isb)+1)
        #     if s[idx]=='a':
        #         if not isb:
        #             res = min(res,recur(idx+1,isb))
        #     else:
        #         res = min(res,recur(idx+1,True))
        #     return res
        # return recur(0,False)

        # dp = [[0]*2 for _ in range(n+1)]
        # for idx in range(n-1,-1,-1):
        #     for isb in range(2):
        #         res = INF
        #         res = min(res,dp[idx+1][isb]+1)
        #         if s[idx]=='a':
        #             if not isb:
        #                 res = min(res,dp[idx+1][isb])
        #         else:
        #             res = min(res,dp[idx+1][1])
        #         dp[idx][isb]=res
        # return dp[0][0]


        dp = [0]*2
        for idx in range(n-1,-1,-1):
            result = list(dp)
            for isb in range(2):
                res = INF
                res = min(res,dp[isb]+1)
                if s[idx]=='a':
                    if not isb:
                        res = min(res,dp[isb])
                else:
                    res = min(res,dp[1])
                result[isb]=res
            dp = list(result)
        return dp[0]
