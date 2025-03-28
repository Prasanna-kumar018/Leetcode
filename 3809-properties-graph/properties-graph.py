class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
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
            par[a]=b
        for i in range(n):
            for j in range(i+1,n):
                if len(set(properties[i])&set(properties[j]))>=k:
                    union(i,j)
        s = set()
        for x in range(n):
            s.add(find(x))
        return len(s)