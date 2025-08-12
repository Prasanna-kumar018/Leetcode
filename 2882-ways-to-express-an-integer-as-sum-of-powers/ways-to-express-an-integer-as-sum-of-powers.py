class Solution:
    def numberOfWays(self, nn: int, x: int) -> int:

        MOD = 10**9 + 7
        @cache
        def recur(val,n):
            if val==nn+1:
                if n==0:
                    return 1
                return 0
            res = 0
            res += recur(val+1,n)
            v= pow(val,x)
            if n-v>=0:
                res += recur(val+1,n-v)
            return res % MOD
        return recur(1,nn)