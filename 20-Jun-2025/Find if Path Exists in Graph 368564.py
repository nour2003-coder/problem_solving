# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    from collections import defaultdict
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        d=defaultdict(list)
        for i,j in edges:
            d[i].append(j)
            d[j].append(i)
        v=set()
        def dfs(node,visited):
            if node == destination:
                return True
            visited.add(node)
            for i in d[node]:
                if i not in visited:
                    found=dfs(i,visited)
                    if found:
                        return True
            return False

        return(dfs(source,v))

        
            
