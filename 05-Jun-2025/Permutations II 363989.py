# Problem: Permutations II - https://leetcode.com/problems/permutations-ii/description/

from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        c=Counter(nums)
        def helper(l):
            if len(nums) == len(l):
                res.append(l)
                return
            for i in c:
                if c[i]:
                    c[i]-=1
                    helper(l+[i])
                    c[i]+=1
        helper([])
        return res


