# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    from collections import defaultdict,deque
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        for u,v in redEdges:
            graph[u].append([v,0])
        for u,v in blueEdges:
            graph[u].append([v,1])
        def bfs(root,n,graph):
            distance=[[float("inf"), float("inf")] for _ in range(n)]
            distance[root]=[0,0]
            q=deque()
            q.append([root,0,0])
            q.append([root,1,0])
            while(q):
                node,color,dist=q.popleft()
                for adj,col in graph[node]:
                    if color!=col and distance[adj][col]>distance[node][color]+1:
                        distance[adj][col]=distance[node][color]+1
                        q.append([adj, col, distance[adj][col]])
            shortest_distance = [0]*n
            for i in range(n):
                if distance[i][0] == distance[i][1] == float("inf"):
                    shortest_distance[i] = -1
                else:
                    shortest_distance[i] = min(distance[i][0], distance[i][1])
            return shortest_distance
        return bfs(0, n, graph)