# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    from collections import defaultdict,deque
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        riches=[0]*len(quiet)
        d=defaultdict(list)
        for rich , poor in richer:
            d[rich].append(poor)
            riches[poor]+=1
        q=deque()
        res=[idx for idx in range(len(quiet))]
        for i in range(len(riches)):
            if riches[i] ==0:
                q.append(i)
        while(q):
            r=q.popleft()
            for nei in d[r]:
                if quiet[res[nei]] > quiet[res[r]]:
                    res[nei]=res[r]
                riches[nei]-=1
                if riches[nei] ==0:
                    q.append(nei)
        return res