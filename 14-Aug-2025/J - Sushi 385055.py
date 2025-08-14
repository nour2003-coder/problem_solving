# Problem: J - Sushi - https://atcoder.jp/contests/dp/tasks/dp_j

N = int(input())
a = list(map(int, input().split()))

# Count initial c1, c2, c3
c1 = a.count(1)
c2 = a.count(2)
c3 = a.count(3)

# DP array
dp = [[[0.0] * (N+1) for _ in range(N+1)] for _ in range(N+1)]

for x3 in range(N+1):
    for x2 in range(N+1):
        for x1 in range(N+1):
            if x1 + x2 + x3 == 0:
                continue
            s = x1 + x2 + x3
            p0 = (N - s) / N
            res = 1.0  # the +1 in the formula

            if x1 > 0:
                res += (x1 / N) * dp[x1 - 1][x2][x3]
            if x2 > 0:
                res += (x2 / N) * dp[x1 + 1][x2 - 1][x3]
            if x3 > 0:
                res += (x3 / N) * dp[x1][x2 + 1][x3 - 1]

            dp[x1][x2][x3] = res / (1 - p0)

print(dp[c1][c2][c3])
