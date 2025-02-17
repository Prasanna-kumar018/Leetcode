class Solution:
    def punishmentNumber(self, n: int) -> int:
        # print(37*37)
        def isSafe(start,s,val):
            if val<0:
                return False
            if start==len(s):
                if val==0:
                    return True
                return False
            for j in range(start+1,len(s)+1):
                if isSafe(j,s,val-int(s[start:j])):
                    return True
            return False
        res = 0
        for i in range(1,n+1):
            if isSafe(0,str(i*i),i):
                # print(i)
                res+= (i*i)
        return res