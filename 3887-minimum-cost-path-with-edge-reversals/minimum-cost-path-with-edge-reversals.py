class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        for x,y,z in edges:
            g[x].append((y,z))
            g[y].append((x,2*z))
        INF = 10**20
        dp = [INF]*n
        q = collections.deque()
        q.append((0,0))
        dp[0]= 0
        while q:
            cost , node = q.popleft()
            for des,val in g[node]:
                if dp[des]>cost+val:
                    dp[des]=cost+val
                    q.append((dp[des],des))
        return dp[-1] if dp[-1]!=INF else -1
        

        