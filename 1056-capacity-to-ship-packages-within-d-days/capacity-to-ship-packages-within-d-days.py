class Solution:
    def shipWithinDays(self, w: List[int], days: int) -> int:
        n = len(w)
        def isSafe(val):
            c = ans = 0
            for x in w:
                ans += x
                if ans>val:
                    ans = x
                    c += 1
            if ans>0:
                c+=1
            return c<=days
        l,r  = max(w),10**9
        ans  = -1
        while l<=r:
            mid = (l+r)//2
            if isSafe(mid):
                r = mid-1
                ans= mid
            else:
                l = mid+1
        return ans