class Solution:
    def smallestValue(self, n: int) -> int:
        MAXI = max(2,n+1)
        res = [[] for _ in range(MAXI)]
        for i in range(2,MAXI):
            j = i
            while j<MAXI:
                res[j].append(i)
                j+=i
        def get(x):
            v = x
            s = 0
            for a in res[v]:
                while x%a==0:
                    s += a
                    x //= a 
            return s

        while n!=get(n):
            n = get(n)

        return n
