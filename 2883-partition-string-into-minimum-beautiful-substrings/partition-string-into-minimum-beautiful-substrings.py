class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        n = len(s)
        INF = 10**20
        @cache
        def recur(idx):
            if idx==n:
                return 0
            if s[idx]=='0':
                return INF
            res = INF
            v = 0
            for index in range(idx,n):
                val = int(s[index])
                v = v<<1
                v |= val
                xx = int(math.log(v)/math.log(5))
                if 5**xx == v:
                    res = min(res,recur(index+1)+1)
            return res
        x = recur(0)
        return x if x!=INF else -1
        