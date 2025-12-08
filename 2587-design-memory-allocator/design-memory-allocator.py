class Allocator:

    def __init__(self, n: int):
        self.arr = [0]*n
        self.n = n
    def allocate(self, size: int, mID: int) -> int:
        i = 0
        while i<self.n:
            c = 0
            t = i
            while i<self.n and self.arr[i]==0:
                i+=1
                c+=1
            if c>=size:
                for x in range(size):
                    self.arr[x+t]=mID
                return t

            i = max(i,t+1)
        return -1

    def freeMemory(self, mID: int) -> int:
        count = 0
        for idx,val in enumerate(self.arr):
            if val==mID:
                count+=1
                self.arr[idx]=0
        return count
# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)