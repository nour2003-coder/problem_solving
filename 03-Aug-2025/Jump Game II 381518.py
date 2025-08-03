# Problem: Jump Game II - https://leetcode.com/problems/jump-game-ii/description/

class Solution:
    def jump(self, nums: List[int]) -> int:
        m=len(nums)
        goal=m-1
        n=m-2
        dp=[0]*m
        for i in range(n,-1,-1):
            min_=float("inf")
            for j in range(1,nums[i]+1):
                if i+j>m-1:
                    break
                min_=min(min_,dp[i+j]+1)
            dp[i]=min_
        return dp[0]
