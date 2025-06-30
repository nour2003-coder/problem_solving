# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        r=len(isConnected)
        c=len(isConnected[0])
        visited=set()
        def dfs(node):
            visited.add(node)
            for j in range(c):
                if isConnected[node][j] ==1 and j not in visited:
                    dfs(j)
        s=0
        for i in range(r):
            if i not in visited:
                s+=1
                dfs(i)
        return s

