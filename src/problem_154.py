# Problem 154: https://projecteuler.net/problem=154

import numpy as np


def factorial_exponents(n, p):
    values = np.zeros(n + 1, dtype=np.int32)
    for k in range(1, n + 1):
        x = k
        c = 0
        while x % p == 0:
            c += 1
            x //= p
        values[k] = values[k - 1] + c
    return values


def solve():
    n = 200_000
    v2 = factorial_exponents(n, 2)
    v5 = factorial_exponents(n, 5)
    total = 0

    for i in range(n + 1):
        e2 = int(v2[n] - v2[n - i] - v2[i])
        e5 = int(v5[n] - v5[n - i] - v5[i])
        m = i // 2 + 1

        good = (
            e2 + v2[i] - v2[:m] - v2[i - m + 1:i + 1][::-1] >= 12
        ) & (
            e5 + v5[i] - v5[:m] - v5[i - m + 1:i + 1][::-1] >= 12
        )

        count = int(good.sum()) * 2
        if i % 2 == 0 and good[-1]:
            count -= 1
        total += count

    return total


if __name__ == "__main__":
    print(solve())
