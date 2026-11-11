# Problem 730: https://projecteuler.net/problem=730

from math import gcd, isqrt

import numpy as np


def solve(m=100, n=10**8):
    total = 0
    roots = []
    for p in range(isqrt(m // 2) + 1):
        limit = m // (2 * p) if p else max(1, m // 2)
        for q in range(p, limit + 1):
            for r in range(max(1, p + q), isqrt(p * p + q * q + m) + 1):
                if gcd(p, q, r) == 1 and p + q + r <= n:
                    roots.append((p, q, r))

    for p, q, r in roots:
        total += p > 0
        children = set()
        for u in (p, -p):
            for v in (q, -q):
                x, y = sorted((2 * r - u - 2 * v, 2 * r - 2 * u - v))
                z = 3 * r - 2 * u - 2 * v
                if z > r and x + y + z <= n:
                    children.add((x, y, z))
        if not children:
            continue
        triples = np.array(list(children), dtype=np.int64).T

        while triples.shape[1]:
            p, q, r = triples
            tail = 7 * r - 5 * p + 5 * q > n
            x, y, z = triples[:, tail]
            a = z - y
            s = x + y + z
            b = 2 * x + a
            t = ((np.sqrt(b * b + 4 * a * (n - s)) - b) / (4 * a)).astype(np.int64)
            t -= s + 2 * b * t + 4 * a * t * t > n
            t += s + 2 * b * (t + 1) + 4 * a * (t + 1) * (t + 1) <= n
            total += int(np.sum(t + 1))

            p, q, r = triples[:, np.logical_not(tail)]
            total += p.size
            first = np.array((2 * r + p - 2 * q, 2 * r + 2 * p - q, 3 * r + 2 * p - 2 * q))
            distinct = p < q
            x, y, z = p[distinct], q[distinct], r[distinct]
            second = np.array((2 * z - 2 * x + y, 2 * z - x + 2 * y, 3 * z - 2 * x + 2 * y))
            fits = 7 * r + 5 * p + 5 * q <= n
            x, y, z = p[fits], q[fits], r[fits]
            third = np.array((2 * z + 2 * x + y, 2 * z + x + 2 * y, 3 * z + 2 * x + 2 * y))
            triples = np.concatenate((first, second, third), axis=1)

    return total


if __name__ == "__main__":
    print(solve())
