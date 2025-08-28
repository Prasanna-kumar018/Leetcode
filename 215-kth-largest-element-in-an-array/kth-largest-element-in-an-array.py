class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def isSafe(val):
            count = 0
            for x in nums:
                if x >= val:
                    count+=1
            return count>=k
        l,r = min(nums),max(nums)
        ans = -1
        while l<=r:
            mid = (l+r)//2
            if isSafe(mid):
                print(mid)
                ans = mid
                l = mid+1
            else:
                r = mid-1
        return ans