# Problem 581: https://projecteuler.net/problem=581

from sympy import primerange
from sympy.solvers.diophantine.diophantine import diop_DN


def solve():
    limit = 47
    primes = list(primerange(2, limit + 1))

    def is_smooth(n):
        for p in primes:
            while n % p == 0:
                n //= p
        return n == 1

    ds = [1]
    for p in primes:
        ds += [d * p for d in ds]

    indices = set()
    for d in ds[1:]:
        a, b = map(int, diop_DN(d, 1)[0])
        if not is_smooth(b):
            continue

        x, y = 1, 0
        for _ in range(limit + 1):
            x, y = a * x + d * b * y, b * x + a * y
            if y % 2 == 0 and is_smooth(y):
                indices.add((x - 1) // 2)

    return sum(indices)


if __name__ == "__main__":
    print(solve())
