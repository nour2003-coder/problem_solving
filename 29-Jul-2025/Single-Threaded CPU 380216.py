# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    import heapq
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks=sorted([(temp,idx,dur) for idx,(temp,dur) in enumerate(tasks)])
        i=0
        time=0
        res=[]
        h=[]
        n=len(tasks)
        while(i<n or h):
            if not(h) and time<tasks[i][0]:
                time=tasks[i][0]
            while(i<n and tasks[i][0]<=time):
                t,index,dur=tasks[i]
                heapq.heappush(h,(dur,index))
                i+=1
            if (h):
                dur,idx=heapq.heappop(h)
                res.append(idx)
                time+=dur
                
        return res