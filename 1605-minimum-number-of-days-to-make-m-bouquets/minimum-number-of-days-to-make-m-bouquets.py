class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        INF=-10**10
        n = len(bloomDay)
        def isSafe(mid):
            t=0
            c=0
            for x in bloomDay:
                if x <=mid:
                    t+=1
                else:
                    t=0
                if t==k:
                    t=0
                    c+=1
            return True if c>=m else False
        l = min(bloomDay)
        r = max(bloomDay)
        ans = -1 
        while l<=r:
            mid = (l+r)//2
            if isSafe(mid):
                r= mid-1
                ans = mid
            else:
                l=mid+1
        return ans
        


        