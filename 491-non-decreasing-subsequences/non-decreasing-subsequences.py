class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def recur(prev,l):
            nonlocal res
            vis = set()
            for idx in range(prev+1,n):
                # Strategy to remove duplicates
                if nums[idx] in vis:
                    continue
                if nums[idx] >= nums[prev]:
                    l.append(nums[idx])
                    recur(idx,l)
                    l.pop()
                vis.add(nums[idx])
            if len(l)>=2:
                res.append(list(l))
        vv = set()
        for i in range(n):
            # Strategy to remove duplicates
            if nums[i] in vv:
                continue
            recur(i,[nums[i]])
            vv.add(nums[i])
        return res