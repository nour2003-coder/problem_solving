# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    from collections import defaultdict
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        d=[0]*n
        for a,b in edges:
            d[b]+=1
        l=[]
        for i in range (len(d)) :
            if d[i] ==0:
                l.append(i)
        return l