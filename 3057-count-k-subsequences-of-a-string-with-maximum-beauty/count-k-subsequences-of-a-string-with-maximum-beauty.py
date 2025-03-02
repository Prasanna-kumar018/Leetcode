class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        c = Counter(s)
        MOD = 10**9+7
        ff = Counter(c.values())
        count = 1
        for x in sorted(ff.keys(),reverse=True):
            cc = ff[x]
            if k-cc<0:
                count*=(math.comb(cc,k)*pow(x,k,MOD))
                k-=cc
                break
            count*=pow(x,cc,MOD)
            k-=cc
        if k>0:
            return 0
        return count%MOD