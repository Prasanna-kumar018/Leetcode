class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        nums = [int(x%modulo == k) for x in nums]
        s = 0
        d = collections.defaultdict(int)
        d[0]=1
        res = 0
        print(nums)
        for idx,val in enumerate(nums):
            s+=val
            res += d[(s-k)%modulo]
            d[s%modulo]+=1
        return res