class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = 10**20
        @cache
        def recur(val):
            if val<0:
                return INF
            if val==0:
                return 0
            res = INF
            for x in coins:
                res = min(res,recur(val-x)+1)
            return res
        x = recur(amount)
        return x if x!=INF else -1