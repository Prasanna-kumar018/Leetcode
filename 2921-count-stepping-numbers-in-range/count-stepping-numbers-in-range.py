class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        MOD = 10**9 + 7
        low = int(low)
        low -=1
        low = str(low)
        @cache
        def go(vv,prev):
            if vv==0:
                return 1
            r = 0
            for i in range(10):
                if abs(prev-i)==1:
                    r += go(vv-1,i)
            return r
        @cache
        def help(v):
            res = 0
            for i in range(1,10):
                res += go(v-1,i)
            return res 
        
        

        def getLast(val):
            N = len(val)
            @cache
            def recur(idx,isless,prev):
                if idx==N:
                    return 1
                c = 0
                for i in range(10):
                    if abs(i-prev)==1:
                        if isless:
                            c += recur(idx+1,isless,i)
                        elif i<=int(val[idx]):
                            c += recur(idx+1,i<int(val[idx]),i)
                return c 
            t = 0
            for i in range(1,10):
                if i <= int(val[0]):
                    t += recur(1,i<int(val[0]),i)
            recur.cache_clear()
            return t 

        def get(val):
            n = len(val)
            total = 0
            for x in range(1,n):
                total += help(x)
            total += getLast(val)
            return total 
        return (get(high)-get(low))% MOD