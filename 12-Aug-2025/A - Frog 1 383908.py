# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

N = int(input())
h = list(map(int, input().split()))

dp = [0] * N
dp[0] = 0
dp[1] = abs(h[1] - h[0])

for i in range(2, N):
    cost1 = dp[i-1] + abs(h[i] - h[i-1])
    cost2 = dp[i-2] + abs(h[i] - h[i-2])
    dp[i] = min(cost1, cost2)

print(dp[N-1])
