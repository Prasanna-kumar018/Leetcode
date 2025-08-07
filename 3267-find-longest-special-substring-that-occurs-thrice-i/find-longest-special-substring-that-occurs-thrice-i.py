class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        MOD = 10**12 + 7
        def isSafe(ll,char):
            need = 0
            d = 26
            for x in range(ll):
                need = ((need*d) + (char+97)) % MOD
            dd = collections.defaultdict(int)
            hashh = 0
            l,r = 0,0
            while r<ll:
                hashh = ((hashh * d) + ord(s[r])) % MOD
                r+=1
            # print(hashh,need)
            if hashh == need:
                dd[hashh]+=1
            XX = pow(d,ll-1,MOD)
            while r<n:
                hashh = (hashh - (XX*ord(s[l]))) % MOD
                hashh = (hashh * d) % MOD
                hashh = (hashh + ord(s[r])) % MOD
                # print("loop",i,hashh,need)
                if hashh == need:
                    dd[hashh]+=1
                l+=1
                r+=1
            # print(dd,char,ll, max(dd.values()) if dd else 0)
            return ( max(dd.values()) if dd else 0)>=3
        ans = -1
        for i in range(26):
            l,r = 1,n
            res = -1
            while l<=r:
                mid = (l+r)//2
                if isSafe(mid,i):
                    l = mid+1
                    res = mid
                else:
                    r = mid-1
            ans = max(res,ans)
        return ans