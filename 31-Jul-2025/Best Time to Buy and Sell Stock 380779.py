# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        maxProfit=0
        minprice=prices[0]
        for i in range(1,n):
            p=prices[i]-minprice
            if maxProfit<p:
                maxProfit=p
            else:
                if prices[i]<minprice:
                    minprice=prices[i]
        return maxProfit
