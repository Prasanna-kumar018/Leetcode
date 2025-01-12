class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        q = []
        m = len(grid)
        n = len(grid[0])
        dir = [(-1,0),(1,0),(0,-1),(0,1)]
        vis = set()
        def push(val):
            heapq.heappush(q,val)
        def pop():
            return heapq.heappop(q)
        push((grid[0][0],0,0))
        total = 0 
        def go(val):
            nonlocal total
            while q:
                if q[0][0]>=val:
                    return
                _,x,y = pop()
                if (x,y) in vis:
                    continue
                total+=1
                vis.add((x,y))
                for dx,dy in dir:
                    nx,ny = x+dx,y+dy
                    if 0<=nx <m and 0<= ny <n and (nx,ny) not in vis:
                        push((grid[nx][ny],nx,ny))
        queries = [(val,idx) for idx,val in enumerate(queries)]
        queries.sort()
        ans = [0]*len(queries)
        for x,idx in queries:
            # print(x)
            go(x)
            # print(total,q)
            ans[idx]=total
        return  ans