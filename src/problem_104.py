# Problem 104: https://projecteuler.net/problem=104

from math import log10


MASK = (1 << 10) - 2
MOD = 10**9
PHI = (1 + 5**0.5) / 2
LOG_PHI = log10(PHI)
LOG_SQRT5 = log10(5) / 2


def pandigital(n):
    mask = 0
    while n:
        n, d = divmod(n, 10)
        mask |= 1 << d
    return mask == MASK


def first_digits(k):
    x = k * LOG_PHI - LOG_SQRT5
    return int(10 ** (x - int(x) + 8))


def solve():
    a, b = 1, 1
    k = 2

    while True:
        a, b = b, (a + b) % MOD
        k += 1

        if pandigital(b) and pandigital(first_digits(k)):
            return k


if __name__ == "__main__":
    print(solve())
