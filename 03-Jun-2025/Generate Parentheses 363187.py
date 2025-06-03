# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def helper(opened,closed,ch):
            if opened == 0 and closed == 0:
                res.append(ch)
                return 
            if opened >0 :
                helper(opened-1,closed,ch+"(")
            if closed>opened:
                helper(opened,closed-1,ch+")")
        helper(n-1,n,"(")
        return res
        