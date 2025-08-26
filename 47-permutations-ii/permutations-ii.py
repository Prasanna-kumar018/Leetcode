class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        res = set()
        ans =  []
        for a in permutations(nums):
            if a not in res:
                res.add(a)
                ans.append(list(a))
        return ans