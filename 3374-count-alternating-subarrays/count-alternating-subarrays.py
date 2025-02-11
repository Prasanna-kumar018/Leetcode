class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        res = 0
        while i<n:
            t = i
            while t+1<n and nums[t+1]==int(not nums[t]):
                t+=1
            res+=(t-i+1)*(t-i+2)//2
            i = t+1
        return res