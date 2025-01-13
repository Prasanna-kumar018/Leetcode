class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        parent= {}
        def find(x):
            if x not in parent:
                parent[x]=x
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        
        def union(a,b):
            x = find(a)
            y = find(b)
            parent[x]=y
        
        for i in range(0,n,2):
            a,b = row[i]//2,row[i+1]//2
            if a!=b:
                union(a,b)
        count = 0
        for i in range(n//2):
            if find(i)!=i:
                count+=1

        return count