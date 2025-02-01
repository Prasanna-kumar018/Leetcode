class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        for x,y in connections:
            g[x].append((y,0))
            g[y].append((x,1))
        d= {}
        def dfs(dep,start,par,ans):
            for des,wt in g[start]:
                if des!=par:
                    d[des]=dep-(ans+wt)
                    dfs(dep+1,des,start,dep)
        dfs(1,0,-1,0)
        return sum(d.values())