class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        MOD = 10**9 + 7
        left = target//2  
        if n<=left:
            v = min(left,n)
            return ((v*(v+1))//2)%MOD
        minus = ((target-1)*(target)//2) - (left*(left+1)//2)
        L = (target-1-left)
        return ((n+L)*(n+L+1)//2 - minus) % MOD