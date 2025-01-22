class Solution:
    def maximumSwap(self, num: int) -> int:
        x=  [int(c) for c in str(num)]
        res = [-1]*len(x)
        val = -1
        d = float('-inf')
        for idx in range(len(x)-1,-1,-1):
            if x[idx]>d:
                d=x[idx]
                val = idx
            elif x[idx]<d:
                res[idx]=val
        print(res)
        for idx,val in enumerate(res):
            if val!=-1:
                x[idx],x[val]=x[val],x[idx]
                break
        return int(''.join(map(str,x)))
        