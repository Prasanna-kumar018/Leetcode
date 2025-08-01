class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        # if any edge has indegree 2 the answer is any one of these two edges or cycle edge
        # else find redundant edge for all nodes which has 1 as indegree 
        # by ufd(Cycle detection)
        parent={}
        def find(x):
            if x not in parent:
                parent[x]=x
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def uunion(a,b):
            x = find(a)
            y = find(b)
            parent[x]=y
            return [x,y]
        n = len(edges)
        indegree=[-1]*(n+1)
        a,b=-1,-1
        for i,(x,y) in enumerate(edges):
            if indegree[y]==-1:
                indegree[y]=i
            else:
                a=i
                b=indegree[y]
        # print(a,b)
        for i,(x,y) in enumerate(edges):
            if a==i:
                continue
            s,d= uunion(x,y)
            if s==d:
                if a==-1: # If All the edges have 1 as indegree cycle
                    return [x,y]
                else: # Even after removing one of the edges(a) still cycle occurs
                    return edges[b]  # b must be the answer 

        return edges[a] # Else a 