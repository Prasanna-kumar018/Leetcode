class Solution:
    def numPermsDISequence(self, s: str) -> int:
        n  = len(s)
        mod = 10**9 + 7
        if n==1:
            return 1
        vis = set()
        @cache
        def recur(index,prev):
            if index==n:
                return 1
            total=0
            for x in range(n+1):
                if s[index]=='D' and x<prev and x not in vis:
                    vis.add(x)
                    total+=recur(index+1,x)
                    total%=mod
                    vis.discard(x)
                elif s[index]=='I' and x>prev and x not in vis:
                    vis.add(x)
                    total+=recur(index+1,x)
                    total%=mod
                    vis.discard(x)
            return total%mod
        res = 0
        for i in range(n+1):
            vis.add(i)
            res= (res+recur(0,i))%mod
            vis.discard(i)
        return res