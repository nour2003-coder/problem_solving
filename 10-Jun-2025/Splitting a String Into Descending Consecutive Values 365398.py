# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(index: int, prev: int, count: int) -> bool:
            if index == len(s):
                return count >= 2  

            for i in range(index + 1, len(s) + 1):
                curr = int(s[index:i])
                if prev is None or prev - 1 == curr:
                    if backtrack(i, curr, count + 1):
                        return True
            return False

        return backtrack(0, None, 0)
