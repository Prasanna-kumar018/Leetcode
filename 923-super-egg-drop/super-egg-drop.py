class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        INF = 10**10
        @cache
        def recur(n,k): # n egg k floor
            if k<=1 or n==1:
                return k
            res = INF
            l,r=1,k
            while l<=r:
                i = (l+r)//2
                down = recur(n-1,i-1)
                up = recur(n,k-i)
                v = 1 + max(down,up)
                if down > up:
                    r = i-1
                else:
                    l = i+1
                res = min(res,v)
            return res
            # for i in range(1,k+1):
            #     v = 1 + max(recur(n-1,i-1),recur(n,k-i))
            #     res = min(res,v)
            # return res
        return recur(k,n)
