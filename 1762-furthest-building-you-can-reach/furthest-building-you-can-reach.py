class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        import heapq
        n = len(heights)
        q = []
        def push(val):
            heapq.heappush(q,val)
        def pop():
            return heapq.heappop(q)
        t = 0
        for i in range(1,n):
            val = heights[i]-heights[i-1]
            if  val>0:
                push(-val)
                t+=val
            while t>bricks and ladders>0:
                ladders-=1
                val = pop()
                t-=abs(val)
            if t>bricks:
                return i-1
        return n-1
