class Solution:
    def countServers(self, n: int, logs: List[List[int]], xx: int, queries: List[int]) -> List[int]:
        g = collections.defaultdict(set)
        for x,y in logs:
            g[y].add(x)
        d = collections.defaultdict(int)
        qs = sorted(set(queries+[x for _,x in logs]))
        # qs = sorted(set(queries+g.keys()))
        # print(qs)
        q = {}
        have = 0
        MAXI = max(queries)+1
        left = 0
        for r in qs:
            for x in g[r]:
                if d[x]==0:
                    have += 1
                d[x]+=1
            while qs[left]< r-xx:
                for x in g[qs[left]]:
                    d[x]-=1
                    if d[x]==0:
                        have -=1
                left+=1
            q[r]=n-have
                
        res = []
        for x in queries:
            res.append(q[x])
        return res
