class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7
        """
        key point -> 
        Natural handling of shorter lengths via leading zeros (no need for separate g() and gc()).

            def gc(c,val):
                if c==0:
                    if min_sum <= val <= max_sum:
                        return 1
                    return 0
                r = 0
                for i in range(10):
                    r += gc(c-1,min(val+i,max_sum))
                return r
            def g(c):
                res = 0
                for i in range(1,10):
                    res += gc(c-1,min(i,max_sum))
                return res
        """

        def go(ss):
            N = len(ss)
            @cache
            def g(idx,isless,val):
                if val>max_sum:
                    return 0
                if idx==N:
                    if min_sum <= val <= max_sum:
                        return 1
                    return 0
                r = 0
                x = int(ss[idx])
                end = 10 if isless else x+1
                for i in range(end):
                    v = bool(i<x)
                    r += g(idx+1,isless or v,i+val)
                return r
            x = g(0,False,0)
            return x
        vv = str(int(num1)-1)
        return (go(num2)- go(vv)) % MOD