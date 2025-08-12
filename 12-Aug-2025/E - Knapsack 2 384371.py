# Problem: E - Knapsack 2 - https://atcoder.jp/contests/dp/tasks/dp_e

N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

MAX_VALUE = N * 1000  # max possible value sum
INF = 10**18
dp = [INF] * (MAX_VALUE + 1)
dp[0] = 0

for w, v in items:
    for cur_v in range(MAX_VALUE - v, -1, -1):
        if dp[cur_v] != INF:
            dp[cur_v + v] = min(dp[cur_v + v], dp[cur_v] + w)

ans = 0
for value in range(MAX_VALUE + 1):
    if dp[value] <= W:
        ans = value

print(ans)
