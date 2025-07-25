class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        count = Counter(nums)
        n = len(nums)
        @cache
        def recur(idx):
            if idx==n:
                return 0
            res = 0
            nxt = bisect.bisect_left(nums,nums[idx]+2)
            res = max(res,recur(idx+1))
            res = max(res,recur(nxt)+nums[idx]*count[nums[idx]])
            return res
        return recur(0)