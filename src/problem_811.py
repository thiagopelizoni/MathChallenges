# Problem 811: https://projecteuler.net/problem=811

from math import comb


def solve():
    t = 10**14 + 31
    r = 62
    mod = 1_000_062_031
    positions = []
    for k in range(r + 1):
        coefficient = comb(r, k)
        pos = k * t
        while coefficient:
            coefficient, digit = divmod(coefficient, 2)
            if digit:
                positions.append(pos)
            pos += 1

    factor = 1
    total = 1
    for i in reversed(range(len(positions))):
        factor = (3 + 5 * factor) % mod
        previous = positions[i - 1] if i else -1
        zeros = positions[i] - previous - 1
        total = total * pow(factor, zeros, mod) % mod
    return total


if __name__ == "__main__":
    print(solve())
