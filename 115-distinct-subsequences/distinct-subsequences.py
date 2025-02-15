class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        @cache
        def recur(idx,prev):
            if prev==m:
                return 1
            if idx==n:
                return 0
            res = 0        
            if t[prev]==s[idx]:
                res+=recur(idx+1,prev+1)
            res+=recur(idx+1,prev)
            return res
        return recur(0,0)
