class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()
        def lte(val):
            nonlocal n
            l,r = 0,n-1
            res= 0
            while l<n and l<r:
                while r>l and nums[l]+nums[r]>val:
                    r-=1
                res+=r-l
                l+=1
            return res
        return lte(upper)-lte(lower-1)