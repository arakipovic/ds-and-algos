n, m = map(int, raw_input().split())
coins = map(int, raw_input().split())
dp = [[-1 for i in range(len(coins)+1)] for j in range(n+1)]

def solve(n, coins, i):
    if n < 0 or i >= len(coins):
        return 0
    elif n == 0:
        return 1

    if dp[n][i] == -1:
        dp[n][i] = solve(n-coins[i], coins, i) + solve(n, coins, i+1)
    return dp[n][i]


print solve(n, coins, 0)
