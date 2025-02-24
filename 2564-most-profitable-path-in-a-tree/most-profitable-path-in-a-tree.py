class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        g = collections.defaultdict(list)
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
        depth = {}
        parent = {}
        def dfs(node,par,d):
            depth[node]=d
            for des in g[node]:
                if des!=par:
                    parent[des]=node
                    dfs(des,node,d+1)
        dfs(0,-1,0)
        # print(depth,parent) 
        def dfs2(x,d):
            if depth[x]>d:
                amount[x]=0
            if depth[x]==d:
                amount[x]//=2
            if x in parent:
                dfs2(parent[x],d+1)
        dfs2(bob,0)
        INF = 10**20
        def recur(start,par):
            if len(g[start])==1 and par!=-1:
                return amount[start]
            res = -INF
            for des in g[start]:
                if des!=par:
                    res = max(res,recur(des,start))
            return res+amount[start]
        return recur(0,-1)