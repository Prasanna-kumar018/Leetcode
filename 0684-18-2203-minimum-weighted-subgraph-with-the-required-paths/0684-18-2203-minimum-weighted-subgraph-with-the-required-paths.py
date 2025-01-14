class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        g =  collections.defaultdict(list)
        rg = collections.defaultdict(list)
        for x,y,w in edges:
            g[x].append((y,w))
            rg[y].append((x,w))
        INF = 10**20
        def get(g,src):
            dis = [INF]*n
            dis[src]=0
            q = []
            def push(val):
                heapq.heappush(q,val)
            def pop():
                return heapq.heappop(q)
            push((0,src))
            while q:
                val, x = pop()
                if dis[x]<val:
                    continue
                for y,w in g[x]:
                    if val+w<dis[y]:
                        dis[y]=val+w
                        push((dis[y],y))
            return dis
        d1 = get(g,src1)
        d2 = get(g,src2)
        d3 = get(rg,dest)
        best = INF
        for i in range(n):
            best = min(best,d1[i]+d2[i]+d3[i])
        return best if best!=INF else -1