class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        N = len(nums)
        par = {}
        comp = 0
        def find(x):
            nonlocal comp
            if x not in par:
                par[x]=x
                comp += 1
            if par[x]!=x:
                par[x]=find(par[x])
            return par[x]
        def union(a,b):
            nonlocal comp
            a = find(a)
            b = find(b)
            if a==b:
                return 
            comp -=1
            par[a]=b
        count = 0
        for i in range(N):
            par = {} # Creating new DSU each time ...
            comp = 0
            vis = set()
            for j in range(i,N):
                find(nums[j])
                vis.add(nums[j])
                for k in [nums[j]-1,nums[j]+1]:
                    if k in vis:
                        union(k,nums[j])
                count += comp -1
        return count