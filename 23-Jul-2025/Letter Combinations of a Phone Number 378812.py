# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        l=[]
        if not(digits):
            return []
        def comb(i=0,ch=""):
            if i == len(digits):
                l.append(ch)
                return
            for j in letters[digits[i]]:
                comb(i+1,ch+j)
        comb()
        return l

