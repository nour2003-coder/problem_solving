# Problem: I - Coins - https://atcoder.jp/contests/dp/tasks/dp_i

N = int(input())
p = list(map(float, input().split()))

# dp[j] = probability of having j heads after current processing
dp = [0.0] * (N + 1)
dp[0] = 1.0

for i in range(N):
    next_dp = [0.0] * (N + 1)
    for j in range(i + 1):
        # If coin i is heads
        next_dp[j + 1] += dp[j] * p[i]
        # If coin i is tails
        next_dp[j] += dp[j] * (1 - p[i])
    dp = next_dp

# Sum over cases where heads > tails
threshold = (N // 2) + 1
ans = sum(dp[threshold:])
print(ans)
