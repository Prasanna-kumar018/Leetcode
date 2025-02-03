class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        maxi = -1
        n = len(nums)
        if n==1 and k%2==1:
            return -1
        if k-1>=1:
            maxi = max(maxi,max(nums[:k-1]))
        if k<n:
            maxi = max(maxi,nums[k])
        return maxi