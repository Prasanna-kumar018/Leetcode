class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        n = len(strength)
        nse = [n]*n
        psee = [-1]*n
        MOD = 10**9 + 7
        s = []
        
        for idx,x in enumerate(strength):
            while s and strength[s[-1]] > x:
                ind = s.pop()
                nse[ind]=idx
            s.append(idx)

        s = []
        for idx in range(n-1,-1,-1):
            x = strength[idx]
            while s and strength[s[-1]] >= x:
                ind = s.pop()
                psee[ind]=idx
            s.append(idx)
        prefix = [strength[0]]
        for i in range(1,n):
            prefix.append(prefix[i-1]+strength[i])
        pre =  [prefix[0]]
        for i in range(1,n):
            pre.append(pre[i-1]+prefix[i])
        suffix = [strength[-1]]
        for idx in range(n-2,-1,-1):
            suffix.append(suffix[-1]+strength[idx])
        suffix.reverse()
        suff = [suffix[-1]]
        for idx in range(n-2,-1,-1):
            suff.append(suff[-1]+suffix[idx])
        suff.reverse()
        def get(l,r):
            if l>r:
                return 0
            return pre[r]-(pre[l-1] if l-1>=0 else 0)

        def getp(l,r):
            if l>r:
                return 0
            return prefix[r]-(prefix[l-1] if l-1>=0 else 0)

        def g(l,r):
            if l>r:
                return 0
            return suff[l]-(suff[r+1] if r+1<n else 0)

        def gs(l,r):
            if l>r:
                return 0
            return suffix[l]-(suffix[r+1] if r+1<n else 0)
        res = 0 
        print(psee,nse)
        for idx,val in enumerate(strength):
            left = idx-psee[idx]
            right = nse[idx]-idx
            ri = get(idx,nse[idx]-1) - (right*getp(0,idx-1))
            # for 0 length if we calculate the left prefix sum -> that is no need = negative values = so we take max(0,....)
            le = g(psee[idx]+1,idx-1) - ((left-1)*gs(idx,n-1))
            rr = ri*left
            ll = le*right
            res += (val*(ll+rr))
        return res % MOD