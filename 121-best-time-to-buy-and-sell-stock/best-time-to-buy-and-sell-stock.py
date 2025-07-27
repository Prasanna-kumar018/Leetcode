class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        INF = 10**20
        buy = -INF
        sell = -INF
        for idx,val in enumerate(prices):
            buy = max(buy, -val)
            sell = max(sell,buy+val)
        return sell