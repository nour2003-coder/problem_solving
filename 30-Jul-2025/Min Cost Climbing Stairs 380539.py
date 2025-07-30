# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        pre,prepre=0,0
        n=len(cost)
        for i in range(2,n+1):
            cur=min(cost[i-1]+pre,cost[i-2]+prepre)
            prepre=pre
            pre=cur
        return cur
