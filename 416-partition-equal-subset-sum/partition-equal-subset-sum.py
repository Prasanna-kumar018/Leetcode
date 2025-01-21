class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2==1:
            return False
        need = s//2
        n = len(nums)
        @cache
        def recur(idx,val):
            if val<0 or idx==n:
                return False
            if val==0:
                return True
            return recur(idx+1,val) or recur(idx+1,val-nums[idx])
        return  recur(0,need)