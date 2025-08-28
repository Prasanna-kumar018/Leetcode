class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        @cache
        def recur(prev,mask):
            if mask==0:
                return 1
            res = 0
            for idx,val in enumerate(nums):
                if ((mask & (1<<idx))>0) and (nums[prev]%val ==0 or val%nums[prev]==0):
                    res += recur(idx,mask^(1<<idx))
            return res % MOD
        ans = 0
        for i in range(n):
            ans += recur(i,((1<<n)-1)^(1<<i))
        return ans % MOD