class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        INF = 10**20
        res = INF
        # till idx-1 the nums[i]+k is applied
        for idx in range(n+1):
            left = -INF
            MAXI = -INF
            if idx-1>=0:
                left = nums[idx-1]+k
                MAXI = left
            if idx<n:
                MAXI = max(nums[-1]-k,MAXI)

            MINI = INF
            right = INF
            if idx-1>=0:
                right = nums[0]+k
                MINI = right
            if idx<n:
                MINI = min(nums[idx]-k,MINI)
            res = min(res,MAXI-MINI)
        return res
