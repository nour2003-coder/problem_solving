# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        s=set(nums)
        max_=0
        for i in s:
            if (i-1) not in s:
                j=i+1
                while(j in s):
                    j+=1
                max_=max(max_,j-i)
        return max_
                