class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        mod = 10**9+7
        n = len(nums)
        # @cache
        # def recur(idx,prev):
        #     nonlocal n
        #     if idx==n:
        #         return 1
        #     total = 0
        #     for i in range(nums[idx]+1):
        #         if  prev <= i and (nums[idx-1]-prev)>=(nums[idx]-i):
        #             total+=recur(idx+1,i)
        #     return total%mod
        # total = 0
        # for i in range(nums[0]+1):
        #     total+=recur(1,i)
        # return total%mod
        M = max(nums)
        dp = [0]*(M+1)
        for i in range(M+1):
            dp[i]=1
        ans = sum(dp)
        for idx in range(n-1,-1,-1):
            """
            prev<= i and i>=(nums[idx]-nums[idx-1] + prev) 
            """
            # prefix = 
            res = list(dp)
            for prev in range(M+1):
                total = 0
                for i in range(nums[idx]+1):
                    if  prev <= i and (nums[idx-1]-prev)>=(nums[idx]-i):
                        total+=dp[i]
                res[prev]=total
            dp = res
            if idx==1:
                print(res)
                ans = sum(res)
                break
        return ans%mod