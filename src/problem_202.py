# Problem 202: https://projecteuler.net/problem=202
from sympy import factorint


def count_residue(n, r):
    if r == 0:
        return n // 3
    if n < r:
        return 0
    return (n - r) // 3 + 1


def ways(reflections):
    n = (reflections + 3) // 2
    limit = n // 2
    primes = list(factorint(n))
    total = 0

    for mask in range(1 << len(primes)):
        d = 1
        bits = 0
        for i, p in enumerate(primes):
            if mask >> i & 1:
                d *= p
                bits += 1

        inv = 1 if d % 3 == 1 else 2
        count = count_residue(limit // d, (2 * inv) % 3)
        total += -count if bits % 2 else count

    return 2 * total


def solve():
    return ways(12_017_639_147)


if __name__ == "__main__":
    print(solve())
