class Solution:
    def countAnagrams(self, s: str) -> int:
        n = len(s)
        MOD = 10**9+7
        fact = [1]*(n+1)
        for i in range(1,n+1):
            fact[i]=(fact[i-1]*i)
            fact[i]%=MOD
        res = 1  
        for x in s.split(' '):
            c = Counter(x)
            v = fact[len(x)]
            for y,z in c.items():
                # v//=fact[z]
                v= (v*pow(fact[z],-1,MOD))
            res*=v
            res%=MOD
        return res