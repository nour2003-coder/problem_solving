# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        max_=0
        for i in range(len(nums)-1,1,-1):
            if nums[i]<nums[i-2]+nums[i-1]:
                max_=max(max_,nums[i-2]+nums[i]+nums[i-1])
        return(max_)