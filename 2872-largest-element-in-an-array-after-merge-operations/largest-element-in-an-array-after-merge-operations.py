class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        best = 0
        N = len(nums)
        INF = 10**20
        last = -INF
        """
        this works because
        if we get some x that is greater than the current sum i.e. last
        _ _ _ _ _ _ x last _ _ _ 
        if x>last:
            then x will grow again which will never be <= last
        """
        for i in range(N-1,-1,-1):
            if nums[i]<=last:
                last += nums[i]
            else:
                last = nums[i]
            best = max(best,last)
        return best