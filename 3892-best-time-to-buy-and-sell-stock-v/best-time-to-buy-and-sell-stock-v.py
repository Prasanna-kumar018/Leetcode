class Solution:
    def maximumProfit(self, prices: List[int], kk: int) -> int:
        n = len(prices)
        """
        0 - can't buy ( sell ) 1 - can buy (buy) 2 - can both buy and sell
        """
        INF = 10**20
        # @cache
        # def recur(idx,canbuy,k):
        #     if idx==n:
        #         if canbuy==2:
        #             return 0
        #         return -INF
        #     res = recur(idx+1,canbuy,k)
        #     if canbuy == 0 and k>0:
        #         res= max(res,prices[idx]+recur(idx+1,2,k-1))
        #     elif canbuy == 1 and k>0:
        #         res = max(res,-prices[idx]+recur(idx+1,2,k-1))
        #     else:
        #         res = max(res,-prices[idx]+recur(idx+1,0,k))
        #         res = max(res,prices[idx]+recur(idx+1,1,k))
        #     return res
        # return recur(0,2,kk)

        dp = [[[-INF]*(kk+1) for _ in range(3)]  for _ in range(n+1)]
        for k in range(kk+1):
                dp[n][2][k]=0
        
        for idx in range(n-1,-1,-1):
            for canbuy in range(3):
                for k in range(kk+1):
                    res = dp[idx+1][canbuy][k]
                    if canbuy == 0 and k>0:
                        res= max(res ,prices[idx]+dp[idx+1][2][k-1])
                    elif canbuy == 1 and k>0:
                        res = max(res,-prices[idx]+dp[idx+1][2][k-1])
                    elif canbuy == 2:
                        res = max(res,-prices[idx]+dp[idx+1][0][k])
                        res = max(res,prices[idx]+dp[idx+1][1][k])
                    dp[idx][canbuy][k]=res
        return dp[0][2][k]

