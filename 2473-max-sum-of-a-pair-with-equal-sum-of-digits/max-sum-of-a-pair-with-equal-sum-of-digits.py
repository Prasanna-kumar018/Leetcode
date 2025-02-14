class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = collections.defaultdict(int)
        res = -1
        for a in nums:
            s = sum(int(x) for x in str(a))
            if s in d:
                res = max(res,a+d[s])
            d[s]=max(d[s],a)
        return res