class Solution:
    def minOperations(self, s1: str, s2: str, val: int) -> int:
        INF = 10**20
        n=len(s1)
        @cache
        def recur(idx,k,b):
            if idx==n:
                if k==0 and b:
                    return 0
                return INF
            best = INF
            x = int(s1[idx]) if b else  int(not bool(int(s1[idx])))
            y = int(s2[idx])
            if x!=y:
                if k>0:
                    best = min(best,recur(idx+1,k-1,True))
                best = min(best,recur(idx+1,k+1,True)+val)
                best = min(best,recur(idx+1,k,False)+1)
            else:
                best = min(best,recur(idx+1,k,True))
            return best
        x = recur(0,0,True)
        return x if x!=INF else -1