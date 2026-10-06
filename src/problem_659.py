# Problem 659: https://projecteuler.net/problem=659

import numpy as np


def solve(limit=10**7):
    remaining = 4 * np.arange(limit + 1, dtype=np.int64) ** 2 + 1
    largest = np.ones(limit + 1, dtype=np.int64)

    for k in range(1, limit + 1):
        p = int(remaining[k])
        if p <= 1 or p > 2 * limit:
            continue
        for start in (k, p - k):
            for j in range(start, limit + 1, p):
                value = int(remaining[j])
                while value % p == 0:
                    value //= p
                remaining[j] = value
                largest[j] = max(int(largest[j]), p)

    np.maximum(remaining, largest, out=largest)
    return sum(map(int, largest[1:])) % 10**18


if __name__ == "__main__":
    print(solve())
