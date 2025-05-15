class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        ans = 0
        minj,maxj,blockedj = -1,-1,-1
        for idx,val in enumerate(nums):
            if val<minK or val>maxK:
                blockedj = idx
            if val==minK:
                minj = idx
            if val==maxK:
                maxj = idx
            ans += max(0,min(minj,maxj)-blockedj)
        return ans