# Problem 306: https://projecteuler.net/problem=306

LIM = 1_000_000
START = 53
PERIOD = 34
PRE_LOSING = 10
LOSING = (2, 6, 10, 20, 24)


def losing(n):
    if n < START:
        return sum(k <= n for k in (1, 5, 9, 15, 21, 25, 29, 35, 39, 43))

    q, r = divmod(n - START + 1, PERIOD)
    return PRE_LOSING + q * len(LOSING) + sum(k < r for k in LOSING)


def solve():
    return LIM - losing(LIM)


if __name__ == "__main__":
    print(solve())
