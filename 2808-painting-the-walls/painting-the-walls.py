class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        INF = 10**20
        N = len(cost)
        @cache
        def recur(idx,have):
            if have>=N:
                return 0
            if idx==N:
                return INF
            res = INF
            res = min(res,recur(idx+1,have))
            """
            time[idx] --> no of free painters
            1 --> for the current painter
            """
            res = min(res,recur(idx+1,min(have+time[idx]+1,N))+cost[idx])
            return res
        x = recur(0,0)
        return x 