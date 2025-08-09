# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for i in range(amount+1)]
        dp[0]=1
        for c in coins:
            for i in range(amount+1):
                if i+c<=amount:
                    dp[i+c]+=dp[i]

        return dp[amount]