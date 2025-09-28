class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        l,r = 0,0
        n = len(s)
        have = 0
        res = 0
        while r<n:
            while l<r and have>1:
                if s[l]==s[l+1]:
                    have-=1 
                l+=1
            res = max(res,r-l+1)
            if r+1<n and s[r]==s[r+1]:
                have+=1
            r+=1
        return res