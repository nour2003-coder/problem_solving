# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF  
        MAX_INT = 0x7FFFFFFF  

        x = a & MASK
        y = b & MASK

        while y != 0:
            car = (x & y) << 1
            x = x ^ y
            y = car & MASK  

        
        return x if x <= MAX_INT else ~(x ^ MASK)
