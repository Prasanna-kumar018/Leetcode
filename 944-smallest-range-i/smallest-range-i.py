class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        first = nums[0]+k
        last = nums[-1]-k
        return max(last-first,0)