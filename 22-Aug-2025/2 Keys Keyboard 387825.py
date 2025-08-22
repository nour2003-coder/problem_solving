# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:
        current=1
        copied=0
        s=0
        while current !=n:
            if n % current ==0:
                copied=current
                s+=1
            current+=copied
            s+=1
        return s