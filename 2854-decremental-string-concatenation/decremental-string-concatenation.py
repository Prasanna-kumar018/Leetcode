class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        n = len(words)
        INF = 10**10
        length = [0]*n
        for idx,x in enumerate(words):
            length[idx]=len(x)
        @cache
        def recur(idx,first,last):
            if idx==n:
                return 0
            res = INF
            val = length[idx]
            if last==words[idx][0]:
                res=min(res,recur(idx+1,first,words[idx][-1])+val-1)
            else:
                res=min(res,recur(idx+1,first,words[idx][-1])+val)
            if first==words[idx][-1]:
                res=min(res,recur(idx+1,words[idx][0],last)+val-1)
            else:
                res=min(res,recur(idx+1,words[idx][0],last)+val)
            return res
        return recur(1,words[0][0],words[0][-1])+length[0]