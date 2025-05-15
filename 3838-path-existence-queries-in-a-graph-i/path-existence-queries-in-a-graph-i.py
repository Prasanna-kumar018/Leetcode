class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
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
        for i in range(n-1):
            if abs(nums[i]-nums[i+1])<=maxDiff:
                union(i,i+1)
        res = []
        for x,y in queries:
            res.append(find(x)==find(y))
        return res