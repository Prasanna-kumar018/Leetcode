class Solution:
    def maximumLength(self, s: str) -> int:
        arr = []
        n = len(s)
        for ch,ll in groupby(s):
            arr.append((ch,len(list(ll))))
        
        def isSafe(val):
            d = collections.defaultdict(int)
            for char,count in arr:
                d[char]+= max(0,count-val+1)
            return max(d.values())>=3

        l,r = 1,n
        ans = -1
        while l<=r:
            mid = (l+r)//2
            if isSafe(mid):
                ans = mid
                l = mid+1
            else:
                r = mid-1
        return ans