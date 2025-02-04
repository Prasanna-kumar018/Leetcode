class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k==0:
            return 0
        s = s+s
        n = len(s)
        l,r = 0,0
        d = collections.defaultdict(int)
        have = 0
        ans = float('inf')
        need= 3
        while l<=r and l<n:
            while have<need and r<n:
                d[s[r]]+=1
                if d[s[r]]==k:
                    have+=1
                r+=1
            if r-l<=n//2 and have>=need:
                # print(l,r)
                ans = min(ans,r)
                ans = min(ans,r-l+(n-r))
                if l==0 or (l>0 and l<n//2 and r>=(n//2)):
                    ans = min(ans,r-l)
                # print(ans)
            # print(d)
            d[s[l]]-=1
            if d[s[l]]==k-1:
                have-=1
            l+=1
        return ans if ans!=float('inf') else -1