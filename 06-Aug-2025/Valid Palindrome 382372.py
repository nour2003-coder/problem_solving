# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=(s.split())
        ch="".join(l)
        s=""
        for i in ch:
            i=i.lower()
            if ord("a")<=ord(i)<=ord("z") or "0"<=i<="9":
                s+=i.lower()
        left,right=0,len(s)-1
        print(s)
        while(left<=right):
            if s[left] ==s[right]:
                left+=1
                right-=1
            else:
                return False
        return True