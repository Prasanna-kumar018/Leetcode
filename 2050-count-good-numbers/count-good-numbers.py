class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        if n==0:
            return 0
        even = ((n+1)//2)
        odd = (n//2)
        def find(val,n):
            if n==1:
                return val
            if n==0:
                return 1 
            res = find(val,n//2)
            if n%2==0:
                res = (res*res)
            else:
                res = (res*res*val)
            return res%mod
        # return (find(5,even)*find(4,odd))%mod
        return (pow(5,even,mod)*pow(4,odd,mod))%mod
