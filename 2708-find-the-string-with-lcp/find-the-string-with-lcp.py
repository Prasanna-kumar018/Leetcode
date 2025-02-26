class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        parent = {}
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
        m = len(lcp)
        n = len(lcp)
        for i in  range(m):
            for j in range(i+1,n):
                if lcp[i][j]>0:
                    union(i,j)

        lookup = {}
        d = 0
        for i in range(n):
            x = find(i)
            if x not in lookup:
                lookup[x]=d
                d+=1

        if d>=27:
            return ''
        words = []
        for i in range(n):
            words.append(chr(ord('a')+lookup[find(i)]))
        INF = -10**20
        cache = [[-1]*(n) for _ in range(n)]
        def recur(x,y):
            if x==m or y==n:
                return 0
            if cache[x][y]!=-1:
                return cache[x][y]
            res = 0
            if words[x]==words[y]:
                res = max(res,1+recur(x+1,y+1))
            cache[x][y]=res
            return res
        for i in range(m):
            for j in range(n):
                recur(i,j)
        if cache==lcp:
            return ''.join(words)
        return ""