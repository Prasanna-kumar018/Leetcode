class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        start = collections.defaultdict(list)
        end = collections.defaultdict(list)
        total = set() # 0 - start ,  1-end
        for x,y,z in buildings:
            start[x].append(z)
            end[y].append(z)
            total.add(x)
            total.add(y)
        # print(total)
        total = sorted([x for x in total])
        q = []
        def push(val):
            heapq.heappush(q,val)
        def pop():
            return heapq.heappop(q)
        # print(start,end,total)
        result = []
        prev = -1
        remove = collections.defaultdict(int)
        for x in total:
            for y in end[x]:
                remove[y]+=1
            for y in start[x]:
                push(-y)
            while q and remove[abs(q[0])]>0:
                remove[abs(q[0])]-=1
                pop()
            if q and prev!=abs(q[0]):
                prev = abs(q[0])
                result.append([x,prev])
            elif not q:
                prev = 0
                result.append([x,prev])
        return result