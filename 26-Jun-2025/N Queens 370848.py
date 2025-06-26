# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        cols=set()
        rightdiag=set()
        leftdiag=set()
        res=[]
        def backtrack(level):
            nonlocal res
            if level == n:
                res.append(["".join(x) for x in board])
                return
            for col in range(n):
                if col in cols or level-col in rightdiag or level+col in leftdiag:
                    continue
                board[level][col]='Q'
                cols.add(col)
                rightdiag.add(level-col)
                leftdiag.add(level+col)
                backtrack(level+1)
                board[level][col]='.'
                cols.remove(col)
                rightdiag.remove(level-col)
                leftdiag.remove(level+col)            
        backtrack(0)
        return res