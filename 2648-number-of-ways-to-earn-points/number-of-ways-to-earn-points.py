class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        n = len(types)
        MOD = 10**9 + 7
        @cache
        def recur(idx,tar):
            if tar<0:
                return 0
            if idx==n:
                if tar==0:
                    return 1
                return 0
            best = 0
            x,y = types[idx]
            for i in range(x+1):
                best += recur(idx+1,tar-(i*y))
            return best%MOD
        return recur(0,target)