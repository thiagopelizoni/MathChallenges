# Problem 274: https://projecteuler.net/problem=274


LIMIT = 10**7


def prime_sieve(n):
    sieve = bytearray(b"\x01") * n
    sieve[:2] = b"\x00\x00"

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            start = i * i
            sieve[start:n:i] = b"\x00" * ((n - 1 - start) // i + 1)

    return sieve


def multiplier(p):
    return ((-pow(p, -1, 10) % 10) * p + 1) // 10


def solve():
    sieve = prime_sieve(LIMIT)
    return sum(multiplier(p) for p in range(3, LIMIT, 2) if p != 5 and sieve[p])


if __name__ == "__main__":
    print(solve())
