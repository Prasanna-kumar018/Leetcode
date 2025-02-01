class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,0
        have = 0
        ans = 0
        while l<=r and r<n:
            while r<n and (nums[r]==1 or (nums[r]==0 and have<1)):
                if nums[r]==0:
                    have+=1
                r+=1
            ans = max(ans,r-l-max(have,1))
            if nums[l]==0:
                have-=1
            l+=1
        return ans