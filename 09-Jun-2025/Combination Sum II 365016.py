# Problem: Combination Sum II - https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def backtrack(l,index,s):
            if  s == target:
                res.append(l[:])
                return
            if s> target  :
                return
            for i in range (index,len(candidates)):
                if i>index and candidates[i] == candidates[i-1]:
                    continue
                l.append(candidates[i])
                backtrack(l,i+1,s+candidates[i])
                l.pop()
        backtrack([],0,0)
        return res