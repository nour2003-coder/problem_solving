# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    import heapq
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexed_tasks = sorted([(t, dur, idx) for idx, (t, dur) in enumerate(tasks)])
        i = 0
        time = 0
        n = len(tasks)
        h = []
        res = []
        while i < n or h:
            if not h and time < indexed_tasks[i][0]:
                time = indexed_tasks[i][0]
            while i < n and indexed_tasks[i][0] <= time:
                t, dur, idx = indexed_tasks[i]
                heapq.heappush(h, (dur, idx)) 
                i += 1
            if h:
                dur, idx = heapq.heappop(h)
                time += dur
                res.append(idx)
        return res
