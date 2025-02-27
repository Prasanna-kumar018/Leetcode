class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        d = Counter(basket1+basket2)
        for x,y in d.items():
            if y%2==1:
                return -1
            d[x]//=2
        mini = min(d.keys())
        # Either we can take the mini and swap twice 
        extra = []
        c = Counter(basket1)
        for x,y in c.items():
            for i in range(y-d[x]):
                extra.append(x)
        c = Counter(basket2)
        for x,y in c.items():
            for i in range(y-d[x]):
                extra.append(x)
        extra.sort()
        return sum( min(mini*2,extra[i])   for i in range(len(extra)//2))