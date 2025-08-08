class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], costt: List[int]) -> int:
        INF = 10**20
        g = collections.defaultdict(list)
        for x,y,z in zip(original,changed,costt):
            g[x].append((y,z))
        
        dis = collections.defaultdict(lambda : collections.defaultdict( lambda : INF))
        def recur(src):
            nonlocal dis
            q = []
            def push(val):
                heapq.heappush(q,val)
            def pop():
                return heapq.heappop(q)
            push((0,src))
            dis[src][src]=0
            while q:
                cost, node = pop()
                if dis[src][node]<cost:
                    continue
                for des,c in g[node]:
                    if dis[src][des]>cost+c:
                        dis[src][des]=cost+c
                        push((dis[src][des],des))

        for x in original:
            recur(x)

        print(dis)
        n = len(source)
        m = len(original) 
        @cache
        def rec(idx):
            if idx==n:
                return 0
            res = INF
            if target[idx]==source[idx]:
                res = min(res,rec(idx+1))
            for i in range(m):
                if source[idx:].startswith(original[i]):
                    L = len(original[i])
                    if target[idx:idx+L] in dis[original[i]]:
                        res = min(res,dis[original[i]][target[idx:idx+L]] + rec(idx+L))
            return res
        xx = rec(0)
        return xx if xx!=INF else -1
        