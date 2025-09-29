class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        res = [0]*n
        total = 0
        ans = []
        for x,y in queries:
            c = 0
            if x-1>=0 and res[x-1]==res[x] and res[x]!=0:
                c-=1
            if x+1<n and res[x+1]==res[x] and res[x]!=0:
                c-=1
            res[x]=y
            if x-1>=0 and res[x-1]==res[x] and res[x]!=0:
                c+=1
            if x+1<n and res[x+1]==res[x] and res[x]!=0:
                c+=1
            total += c
            ans.append(total)
        return ans