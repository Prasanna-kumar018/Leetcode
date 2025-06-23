class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:

        INF = 10**20
        n = len(nums)
        premaxi = [nums[0]]*n
        premini = [nums[0]]*n
        for i in range(1,n):
            premaxi[i]=max(premaxi[i-1],nums[i])
            premini[i]=min(premini[i-1],nums[i])
        res = -INF
        for i in range(n-1,-1,-1):
            if i-m+1>=0:
                res = max(res,premaxi[i-m+1]*nums[i])
                res = max(res,premini[i-m+1]*nums[i])
        return res

