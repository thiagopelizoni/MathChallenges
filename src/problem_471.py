# Problem 471: https://projecteuler.net/problem=471

from mpmath import mp


def harmonic_sums(n):
    h = mp.harmonic(n)
    s1 = n * (n + 1) // 2
    s2 = n * (n + 1) * (2 * n + 1) // 6
    f0 = (n + 1) * h - n
    f1 = s1 * h - mp.mpf(n * (n - 1)) / 4
    f2 = s2 * h - mp.mpf(2 * s2 - 3 * s1 + n) / 6
    return f0, f1, f2


def solve():
    mp.dps = 50
    n = 10**11
    even = n // 2
    odd = (n - 1) // 2

    _, _, f2n = harmonic_sums(n)
    _, _, f2e = harmonic_sums(even)
    f0o, f1o, f2o = harmonic_sums(odd)

    s1e = even * (even + 1) // 2
    s2e = even * (even + 1) * (2 * even + 1) // 6
    s1o = odd * (odd + 1) // 2
    s2o = odd * (odd + 1) * (2 * odd + 1) // 6

    polynomial = 3 * (s2e - s1e) + 3 * s2o + 2 * s1o
    harmonic = f2n - n * (n + 1) // 2
    split = 4 * f2e + 4 * f2o + 4 * f1o + f0o
    result = polynomial - harmonic + split
    return mp.nstr(result, 10, min_fixed=0, max_fixed=0).replace("e+", "e")


if __name__ == "__main__":
    print(solve())
