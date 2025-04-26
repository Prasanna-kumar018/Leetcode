class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        INF =-10**20
        @cache
        def recur(idx,inc):
            if idx==n-1:
                return 0
            r = 0
            if inc and arr[idx+1]>arr[idx]:
                r = max(r,recur(idx+1,not inc)+1)
            elif not inc and arr[idx+1]<arr[idx]:
                r = max(r,recur(idx+1,not inc)+1)
            return r
        res = 0
        for i in range(n):
            res = max(res,recur(i,True)+1,recur(i,False)+1)
        return res