class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l,r = 0,0
        ans = 1
        res = 0
        n = len(nums)
        while r<n:
            ans *= nums[r]
            while l<=r and ans>=k:
                ans //= nums[l]
                l+=1
            res += (r-l+1)
            r+=1
        return res