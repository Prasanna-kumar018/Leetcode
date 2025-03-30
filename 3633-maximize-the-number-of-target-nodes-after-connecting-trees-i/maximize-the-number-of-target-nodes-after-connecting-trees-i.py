class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        d = collections.defaultdict(list)
        g = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for x,y in edges1:
            d[x].append(y)
            d[y].append(x)
        for x,y in edges2:
            g[x].append(y)
            g[y].append(x)
            indegree[x]+=1
            indegree[y]+=1
        n = len(edges1)+1
        m = len(edges2)+1
        dis = [ [0]*(k+1) for _ in range(n)]
        def go(node,par):
            for des in d[node]:
                if des!=par:
                    go(des,node)
                    for i in range(1,k+1):
                        dis[node][i]+=dis[des][i-1]
            dis[node][0]=1
        go(0,-1)
        def go1(node,par):
            for des in d[node]:
                if des!=par:
                    for i in range(k,0,-1):
                        val=0
                        if i>=2:
                            val = dis[des][i-2]
                        dis[des][i]+=(dis[node][i-1]-val)
                    go1(des,node)
        go1(0,-1)
        def go2(node,par,val):
            if val<0:
                return 0
            res = 1
            for des in g[node]:
                if des!=par:
                    res+= go2(des,node,val-1)
            return res
        count = 0
        for i in range(m):
            count = max(count,go2(i,-1,k-1))
        ans = []
        for i in range(n):
            ans.append(count+sum(dis[i]))
        return ans