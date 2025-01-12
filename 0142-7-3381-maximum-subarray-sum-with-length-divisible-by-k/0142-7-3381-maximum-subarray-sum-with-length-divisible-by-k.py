class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        s = 0
        INF = 10**20
        ans = -INF
        mini = collections.defaultdict(lambda : INF)
        maxi = collections.defaultdict(lambda : -INF)
        mini[0]=0
        maxi[0]=0
        for idx,val in enumerate(nums):
            idx+=1
            s+=val
            m = maxi[(idx%k)]
            n = mini[(idx%k)]
            if m!=-INF:
                ans = max(s-m,ans)
            if n!=INF:
                ans = max(s-n,ans)
            mini[(idx%k)]=min(mini[idx%k],s)
            maxi[(idx%k)]=max(maxi[idx%k],s)
        return ans