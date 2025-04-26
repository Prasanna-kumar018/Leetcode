class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = 10**9+7
        @cache
        def recur(prev1,prev2,n):
            if n==0:
                return 1
            res = 0
            for x in [True,False]:
                for y in [True,False]:
                    if x or y:
                        if x and y:
                            if x and not prev1 and y and not prev2:
                                res+=recur(x,y,n-1)
                        elif x:
                            if x and not prev1:
                                res+=recur(x,y,n-1)
                        else:
                            if y and not prev2:
                                res+=recur(x,y,n-1)
                    else:
                        res += recur(x,y,n-1)
            return res
        x =recur(False,False,n)
        return x%MOD