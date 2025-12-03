class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        s = ans = 0
        for x,y in zip(nums1,nums2):
            if (k!=0 and (x-y)%k !=0) or (k==0 and x!=y):
                return -1
            s += (x-y)
            if x-y > 0:
                ans += (x-y)//k
        return ans if s==0 else -1 