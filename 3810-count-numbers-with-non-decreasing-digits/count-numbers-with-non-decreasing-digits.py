class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        MOD = 10**9 + 7
        def conv(val):
            nonlocal b
            val = int(val)
            s = []
            while val>0:
                s.append(str(val%b))
                val //= b
            s.reverse()
            return ''.join(s)
        l,r = conv(str(int(l)-1)),conv(r)
        def go(val):
            nonlocal b
            N = len(val)
            @cache
            def recur(idx,isless,prev):
                if idx==N:
                    return 1
                x = int(val[idx])
                end = b if isless else x+1
                res = 0
                for i in range(end):
                    if prev==-1 or prev<=i:
                        v = bool(i<x)
                        res += recur(idx+1,isless or v,-1 if i==0 and prev==-1 else i)
                return res
            x = recur(0,False,-1)
            return x

        return (go(r)-go(l))% MOD