# Problem: Find K Pairs with Smallest Sums - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

class Solution:
    import heapq
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res=[]
        pairs=[]
        for x in nums1:
            heapq.heappush(pairs,[nums2[0]+x,0])
        while(k>0 and pairs):
            pair=heapq.heappop(pairs)
            s,pos=pair[0],pair[1]
            res.append([s-nums2[pos],nums2[pos]])
            if pos+1<len(nums2):
                heapq.heappush(pairs,[s-nums2[pos]+nums2[pos+1],pos+1])
            k-=1
        return res
        
