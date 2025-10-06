class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l,r = 0,10**10
        ans = -1
        n = len(nums)
        def isSafe(val):
            i = c = 0
            while i<n:
                x = nums[i]
                if x<=val:
                    c+=1
                    i+=1
                i+=1
            return c>=k

        while l<=r:
            mid = (l+r)//2
            if isSafe(mid):
                r = mid-1
                ans = mid
            else:
                l = mid+1
        return ans