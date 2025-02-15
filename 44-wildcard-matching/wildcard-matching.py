class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        @cache
        def recur(idx,index):
            if idx==-1 and index==-1:
                return True
            best = False
            if (index>=0 and p[index]=='?') or (idx>=0 and index>=0 and s[idx]==p[index]):
                best = best or recur(idx-1,index-1)
            if index>=0 and p[index]=='*':
                if idx>=0:
                    best = best or recur(idx-1,index)
                best = best or recur(idx,index-1)
            return best
        return recur(m-1,n-1)