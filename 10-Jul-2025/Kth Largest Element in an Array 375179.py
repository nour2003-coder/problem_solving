# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h=[]
        for i in nums:
            heapq.heappush(h,i)
            if len(h)>k:
                heapq.heappop(h)
        return(h[0])