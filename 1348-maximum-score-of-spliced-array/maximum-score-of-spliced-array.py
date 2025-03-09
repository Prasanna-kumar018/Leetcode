class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        INF = -10**20
        @cache
        def recur(idx,takeone,k):
            if k>2:
                return INF
            if idx==n:
                return 0
            res = INF
            if takeone:
                res = max(res,nums1[idx]+recur(idx+1,True,k))
                res = max(res,nums2[idx]+recur(idx+1,False,k+1))
            else:
                res = max(res,nums2[idx]+recur(idx+1,False,k))
                res = max(res,nums1[idx]+recur(idx+1,True,k+1))
            return res
        return max(recur(0,True,0),recur(0,False,0))