
def max_cont_sum_brute(a):
    max_sum = 0
    for i in range(len(a)):
        curr_sum = 0
        for j in range(i, len(a)):
            curr_sum += a[j]
            if curr_sum > max_sum:
                max_sum = curr_sum

    return max_sum

a = [1, 5, -1, 3, -5, 5, -6, -5, 10]
print max_cont_sum_brute(a)

def max_cont_sum(a):
    dp = [0] * (len(a)+1)
    dp[0] = max(a[0], 0)
    for i in range(1, len(a)):
        dp[i] = max(dp[i-1] + a[i], 0)

    return max(dp)

print max_cont_sum(a)


def non_cont_max_sum(a):
    dp = [0] * (len(a)+1)
    dp[0] = max(a[0], 0)
    for i in range(1, len(a)):
        dp[i] = max(dp[i-1]+a[i], a[i], 0)

    return max(dp)