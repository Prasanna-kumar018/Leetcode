class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for x in range(low,high+1):
            x = list(map(int,str(x)))
            n = len(x)
            if n%2==0:
                res += 1 if (sum(x[:n//2])==sum(x[-(n//2):])) else 0
        return res