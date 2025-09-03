class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        INF = 10**20
        N = len(cost)
        lower = -N
        upper = N
        @cache
        def recur(idx,have):
            if idx==N:
                if have>=0:
                    return 0
                return INF
            res = INF
            res = min(res,recur(idx+1,max(lower,have-1)))
            res = min(res,recur(idx+1,min(have+time[idx],upper))+cost[idx])
            return res
        x = recur(0,0)
        return x 