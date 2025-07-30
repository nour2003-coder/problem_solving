# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo={}
        def climb(n):
            if n<=0:
                return 0
            if n not in memo: 
                memo[n]=min(cost[n]+climb(n-1),cost[n-1]+climb(n-2))
            return memo[n]
        n=len(cost)
        climb(n-1)
        return memo[n-1]