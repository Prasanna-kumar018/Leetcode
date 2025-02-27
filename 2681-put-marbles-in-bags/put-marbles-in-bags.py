class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        mini = []
        maxi = []
        def push(x,val):
            heapq.heappush(x,val)
        def pop(x):
            return heapq.heappop(x)
        n = len(weights)
        mitotal,matotal = 0,0
        for i in range(n-1):
            push(mini,weights[i]+weights[i+1])
            push(maxi,-(weights[i]+weights[i+1]))
            mitotal+=(weights[i]+weights[i+1])
            matotal+=(weights[i]+weights[i+1])
            if len(mini)==k:
                x = pop(mini)
                mitotal-=x
            if len(maxi) == k:
                x = pop(maxi)
                matotal-=abs(x)
        return mitotal-matotal
            