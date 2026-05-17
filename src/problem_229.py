# Problem 229: https://projecteuler.net/problem=229
from array import array
from math import gcd, isqrt


LIMIT = 2_000_000_000
MOD = 168
RES = (1, 25, 121)


def base_primes(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p * p:n + 1:p] = b"\x00" * ((n - p * p) // p + 1)
    return [p for p in range(2, n + 1) if sieve[p]]


def good_primes_upto(n):
    primes = base_primes(isqrt(n))
    out = array("I")
    block = 8_000_000

    for lo in range(0, n + 1, block):
        hi = min(n, lo + block - 1)
        sieve = bytearray(b"\x01") * (hi - lo + 1)
        for p in primes:
            start = max(p * p, ((lo + p - 1) // p) * p)
            if start <= hi:
                sieve[start - lo:hi - lo + 1:p] = b"\x00" * ((hi - start) // p + 1)

        for r in RES:
            x = lo + (r - lo) % MOD
            if x < 2:
                x += MOD
            while x <= hi:
                if sieve[x - lo]:
                    out.append(x)
                x += MOD

    return sorted(out)


def square_marks(t, d):
    ok = bytearray(t + 1)
    for n in range(1, isqrt(2 * t // d + 2) + 3):
        m = 1
        while True:
            z0 = m * m + d * n * n
            if z0 > 2 * t:
                break
            x0 = abs(m * m - d * n * n)
            if x0:
                y0 = 2 * m * n
                z = z0 // gcd(gcd(x0, y0), z0)
                if z <= t:
                    ok[z:t + 1:z] = b"\x01" * ((t - z) // z + 1)
            m += 1
    return ok


def good_squares(t):
    marks = [square_marks(t, d) for d in (1, 2, 3, 7)]
    return sum(marks[0][i] and marks[1][i] and marks[2][i] and marks[3][i] for i in range(1, t + 1))


def solve():
    primes = good_primes_upto(LIMIT)
    total = 0

    def count(pos, prod):
        nonlocal total
        total += isqrt(LIMIT // prod)
        lim = LIMIT // prod
        i = pos
        while i < len(primes) and primes[i] <= lim:
            count(i + 1, prod * primes[i])
            i += 1

    count(0, 1)
    t = isqrt(LIMIT)
    return total - t + good_squares(t)


if __name__ == "__main__":
    print(solve())
