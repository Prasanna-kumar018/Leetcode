class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        d = collections.defaultdict(int)
        for x in nums:
            d[x%value]+=1
        i = 0
        n = len(nums)
        while i<n+1:
            idx = i%value
            if d[idx]>0:
                d[idx]-=1
            else:
                return i
            i+=1
        return -1