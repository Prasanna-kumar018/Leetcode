class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        n = len(s)
        d = collections.Counter(s)
        s = list(s)
        res= 0
        x,y = 0,0
        t= k
        for idx,val in enumerate(s):
            if s[idx]=='N':
                y+=1
            elif s[idx]=='E':
                x+=1
            elif s[idx]=='W':
                if t>0:
                    t-=1
                    x+=1
                else:
                    x-=1
            else:
                if t>0:
                    t-=1
                    y+=1
                else:
                    y-=1
            res = max(res,abs(x)+abs(y))
        x,y = 0,0
        t= k
        res2 = 0
        for idx,val in enumerate(s):
            if s[idx]=='N':
                y+=1
            elif s[idx]=='E':
                if t>0:
                    t-=1
                    x-=1
                else:
                    x+=1
            elif s[idx]=='W':
                x-=1
            else:
                if t>0:
                    t-=1
                    y+=1
                else:
                    y-=1
            res2 = max(res2,abs(x)+abs(y))
        x,y = 0,0
        t= k
        res3 = 0
        for idx,val in enumerate(s):
            if s[idx]=='N':
                if t>0:
                    t-=1
                    y-=1
                else:
                    y+=1
            elif s[idx]=='E':
                if t>0:
                    t-=1
                    x-=1
                else:
                    x+=1
            elif s[idx]=='W':
                x-=1
            else:
                y-=1
            res3 = max(res3,abs(x)+abs(y))
        x,y = 0,0
        t= k
        res4 = 0
        for idx,val in enumerate(s):
            if s[idx]=='N':
                if t>0:
                    t-=1
                    y-=1
                else:
                    y+=1
            elif s[idx]=='E':
                x+=1
            elif s[idx]=='W':
                if t>0:
                    t-=1
                    x+=1
                else:
                    x-=1
            else:
                y-=1
            res4 = max(res4,abs(x)+abs(y))
        return max(res,res2,res3,res4)
    