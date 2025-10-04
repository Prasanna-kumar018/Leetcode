class Solution:
    def minOperations(self, n: int) -> int:
        """
        2^3 - 1 = 2^2 + 2^1 + 2^0
        8   - 1 = (4 + 2 + 1) 

        add 1 and remove 8
        
        """
        res = 0
        while n>0:
            if (n &3 == 3):
                n+=1
                res +=1
            else:
                res += (n&1)
                n>>=1
        return res