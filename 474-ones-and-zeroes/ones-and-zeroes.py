class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        INF = -10**10
        nx = len(strs) 
        dp = []
        for x in strs:
            x = Counter(x)
            dp.append((x['0'],x['1']))
        @cache
        def recur(idx,mi,ni):
            nonlocal nx,strs,dp
            if  mi>m or ni>n:
                return INF
            if idx==nx:
                return 0
            res = INF
            res = max(res,recur(idx+1,mi,ni))
            z,o= dp[idx]
            res = max(res,recur(idx+1,mi+z,ni+o)+1)
            return res
        x=  recur(0,0,0)
        return x
            