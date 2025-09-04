class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        MOD = 10**9 + 7
        def get(val):
            N = len(val)
            @cache
            def recur(idx,isless,prev):
                if idx==N:
                    return 1
                c = 0
                x = int(val[idx])
                end = 10 if isless else x+1 
                for i in range(end):
                    if prev==-1 or abs(i-prev)==1 :
                        v = bool(i<x)
                        c += recur(idx+1,v or isless,-1 if i==0 and prev==-1 else i)
                return c 
            t = recur(0,False,-1)
            return t 
        return (get(high)-get(str(int(low)-1)))% MOD