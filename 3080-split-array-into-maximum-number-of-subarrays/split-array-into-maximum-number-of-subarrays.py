class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        i = count = 0
        while i<n:
            start = nums[i]
            while start>0 and i+1<n:
                start &= nums[i+1]
                i+=1
            if i==n-1 and count>0 and start>0:
                ...
            else:
                count+=1
            i+=1
        return count