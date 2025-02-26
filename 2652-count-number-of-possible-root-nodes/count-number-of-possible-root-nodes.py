class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        n = len(edges)+1
        g = collections.defaultdict(list)
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
        
        lookup = set()
        for x,y in guesses:
            lookup.add((x,y))

        count = [0]*n
        def dfs(node,par):

            ans = 0
            for des in g[node]:
                if des!=par:
                    if (node,des) in lookup:
                        ans+=1
                    ans+=dfs(des,node)
            count[node]=ans
            return ans
        dfs(0,-1)
        def dfs2(node,par):
            for des in g[node]:
                if des!=par:
                    v = 0
                    if (node,des) in lookup:
                        v = 1
                    x = 0
                    if (des,node) in lookup:
                        x = 1
                    count[des]+= (count[node]-count[des]-v)+x   
                    dfs2(des,node)
        dfs2(0,-1)
        res =0 
        for x in count:
            if x>=k:
                res+=1
        return res