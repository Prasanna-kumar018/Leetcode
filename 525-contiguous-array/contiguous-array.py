class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        s = 0
        d= {0:-1}
        ans = 0
        for idx,val in enumerate(nums):
            s+=(1 if val==1 else -1)
            if s in d:
                ans = max(ans,idx-d[s])
            if s not in d:
                d[s]=idx    
        return ans
        
        