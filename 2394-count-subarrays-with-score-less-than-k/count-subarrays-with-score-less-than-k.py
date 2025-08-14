class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l,r = 0,0
        s  = res = 0
        while r<n:
            s += nums[r]
            while l<=r and (s*(r-l+1))>=k:
                s -= nums[l]
                l+=1
            res += (r-l+1)
            r+=1
        return res