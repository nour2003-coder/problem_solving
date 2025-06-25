# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        c=len(grid[0])
        r=len(grid)
        max_=0
        visited=set()
        def dfs(node):
            if not(0<=node[0]<r) or not(0<=node[1]<c) or grid[node[0]][node[1]] == 0 or node in visited:
                return 0
            steps={(0,1),(1,0),(-1,0),(0,-1)}
            visited.add(node)
            area=1
            for i in steps:
                u=(node[0]+i[0],node[1]+i[1])
                area+=dfs(u)
            return area
        for i in range(r):
            for j in range(c):
                if (i,j) not in visited and grid[i][j] == 1:
                    max_=max(max_,dfs((i,j)))
        return max_