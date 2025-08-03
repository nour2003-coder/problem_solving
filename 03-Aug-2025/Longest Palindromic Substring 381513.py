# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        res=""
        maxlen=0
        def palindrome(l,r):
            nonlocal res,maxlen
            while(r<n and l>=0 and s[l] ==s[r]):
                if r-l+1>maxlen:
                    res=s[l:r+1]
                    maxlen=r-l+1
                r+=1
                l-=1
        for i in range(n):
            palindrome(i,i)
            palindrome(i,i+1)
        return res