# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    from collections import Counter
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtrack(l,index,s):
            if  s == target:
                print(l)
                res.append(l[:])
                return
            if s> target or index>=len(candidates):
                return
            l.append(candidates[index])
            backtrack(l,index,s+candidates[index])
            l.pop()
            backtrack(l,index+1,s)
        backtrack([],0,0)
        return res