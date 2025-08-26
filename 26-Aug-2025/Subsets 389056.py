# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(l,start):
            res.append(l[:])
            for i in range(start,len(nums)):
                l.append(nums[i])
                backtrack(l,i+1)
                l.pop()
        backtrack([],0)
        return(res)