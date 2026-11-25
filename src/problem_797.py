# Problem 797: https://projecteuler.net/problem=797

import numpy as np


def solve(n=10**7):
    mod = 1_000_000_007
    phi = np.empty(n + 1, dtype=np.int64)
    phi[0] = 1
    size = 1
    while size <= n:
        count = min(size, n + 1 - size)
        phi[size:size + count] = phi[:count] * pow(2, size, mod) % mod
        size *= 2
    phi -= 1

    products = np.ones(n + 1, dtype=np.int64)
    lower = np.zeros(n + 1, dtype=np.int64)
    total = 0
    for d in range(1, n // 2 + 1):
        factor = int(phi[d])
        exact = (int(products[d]) * (factor + 1) - int(lower[d])) % mod
        total += exact
        multiples = slice(2 * d, n + 1, d)
        phi[multiples] = phi[multiples] * pow(factor, -1, mod) % mod
        products[multiples] = products[multiples] * (factor + 1) % mod
        lower[multiples] += exact

    tail = slice(n // 2 + 1, n + 1)
    exact = (products[tail] * (phi[tail] + 1) - lower[tail]) % mod
    return (total + int(exact.sum())) % mod


if __name__ == "__main__":
    print(solve())
