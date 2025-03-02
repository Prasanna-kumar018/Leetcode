class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9+7
        n = len(s)
        # @cache
        # def recur(idx):
        #     if idx==n:
        #         return 1
        #     res = 2*recur(idx+1)
        #     for i in range(idx+1,n):
        #         if s[i]==s[idx]:
        #             res -= recur(i+1)
        #             break
        #     return res
        # return (recur(0)-1)%MOD
        """
        aba

        a  - 1

        b  - 1 + a(1)  == 2
             b , ba
        a = 1 + b(2)+ a(1) ==> 4
            a , ab, aba, aa

            Add a to empty string  or
            all the characters....
        """

        add = {}
        for x in range(26):
            add[chr(x+ord('a'))]=0
        for x in s[::-1]:
            add[x]=sum(add.values())+1
        return sum(add.values())%MOD