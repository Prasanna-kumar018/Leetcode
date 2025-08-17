class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9+7
        for l,r,k,v in queries:
            for idx in range(l,r+1,k):
                nums[idx] *= v
                nums[idx] %= MOD
        def xor(arr):
            s = 0
            for x in arr:
                s^=x
            return s
        return xor(nums)