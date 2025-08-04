class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # source to target so dijkstra's algo
        n = len(routes) # no of buses
        if source == target:
            return 0 # They are not different stops of the same bus(1)  
        targetbuses = set()
        lookup = collections.defaultdict(set)
        for i in range(n):
            for stop in routes[i]:
                lookup[stop].add(i)
                if stop==target:
                    targetbuses.add(i)
        if not targetbuses:
            return -1
        INF = 10**10
        distance = [INF]*n
        q = collections.deque()
        for bus in lookup[source]:
            q.append((1,bus))
            distance[bus] = 1
        while q:
            value,bus = q.popleft()
            if distance[bus]<value:
                continue
            for stop in routes[bus]:
                for nbus in lookup[stop]:
                    if distance[nbus]>distance[bus]+1:
                        distance[nbus]=distance[bus]+1
                        q.append((distance[nbus],nbus))
        res = min([distance[x] for x in targetbuses])
        return res if res!=INF else -1