# Problem: Course Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    from collections import defaultdict
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        WHITE=1
        GRAY=2
        BLACK=3
        color={k:WHITE for k in range(numCourses)}
        is_possible=True
        d=defaultdict(list)
        for i in prerequisites:
            d[i[1]].append(i[0])

        def dfs(node):
            nonlocal is_possible
            if not(is_possible):
                return
            color[node]=GRAY
            if node in d:
                for neighbor in d[node]:
                    if color[neighbor] == WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == GRAY:
                        is_possible=False
            color[node]=BLACK
        for i in range(numCourses):
            if color[i] ==WHITE:
                dfs(i)
                if not(is_possible):
                    return False
        return True
