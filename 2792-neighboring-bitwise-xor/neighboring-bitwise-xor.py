class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        res = [0]*n
        for i in range(n-1):
            if derived[i]==1:
                res[i+1]=1-res[i]
            else:
                res[i+1]=res[i]
        if derived[-1]==0:
            if res[0]!=res[-1]:
                return False
        else:
            if res[0]==res[-1]:
                return False
        return True
