# Problem: From adjacency list to adjacency matrix - https://basecamp.eolymp.com/en/problems/3982

# example below, replace it with your solution
n = int(input())
M = [["0" for _ in range(n)] for _ in range(n)]
for i in range(n):
    l=list(map(int,input().split()))
    l=l[1:]
    if l:
        for j in l:      
            M[i][j-1]="1"

for i in M:
    print(" ".join(i)) 

