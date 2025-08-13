class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        best = 0
        N = len(nums)
        INF = 10**20
        last = -INF
        for i in range(N-1,-1,-1):
            if nums[i]<=last:
                last += nums[i]
            else:
                last = nums[i]

            best = max(best,last)
        return best