# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_=0
        n=len(height)
        left=0
        right=n-1
        while(left<right):
            area=(right-left)*min(height[left],height[right])
            
            max_=max(max_,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_