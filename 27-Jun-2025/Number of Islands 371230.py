# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r=len(grid)
        c=len(grid[0])
        islands=0
        steps={(0,1),(1,0),(-1,0),(0,-1)}
        visited=set()
        def inbound(x,y):
            if not(0<=x<r) or not(0<=y<c):
                return False
            return True
        def dfs(node):
            if not(inbound(node[0],node[1])) or grid[node[0]][node[1]] =='0' or node in visited:
                return
            visited.add(node)
            for s in steps:
                u=(node[0]+s[0],node[1]+s[1])
                dfs(u)
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1' and (i,j) not in visited:
                    islands+=1
                    dfs((i,j))
        return islands
            
