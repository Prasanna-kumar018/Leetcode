class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        n = len(ranks)
        def isSafe(val):
            count = 0
            for idx,v in enumerate(ranks):
                vv = int((val/v)**(0.5))
                count += vv
            return count>=cars
        INF = 10**20
        l,r = 0,INF
        ans = INF
        while l<=r:
            mid = (l+r)//2
            if isSafe(mid):
                ans = min(ans,mid)
                r = mid-1
            else:
                l = mid+1
        return ans 