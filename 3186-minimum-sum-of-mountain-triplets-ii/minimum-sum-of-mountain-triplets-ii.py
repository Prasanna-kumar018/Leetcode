class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        mini1 = nums[0]
        mini2 = nums[-1]
        nums = nums[1:-1]
        n = len(nums)
        INF = 10**20
        MINI = [0]*n
        for idx in reversed(range(n)):
            MINI[idx]=mini2
            val = nums[idx]
            mini2 = min(mini2,val)
        for idx,val in enumerate(nums):
            if  mini1 < nums[idx] > MINI[idx]:
                nums[idx]+=mini1+MINI[idx]
            else:
                nums[idx]= INF
            mini1 = min(mini1,val)
        x = min(nums)
        return x if x!=INF else -1