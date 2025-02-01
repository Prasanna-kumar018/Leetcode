class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        for x,y in connections:
            g[x].append((y,0))
            g[y].append((x,1))
        ans = 0
        def dfs(start,par):
            nonlocal ans
            for des,wt in g[start]:
                if des!=par:
                    ans+=(1-wt)
                    dfs(des,start)
        dfs(0,-1)
        return ans