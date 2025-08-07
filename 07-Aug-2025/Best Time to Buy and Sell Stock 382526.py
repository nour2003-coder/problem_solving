# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        left=0
        maxprofit=0
        for right in range(1,len(prices)):
            while(prices[left]>prices[right]):
                left+=1
            maxprofit=max(maxprofit,prices[right]-prices[left])
        return maxprofit