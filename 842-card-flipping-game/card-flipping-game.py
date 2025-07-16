class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        INF = 10**20
        res = INF
        s = set()
        for x,y in zip(fronts,backs):
            if x==y:
                s.add(x)
        for x,y in zip(fronts,backs):
            if x not in s:
                res = min(res,x)
            if y not in s:
                res = min(res,y)
        return res if res!=INF else 0