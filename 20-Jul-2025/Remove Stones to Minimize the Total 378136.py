# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    import heapq
    import math
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap=[-x for x in piles]
        heapq.heapify(heap)
        count=0
        while(count<k):
            s=heapq.heappop(heap)
            b=math.ceil(s/2)
            s-=b
            heapq.heappush(heap,s)
            count+=1
        return -sum(heap)