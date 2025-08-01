class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # 1 2 3 4
        # 2 4 6 8 
        # 3 6 9 12   so if the val if 10 then all the row before it are less than 10 i.e(row 1,2)
        # "4 8" 12 16  # These are the value which are less than  
        def isSafe(val):
            count=0
            for i in range(1,m+1):
                value = min(val//i,n)
                count += value
            return count>=k
        l,r = 1, m*n
        ans = -1
        while l<=r:
            mid = (l+r)//2
            if isSafe(mid):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans