class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        n = len(binary)
        ones = 0 
        zeros = 0
        """
        101
        0 - 0
        1 - 0

        0 - 0
        1 - 1 // 1

        0 - 2  ("0","01")
        1 - 1 ("1")

        0 - 2
        1 - 4  ("1","11","10","101")
                "" -  1 -  0 
        """
        for x in binary[::-1]:
            if x=='0':
                zeros = zeros + ones + 1
            else:
                ones = ones  + zeros + 1
        MOD = 10**9+7
        ans = ones
        if binary.count('0')>0:
            ans+=1
        return ans%MOD