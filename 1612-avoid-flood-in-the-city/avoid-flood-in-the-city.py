class Solution:
    def avoidFlood(self, rain: List[int]) -> List[int]:
        n = len(rain)
        ans = [1]*n
        par = {}
        def find(x):
            if x not in par:
                par[x]=x
            if x!=par[x]:
                par[x]=find(par[x])
            return par[x]
        
        def union(x):
            par[x]=find(x+1)

        d = {}
        for idx,val in enumerate(rain):
            if val!=0:
                union(idx)
                ans[idx]=-1
                if val in d:
                    prev = d[val]
                    ind = find(prev)
                    if ind>=idx:
                        return []
                    ans[ind]=val
                    union(ind)

                d[val]=idx
        return ans