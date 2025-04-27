class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        """
        1 - 001
        2 - 010
        3 - 011
        4 - 100
        5 - 101
        6 - 110
        7 - 111

        converted to 

        1 - 001
        2 - 001 (swapped with 5)
        3 - 001 (swapped with 4)
        4 - 110
        5 - 110
        6 - 110 2**p-2
        7 - 111 2**p-1  n= 3
        """
        MOD = 10**9+7
        return (pow(2**p-2,(2**p-2)//2,MOD)*(2**p-1))%  MOD