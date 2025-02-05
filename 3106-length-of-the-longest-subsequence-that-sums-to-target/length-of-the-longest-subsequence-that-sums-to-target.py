class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        INF = -10**20
        dp = [[INF]*(target+1) for _ in range(n)]
        for i in range(n):
            dp[i][0]=0
            for j in range(target+1):
                if i==0:
                    if j-nums[i]==0:
                        dp[i][j]=1
                elif j>=nums[i]:
                    dp[i][j]=max(1+dp[i-1][j-nums[i]],dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1] if dp[-1][-1]>=0 else -1

