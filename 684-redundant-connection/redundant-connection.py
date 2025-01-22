class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        g = collections.defaultdict(list)
        n = 0
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
        INF = 10**20
        lt = collections.defaultdict(lambda :INF)
        idx = 0
        res = set()
        def arti(start,par):
            nonlocal idx,res
            lt[start]=idx
            idx+=1
            for neigh in g[start]:
                if neigh==par:
                    continue
                if lt[neigh]==INF:
                    arti(neigh,start)
                    if lt[neigh]<=lt[start]:
                        lt[start]=lt[neigh]
                        res.add((start,neigh)) 
                elif lt[neigh]<lt[start]:
                    lt[start]=lt[neigh]
                    res.add((start,neigh)) 
        arti(1,-1)
        for x,y in edges[::-1]:
            if (x,y) in res or (y,x) in res:
                return [x,y]
        return [] # dummy