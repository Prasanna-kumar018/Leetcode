class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        INF = 10**20
        maxi = collections.defaultdict(lambda : -INF)
        mini = collections.defaultdict(lambda : INF)
        res = -10**20 # nums[i]-k  nums[i]+k
        s = 0
        for i,x in enumerate(nums):
            s+=x
            if maxi[x-k]!=-INF:
                res = max(res,s-maxi[x-k])
            if mini[x-k]!=INF:
                res = max(res,s-mini[x-k])
            if maxi[x+k]!=-INF:
                res = max(res,s-maxi[x+k])
            if mini[x+k]!=INF:
                res = max(res,s-mini[x+k])
            maxi[x]=max(maxi[x],s-x)
            mini[x]=min(mini[x],s-x)
        return res if res!=-10**20 else 0