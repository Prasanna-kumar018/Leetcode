class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:    
        nums.sort()
        total = 0
        ans = -1
        # print(nums)
        for idx,x in enumerate(nums):
            if total>x and idx>=2:
                ans = max(ans,total+x)
            total += x
        return ans