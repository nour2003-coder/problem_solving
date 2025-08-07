# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    from collections import defaultdict
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        num=k
        left=0
        max_=0
        count=defaultdict(int)
        m=0
        for r in range(n):
            count[s[r]]+=1
            max_=max(max_,count[s[r]])
            while r-left+1-max_>k :
                count[s[left]]-=1
                left+=1
            m=max(m,r-left+1)
        return m

