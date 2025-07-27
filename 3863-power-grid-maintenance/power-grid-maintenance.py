class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:

        blocked = collections.Counter()
        for x,y in queries:
            if x==2:
                blocked[y]+=1
        par = {}
        mini = {}
        INF = 10**20
        def find(x):
            if x not in par:
                par[x]=x
                mini[x]=(x if blocked[x]==0 else INF)
            if par[x]!=x:
                par[x]=find(par[x])
            return par[x]

        def union(x,y):
            # print(x,y)
            x= find(x)
            y= find(y)
            if x==y:
                return
            par[x]=y
            mini[y]=min(mini[y],mini[x])


        for x,y in connections:
            union(x,y)
        # print()
        res = []
        for x,y in reversed(queries):
            if x==1:
                if blocked[y]==0:
                    res.append(y)
                else:
                    MAXI = mini[find(y)]
                    res.append(MAXI if MAXI != INF else -1)
            else:
                blocked[y]-=1
                if blocked[y]==0:
                    p = find(y)
                    mini[p]=min(mini[p],y)
        res.reverse()
        return res