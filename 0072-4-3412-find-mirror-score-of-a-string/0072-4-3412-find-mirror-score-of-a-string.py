class Solution:
    def calculateScore(self, s: str) -> int:
        d = {}
        A = 26
        for i in range(A):
            last = 25-i
            d[chr(97+i)]=chr(last+97)
        # print(d)
        def push(x,val):
            heapq.heappush(x,val)
        def pop(x):
            return heapq.heappop(x)
        
        res = collections.defaultdict(list)
        total = 0
        for idx,x in enumerate(s):
            need = d[x]
            if res[need]:
                j = abs(pop(res[need]))
                total += idx-j
            else:
                push(res[x],-idx)
            # print(total,res)
        return total
