
#O(N^2)
def solve(a, n):
    dp = [1] * (n + 1)
    for i in range(1, n):
        dp[i] = max([dp[j] for j in range(i) if a[j] < a[i]] or [0]) + 1
    return max(dp)

#O(NlogN)


def solve(a, n):
    dp = [0] * (n+1)
    p = [0] * n

    L = 0
    for i in range(n):
        lo = 1
        hi = L

        while lo <= hi:
            mid = int(lo + (hi - lo) / 2)

            if a[i] > a[dp[mid]]:
                lo = mid + 1
            else:
                hi = mid - 1

        newL = lo
        p[i] = dp[newL-1]
        dp[newL] = i

        L = newL if newL > L else L

    sol = []
    k = dp[L]
    for i in range(L-1, -1, -1):
        sol.append(a[k])
        k = p[k]

    return len(sol)