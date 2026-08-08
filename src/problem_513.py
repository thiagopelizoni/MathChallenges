# Problem 513: https://projecteuler.net/problem=513

from math import gcd, isqrt

N = 100000


def solve():
    n = N
    M = n // 2
    ans = 0
    for d1 in range(1, M + 1):
        f1_lim = isqrt(d1 * n + d1 * d1) + 1
        G = M // d1
        odd1 = d1 % 2
        for f1 in range(d1 + 1, f1_lim + 1):
            if f1 * f1 >= 3 * d1 * d1:
                num, den = f1, d1
            else:
                num, den = 3 * d1 - f1, f1 - d1
            if (num + den - 1) // den > (n + d1) // f1:
                continue
            if gcd(d1, f1) != 1:
                continue
            both = odd1 and f1 % 2
            for g0 in range(1, G + 1):
                tmin = (g0 * num + den - 1) // den
                tmax = (n + g0 * d1) // f1
                if tmin > tmax:
                    break
                if both:
                    lo = tmin + (tmin % 2 != g0 % 2)
                    if lo <= tmax:
                        ans += (tmax - lo) // 2 + 1
                else:
                    if g0 % 2:
                        continue
                    lo = tmin + (tmin % 2)
                    if lo <= tmax:
                        ans += (tmax - lo) // 2 + 1
    return ans


if __name__ == "__main__":
    print(solve())
