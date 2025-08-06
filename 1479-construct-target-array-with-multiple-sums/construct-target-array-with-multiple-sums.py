class Solution:
    def isPossible(self, target: List[int]) -> bool:
        """
        forward approach does not work
        """
        n =len(target)
        q = []
        total = 0
        for x in target:
            total += x
            heapq.heappush(q,-x)
        while True:
            if total==n:
                return True
            largest = abs(heapq.heappop(q))
            rem = (total-largest)
            prev = largest - rem 
            if prev<=0 or rem==0: # rem==0 for single element 
                return False
            nex = largest % (rem)
            if nex==0:
                nex = rem
            total -= largest
            total += nex
            heapq.heappush(q,-nex)
            # print(q,nex,rem,total)

        return True