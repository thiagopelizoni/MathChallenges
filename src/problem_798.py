# Problem 798: https://projecteuler.net/problem=798

import numpy as np


def losing_deals(n, suits, mod):
    size = 1
    while size <= n:
        size *= 2
    counts = np.zeros(size, dtype=np.int64)
    half = pow(2, -1, mod)
    tail = (pow(2, n, mod) - 1) % mod
    balance = 1

    for k in range((n + 1) // 2):
        gap = n - 2 * k - 1
        if gap <= 1:
            next_tail = next_balance = 0
        else:
            row = n - k - 1
            ratio = balance * gap * pow((k + 1) * row, -1, mod) % mod
            next_tail = ((tail - balance) * half - ratio * row) % mod
            next_balance = ratio * (gap - 1) % mod
        total = tail - next_tail
        diff = balance - next_balance
        counts[2 * k] = (total + diff) * half % mod
        counts[2 * k + 1] = (total - diff) * half % mod
        tail, balance = next_tail, next_balance
    counts[0] += 1

    width = 1
    while width < size:
        pairs = counts.reshape(-1, 2 * width)
        left = pairs[:, :width].copy()
        right = pairs[:, width:]
        pairs[:, :width] = left + right
        right[:] = left - right
        width *= 2

    total = sum(pow(int(x), suits, mod) for x in counts)
    return total * pow(size, -1, mod) % mod


def solve():
    return losing_deals(10**7, 10**7, 1_000_000_007)


if __name__ == "__main__":
    print(solve())
