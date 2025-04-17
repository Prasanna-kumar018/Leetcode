class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        parent = {}
        """
        t a r s
        r a t s
        a[0]   b[0]
        a[1]   b[1]
        """
        def find(x):
            if x not in parent:
                parent[x]=x
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def ufind(x,y):
            a = find(x)
            b = find(y)
            parent[a]=b

        n= len(strs)
        for i in range(n):
            for j in range(i+1,n):
                a,b = None,None
                count = 0
                for (x,y) in zip(strs[i],strs[j]):
                    if x!=y:
                        if not a:
                            a= [x,y]
                        else:
                            b =[x,y]
                        count+=1
                if count==0 or  (count==2 and a and b and (a[0]==b[1]) and (a[1]==b[0])):
                    ufind(i,j)
        count = collections.defaultdict(int)
        for i in range(n):
            count[find(i)]+=1
        return len(count)