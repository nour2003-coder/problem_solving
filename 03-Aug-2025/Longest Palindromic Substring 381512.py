# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxlen = 0
        res = ""

        def palindrome(r, l):
            nonlocal maxlen, res
            while r < n and l >= 0 and s[l] == s[r]:
                if maxlen < r - l + 1:
                    maxlen = r - l + 1
                    res = s[l:r+1]
                r += 1
                l -= 1

        for i in range(n):
            palindrome(i, i)     
            palindrome(i+1, i)   

        return res

        
