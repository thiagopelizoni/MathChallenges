# Problem 560: https://projecteuler.net/problem=560
import numpy as np
from sympy import primerange


MOD = 1_000_000_007


def solve():
    n = 10_000_000
    lim = n - 1
    primes = np.fromiter(primerange(2, n), dtype=np.int64)

    grundy = np.zeros(n, dtype=np.int32)
    grundy[1] = 1
    for i, value in enumerate(primes, 1):
        p = int(value)
        if p == 2:
            continue
        if p * p > lim:
            break
        part = grundy[p:n:2 * p]
        part[part == 0] = i
    grundy[primes[1:]] = np.arange(2, len(primes) + 1, dtype=np.int32)

    size = 1
    while size <= len(primes):
        size *= 2
    values = np.bincount(grundy, minlength=size).astype(np.int64)
    values[0] -= 1

    step = 1
    while step < size:
        blocks = values.reshape(-1, 2 * step)
        left = blocks[:, :step].copy()
        right = blocks[:, step:].copy()
        blocks[:, :step] = (left + right) % MOD
        blocks[:, step:] = (left - right) % MOD
        step *= 2

    result = np.ones_like(values)
    power = n
    while power:
        if power % 2:
            result = result * values % MOD
        values = values * values % MOD
        power //= 2

    return int(result.sum() % MOD) * pow(size, -1, MOD) % MOD


if __name__ == "__main__":
    print(solve())
