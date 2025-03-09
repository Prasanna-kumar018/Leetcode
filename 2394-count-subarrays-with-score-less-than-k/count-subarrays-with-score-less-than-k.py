class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0]*n
        prefix[0]=nums[0]
        for i in range(1,n):
            prefix[i]=prefix[i-1]+nums[i]
        def get(x,y):
            return prefix[y]-(prefix[x-1] if x-1>=0 else 0)
        
        ans  = 0
        for idx,val in enumerate(nums):
            l,r = idx,n-1
            res = -1
            while l<=r:
                mid = (l+r)//2
                if get(idx,mid)*(mid-idx+1)>=k:
                    r = mid-1
                else:
                    l =mid+1
                    res =(mid-idx) 
            ans += res+1
        return ans