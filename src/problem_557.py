# Problem 557: https://projecteuler.net/problem=557
import numpy as np


def solve(limit=10_000):
    total = 0

    for s in range(4, limit + 1):
        a = np.arange(1, s - 2, dtype=np.int64)
        aa = a * a
        step = (s + a) // np.gcd(aa, s + a)
        count = (s - a - 2) // step
        keep = count > 0
        a = a[keep]
        step = step[keep]
        count = count[keep]
        size = int(count.sum())

        if size == 0:
            continue

        av = np.repeat(a, count)
        dv = np.repeat(step, count)
        starts = np.repeat(np.cumsum(count) - count, count)
        k = np.arange(size, dtype=np.int64) - starts + 1
        d = dv * k
        bc = av * av * d // (s + av)
        bpc = s - av - d
        delta = bpc * bpc - 4 * bc
        possible = delta >= 0
        delta = delta[possible]
        bpc = bpc[possible]
        root = np.sqrt(delta).astype(np.int64)
        valid = root * root == delta
        valid = np.logical_and(valid, (bpc - root) % 2 == 0)
        valid = np.logical_and(valid, bpc > root)
        total += s * int(np.count_nonzero(valid))

    return total


if __name__ == "__main__":
    print(solve())
