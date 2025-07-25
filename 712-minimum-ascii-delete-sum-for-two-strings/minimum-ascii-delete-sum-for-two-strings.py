class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        INF = 10**20
        m = len(s1)
        n = len(s2)
        @cache
        def recur(idx1,idx2):
            if idx1 ==m and idx2==n:
                return 0
            res = INF
            if idx1<m and idx2<n and s1[idx1]==s2[idx2]:
                res = min(res,recur(idx1+1,idx2+1))
            if idx1<m:
                res = min(res,recur(idx1+1,idx2)+ord(s1[idx1]))
            if idx2<n:
                res = min(res,recur(idx1,idx2+1)+ord(s2[idx2]))
            return res
        return recur(0,0)