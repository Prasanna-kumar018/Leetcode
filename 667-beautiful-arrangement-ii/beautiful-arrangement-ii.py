class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = []
        s,e = 1,n
        isstart = True
        while k>0:
            if isstart:
                res.append(s)
                s+=1
            else:
                res.append(e)
                e-=1
            k-=1
            isstart= not isstart
        if not  isstart:
            res.extend([i for i in range(s,e+1)])
        else:
            res.extend([i for i in range(e,s-1,-1)])
        return res