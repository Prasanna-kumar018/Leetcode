class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        m = len(queries)
        r , c= set(), set()
        res = 0
        for i in range(m-1,-1,-1):
            t,idx,val = queries[i]
            if t==0:
                if idx in r:
                    continue
                res+= (val*(n-len(c)))
                r.add(idx)
            else:
                if idx in c:
                    continue
                res+=(val*(n-len(r)))
                c.add(idx)
        return res