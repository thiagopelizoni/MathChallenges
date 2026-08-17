# Problem 546: https://projecteuler.net/problem=546

from math import comb


MOD = 1_000_000_007


def coefficients(k, depth):
    coeffs = []
    first = []
    for r in range(k):
        first.append([(r + 1 - k) % MOD, k])
    coeffs.append(first)

    for j in range(1, depth + 1):
        previous = coeffs[-1]
        totals = [0] * (j + 1)
        prefixes = []
        running = [0] * (j + 1)

        for row in previous:
            for p, a in enumerate(row):
                totals[p] = (totals[p] + a) % MOD
                running[p] = (running[p] + a) % MOD
            prefixes.append(running[:])

        current = []
        for prefix in prefixes:
            row = [0] * (j + 2)
            row[0] = (prefix[0] - totals[0]) % MOD
            for p in range(1, j + 1):
                row[p] = (prefix[p] - totals[p] + totals[p - 1]) % MOD
            row[-1] = totals[-1]
            current.append(row)
        coeffs.append(current)

    return coeffs


def value(k, n):
    chain = [n]
    while chain[-1] >= k:
        chain.append(chain[-1] // k)

    depth = len(chain) - 1
    coeffs = coefficients(k, depth)
    base = chain[-1]
    values = [
        comb(base + j + 1, j + 1) % MOD
        for j in range(depth + 1)
    ]

    for level in range(depth - 1, -1, -1):
        r = chain[level] % k
        next_values = []
        for j in range(level + 1):
            total = 0
            for a, b in zip(coeffs[j][r], values):
                total += a * b
            next_values.append(total % MOD)
        values = next_values

    return values[0]


def solve():
    return sum(value(k, 10**14) for k in range(2, 11)) % MOD


if __name__ == "__main__":
    print(solve())
