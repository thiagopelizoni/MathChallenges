# Problem 117: https://projecteuler.net/problem=117


def solve():
    dp = [0] * 51
    dp[0] = 1

    for n in range(1, 51):
        dp[n] = sum(dp[n - k] for k in (1, 2, 3, 4) if n >= k)

    return dp[50]


if __name__ == "__main__":
    print(solve())
