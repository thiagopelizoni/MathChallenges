# Problem 304: https://projecteuler.net/problem=304

from math import isqrt


START = 10**14
COUNT = 100_000
MOD = 1_234_567_891_011
SPAN = 5_000_000


def small_primes(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"

    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = b"\x00" * ((n - p * p) // p + 1)

    return [p for p in range(2, n + 1) if sieve[p]]


def primes_after(n, count):
    root = isqrt(n + SPAN) + 10
    base = small_primes(root)
    ans = []
    low = n + 1

    while len(ans) < count:
        high = low + SPAN
        if high % 2 == 0:
            high -= 1
        if low % 2 == 0:
            low += 1

        block = bytearray(b"\x01") * ((high - low) // 2 + 1)
        lim = isqrt(high)

        if base[-1] < lim:
            base = small_primes(lim)

        for p in base[1:]:
            if p > lim:
                break
            first = max(p * p, ((low + p - 1) // p) * p)
            if first % 2 == 0:
                first += p
            block[(first - low) // 2 :: p] = b"\x00" * ((high - first) // (2 * p) + 1)

        for i, ok in enumerate(block):
            if ok:
                ans.append(low + 2 * i)
                if len(ans) == count:
                    return ans

        low = high + 2


def fib(n):
    if n == 0:
        return 0, 1

    a, b = fib(n // 2)
    c = a * (2 * b - a) % MOD
    d = (a * a + b * b) % MOD

    if n % 2:
        return d, (c + d) % MOD
    return c, d


def solve():
    return sum(fib(p)[0] for p in primes_after(START, COUNT)) % MOD


if __name__ == "__main__":
    print(solve())
