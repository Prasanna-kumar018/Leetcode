import bisect
class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0]*(n+1)
        """
        prefix of i contains sum from 0 to i-1
        1 2 3 | 4 5 |
            i     j
            1     2
        """
        for i in range(1,n+1):
            prefix[i]=prefix[i-1]+nums[i-1]
        prev = collections.defaultdict(lambda : -1)
        i = 0
        dp = [0]*(n+1)
        for j in range(1,n+1):
            # prefix[j]-prefix[i] <= prefix[k]-prefix[j]
            # 2*prefix[j]-prefix[i] <= prefix[k]
            i = max(i,prev[j])
            dp[j]=dp[i]+1
            idx = bisect.bisect_left(prefix,2*prefix[j]-prefix[i])
            prev[idx]=j
        return dp[n]