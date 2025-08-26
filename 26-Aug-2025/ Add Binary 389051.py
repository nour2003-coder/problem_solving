# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        r=0
        ch=""
        n=len(a)
        m=len(b)
        if m>n:
            a="0"*(m-n)+a
        elif n>m:
            b="0"*(n-m)+b
        m=max(n,m)
        for i in range(m-1,-1,-1):
                sum=int(a[i])+int(b[i])+r
                if sum == 2:
                    r=1
                    ch="0"+ch
                elif sum ==3:
                    ch="1"+ch
                    r=1
                else:
                    r=0
                    ch=str(sum)+ch
        if r==1:
            ch="1"+ch
        return ch