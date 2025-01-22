class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums = collections.Counter(nums)
        res = 0
        vis = set()
        for x in sorted(nums.keys()):
            if x-k in vis:
                res+=1
            elif nums[x-k]>1:
                res+=1 
            vis.add(x)
        return res