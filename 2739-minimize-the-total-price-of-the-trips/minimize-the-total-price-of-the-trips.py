class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
        count = [0]*n
        INF = 10**20
        for x,y in trips:
            q = collections.deque()
            q.append((x,0))
            parent = collections.defaultdict(lambda :-1)
            d = collections.defaultdict(lambda :INF )
            d[x]=0
            while q:
                node , val=q.popleft()
                if d[node]<val:
                    continue
                for des in g[node]:
                    if d[des]>d[node]+1:
                        d[des]=d[node]+1
                        q.append((des,d[des]))
                        parent[des]=node
            start = y

            while start!=-1:
                count[start]+=1
                start = parent[start]
        # print(count)
        @cache
        def recur(node,par,lused): # lused == last used...
            total = INF
            if not lused:
                res = (price[node]//2)*(count[node])
                for des in g[node]:
                    if des!=par:
                        res += recur(des,node,True)
                total = min(total,res)
            res = price[node]*(count[node])
            for des in g[node]:
                if des!=par:
                    res+= recur(des,node,False)
            total = min(res,total)
            return  total
        return recur(0,-1,False)