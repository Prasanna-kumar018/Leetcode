class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = 0
        while numBottles>=numExchange:
            c = 0
            while numBottles>=numExchange:
                numBottles-=numExchange
                res+=numExchange
                c+=1
                numExchange+=1 
            # print(c,numBottles)
            numBottles+=c
        return res+numBottles