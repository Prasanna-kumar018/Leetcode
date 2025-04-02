class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        INF = 10**20
        @cache
        def recur(s,t):
            dis = collections.defaultdict(lambda : INF)
            q = []
            def push(val):
                heapq.heappush(q,val)
            def pop():
                return heapq.heappop(q)
            push((0,s))
            dis[s]=0
            while q:
                val , node = pop()
                if dis[node]<val:
                    continue
                x = ord(node)-ord('a')
                c = chr((x+1)%26+ord('a'))
                if dis[c]>dis[node]+nextCost[x]:
                    dis[c] = dis[node]+nextCost[x]
                    push((dis[c],c))
                c = chr((x-1)%26+ord('a'))
                if dis[c]>dis[node]+previousCost[x]:
                    dis[c] = dis[node]+previousCost[x]
                    push((dis[c],c))
            return dis[t]
        res = 0
        for x,y in zip(s,t):
            res += recur(x,y)
        return res