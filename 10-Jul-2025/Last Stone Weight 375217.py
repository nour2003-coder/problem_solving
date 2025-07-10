# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[-i  for i in stones]
        heapq.heapify(heap)
        while(len(heap)>1):
            y=-heapq.heappop(heap)
            x=-heapq.heappop(heap)
            if y!=x:
                heapq.heappush(heap,-(y-x))
        if len(heap) == 1:
            return (-heap[0])
        return 0