class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        d = {'Q':0,'W':0,'E':0,'R':0}
        need = n//4
        for c in s:
            d[c]+=1
        # for 0
        res = True
        for y in d.values():
            if y!=need:
                res = False
        if res: return 0
        l,r = 0,0
        def issafe():
            nonlocal d
            res = True
            for x,y in d.items():
                if y>need:
                    res = False
            return res
        res = 10**20
        while r<n:
            d[s[r]]-=1
            while issafe() and l<=r:
                # print(d,l,r)
                res = min(res,r-l+1)
                d[s[l]]+=1
                l+=1
            r+=1
        return res