# Problem 615: https://projecteuler.net/problem=615

from heapq import heappop, heappush

from sympy import sieve


def solve(n=10**6, rank=10**6, mod=123454321):
    k = 0
    while k < n and 3**k <= rank * 2**k:
        k += 1

    start = 2**k
    limit = rank * start
    primes = list(sieve.primerange(2 * rank + 1))
    heap = [(start, 0)]

    for _ in range(rank - 1):
        value, i = heappop(heap)
        p = primes[i]

        if i == 0:
            child = value * 2
            if child <= limit:
                heappush(heap, (child, i))
        elif value % 2 == 0:
            child = value // 2 * p
            if child <= limit:
                heappush(heap, (child, i))

        if i + 1 < len(primes):
            child = value // p * primes[i + 1]
            if child <= limit:
                heappush(heap, (child, i + 1))

    return heap[0][0] * pow(2, n - k, mod) % mod


if __name__ == "__main__":
    print(solve())
