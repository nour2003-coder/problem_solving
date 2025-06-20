# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r=len(grid)
        c=len(grid[0])
        visited=set()
        islands=0
        def dfs(node):
            if not(0<=node[0]<r) or not(0<=node[1]<c) or grid[node[0]][node[1]] == '0' or (node[0],node[1]) in visited:
                return 
            steps={(0,1),(1,0),(-1,0),(0,-1)}
            visited.add((node[0],node[1]))
            for s in steps:
                u=(node[0]+ s[0],node[1]+s[1])
                dfs(u)

        for i in range(r):
            for j in range(c):
                if (i,j) not in visited and grid[i][j] == '1':
                    islands+=1
                    dfs((i,j))
        return islands
