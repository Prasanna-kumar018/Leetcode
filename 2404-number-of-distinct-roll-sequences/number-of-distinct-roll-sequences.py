class Solution:
    def distinctSequences(self, n: int) -> int:
        MOD = 10**9+7
        # @cache
        # def recur(n,prev,bprev):
        #     if n==0:
        #         return 1
        #     res = 0
        #     for i in range(1,7):
        #         if i!=prev and i!=bprev and math.gcd(prev,i)==1:
        #             res += recur(n-1,i,prev)
        #     return res 
        # total = 0
        # for i in range(1,7):
        #     total += recur(n-1,i,-1)
        # return total%MOD

        dp = collections.defaultdict(lambda : collections.defaultdict(int))
        for prev in range(1,7):
            for bprev in [-1,1,2,3,4,5,6]:
                dp[prev][bprev]=1
        for o in range(1,n):
            result = collections.defaultdict(lambda : collections.defaultdict(int))
            for prev in range(1,7):
                for bprev in [-1,1,2,3,4,5,6]:
                    res = 0
                    for i in range(1,7):
                        if i!=prev and i!=bprev and math.gcd(prev,i)==1:
                            res += dp[i][prev]
                    result[prev][bprev]=res
            dp = result
        
        total = 0
        for i in range(1,7):
            total += dp[i][-1]
        return total%MOD
