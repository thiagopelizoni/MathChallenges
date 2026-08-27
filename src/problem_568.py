# Problem 568: https://projecteuler.net/problem=568
from mpmath import mp


def solve():
    n = 123_456_789
    digits = 7
    mp.dps = 2 * (digits + len(str(n)))
    logarithm = mp.log10(mp.harmonic(n)) - n * mp.log10(2)
    fraction = logarithm - mp.floor(logarithm)
    return int(mp.power(10, fraction + digits - 1))


if __name__ == "__main__":
    print(solve())
