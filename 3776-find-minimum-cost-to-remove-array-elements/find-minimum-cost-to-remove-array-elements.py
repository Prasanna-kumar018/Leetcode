class Solution:
    def minCost(self, nums: List[int]) -> int:
        n = len(nums)
        INF=10**20
        MAXI = max(nums)+1
        # @cache
        # def recur(idx,past):
        #     if idx==n:
        #         return past
        #     if idx+1>=n:
        #         return max(past,nums[idx])
        #     a,b,c = past,nums[idx],nums[idx+1]
        #     best = INF
        #     best = min(best,recur(idx+2,a)+max(b,c))
        #     best = min(best,recur(idx+2,b)+max(a,c))
        #     best = min(best,recur(idx+2,c)+max(a,b))
        #     return best

        s = list(set(nums))
        dp = [collections.Counter() for _ in range(n+1)]
        for idx,val in enumerate(s):
            dp[n][val]=val
        for idx,val in enumerate(s):
            dp[n-1][val]=max(val,nums[n-1])
        start = n-1 if n%2==0 else n-2  
        for idx in range(start,0,-2):
            if idx==n-1:
                continue
            for past in s:
                a,b,c = past,nums[idx],nums[idx+1]
                best = INF
                best = min(best,dp[idx+2][a]+max(b,c))
                best = min(best,dp[idx+2][b]+max(a,c))
                best = min(best,dp[idx+2][c]+max(a,b))
                dp[idx][past]=best
        return dp[1][nums[0]]