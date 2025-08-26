# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    from collections import Counter
    def singleNumber(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        s=set(nums)
        res=[]
        for i in s:
            if c[i] !=2:
                res.append(i)
        return res