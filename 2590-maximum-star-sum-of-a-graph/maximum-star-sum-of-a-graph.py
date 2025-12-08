class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        n = len(vals)
        g = collections.defaultdict(list)
        def push(q,x):
            heapq.heappush(q,x)
        def pop(q):
            return heapq.heappop(q)
        for x,y in edges:
            if vals[y]>0:
                push(g[x],vals[y])
            while len(g[x])>k:
                pop(g[x])
            if vals[x]>0:
                push(g[y],vals[x])
            while len(g[y])>k:
                pop(g[y])

        c = max(vals) # for 0 edges i.e one node
        for x,y in g.items():
            c = max(c,vals[x]+sum(y))
            print(x,y)
        return c
        """
        0
        |/-----\
        3 - 1 - 4 - 6
            | 
            5

        """
