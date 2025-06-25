# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        colors=[-1]*n
        test=True
        def dfs(node,color):
            nonlocal test
            if not(test):
                return
            colors[node]=color
            for i in graph[node]:
                if colors[i] == -1:
                    dfs(i,color^1)
                elif colors[i] == colors[node]:
                    test=False
        for i in range(n):
            if not(test):
                return False
            if colors[i] == -1:
                dfs(i,0)
        return True
            

    
