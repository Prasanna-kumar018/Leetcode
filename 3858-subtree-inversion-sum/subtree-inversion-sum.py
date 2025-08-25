class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(edges)+1
        g = collections.defaultdict(set)
        for x,y in edges:
            g[x].add(y)
            g[y].add(x)
        def go(node,par):
            g[node].discard(par)
            for des in g[node]:
                go(des,node)
        go(0,-1)
        INF = 10**20
        @cache
        def recur(node,dis,add):
            val = nums[node] if add else -nums[node]
            res = val
            for des in g[node]:
                v = -INF
                v = max(v, recur(des,max(0,dis-1),add))
                if dis==0:
                    v = max(v,recur(des,k-1, not add))
                res += v
            return res
        x = max(recur(0,0,True),recur(0,k-1,False))
        return x