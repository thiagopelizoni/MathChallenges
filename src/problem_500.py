# Problem 500: https://projecteuler.net/problem=500

from heapq import heapify, heappop, heappush

from sympy import prime, primerange


COUNT = 500_500
MOD = 500_500_507


def smallest_number(count, mod):
    factors = list(primerange(2, prime(count) + 1))
    heapify(factors)
    result = 1
    for _ in range(count):
        factor = heappop(factors)
        result = result * factor % mod
        heappush(factors, factor * factor)
    return result


def solve():
    return smallest_number(COUNT, MOD)


if __name__ == "__main__":
    print(solve())
