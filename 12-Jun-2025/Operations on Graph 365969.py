# Problem: Operations on Graph - https://www.eolymp.com/en/contests/9060/problems/78602

# example below, replace it with your solution
n = int(input())
k = int(input())
d={i: [] for i in range(1,n+1)}
for _ in range(k):
    oper=list(map(int,input().split()))
    if oper[0] == 1:
        d[oper[1]].append(str(oper[2]))
        d[oper[2]].append(str(oper[1]))
    else:
        if d[oper[1]]:
            print(" ".join(d[oper[1]]))

