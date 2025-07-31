class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        edges.sort(key=lambda x: -x[2])
        """
        Assume initially all nodes are separate...
        """
        par = {}
        def find(x):
            if x not in par:
                par[x]=x
            if par[x]!=x:
                par[x]=find(par[x])
            return par[x]
        
        def union(x,y):
            x = find(x)
            y = find(y)
            if x==y:
                return False
            par[x]=y
            return True
        count = n
        for x,y,wt in edges:
            if union(x,y):
                count-=1
            if count<k:
                return wt
        return 0
       