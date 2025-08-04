# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[amount+1]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            for c in coins:
                if i-c>=0:
                    dp[i]=min(dp[i],1+dp[i-c])
        if dp[amount]==amount+1:
            return -1
        return dp[amount]

