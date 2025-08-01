class Solution:
    def smallestString(self, s: str) -> str:
        INF = 10**20
        last = -INF
        s = list(s)
        done = False
        for idx,val in enumerate(s):
            if val!='a' and ((not done) or (done and last==idx-1)):
                if not done:
                    done = True
                last = idx
                s[idx] = chr(ord(s[idx])-1)
        if not done:
            s[-1] = chr(((ord(s[-1])-ord('a'))-1)%26 + ord('a'))
        return ''.join(s)

