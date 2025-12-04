class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        ans = 0
        def isSafe(val):
            prev = price[0]
            cnt = 1
            for x in price[1:]:
                if x-prev>=val:
                    cnt+=1
                    prev = x
            return cnt>=k
        l,r = 1,10**10
        while l<=r:
            mid = (l+r)//2
            if isSafe(mid):
                ans = mid
                l = mid+1
            else:
                r = mid-1
        return ans