# Problem 116: https://projecteuler.net/problem=116


def count(length, tile):
    dp = [0] * (length + 1)
    dp[0] = 1

    for n in range(1, length + 1):
        dp[n] = dp[n - 1]
        if n >= tile:
            dp[n] += dp[n - tile]

    return dp[length] - 1


def solve():
    return sum(count(50, tile) for tile in (2, 3, 4))


if __name__ == "__main__":
    print(solve())
