class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        bombs = list(map(tuple,bombs))
        c = collections.Counter(bombs)
        n = len(bombs)
        def get(x,y):
            dis = (x[0]-y[0])**2 + (x[1]-y[1])**2 
            r = x[2]**2
            if dis<=r:
                return True
            return False
        for i in range(n):
            for j in range(n):
                if get(bombs[i],bombs[j]):
                    g[bombs[i]].append(bombs[j])
        vis = set()
        def dfs(node):
            res = 0
            vis.add(node)
            for des in g[node]:
                if des not in vis:
                    res += (dfs(des)+c[des])
            return res
        res = 1
        for x in bombs:
            vis = set()
            res = max(res,dfs(x)+c[x])
        return res