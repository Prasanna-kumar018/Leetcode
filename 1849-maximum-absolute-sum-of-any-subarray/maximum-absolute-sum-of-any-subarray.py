class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxi = mini = s = 0
        res = 0
        for x in nums:
            s+=x
            res = max(res,abs(s-maxi))
            res = max(res,abs(s-mini))
            maxi =max(maxi,s)
            mini = min(mini,s)
        return res