class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        N = len(nums)
        @cache
        def recur(idx,prev):
            if idx==N:
                return 0
            res = 0
            res = max(res,recur(idx+1,prev))
            val = recur(idx+1,nums[idx]%2)+nums[idx]
            if prev == nums[idx]%2:
                res = max(res,val)
            else:
                res = max(res,val-x)
            return res
        return recur(1,nums[0]%2)+nums[0]