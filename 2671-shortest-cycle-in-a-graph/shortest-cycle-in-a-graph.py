class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        # dfs don't work for this approach....
        g = collections.defaultdict(list)
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
        INF = 10**20
        ans =  INF
        for i in range(n):
            F = 0
            q = collections.deque()
            depth = [-1]*n
            q.append((i,0,-1))
            while q:
                node,count,par = q.popleft()
                depth[node]=count
                for des in g[node]:
                    if des==par:
                        continue
                    if depth[des]==-1:
                        q.append((des,count+1,node))
                    else:
                        ans = min(ans,(count+depth[des]+1))
                        F = 1
                        break
                if F == 1 :
                    break

        return ans if ans!=INF else -1