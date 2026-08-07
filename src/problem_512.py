# Problem 512: https://projecteuler.net/problem=512

from functools import cache

import numpy as np

N = 5 * 10**8
L = int(N ** (2 / 3)) + 10

phi = np.arange(L + 1, dtype=np.int64)
for i in range(2, L + 1):
    if phi[i] == i:
        phi[i::i] //= i
        phi[i::i] *= i - 1
pref = np.cumsum(phi)


@cache
def totient_sum(n):
    if n <= L:
        return int(pref[n])
    s = n * (n + 1) // 2
    i = 2
    while i <= n:
        q = n // i
        r = n // q
        s -= (r - i + 1) * totient_sum(q)
        i = r + 1
    return s


def solve():
    vals = []
    m = N
    while m:
        vals.append(m)
        m //= 2

    odd = {0: 0}
    for m in reversed(vals):
        sub = 0
        w = 1
        sm = m // 2
        while sm:
            sub += w * odd[sm]
            w *= 2
            sm //= 2
        odd[m] = totient_sum(m) - sub
    return odd[N]


if __name__ == "__main__":
    print(solve())
