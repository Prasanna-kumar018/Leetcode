class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0,0
        n = len(nums)
        INF = 10**20
        s = 0
        res = INF
        while l<n:
            while r<n and s<target:
                s+=nums[r]
                r+=1
            if s>=target:
                res = min(res,r-l)
            s-=nums[l]
            l+=1
        return res if res!=INF else 0