class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        n = len(prices)
        s = []
        for idx,x in enumerate(prices):
            while s and prices[s[-1]]>=x:
                ind = s.pop()
                prices[ind]-=x
            s.append(idx)
        return prices