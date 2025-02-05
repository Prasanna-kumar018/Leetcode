class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        n = len(words)
        INF = 10**10
        length = [0]*n
        for idx,x in enumerate(words):
            length[idx]=len(x)
        @cache
        def recur(idx,f,l):
            if idx==n:
                return 0
            res = INF
            val = length[idx]
            if f ==words[idx][-1]:
                res = min(res,recur(idx+1,words[idx][0],l)+(val-1))
            else:
                res = min(res,recur(idx+1,words[idx][0],l)+val)
            if l ==words[idx][0]:
                res = min(res,recur(idx+1,f,words[idx][-1])+(val-1))
            else:
                res = min(res,recur(idx+1,f,words[idx][-1])+val)
            return  res
        return recur(1,words[0][0],words[0][-1])+length[0]