# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    from collections import defaultdict
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph=defaultdict(list)
        for e in employees:
            graph[e.id]=(e.importance,e.subordinates)
        res=0
        def dfs(node):
            nonlocal res
            imp,sub=graph[node]
            res+=imp
            for i in sub:
                dfs(i)
        dfs(id)
        return (res)




        