# Problem 801: https://projecteuler.net/problem=801

from sympy import factorint, primerange


def f(p):
    m = p - 1
    gcd_sum = 1
    for q, e in factorint(m).items():
        r = q**e
        gcd_sum *= r * r + (r // q) * (r - 1)
    return m * (m + gcd_sum)


def solve():
    start = 10**16
    stop = start + 10**6
    return sum(f(p) for p in primerange(start, stop + 1)) % 993_353_399


if __name__ == "__main__":
    print(solve())
