# Problem: Cities and Roads - https://www.eolymp.com/en/contests/9060/problems/78597

n = int(input())
s=0
for i in range(n):
    l=list(map(int,input().split()))
    s+=sum(l[i:])
print(s)