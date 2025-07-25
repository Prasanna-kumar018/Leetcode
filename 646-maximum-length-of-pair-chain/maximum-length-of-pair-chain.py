class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort()
        @cache
        def recur(prev):
            if prev==n-1:
                return 0
            res = 0
            for idx in range(prev+1,n):
                if prev==-1:
                    res = max(res,recur(idx)+1)
                elif pairs[prev][-1] < pairs[idx][0]:
                    res = max(res,recur(idx)+1)
            return res
        return recur(-1)