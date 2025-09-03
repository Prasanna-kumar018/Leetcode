class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = {}
        def find(x):
            if x not in par:
                par[x]=x
            if par[x]!=x:
                par[x]=find(par[x])
            return par[x]
        def union(a,b):
            a = find(a)
            b = find(b)
            if a==b:
                return True
            par[a]=b
            return False
        
        for x,y in edges:
            if union(x,y):
                return [x,y]
        return [-1,-1]