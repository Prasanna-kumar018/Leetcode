class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        for idx,val in enumerate(nums):
            if s[idx]=='R':
                nums[idx]+=d
            else:
                nums[idx]-=d
        nums.sort() # sorting makes the n2 --> n
        total = 0
        s = 0
        MOD = 10**9 + 7
        for idx,x in enumerate(nums):
            total += (idx*x)-s
            s += x
        return total % MOD
