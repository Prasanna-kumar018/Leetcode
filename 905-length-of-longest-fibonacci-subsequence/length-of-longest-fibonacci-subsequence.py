class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = collections.defaultdict(lambda :2)
        for i in range(n):
            vis = set()
            for j in range(i):
                if arr[i]-arr[j] in vis and (arr[i]-arr[j])<arr[j]:
                    dp[(arr[j],arr[i])]=max(dp[((arr[i]-arr[j]),arr[j])]+1,dp[(arr[j],arr[i])])
                vis.add(arr[j])
        return max(dp.values()) if dp else 0