class Solution:
    def countDigitOne(self, n: int) -> int:
        n = str(n)
        xx = len(n)
        @cache
        def help(val):
            if val==0:
                return (1,0)
            a = 0
            b = 0
            for x in range(10):
                v =  help(val-1)
                a+=v[0]
                b+=v[1]
                if x==1:
                    b+=(v[0])
            return (a,b)
            
        def get(val):
            a = 0
            b = 0
            for x in range(1,10):
                v =  help(val-1)
                a+=v[0]
                b+=v[1]
                if x==1:
                    b+=(v[0])
            return (a,b)
        @cache
        def gethelp(idx,isless):
            if idx==xx:
                return (1,0)
            a = 0
            b = 0
            for x in range(10):
                if isless:
                    v =  gethelp(idx+1,isless)
                    a+=v[0]
                    b+=v[1]
                    if x==1:
                        b+=(v[0])
                elif x<=int(n[idx]):
                    vv = True if x< int(n[idx]) else False
                    v =  gethelp(idx+1,vv)
                    a+=v[0]
                    b+=v[1]
                    if x==1:
                        b+=(v[0])
            return (a,b)

        def getlast(idx,isless):
            a = 0
            b = 0
            for x in range(1,10):
                if isless:
                    v =  gethelp(idx+1,isless)
                    a+=v[0]
                    b+=v[1]
                    if x==1:
                        b+=(v[0])
                elif x<=int(n[idx]):
                    vv = True if x< int(n[idx]) else False
                    v =  gethelp(idx+1,vv)
                    a+=v[0]
                    b+=v[1]
                    if x==1:
                        b+=(v[0])
            return (a,b)
        total = 0
        for i in range(1,xx):
            total += get(i)[1]
        total += getlast(0,False)[1]
        return total