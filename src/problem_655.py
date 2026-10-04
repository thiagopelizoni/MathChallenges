# Problem 655: https://projecteuler.net/problem=655

import numpy as np


def solve(digits=32, modulus=10_000_019):
    total = -2
    for length in (digits - 1, digits):
        counts = np.zeros(modulus, dtype=np.int64)
        counts[0] = 1

        for i in range((length + 1) // 2):
            weight = pow(10, i, modulus)
            if 2 * i + 1 < length:
                weight += pow(10, length - 1 - i, modulus)
            weight %= modulus

            updated = counts.copy()
            for digit in range(1, 10):
                updated += np.roll(counts, digit * weight % modulus)
            counts = updated

        total += int(counts[0])

    return total


if __name__ == "__main__":
    print(solve())
