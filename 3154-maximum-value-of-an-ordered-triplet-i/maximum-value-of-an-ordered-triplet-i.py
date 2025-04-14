class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        INF = 10**20
        n = len(nums)
        maxi = -INF
        arr = [-1]*n
        for i in range(n-1,-1,-1):
            arr[i]=maxi
            maxi = max(maxi,nums[i])
        maxi = nums[0]
        res = 0
        for i in range(1,n-1):
            res = max(res,((maxi-nums[i])*arr[i]))
            maxi = max(maxi,nums[i])
        return res