class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        """
        lexicographically smallest subsequence of length k
        """
        s = []
        n = len(nums)
        for idx, val in enumerate(nums):
            while s and s[-1]>val and len(s)+(n-idx)>k:
                s.pop()
            s.append(val)
        while len(s)>k:
            s.pop()
        return  s