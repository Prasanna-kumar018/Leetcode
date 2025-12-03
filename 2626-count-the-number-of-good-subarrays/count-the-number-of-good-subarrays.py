class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        d = collections.Counter()
        n = len(nums)
        ans = l = s = 0
        for r in range(n):
            v = nums[r]
            s -= ((d[v]-1)*d[v]//2)
            d[v]+=1
            s += ((d[v]-1)*d[v]//2)
            while s>=k and l<r:
                ans += n-r
                v = nums[l]
                s -= ((d[v]-1)*d[v]//2)
                d[v]-=1
                s += ((d[v]-1)*d[v]//2)
                l+=1
        return ans