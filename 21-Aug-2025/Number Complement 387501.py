# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        ch1=bin(num)
        ch=""
        n=len(ch1)
        j=ch1.find("b")
        for i in range(j+1,n):
            a=1-int(ch1[i])
            ch+=str(a)
        return int(ch, 2)
        