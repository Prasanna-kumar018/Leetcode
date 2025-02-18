import copy
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        INF = -10**10
        n = len(nums)
        dp = [{} for _ in range(n)]
        d = {}
        for idx in range(n-1,-1,-1):
            dp[idx]= copy.deepcopy(d) # since it is a list deep copy is needed
            if nums[idx] in d:
                d[nums[idx]].append(idx)
            else:
                d[nums[idx]]=[idx]
        # print(dp)
        @cache
        def find(prev,diff,isPossible):
            # print(prev,diff,isPossible)
            nonlocal n,nums
            if prev==n-1:
                if isPossible:
                    return 1
                return 0
            res = 0
            if isPossible:
                res+=1
            if nums[prev]-diff in dp[prev]:
                for x in dp[prev][nums[prev]-diff]:
                    res += find(x,diff,True)
            return res
        total = 0
        for i in range(n):
            for j in range(i+1,n):
                total += find(j,nums[i]-nums[j],False)
        # find.cache_clear()
        return total