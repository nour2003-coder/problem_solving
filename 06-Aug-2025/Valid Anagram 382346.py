# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d1=Counter(s)
        d2=Counter(t)
        for i in d1:
            if i not in d2:
                return False
            if d1[i] != d2[i]:
                return False
        return True
