# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        memo=[0]*m
        memo[0]=1
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] ==1:
                    memo[j]=0
                else:
                    if j > 0:
                        memo[j]+=memo[j-1]
        return memo[m-1]