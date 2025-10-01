class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        q = []
        def push(val):
            heapq.heappush(q,val)
        def pop():
            return heapq.heappop(q)
        
        INF = 10**20
        dis = collections.defaultdict(lambda : collections.defaultdict(lambda : INF))
        dis[start[0]][start[1]]=0
        push((0,start[0],start[1]))
        while q:
            cost , x , y = pop()
            for dx,dy,z,a,c in specialRoads:
                cc = abs(x-dx)+abs(y-dy) + c + cost
                if cc < dis[z][a]:
                    dis[z][a]=cc
                    push((cc,z,a))
            cc = abs(x-target[0]) + abs(y-target[1])
            dis[target[0]][target[1]] = min(dis[target[0]][target[1]],cost+cc)
        return dis[target[0]][target[1]]
