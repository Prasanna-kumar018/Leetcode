class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        par = {}
        mini = {}
        INF = 10**10
        def find(x):
            if x not in par:
                par[x]=x
                mini[x]=INF
            if par[x]!=x:
                par[x]=find(par[x])
            return par[x]
        
        def union(a,b,z):
            a = find(a)
            b = find(b)
            par[a]=b
            mini[b]=min(mini[b],mini[a],z)
        
        for x,y,z in roads:
            union(x,y,z)
        
        return mini[find(1)]