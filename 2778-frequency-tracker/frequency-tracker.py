class FrequencyTracker:

    def __init__(self):
        self.f = collections.defaultdict(int)        
        self.d = collections.defaultdict(int)        

    def add(self, number: int) -> None:
        self.d[self.f[number]]-=1
        self.f[number]+=1
        self.d[self.f[number]]+=1

    def deleteOne(self, number: int) -> None:
        if self.f[number]>=1:
            self.d[self.f[number]]-=1
            self.f[number]-=1
            self.d[self.f[number]]+=1

    def hasFrequency(self, frequency: int) -> bool:
        return self.d[frequency]>=1        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)