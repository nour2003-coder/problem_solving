# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    import heapq
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=Counter(nums)
        l=[]
        for i in d:
            heapq.heappush(l,(d[i],i))
            if len(l)>k:
                heapq.heappop(l)
        l1=[]
        n=len(l)
        for i in range(n-1,-1,-1):
            l1.append(l[i][1])
        return(l1)
"""         d=[(value,key) for (key,value) in d.items()]
        d.sort(reverse=True)
        l=[]
        for i in range(k):
            l.append(d[i][1]) """
