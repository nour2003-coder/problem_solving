# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal=len(nums)-1
        n=len(nums)-2
        for i in range(n,-1,-1):
            if i+nums[i]>=goal:
                goal=i
        if goal!=0:
            return False
        else:
            return True