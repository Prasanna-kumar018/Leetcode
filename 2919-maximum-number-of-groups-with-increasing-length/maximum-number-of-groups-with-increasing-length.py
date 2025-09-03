class Solution:
    def maxIncreasingGroups(self, u: List[int]) -> int:
        N = len(u)
        u = [ min(x,N) for x in u]
        u.sort(reverse = True)
        def isSafe(val):
            need = 0
            h = val
            for val in u:
                need = max(h+need-val,0)
                if h>0:
                    h-=1
            return need==0
        l,r = 0,N
        ans = 0
        while l<=r:
            mid = (l+r)//2
            if isSafe(mid):
                l = mid+1
                ans = mid
            else:
                r = mid-1
        return ans