# Problem 444: https://projecteuler.net/problem=444

from math import comb

from mpmath import mp


N = 10**14
K = 20


def solve():
    mp.dps = 80
    total = mp.mpf(comb(N + K, K)) * (mp.harmonic(N + K) - mp.harmonic(K))
    return mp.nstr(total, 10, min_fixed=0, max_fixed=0).replace("e+", "e")


if __name__ == "__main__":
    print(solve())
