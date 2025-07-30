# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        n=len(nums)
        def r(n):
            if n ==0:
                return nums[0]
            if n ==1:
                return max(nums[0],nums[1])
            if n not in memo:
                memo[n]=max(r(n-1),nums[n]+r(n-2))
                print(n,memo[n])
            return memo[n]
        if n==0:
            return  0
        return r(n-1)