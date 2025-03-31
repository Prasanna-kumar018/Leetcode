class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = sum(nums)
        count = Counter(nums)
        """
        total = 2* sum() + outlier
        """
        res = -10**20
        for x in count.keys(): # 1000
            out = total - 2*x
            count[x]-=1
            if count[out]>=1:
                res = max(out,res)
            count[x]+=1
        return res