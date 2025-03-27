class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        mid = nums[n//2]
        count = 0
        for x in nums:
            count += abs(x-mid)
        return count