# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        M = [[0 for _ in range(n)] for _ in range(n)]
        for i in trust:
            M[i[0]-1][i[1]-1]=1
        judge=-1
        for i in range(len(M)):
                if sum(M[i])==0 and sum(M[j][i] for j in range(n)) == n-1:
                    judge=i+1
        return(judge)

