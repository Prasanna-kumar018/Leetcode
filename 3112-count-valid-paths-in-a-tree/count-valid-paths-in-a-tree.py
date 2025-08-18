class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
        M = max(2,n+1)
        isprime = [True]*M
        isprime[0] = isprime[1] = False
        for i in range(2,M):
            if isprime[i]:
                for j in range(2*i,M,i):
                    isprime[j]=False

        par = {}
        size = {}
        def find(x):
            if x not in par:
                par[x]=x
                size[x]=1
            if par[x]!=x:
                par[x]=find(par[x])
            return par[x]
        def union(x,y):
            x = find(x)
            y = find(y)
            par[x]=y
            if x==y:
                return
            size[y]+=size[x]
        
        for x,y in edges:
            if not isprime[x] and not isprime[y]:
                union(x,y)
        
        total = 0
        for x in range(1,n+1):
            if isprime[x]:
                curr = 1
                for des in g[x]:
                    if not isprime[des]:
                        s = size[find(des)]
                        total += curr * s
                        curr += s
        return total