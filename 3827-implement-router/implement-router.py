class Router:

    def __init__(self, memoryLimit: int):
        self.limit =  memoryLimit
        self.set = set()
        self.queue = collections.deque()
        self.dict = collections.defaultdict(collections.deque)
    def deleteone(self):
        x = self.queue[0]
        self.dict[x[1]].popleft()
        self.set.remove(x)
        self.queue.popleft()
        return x
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        x = (source,destination,timestamp)
        if x in self.set:
            return False
        if len(self.queue)==self.limit:
            a = self.deleteone()
        self.set.add(x)
        self.dict[destination].append(timestamp)
        self.queue.append(x)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        return self.deleteone()

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        des = self.dict[destination]
        l,r = 0,len(des)-1
        start,end = -1,-1
        while l<=r:
            mid = (l+r)//2
            if des[mid]>=startTime:
                start = mid
                r = mid-1
            else:
                l = mid+1
        l,r =  0,len(des)-1
        while l<=r:
            mid = (l+r)//2
            if des[mid]<=endTime:
                end = mid
                l = mid+1
            else:
                r = mid-1
        if start==-1 or end==-1:
            return 0
        return end-start+1
# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)