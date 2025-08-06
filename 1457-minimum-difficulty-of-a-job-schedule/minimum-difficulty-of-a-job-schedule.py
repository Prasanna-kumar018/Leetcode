class Solution:
    def minDifficulty(self, arr: List[int], d: int) -> int:
        n = len(arr)
        INF = 10**20
        @cache
        def recur(idx,d):
            if d<0:
                return INF
            if idx==n:
                if d==0:
                    return 0
                return INF
            best = INF
            maxi = -INF
            for i in range(idx,n):
                maxi = max(arr[i],maxi)
                best = min(best,maxi+recur(i+1,d-1))
            return best
        res = recur(0,d)
        return res if res!=INF else -1