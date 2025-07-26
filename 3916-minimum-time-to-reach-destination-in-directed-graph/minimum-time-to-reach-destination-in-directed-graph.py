class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        for x,y,s,e in edges:
            g[x].append((y,s,e))
        
        start = 0
        q = []
        def push(val):
            heapq.heappush(q,val)
        def pop():
            return heapq.heappop(q)
        
        push((0,start)) # time , start  
        INF = 10**20
        dis = [INF]*n
        dis[start]=0
        while q:
            time , node = pop()
            
            for des,st,end in g[node]:
                if time <= end:
                    val = max(time,st)
                    val = val+1  
                    if dis[des]>val:
                        dis[des]=val
                        push((dis[des],des))
                        # print(dis)
        
        return dis[-1] if dis[-1]!=INF else -1