class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i = n-2
        n //= 3
        ans = 0 
        while n>0:
            ans += nums[i]
            i-=2
            n-=1
        return ans