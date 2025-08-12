class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        INF = 10**20
        @cache
        def recur(left,right):
            if left>=right:
                return 0
            res = INF
            if s[left]==s[right]:
                res = min(res,recur(left+1,right-1))
            res = min(res,recur(left+1,right)+1)
            res = min(res,recur(left,right-1)+1)
            return res
        x = recur(0,n-1)
        return x