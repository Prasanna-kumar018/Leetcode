class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        g = collections.defaultdict(list)
        g1 = collections.defaultdict(list)
        d = collections.defaultdict(float)
        for p,r in zip(pairs1,rates1):
            g[p[0]].append((p[1],r))
            g[p[1]].append((p[0],1/r))
        for p,r in zip(pairs2,rates2):
            g1[p[0]].append((p[1],r))
            g1[p[1]].append((p[0],1/r))
        q = collections.deque([(1.0,initialCurrency)])
        d[initialCurrency]=1.0
        while q:
            val , curr  =  q.popleft()
            if val < d[curr]:
                continue
            for des,r in g[curr]:
                if d[des]<r*val:
                    d[des]=r*val
                    q.append((d[des],des))
        for x,v in d.items():
            q.append((v,x))
        while q:
            val , curr  =  q.popleft()
            if val < d[curr]:
                continue
            for des,r in g1[curr]:
                if d[des]<r*val:
                    d[des]=r*val
                    q.append((d[des],des))
        return d[initialCurrency]