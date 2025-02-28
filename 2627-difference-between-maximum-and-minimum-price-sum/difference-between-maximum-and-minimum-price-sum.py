class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        g = collections.defaultdict(list)
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
        ans = collections.defaultdict(list)
        INF = 10**20
        def dfs(node,par):
            maxi = [price[node]]
            for des in g[node]:
                if des!=par:
                    maxi.append(dfs(des,node)+price[node])
            maxi.sort(reverse=True)
            ans[node] = maxi[:2]
            return maxi[0]
        dfs(0,-1)
        res = [-1]*n
        res[0]=ans[0][0]
        def dfs2(node,par,prev):
            for des in g[node]:
                if des!=par:
                    v = ans[node][0]
                    if v == ans[des][0]+price[node]:
                        v = ans[node][1]
                    v+=price[des]
                    res[des]=max(v,ans[des][0],prev+price[des])
                    dfs2(des,node,max(v,prev+price[des]))
        dfs2(0,-1,price[0])
        s = -INF
        for x,y in zip(res,price):
            s = max(s,(x-y))
        return s