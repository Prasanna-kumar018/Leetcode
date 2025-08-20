class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        """
        It is pure binary lifting
        """
        N = len(receiver)
        M = int(math.ceil(math.log2(k)))+1
        child = [[receiver[i] for i in range(N)]  for _ in range(M)]
        cost = [[receiver[i] for i in range(N)]  for _ in range(M)]
        for i in range(1,M):
            for j in range(N):
                p = child[i-1][j]
                child[i][j] = child[i-1][p]
                cost[i][j] = cost[i-1][j] + cost[i-1][p]
        ans = 0
        for start in range(N):
            total = start
            node = start
            for i in range(M):
                if (k&(1<<i))>0:
                    total += cost[i][node]
                    node = child[i][node]
            ans = max(ans,total)
        return ans