def unbounded(weights, items_number, knapsack_size):
    dp = [0] * (knapsack_size + 1)

    for i in range(1, knapsack_size+1):
        dp[i] = max([weights[j] + dp[i - weights[j]] for j in range(items_number) if weights[j] <= i] or [0])

    return dp[knapsack_size]


def zero_one(weights, items_number, knapsack_size):
    dp = [[0 for i in range(knapsack_size+1)] for j in range(items_number)]

    for i in range(1, items_number):
        for j in range(1, knapsack_size+1):
            value = weights[i]
            weight = weights[i]
            if weight > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)

    return dp[items_number-1][knapsack_size]

