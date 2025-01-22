class Solution:
    def minSteps(self, n_: int) -> int:
        INF = 10**20
        def recur(n,avail):
            if n==0:
                return 0
            if n<0:
                return INF
            best = INF
            # copy
            if (n_-n)> avail:
                best = min(best,recur(n,(n_-n))+1)
            # paste
            if avail!=0:
                best = min(best,recur(n-avail,avail)+1)
            return best
        res = recur(n_-1,0)
        return res
        