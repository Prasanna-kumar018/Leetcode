class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n=len(parents)
        graph = [[] for i in range(n)]
        for idx,i in enumerate(parents):
            if i !=-1:
                graph[idx].append(i)
                graph[i].append(idx)
        res = collections.defaultdict(int)
        def dfs(node,par):
            nonlocal n,res
            t = []
            for x in graph[node]:
                if x!=par:
                    t.append(dfs(x,node))
            s = sum(t)+1
            t.append(n-s)
            # print(node,t)
            r = 1
            for x in t:
                r *= max(1,x)
            res[r]+=1
            return s
        dfs(0,-1)
        return res[max(res.keys())]
        