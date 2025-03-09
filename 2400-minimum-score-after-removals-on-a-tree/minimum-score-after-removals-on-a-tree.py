class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
        n = len(nums)
        exor = [0]*(n)
        def go(node,par):
            curr = nums[node]
            for des in g[node]:
                if des!=par:
                    curr = curr ^ go(des,node)
            exor[node]=curr
            return curr
        go(0,-1)
        par = [None]*n
        def go2(node,parent):
            curr = set([node])
            for des in g[node]:
                if des!=parent:
                    curr |= go2(des,node)
            par[node]=curr
            return curr
        go2(0,-1)
        best = 10**20
        for i in range(1,n):
            for j in range(i+1,n):
                a,b,c = 0,0,0
                if j in par[i]:
                    a = exor[0]^exor[i]
                    b = exor[i]^exor[j]
                    c = exor[j]
                elif i in par[j]:
                    a = exor[0]^exor[j]
                    b = exor[j]^exor[i]
                    c = exor[i]
                else:
                    a = exor[0]^exor[j]^exor[i]
                    b = exor[j]
                    c = exor[i]
                best = min(best,max(a,b,c)-min(a,b,c))
        return best