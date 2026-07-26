# Problem 455: https://projecteuler.net/problem=455


LIMIT = 1_000_000
MOD = 10**9


def fixed_point(n):
    exponent = n
    while True:
        value = pow(n, exponent, MOD)
        if value == 0 or value == exponent:
            return value
        exponent = value


def solve():
    return sum(fixed_point(n) for n in range(2, LIMIT + 1))


if __name__ == "__main__":
    print(solve())
