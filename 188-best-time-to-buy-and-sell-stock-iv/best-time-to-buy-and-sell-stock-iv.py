class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        INF = 10**20
        buy = [-INF]*k
        sell = [0]*k
        for val in prices:
            for i in range(k):
                if i==0:
                    buy[0]=max(buy[0],-val)
                if i!=0:
                    buy[i]=max(buy[i],sell[i-1]-val)
                sell[i]=max(sell[i],buy[i]+val)
        return sell[-1]