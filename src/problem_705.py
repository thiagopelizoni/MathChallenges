# Problem 705: https://projecteuler.net/problem=705

from math import lcm

import numpy as np
from sympy import divisors, sieve


def solve(n=10**8):
    mod = 1_000_000_007
    s = "".join(str(p) for p in sieve.primerange(n)).replace("0", "")
    digits = np.frombuffer(s.encode(), dtype=np.uint8) - ord("0")
    del s
    counts = np.bincount(digits, minlength=10)
    divs = [[]] + [divisors(d) for d in range(1, 10)]
    scale = lcm(*(len(divs[d]) for d in range(1, 10)))
    total = 0
    ways = 1

    for b in range(1, 10):
        weights = np.zeros(10, dtype=np.int64)
        for a in range(1, 10):
            pairs = sum(x > y for x in divs[a] for y in divs[b])
            weights[a] = pairs * (scale // len(divs[a])) * (scale // len(divs[b]))
        prefix = weights[digits]
        np.cumsum(prefix, out=prefix)
        total += int(prefix[digits == b].sum()) - int(counts[b]) * int(weights[b])
        ways = ways * pow(len(divs[b]), int(counts[b]), mod) % mod

    return total % mod * ways % mod * pow(scale**2, -1, mod) % mod


if __name__ == "__main__":
    print(solve())
