# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        states=[0]*n
        res=[]
        def dfs(node):
            if states[node] == 1:
                return False
            if states[node] == 2:
                return True
            states[node]=1
            for i in graph[node]:
                if not(dfs(i)):
                    return False
            states[node]=2
            res.append(node)
            return True
        for i in range(n):
            if states[i] == 0:
                dfs(i)
        return sorted(res)