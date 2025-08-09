class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        """
        (a XOR x) * (b XOR x) = (a*b) XOR x   -> Not correct

        n represent number of bits
        """
        MOD = 10**9 + 7
        s = []
        for x in range(n):
            x = (1<<x)
            if (a^x)*(b^x) > a * b:
                a ^= x
                b ^= x
        return (a*b)% MOD