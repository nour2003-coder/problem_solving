# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        r, c = len(board), len(board[0])
        visited = set()
        steps = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def inbound(x, y):
            return 0 <= x < r and 0 <= y < c

        def dfs(x, y):
            if (x, y) in visited or not inbound(x, y) or board[x][y] != 'O':
                return
            visited.add((x, y))
            board[x][y] = 'T'  
            for dx, dy in steps:
                dfs(x + dx, y + dy)

        for i in range(r):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][c - 1] == 'O':
                dfs(i, c - 1)

        for j in range(c):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[r - 1][j] == 'O':
                dfs(r - 1, j)


        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
