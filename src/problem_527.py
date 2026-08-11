# Problem 527: https://projecteuler.net/problem=527

from math import log2

from mpmath import mp


N = 10**10


def binary_search_average(n):
    levels = int(log2(n))
    return levels + 1 - mp.mpf(2 ** (levels + 1) - levels - 2) / n


def random_binary_search_average(n):
    return 2 * (n + 1) * mp.harmonic(n) / n - 3


def solve():
    with mp.workdps(30):
        difference = random_binary_search_average(N) - binary_search_average(N)
    return f"{float(difference):.8f}"


if __name__ == "__main__":
    print(solve())
