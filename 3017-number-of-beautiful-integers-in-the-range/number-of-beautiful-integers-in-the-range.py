class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        @cache
        def g(x,even,mod):
            odd = x-even
            if x==0:
                if even==0 and odd==0 and mod==0:
                    return 1
                return 0
            total = 0
            for i in range(10):
                if i%2==0:
                    total += g(x-1,even-1,(mod*10+i)%k)
                else:
                    total += g(x-1,even,(mod*10+i)%k)
            return total
        @cache
        def help(val):
            if val%2==1:
                return 0
            half = (val)//2
            total = 0
            for i in range(1,10):
                if i%2==0:
                    total += g(val-1,half-1,i%k)
                else:
                    total += g(val-1,half,i%k)
            return total
        def help2(val,count):
            s = str(count)
            length = val
            if val%2==1:
                return 0
            half = (val)//2
            @cache
            def go(x,even,isless,mod):
                total = 0
                odd = x-even
                if x==0:
                    if even==0 and odd==0 and mod==0:
                        return 1
                    return 0
                for i in range(10):
                    if isless:
                        if i%2==0:
                            total += go(x-1,even-1,isless,(mod*10+i)%k)
                        else:
                            total += go(x-1,even ,isless,(mod*10+i)%k)
                    elif i<=int(s[length-x]):
                        if i%2==0:
                            xs = True if i<int(s[length-x]) else False
                            total += go(x-1,even-1,xs,(mod*10+i)%k)
                        else:
                            xs = True if i<int(s[length-x]) else False
                            total += go(x-1,even,xs,(mod*10+i)%k)
                return total
            res = 0
            for i in range(1,int(s[0])+1):
                if i%2==0:
                    x = True if i<int(s[0]) else False
                    res += go(val-1,half-1,x,i%k)
                else:
                    x = True if i<int(s[0]) else False
                    res += go(val-1,half,x,i%k)
            go.cache_clear()
            return res

        @cache
        def f(count):
            total = 0
            length = len(str(count))
            for i in range(2,length):
                total += help(i)
            total += help2(length,count)
            return total
        return f(high)-f(low-1)