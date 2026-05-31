# Problem 278: https://projecteuler.net/problem=278


LIMIT = 5000


def primes_below(n):
    sieve = bytearray(b"\x01") * n
    sieve[:2] = b"\x00\x00"

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            start = i * i
            sieve[start:n:i] = b"\x00" * ((n - 1 - start) // i + 1)

    return [i for i in range(n) if sieve[i]]


def solve():
    primes = primes_below(LIMIT)
    prefix = [0]
    for p in primes:
        prefix.append(prefix[-1] + p)

    total = 0
    n = len(primes)
    for i, q in enumerate(primes):
        sp = prefix[i]
        sr = prefix[n] - prefix[i + 1]
        cp = i
        cr = n - i - 1
        total += 2 * q * sp * sr - q * sp * cr - sp * sr - q * cp * sr

    return total


if __name__ == "__main__":
    print(solve())
