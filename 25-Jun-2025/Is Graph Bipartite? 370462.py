# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        colors=[-1]*n
        result =True
        def dfs(node,color):
            nonlocal result
            if not(result):
                return
            colors[node]=color
            for neighbor in graph[node]:
                if colors[neighbor] == -1:
                    dfs(neighbor,color ^ 1)
                elif colors[neighbor] == colors[node]:
                    result=False
        for i in range(n):
            if not result:
                return False
            if colors[i] == -1:
                dfs(i,0)
        return True
            

    
