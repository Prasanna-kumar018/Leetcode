class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        nums.extend(nums)
        n = len(nums)
        prev = {}
        d= collections.defaultdict(int)
        for idx,val in enumerate(nums):
            if val in prev:
                d[val]=max(d[val],(idx-prev[val])//2)
            prev[val]=idx
        return min(d.values())