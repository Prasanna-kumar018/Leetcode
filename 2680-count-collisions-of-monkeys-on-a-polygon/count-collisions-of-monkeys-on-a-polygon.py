class Solution:
    def monkeyMove(self, n: int) -> int:
        MOD = 10**9 + 7
        def p(left):
            if left==0:
                return 1
            x = p(left//2)
            if left%2==0:
                return (x*x) % MOD
            return (x*x*2) % MOD
        return ( p(n) - 2) % MOD