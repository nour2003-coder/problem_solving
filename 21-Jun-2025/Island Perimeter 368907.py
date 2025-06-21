# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        visited=set()
        s=0
        def dfs(node):
            nonlocal s
            if not(0<=node[0]<r) or not(0<=node[1]<c) or grid[node[0]][node[1]] ==0 :
                s+=1
                return
            if   node in visited:
                return
            step={(0,1),(1,0),(-1,0),(0,-1)}
            visited.add(node)
            
            for i,j in step:
                u=(node[0]+i,node[1]+j)
                dfs(u)
        for i in range(r):
                for j in range(c):
                    if grid[i][j] == 1:
                        dfs((i,j))
        return s
    