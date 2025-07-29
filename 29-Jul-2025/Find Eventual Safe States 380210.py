# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        res=[]
        visited=[0]*n
        def dfs(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True
            visited[node] = 1
            for i in graph[node]:
                if not(dfs(i)):
                    return False
            visited[node] =2
            res.append(node)
            return True
        for i in range(n):
            if visited[i]==0:
                dfs(i)
        return sorted(res)