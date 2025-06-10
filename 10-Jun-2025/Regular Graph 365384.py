# Problem: Regular Graph - https://basecamp.eolymp.com/en/problems/5076

n,m=map(int,input().split())
l=[0]*n
for i in range(m):
    i,j=map(int,input().split())
    l[i-1]+=1
    l[j-1]+=1
test=True
for i in range (1,len(l)):
    if l[i-1]!=l[i]:
        test=False
        break
if test:
    print("YES") 
else:
    print("NO")