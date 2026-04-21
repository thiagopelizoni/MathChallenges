# Problem 87: https://projecteuler.net/problem=87

from math import isqrt

from sympy import primerange


def solve():
    lim = 50_000_000
    primes = list(primerange(isqrt(lim - 1) + 1))

    squares = [p * p for p in primes if p * p < lim]
    cubes = [p ** 3 for p in primes if p ** 3 < lim]
    fourths = [p ** 4 for p in primes if p ** 4 < lim]

    nums = set()
    for a in fourths:
        for b in cubes:
            ab = a + b
            if ab >= lim:
                break
            for c in squares:
                n = ab + c
                if n >= lim:
                    break
                nums.add(n)

    return len(nums)


if __name__ == "__main__":
    print(solve())
