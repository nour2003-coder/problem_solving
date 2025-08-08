# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        memo={}
        def dfs(i,j):
            if not(0<=i<n) or not(0<=j<n) :
                return float("inf")
            if i == n-1:
                return matrix[i][j]
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)]=matrix[i][j]+min(dfs(i+1,j-1),dfs(i+1,j),dfs(i+1,j+1))
            return memo[(i,j)]
        min_=float('inf')
        for j in range(n):
            min_=min(min_,dfs(0,j))
        return min_