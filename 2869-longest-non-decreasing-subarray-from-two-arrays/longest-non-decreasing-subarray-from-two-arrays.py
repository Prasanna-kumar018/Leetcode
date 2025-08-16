class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        @cache 
        def recur(idx,isone):
            if idx==n:
                return 0
            prev = nums1[idx-1] if isone else nums2[idx-1]
            res = 0
            if prev <= nums1[idx]:
                res = max(res,recur(idx+1,True)+1)
            if prev<= nums2[idx]:
                res = max(res,recur(idx+1,False)+1)
            return res
        ans = 1
        for i in range(1,n):
            ans = max(ans,recur(i,True)+1,recur(i,False)+1)
        return ans