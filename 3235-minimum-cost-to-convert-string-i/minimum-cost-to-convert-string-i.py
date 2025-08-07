class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], costt: List[int]) -> int:
        INF = 10**20
        g = collections.defaultdict(lambda : collections.defaultdict( lambda : INF))
        for x,y,z in zip(original,changed,costt):
            g[x][y]=min(g[x][y],z)
        @cache
        def recur(src,tar):
            q = []
            def push(val):
                heapq.heappush(q,val)
            def pop():
                return heapq.heappop(q)
            push((0,src))
            dis = collections.defaultdict(lambda : INF)
            dis[src]=0
            while q:
                cost, node = pop()
                if dis[node]<cost:
                    continue
                if node == tar:
                    return cost
                for des in g[node].keys():
                    c = g[node][des]
                    if dis[des]>dis[node]+c:
                        dis[des]=dis[node]+c
                        push((dis[des],des))

            return -1

        total = 0
        for x,y in zip(source,target):
            if x!=y:
                res = recur(x,y)
                if res==-1:
                    return -1
                total += res   
        return total
