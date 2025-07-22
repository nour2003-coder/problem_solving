# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        m=0
        while(target>1):
            if maxDoubles > 0:
                if target % 2 ==0:
                    target//=2
                    maxDoubles-=1
                    m+=1
                else:
                    target-=1
                    m+=1
            else:
                m+=target-1
                target-=target-1

           
        return m