class Solution:
    def numTrees(self, nn: int) -> int:
        @cache
        def recur(n):
            if n<=1:
                return 1
            res = 0
            for x in range(1,n+1):
                l = recur(x-1)
                r = recur(n-x)
                res += l*r
            return res
        return recur(nn)