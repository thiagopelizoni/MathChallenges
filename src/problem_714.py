# Problem 714: https://projecteuler.net/problem=714

from collections import deque
from decimal import Decimal
from itertools import combinations

import numpy as np


def smallest(n):
    best = None
    for a, b in combinations(range(10), 2):
        if n % 10 == 0 and a != 0:
            continue
        seen = [False] * n
        queue = deque()
        for digit in (a, b):
            if digit and not seen[digit % n]:
                queue.append(digit)
                seen[digit % n] = True
        while queue:
            x = queue.popleft()
            if best is not None and x >= best:
                break
            if x % n == 0:
                best = x
                break
            for digit in (a, b):
                y = 10 * x + digit
                r = y % n
                if not seen[r]:
                    seen[r] = True
                    queue.append(y)
    return best


def solve(limit=50_000):
    pairs = {}
    for a, b in combinations(range(10), 2):
        pairs[a, b] = np.array([b] if a == 0 else [a, b], dtype=np.int64)

    pending = list(range(1, limit + 1))
    total = 0
    width = 1
    while pending and width <= limit:
        values = np.unique(np.concatenate(list(pairs.values())))
        remaining = []
        for n in pending:
            matches = np.flatnonzero(values % n == 0)
            if matches.size:
                total += int(values[matches[0]])
            else:
                remaining.append(n)
        pending = remaining
        width *= 2
        if width <= limit:
            for (a, b), values in pairs.items():
                pairs[a, b] = np.concatenate((10 * values + a, 10 * values + b))

    total += sum(smallest(n) for n in pending)
    mantissa, exponent = f"{Decimal(total):.12e}".split("e")
    return f"{mantissa}e{int(exponent)}"


if __name__ == "__main__":
    print(solve())
