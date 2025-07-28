# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        state=[0]*n
        res=[]
        def dfs(node):
            if state[node] ==1:
                return False
            if state[node] == 2:
                return True
            state[node] = 1
            for nei in graph[node]:
                if not(dfs(nei)):
                    return False
            state[node] = 2
            res.append(node)
            return True
        
        for i in range(n):
            if state[i] == 0:
                dfs(i)
        return sorted(res)