# Problem 661: https://projecteuler.net/problem=661

from decimal import Decimal


def expectation(a, b, p):
    q = 1 - p
    delta = (p * p + 2 * p * q * (a + b) + q * q * (a - b) ** 2).sqrt()
    return 2 * a / (delta * (p + q * (b - a) + delta))


def solve(n=50):
    total = Decimal(0)
    for k in range(3, n + 1):
        k = Decimal(k)
        a = 1 / (k + 3).sqrt()
        total += expectation(a, a + 1 / k**2, 1 / k**3)
    return f"{total:.4f}"


if __name__ == "__main__":
    print(solve())
