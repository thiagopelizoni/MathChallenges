# Problem 700: https://projecteuler.net/problem=700

from math import isqrt


def solve():
    a = 1504170715041707
    m = 4503599627370517
    cutoff = isqrt(m)
    coin = a
    value = a
    total = a

    while coin > cutoff:
        value = (value + a) % m
        if value < coin:
            coin = value
            total += coin

    inverse = pow(a, -1, m)
    earliest = m
    for value in range(1, coin):
        index = inverse * value % m
        if index < earliest:
            earliest = index
            total += value

    return total


if __name__ == "__main__":
    print(solve())
