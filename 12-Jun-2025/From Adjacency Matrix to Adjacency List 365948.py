# Problem: From Adjacency Matrix to Adjacency List - https://www.eolymp.com/en/contests/9060/problems/78603

# example below, replace it with your solution
from collections import defaultdict
n = int(input())
d=defaultdict(list)
j=0
for i in range(n):
    l=list(map(int,input().split()))
    g=[]
    for i in range(len(l)):
        if l[i] == 1:        
            g.append(str(i+1))
    ch=" ".join(g)
    print(str(sum(l))+" "+ch)





