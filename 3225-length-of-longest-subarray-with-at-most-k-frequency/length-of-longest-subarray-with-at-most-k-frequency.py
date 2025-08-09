class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l,r = 0,0
        res = 0
        d = collections.defaultdict(int)
        while r<n:
            d[nums[r]]+=1

            # while max(d.values())>k: ---> TLE
            # before d[nums[r]]+=1 everything is perfect so we have to decrement of count of that alone , which is our aim
            while d[nums[r]]>k: 
                d[nums[l]]-=1
                if d[nums[l]]==0:
                    del d[nums[l]]
                l+=1 
            res = max(res,r-l+1)
            r+=1
        return res
