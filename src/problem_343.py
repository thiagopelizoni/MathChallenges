# Problem 343: https://projecteuler.net/problem=343

from array import array
from math import isqrt

from sympy import primerange, sqrt_mod


N = 2_000_000


def solve():
    vals = array("Q", (k * k - k + 1 for k in range(N + 1)))
    best = array("Q", [0]) * (N + 1)

    for p in primerange(2, N + 2):
        for m in range(p, N + 2, p):
            best[m - 1] = p

    for p in primerange(3, isqrt(N * N - N + 1) + 1):
        if p == 3:
            roots = (2,)
        elif p % 3 == 1:
            s = sqrt_mod(-3, p)
            inv2 = pow(2, -1, p)
            roots = ((1 + s) * inv2 % p, (1 - s) * inv2 % p)
        else:
            continue

        for r in roots:
            start = r if r else p
            for k in range(start, N + 1, p):
                if vals[k] % p == 0:
                    best[k] = max(best[k], p)
                    vals[k] //= p
                    while vals[k] % p == 0:
                        vals[k] //= p

    total = 0
    for k in range(1, N + 1):
        if vals[k] > 1:
            best[k] = max(best[k], vals[k])
        total += best[k] - 1

    return total


if __name__ == "__main__":
    print(solve())
