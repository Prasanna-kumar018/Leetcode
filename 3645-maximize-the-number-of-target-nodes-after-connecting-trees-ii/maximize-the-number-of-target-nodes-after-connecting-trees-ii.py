class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        lookup = collections.defaultdict(list)
        look   = collections.defaultdict(list)
        for x,y in edges1:
            look[x].append(y)
            look[y].append(x)
        n = len(edges1)+1
        for x,y in edges2:
            lookup[x].append(y)
            lookup[y].append(x)
        m = len(edges2)+1
        def recur(par,dep,node):
            best = 0
            child = 0
            for x in lookup[node]:
                if x!=par:
                    best+=1
                    child+=recur(node,dep+1,x)
            return best+child if dep%2==0 else child # max()
        x = recur(-1,0,0)
        add = max(x,m-x)
        odd = set()
        def recur2(par,dep,node):
            best = 0
            if dep%2 == 1:
                odd.add(node)
            child = 0
            for x in look[node]:
                if x!=par:
                    best+=1
                    child+=recur2(node,dep+1,x)
            return best+child if dep%2==0 else child
        oddval = recur2(-1,0,0)
        evenval = n-oddval
        res = [add]*n
        for i in range(n):
            if i in odd:
                res[i]+=oddval
            else:
                res[i]+=evenval
        return res