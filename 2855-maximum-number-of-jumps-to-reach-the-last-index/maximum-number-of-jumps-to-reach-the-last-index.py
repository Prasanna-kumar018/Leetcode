class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        INF = 10**20
        @cache
        def recur(prev):
            if prev==n-1:
                return 0
            res = -INF
            for idx in range(prev+1,n):
                if -target <= nums[idx]-nums[prev] <=target:
                    res = max(res,recur(idx)+1)
            return res
        ans = recur(0)
        return ans if ans>=0 else -1