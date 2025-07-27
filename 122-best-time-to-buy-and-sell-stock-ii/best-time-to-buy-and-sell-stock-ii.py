class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)
        for i in range(1,n):
            if prices[i]>prices[i-1]:
                res += (prices[i]-prices[i-1])
        return res