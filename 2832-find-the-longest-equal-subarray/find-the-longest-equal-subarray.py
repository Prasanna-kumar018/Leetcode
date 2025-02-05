class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        l,r = 0,0
        count = Counter()
        maxf = 0
        n = len(nums)
        while r<n:
            count[nums[r]]+=1
            maxf = max(count[nums[r]],maxf)
            while r-l+1-maxf>k:
                count[nums[l]]-=1
                l+=1
            r+=1
        return maxf
