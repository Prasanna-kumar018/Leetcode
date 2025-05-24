class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        l,r = 0,0
        alpha = [0]*26
        def isgood():
            for x in alpha:
                if x>=k:
                    return True
            return False
        res = 0
        while l<n:
            while r<n and not isgood():
                ind = ord(s[r])-ord('a')
                alpha[ind]+=1
                r+=1
            if isgood():
                res+=(n-r+1)
            ind = ord(s[l])-ord('a')
            alpha[ind]-=1
            l+=1
        return res        