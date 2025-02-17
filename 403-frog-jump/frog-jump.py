class Solution:
    def canCross(self, stones: List[int]) -> bool:
        d = collections.defaultdict(lambda :-1)
        for idx,val in enumerate(stones):
            d[val]=idx
        n = len(stones)
        @cache
        def recur(idx,k):
            if idx==n-1:
                return True
            for i in range(k-1,k+2):
                if stones[idx]+i in d and d[stones[idx]+i]> idx:
                    if recur(d[stones[idx]+i],i):
                        return True
            return False
        return recur(d[1],1) if 1 in d else False