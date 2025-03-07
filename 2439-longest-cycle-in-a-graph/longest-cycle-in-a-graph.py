class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        depth = {}
        vis = collections.defaultdict(lambda :-1)
        # -1 :unvisited, 1-visited, 2 - currently visiting....
        res = -1
        def dfs(node,dep):
            nonlocal res
            depth[node]=dep
            vis[node]=2
            des = edges[node]
            if des !=-1:
                if vis[des]==-1:
                    dfs(des,dep+1)
                elif vis[des]==2:
                    res = max(res,abs(dep+1-depth[des]))
            vis[node]=1
        for idx,val in enumerate(edges):
            if vis[idx]==-1:
                dfs(idx,0)
        return res