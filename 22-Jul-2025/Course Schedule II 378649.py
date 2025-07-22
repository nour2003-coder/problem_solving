# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    from collections import defaultdict,deque
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses=[0]*numCourses
        d=defaultdict(list)
        for i,j in prerequisites:
            courses[i]+=1
            d[j].append(i)
        q=deque()
        for i in range(numCourses):
            if courses[i] ==0:
                q.append(i)
        orders=[]
        while(q):
            c=q.popleft()
            print(c)
            orders.append(c)
            for nxt in d[c]:
                courses[nxt]-=1
                if courses[nxt] ==0:
                    print(nxt)
                    q.append(nxt)
        if len(orders)<numCourses:
            return []
        return orders