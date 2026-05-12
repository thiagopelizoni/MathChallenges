# Problem 196: https://projecteuler.net/problem=196
from math import isqrt


MAX_ROW = 7_208_785


def row_start(row):
    return row * (row - 1) // 2 + 1


def row_end(row):
    return row * (row + 1) // 2


def value(row, col):
    return row * (row - 1) // 2 + col


def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"

    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            sieve[start:n + 1:p] = b"\x00" * ((n - start) // p + 1)

    return [p for p in range(2, n + 1) if sieve[p]]


BASE_PRIMES = primes_upto(isqrt(row_end(MAX_ROW + 2)) + 1)


def prime_segment(lo, hi):
    flags = bytearray(b"\x01") * (hi - lo + 1)

    for p in BASE_PRIMES:
        if p * p > hi:
            break
        start = max(p * p, ((lo + p - 1) // p) * p)
        flags[start - lo::p] = b"\x00" * ((hi - start) // p + 1)

    return flags


def neighbours(row, col):
    for rr in (row - 1, row, row + 1):
        for cc in (col - 1, col, col + 1):
            if rr != row or cc != col:
                if 1 <= cc <= rr:
                    yield rr, cc


def s(row):
    lo = row_start(row - 2)
    hi = row_end(row + 2)
    flags = prime_segment(lo, hi)

    def is_prime(row, col):
        return bool(flags[value(row, col) - lo])

    def prime_neighbours(row, col):
        return [(rr, cc) for rr, cc in neighbours(row, col) if is_prime(rr, cc)]

    def member(col):
        ns = prime_neighbours(row, col)
        return len(ns) >= 2 or bool(ns) and len(prime_neighbours(*ns[0])) >= 2

    first = row_start(row)
    offset = first - lo
    total = 0

    for col in range(1, row + 1):
        if flags[offset + col - 1] and member(col):
            total += first + col - 1

    return total


def solve():
    return s(5_678_027) + s(7_208_785)


if __name__ == "__main__":
    print(solve())
