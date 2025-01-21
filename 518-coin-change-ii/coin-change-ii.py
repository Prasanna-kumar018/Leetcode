class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        @cache
        def recur(idx,val):
            if val<0:
                return 0
            if val==0:
                return 1
            if idx==n:
                return 0
            res = 0
            res += recur(idx+1,val)
            res += recur(idx,val-coins[idx])
            return res
        return recur(0,amount)