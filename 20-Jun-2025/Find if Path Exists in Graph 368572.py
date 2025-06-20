# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    from collections import defaultdict
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        vist=set()
        def dfs(node,vist):
            if destination == node:
                return True
            vist.add(node)
            for i in graph[node]:
                if i not in vist:
                    found=dfs(i,vist)
                    if found:
                        return True
            return False
        return dfs(source,vist)


        
            
