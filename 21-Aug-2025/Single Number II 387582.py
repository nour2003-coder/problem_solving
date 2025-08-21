# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    from collections import Counter
    def singleNumber(self, nums: List[int]) -> int:
        c=Counter(nums)
        for i in c:
            if c[i] ==1:
                return i
        