# Problem 772: https://projecteuler.net/problem=772
from sympy import integer_log, sieve


def solve():
    k = 10**8
    mod = 1_000_000_007
    result = 2
    for p in sieve.primerange(k + 1):
        power = p
        if p * p <= k:
            exponent, _ = integer_log(k, p)
            power = p**exponent
        result = result * power % mod
    return result


if __name__ == "__main__":
    print(solve())
