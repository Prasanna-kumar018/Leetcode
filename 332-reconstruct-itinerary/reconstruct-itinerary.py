class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = collections.defaultdict(lambda :collections.defaultdict(int))
        g = collections.defaultdict(set)
        for x,y in tickets:
            g[x].add(y)
            d[x][y]+=1
        g1 = collections.defaultdict(list)
        for x,y in g.items():
            g1[x]=sorted(list(y))
        n = len(tickets)
        def recur(idx,start):
            if idx==n:
                return ['']
            
            for x in g1[start]:
                if d[start][x]>0:
                    d[start][x]-=1
                    a = recur(idx+1,x) 
                    if a:
                        a.append(x)
                        return a
                    d[start][x]+=1
        res = recur(0,"JFK")
        res.append("JFK")
        res.reverse()
        res.pop()
        # print(res)
        return res