class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        return [list(x) for x in permutations(nums)]