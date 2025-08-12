class Solution:
    def minimumOperations(self, num: str) -> int:
        N = len(num)
        INF = 10**20
        @cache
        def recur(idx,mod):
            if idx==N:
                if mod==0:
                    return 0
                return INF 
            res = INF
            res = min(res,recur(idx+1,mod)+1)
            res = min(res,recur(idx+1,((mod*10)+int(num[idx]))%25))
            return res
        x = recur(0,0)
        return x