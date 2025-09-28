class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        N = len(nums)
        INF = 10**20
        res = INF
        dp = nums[:]
        for k in range(N+1):
            cost = k*x
            for i in range(N):
                des = (i-k)%N
                dp[des]=min(dp[des],nums[i])
            res = min(res,sum(dp)+cost)
        return res