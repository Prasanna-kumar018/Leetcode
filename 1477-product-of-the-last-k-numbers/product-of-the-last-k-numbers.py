class ProductOfNumbers:

    def __init__(self):
        self.arr = [1]
        self.maxi = -1

    def add(self, num: int) -> None:
        if num==0:
            self.maxi = max(self.maxi,len(self.arr)-1)
            self.arr.append(self.arr[-1])
        else:
            self.arr.append(self.arr[-1]*num)
        # print(num,self.arr,self.maxi)

    def getProduct(self, k: int) -> int:
        index = len(self.arr)-1-k
        if self.maxi>=index:
            return 0
        return self.arr[-1]//self.arr[-k-1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)