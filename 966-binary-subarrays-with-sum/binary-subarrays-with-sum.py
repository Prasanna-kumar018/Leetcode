class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums) 
        d = {0:1}
        s = 0
        ans = 0
        for x in nums:
            s+=x
            if s-goal in d:
                ans+=d[s-goal]
            if s in d:
                d[s]+=1
            else:
                d[s]=1
        return ans