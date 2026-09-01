# Solution for Project Euler problem 580
from array import array
from functools import lru_cache
from math import isqrt


def integer_cuberoot(number):
    root = int(number ** (1 / 3))
    while (root + 1) ** 3 <= number:
        root += 1
    while root ** 3 > number:
        root -= 1
    return root


def solve(limit):
    maximum = limit - 1
    mobius_limit = max(1_000_000, integer_cuberoot(maximum))
    lookup_limit = min(10_000_000, maximum)

    mobius = array("b", [1]) * (mobius_limit + 1)
    prime_flags = bytearray(b"\x01") * (mobius_limit + 1)
    prime_flags[:2] = b"\x00\x00"
    for prime in range(2, mobius_limit + 1):
        if prime_flags[prime]:
            for multiple in range(prime, mobius_limit + 1, prime):
                mobius[multiple] = -mobius[multiple]
            square = prime * prime
            if square <= mobius_limit:
                count = (mobius_limit - square) // prime + 1
                prime_flags[square : mobius_limit + 1 : prime] = b"\x00" * count
                square_count = (mobius_limit - square) // square + 1
                mobius[square : mobius_limit + 1 : square] = array("b", [0]) * square_count

    mertens_prefix = array("i", [0]) * (mobius_limit + 1)
    running_total = 0
    for number in range(1, mobius_limit + 1):
        running_total += mobius[number]
        mertens_prefix[number] = running_total

    @lru_cache(maxsize=None)
    def mertens(number):
        if number <= mobius_limit:
            return mertens_prefix[number]
        total = 1
        left = 2
        while left <= number:
            quotient = number // left
            right = number // quotient
            total -= (right - left + 1) * mertens(quotient)
            left = right + 1
        return total

    @lru_cache(maxsize=None)
    def odd_mertens(number):
        total = 0
        while number:
            total += mertens(number)
            number //= 2
        return total

    def squarefree_one_mod_four(number):
        maximum_divisor = isqrt(number)
        cutoff = min(maximum_divisor, integer_cuberoot(number))
        total = 0
        for divisor in range(1, cutoff + 1, 2):
            quotient = number // (divisor * divisor)
            total += mobius[divisor] * ((quotient + 3) // 4)
        left = cutoff + 1
        while left <= maximum_divisor:
            quotient = number // (left * left)
            right = min(maximum_divisor, isqrt(number // quotient))
            mobius_sum = odd_mertens(right) - odd_mertens(left - 1)
            total += mobius_sum * ((quotient + 3) // 4)
            left = right + 1
        return total

    squarefree_flags = bytearray(b"\x01") * (lookup_limit + 1)
    squarefree_flags[0] = 0
    for prime in range(2, isqrt(lookup_limit) + 1):
        if prime_flags[prime]:
            square = prime * prime
            count = (lookup_limit - square) // square + 1
            squarefree_flags[square : lookup_limit + 1 : square] = b"\x00" * count

    lookup = array("I", [0]) * (lookup_limit + 1)
    running_total = 0
    for number in range(1, lookup_limit + 1):
        if number % 4 == 1 and squarefree_flags[number]:
            running_total += 1
        lookup[number] = running_total
    del squarefree_flags, prime_flags

    prime_limit = isqrt(maximum)
    odd_prime_flags = bytearray(b"\x01") * (prime_limit // 2 + 1)
    odd_prime_flags[0] = 0
    for prime in range(3, isqrt(prime_limit) + 1, 2):
        if odd_prime_flags[prime // 2]:
            start = prime * prime // 2
            count = (len(odd_prime_flags) - 1 - start) // prime + 1
            odd_prime_flags[start::prime] = b"\x00" * count

    answer = squarefree_one_mod_four(maximum)
    for prime in range(3, prime_limit + 1, 4):
        if odd_prime_flags[prime // 2]:
            reduced_limit = maximum // (prime * prime)
            if reduced_limit <= lookup_limit:
                answer += lookup[reduced_limit]
            else:
                answer += squarefree_one_mod_four(reduced_limit)
    return answer


if __name__ == "__main__":
    print(solve(10**16))
