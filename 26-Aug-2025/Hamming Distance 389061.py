# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x=bin(x)[2:]
        y=bin(y)[2:]
        n,m=len(x),len(y)
        if n>m:
            y="0"*(n-m)+y
        else:
            x="0"*(m-n)+x
        m=max(n,m)
        s=0
        for i in range(m):
            if x[i]!=y[i]:
                s+=1
        return s
        