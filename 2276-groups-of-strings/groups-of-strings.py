class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        par = {}
        size = {}
        def find(x):
            if x not in par:
                par[x]=x
                size[x]=1
            if par[x]!=x:
                par[x]=find(par[x])
            return par[x]
        
        def union(x,y):
            x = find(x)
            y = find(y)
            if x==y:
                return
            par[x]=y
            size[y]+=size[x]
        
        def get(w):
            mask = 0
            for c in w:
                c = ord(c)-ord('a')
                mask |= (1<<c)
            return mask
        N = 26
        s = set()
        deleted = collections.defaultdict(int) # for replace alone
        """
        Replacing exactly one letter from the set of the letters of s1 with any letter, including itself.
        this will cover the exact same string
        abc eg: replacing b with b
        abc

        replace is nothing but two deletions
        abc-> axc -> to replace b with x
        remove b from abc -> ac
        remove x from axc -> ac
        """
        for x in words:
            mask = get(x)

            for i in range(N):
                isdeleted = False
                if (mask&(1<<i) > 0):
                    isdeleted = True
                nmask = mask^(1<<i)
                if nmask in s:
                    union(nmask,mask)
                if isdeleted:
                    if nmask in deleted:
                        union(deleted[nmask],mask)
                    deleted[nmask]=mask
            s.add(mask)

        d = collections.defaultdict(int)
        for x in words:
            mask = get(x)
            d[find(mask)]+=1
        # return [len(d),ss] # won't work because the parent contains only the unique words but the same word may occur for multiple times
        return [len(d),max(d.values())]