# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        self.helper(res,n,0,0,"")
        return res
    def helper(self,res,n,opened,closed,ch):
        if len(ch) == 2*n:
            res.append(ch)
            return 
        if opened <n:
            self.helper(res,n,opened+1,closed,ch+"(")
        if closed<opened:
            self.helper(res,n,opened,closed+1,ch+")")
        