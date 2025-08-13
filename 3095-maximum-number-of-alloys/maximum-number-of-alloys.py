class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        
        def isSafe(val,idx):
            total = 0
            for c,cc in zip(composition[idx],cost):
                total += (val*c*cc)
            for s,c,cc in zip(stock,composition[idx],cost):
                v = min(s,val*c)
                total -= (v*cc)

            return total<=budget

        INF = 10**10
        ans = 0
        for i in range(k):
            res = -1
            l,r = 1,INF
            while l<=r:
                mid = (l+r)//2
                if isSafe(mid,i):
                    l = mid+1
                    res = mid
                else:
                    r = mid-1
            ans = max(res,ans)
        return ans