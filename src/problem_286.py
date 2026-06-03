# Problem 286: https://projecteuler.net/problem=286


TARGET = 0.02


def probability(q):
    dp = [1.0] + [0.0] * 20

    for x in range(1, 51):
        p = 1 - x / q
        miss = x / q
        for k in range(min(x, 20), 0, -1):
            dp[k] = dp[k] * miss + dp[k - 1] * p
        dp[0] *= miss

    return dp[20]


def solve():
    lo, hi = 50.0, 100.0

    for _ in range(100):
        mid = (lo + hi) / 2
        if probability(mid) > TARGET:
            lo = mid
        else:
            hi = mid

    return f"{(lo + hi) / 2:.10f}"


if __name__ == "__main__":
    print(solve())
