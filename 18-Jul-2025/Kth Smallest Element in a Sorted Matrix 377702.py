# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    import heapq
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        m=len(matrix[0])
        l=[]
        for i in range(n):
            for j in range(m):
                heapq.heappush(l,matrix[i][j])
        i=0
        while(i<k-1):
            heapq.heappop(l)
            i+=1
        return(heapq.heappop(l))