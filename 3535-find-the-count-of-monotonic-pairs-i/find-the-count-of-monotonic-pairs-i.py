class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        mod = 10**9+7
        n = len(nums)
        @cache
        def recur(idx,prev):
            nonlocal n
            if idx==n:
                return 1
            total = 0
            for i in range(nums[idx]+1):
                if  prev <= i and (nums[idx-1]-prev)>=(nums[idx]-i):
                    total+=recur(idx+1,i)
            return total%mod
        total = 0
        for i in range(nums[0]+1):
            total+=recur(1,i)
        return total%mod