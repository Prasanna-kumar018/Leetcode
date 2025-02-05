class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        @cache
        def recur(idx,kval):
            nonlocal n
            if idx==n:
                return 0
            res = recur(idx+1,2)+(0 if nums[idx]>=k else (k-nums[idx]))
            if kval>0:
                res = min(res,recur(idx+1,kval-1))
            return res
        return recur(0,2)