# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.' for _ in range(n)] for _ in range(n)]
        cols=set()
        leftdiag=set()
        rightdiag=set()
        res=[]
        def backtrack(rows):
            if rows == n:
                res.append(["".join(x) for x in board])
                return
            
            for col in range(n):
                if col in cols or rows-col in rightdiag or rows+col in leftdiag:
                    continue
                board[rows][col]='Q'
                cols.add(col)
                leftdiag.add(rows+col)
                rightdiag.add(rows-col)
                backtrack(rows+1)
                board[rows][col]='.'
                cols.remove(col)
                leftdiag.remove(rows+col)
                rightdiag.remove(rows-col)
        backtrack(0)
        return res