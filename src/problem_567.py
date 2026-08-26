# Problem 567: https://projecteuler.net/problem=567
from mpmath import mp


def solve():
    n = 123_456_789
    decimal_places = 8
    mp.dps = 2 * decimal_places
    total = 4 * mp.harmonic(n) - 2 * mp.log(2) - 4 / mp.mpf(n)
    return f"{float(total):.{decimal_places}f}"


if __name__ == "__main__":
    print(solve())
