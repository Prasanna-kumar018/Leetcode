class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def go(v):
            if v%2==1:
                return 0
            aa = v//2
            @cache
            def help(idx,s):
                nonlocal aa
                if idx==0:
                    if s==0:
                        return 1
                    return 0
                res  =0 
                print(idx,s)
                for i in range(10):
                    val = -i if idx<=aa else i
                    res += help(idx-1,s+val)
                return res
            t = 0
            for i in range(1,10):
                t += help(v-1,i)
            return t

        def get(n,ee):
            aa = n//2
            @cache
            def help2(idx,s,isless):
                nonlocal ee,aa,n
                if idx==n:
                    if s==0:
                        return 1
                    return 0
                v = int(ee[idx])
                start =1  if idx==0 else 0
                res = 0
                for i in range(start,10):
                    val = i if idx<aa else -i
                    if isless:
                        res += help2(idx+1,s+val,isless)
                    elif i<=v:
                        f = True if i<v else False
                        res += help2(idx+1,s+val,f)
                return res
            x = help2(0,0,False)
            return x
        def f(val):
            val = str(val)
            x = len(val)
            total = 0
            for i in range(2,x):
                total += go(i)
            total+=get(x,val)
            return total
        return f(high)-f(low-1)