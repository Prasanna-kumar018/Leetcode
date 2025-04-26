class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        q = []
        def push(val):
            heapq.heappush(q,val)
        def pop():
            return heapq.heappop(q)
        i = 0
        count = 0
        n = len(stations) 
        while startFuel<target:
            while i<n and stations[i][0]<=startFuel:
                push((-stations[i][1]))
                i+=1
            if not q:
                return -1
            count+=1
            val = abs(pop())
            startFuel+=val
        return count