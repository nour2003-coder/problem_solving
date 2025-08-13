# Problem: G - Longest Path - https://atcoder.jp/contests/dp/tasks/dp_g

from collections import deque

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    indeg = [0] * (N+1)

    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        indeg[y] += 1

    # Topological sort
    q = deque()
    for i in range(1, N+1):
        if indeg[i] == 0:
            q.append(i)

    dp = [0] * (N+1)
    
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dp[v] < dp[u] + 1:
                dp[v] = dp[u] + 1
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    print(max(dp))

if __name__ == "__main__":
    main()
